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
  infectionsByRequestedTimeImpact = get_infections_by_requested_time(currentlyInfectedImpact, 28)
  infectionsByRequestedTimeSevereImpact = get_infections_by_requested_time(currentlyInfectedServereImpact, 28)

  impact = {
    "currentlyInfected": currentlyInfectedImpact,
    "infectionsByRequestedTime": infectionsByRequestedTimeImpact

  }
  severeImpact = {
    "currentlyInfected": currentlyInfectedServereImpact,
    "infectionsByRequestedTime": infectionsByRequestedTimeSevereImpact
  }
  
  return {
    "data": data,
    "impact": impact,
    "severeImpact": severeImpact
  }

def get_infected(reportedCases, factor):
  return reportedCases * factor

def get_infections_by_requested_time(currentlyInfected, days):
  factor = int((days / 3))
  infections = currentlyInfected * (2**factor)
  return infections