from src.helpers.helpers import *

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

def test_normalise_days_days():
    assert normalise_days(input_data['periodType'], input_data['timeToElapse']) == 58

def test_normalise_days_lowercasing():
    assert normalise_days("MONTHS", input_data['timeToElapse']) == 1740

def test_normalise_days_weeks():
    assert normalise_days("weeks", input_data['timeToElapse']) == 406

def test_normalise_days_months():
    assert normalise_days("months", input_data['timeToElapse']) == 1740

def test_get_infections_by_requested_time():
    currentlyInfected = input_data['reportedCases'] * 50
    assert get_infections_by_requested_time(currentlyInfected, input_data['timeToElapse']) == 17668505600

def test_get_severe_cases_by_requested_time():
    infections_by_requested_time = 17668505600
    expected_value = 0.15 * infections_by_requested_time

    assert get_severe_cases_by_requested_time(infections_by_requested_time) == expected_value

def test_get_available_beds():
    severe_cases = 0.15 * 17668505600
    available_beds = 0.35 * input_data['totalHospitalBeds']
    bed_deficit = int(available_beds - severe_cases)

    assert get_available_beds(severe_cases, input_data['totalHospitalBeds']) == bed_deficit

def test_get_cases_for_ICU():
    expected_value = 0.05 * 17668505600
    assert get_cases_for_ICU(17668505600) == expected_value

def test_get_cases_requiring_ventilators():
    expected_value = 0.02 * 17668505600
    assert get_cases_requiring_ventilators(17668505600) == expected_value

def test_get_dollars_in_flight():
    infections_by_requested_time = 17668505600
    avg_daily_income = input_data['region']['avgDailyIncomeInUSD']
    avg_earners = input_data['region']['avgDailyIncomePopulation']
    days = input_data['timeToElapse']

    expected_loss = (infections_by_requested_time * avg_earners * avg_daily_income) // days

    assert get_dollars_in_flight(infections_by_requested_time, avg_earners, avg_daily_income, days) == expected_loss


    