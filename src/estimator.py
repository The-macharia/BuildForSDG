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
  impact = {
    "currentlyInfected": currentlyInfectedImpact,
    "infectionsByRequestedTime": infectionsByRequestedTimeImpact,

  }
  severeImpact = {
    "currentlyInfected": currentlyInfectedServereImpact,
    "infectionsByRequestedTime": infectionsByRequestedTimeSevereImpact,
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