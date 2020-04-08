input_data = {
  "region": {
    "name": "Africa",
    "avgAge": 19.7,
    "avgDailyIncomeInUSD": 5,
    "avgDailyIncomePopulation": 0.71
  },
  "periodType": "days",
  "timeToElapse": 58,
  "reportedCases": 674,
  "population": 66622705,
  "totalHospitalBeds": 1380614
}

def estimator(data):
  currentlyInfectedImpact = get_infected(data['reportedCases'], 10)
  currentlyInfectedServereImpact = get_infected(data['reportedCases'], 50)
  infectionsByRequestedTimeImpact = get_infections_by_requested_time(currentlyInfectedImpact, data['timeToElapse'], data['periodType'])
  infectionsByRequestedTimeSevereImpact = get_infections_by_requested_time(currentlyInfectedServereImpact, data['timeToElapse'], data['periodType'])
  severeCasesByRequestedTimeImpact = get_severe_cases_by_requested_time(infectionsByRequestedTimeImpact)
  severeCasesByRequestedTimeSevereImpact = get_severe_cases_by_requested_time(infectionsByRequestedTimeSevereImpact)
  hospitalBedsByRequestedTimeImpact = get_available_beds(severeCasesByRequestedTimeImpact, data['totalHospitalBeds'])
  hospitalBedsByRequestedTimeSevereImpact = get_available_beds(severeCasesByRequestedTimeSevereImpact, data['totalHospitalBeds'])
  casesForICUByRequestedTimeImpact = get_cases_for_ICU(infectionsByRequestedTimeImpact)
  casesForICUByRequestedTimeSevereImpact = get_cases_for_ICU(infectionsByRequestedTimeSevereImpact)
  casesForVentilatorsByRequestedTimeImpact = get_cases_requiring_ventilators(infectionsByRequestedTimeImpact)
  casesForVentilatorsByRequestedTimeSevereImpact = get_cases_requiring_ventilators(infectionsByRequestedTimeSevereImpact)
  dollarsInFlightImpact = get_dollars_in_flight(
    infectionsByRequestedTimeImpact, 
    data['region']['avgDailyIncomePopulation'],
    data['region']['avgDailyIncomeInUSD'],
    normalise_days(data['periodType'], data['timeToElapse'])
     )
  dollarsInFlightSevereImpact = get_dollars_in_flight(
    infectionsByRequestedTimeSevereImpact, 
    data['region']['avgDailyIncomePopulation'],
    data['region']['avgDailyIncomeInUSD'],
    normalise_days(data['periodType'], data['timeToElapse'])
     )
  impact = {
    "currentlyInfected": currentlyInfectedImpact,
    "infectionsByRequestedTime": infectionsByRequestedTimeImpact,
    "severeCasesByRequestedTime": severeCasesByRequestedTimeImpact,
    "hospitalBedsByRequestedTime": hospitalBedsByRequestedTimeImpact,
    "casesForICUByRequestedTime": casesForICUByRequestedTimeImpact,
    "casesForVentilatorsByRequestedTime": casesForVentilatorsByRequestedTimeImpact,
    "dollarsInFlight": dollarsInFlightImpact

  }
  severeImpact = {
    "currentlyInfected": currentlyInfectedServereImpact,
    "infectionsByRequestedTime": infectionsByRequestedTimeSevereImpact,
    "severeCasesByRequestedTime": severeCasesByRequestedTimeSevereImpact,
    "hospitalBedsByRequestedTime": hospitalBedsByRequestedTimeSevereImpact,
    "casesForICUByRequestedTimeImpact": casesForICUByRequestedTimeSevereImpact,
    "casesForVentilatorsByRequestedTime": casesForVentilatorsByRequestedTimeSevereImpact,
    "dollarsInFlight": dollarsInFlightSevereImpact
  }

  return {
    "data": data,
    "impact": impact,
    "severeImpact": severeImpact
  }

def get_infected(reportedCases, factor):
  return reportedCases * factor

def get_infections_by_requested_time(currentlyInfected, days, periodType):
  normalised_days = normalise_days(periodType, days)
  factor = int((normalised_days / 3))
  infections_after_time_period = currentlyInfected * (2**factor)
  return infections_after_time_period

def normalise_days(periodType, value):
  if periodType == 'weeks':
    normalised_days = value * 7
  elif periodType == 'months':
    normalised_days = value * 30
  else:
    normalised_days = value
  return normalised_days

def get_severe_cases_by_requested_time(value, factor=0.15):
  return factor * value

def get_available_beds(servereCases, totalHospitalBeds, average_available=0.35, ):
  available_beds = (average_available * totalHospitalBeds) - servereCases
  return available_beds

def get_cases_for_ICU(infectedByRequestedTime, factor=0.05):
  return factor * infectedByRequestedTime

def get_cases_requiring_ventilators(infectedByRequestedTime, factor=0.02):
  return factor * infectedByRequestedTime

def get_dollars_in_flight(infections_by_requested_time, avg_earners, avg_daily_income, days):
  expected_loss = infections_by_requested_time * avg_earners * avg_daily_income * days  
  return expected_loss
