from src.estimator import *

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
def test_currently_infected_impact():
    expected_estimate = input_data['reportedCases'] * 10
    assert get_infected(input_data['reportedCases'], 10) == expected_estimate

def test_currently_infected_servere_impact():
    expected_estimate = input_data['reportedCases'] * 50
    assert get_infected(input_data['reportedCases'], 50) == expected_estimate

def test_normalise_days():
    assert normalise_days(input_data['periodType'], input_data['timeToElapse']) == 58

def test_get_infections_by_requested_time():
    currentlyInfected = input_data['reportedCases'] * 50
    assert get_infections_by_requested_time(currentlyInfected, input_data['timeToElapse'], input_data['timeToElapse']) == 17668505600

