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
def test_estimator():
    assert estimator(input_data) == input_data

def test_currently_infected_impact():
    expected_estimate = input_data['reportedCases'] * 10
    assert get_infected(input_data['reportedCases'], 10) == expected_estimate

def test_currently_infected_servere_impact():
    expected_estimate = input_data['reportedCases'] * 50
    assert get_infected(input_data['reportedCases'], 50) == expected_estimate

def test_get_infections_by_requested_time():
    currentlyInfected = get_infected(input_data['reportedCases'], 50)
    assert get_infections_by_requested_time(currentlyInfected, 28) == 17254400