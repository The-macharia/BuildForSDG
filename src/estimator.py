from helpers.helpers import *

def estimator(data):
  currentlyInfectedImpact = get_infected(data['reportedCases'], 10)
  currentlyInfectedServereImpact = get_infected(data['reportedCases'], 50)
  infectionsByRequestedTimeImpact = get_infections_by_requested_time(
    currentlyInfectedImpact, 
    normalise_days(data['periodType'], data['timeToElapse'])
    )

  infectionsByRequestedTimeSevereImpact = get_infections_by_requested_time(
    currentlyInfectedServereImpact, 
    normalise_days(data['periodType'], data['timeToElapse'])
    )

  severeCasesByRequestedTimeImpact = get_severe_cases_by_requested_time(
    infectionsByRequestedTimeImpact
    )
  severeCasesByRequestedTimeSevereImpact = get_severe_cases_by_requested_time(
    infectionsByRequestedTimeSevereImpact
    )

  hospitalBedsByRequestedTimeImpact = get_available_beds(
    severeCasesByRequestedTimeImpact,
    data['totalHospitalBeds']
    )
  hospitalBedsByRequestedTimeSevereImpact = get_available_beds(
    severeCasesByRequestedTimeSevereImpact,
    data['totalHospitalBeds'])

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
    "casesForICUByRequestedTime": casesForICUByRequestedTimeSevereImpact,
    "casesForVentilatorsByRequestedTime": casesForVentilatorsByRequestedTimeSevereImpact,
    "dollarsInFlight": dollarsInFlightSevereImpact
  }
  
  output = {
    "data": data,
    "impact": impact,
    "severeImpact": severeImpact
  }
  return output