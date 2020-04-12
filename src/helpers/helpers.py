def get_infected(reportedCases, factor):
  infected = reportedCases * factor
  return infected

def get_infections_by_requested_time(currentlyInfected, days):
  factor = int((days // 3))
  infections_after_time_period = currentlyInfected * (2**factor)
  return infections_after_time_period

def normalise_days(periodType, value):
  periodType = periodType.lower()
  normalised_days = 0
  if periodType == 'weeks':
    normalised_days = value * 7
  elif periodType == 'months':
    normalised_days = value * 30
  else:
    normalised_days = value
  return normalised_days

def get_severe_cases_by_requested_time(value, factor=0.15):
  cases = factor * value 
  return cases

def get_available_beds(servereCases, totalHospitalBeds, average_available=0.35):
  available_beds = int((average_available * totalHospitalBeds) - servereCases)
  return available_beds

def get_cases_for_ICU(infectionsByRequestedTime, factor=0.05):
  cases_for_ICU = factor * infectionsByRequestedTime
  return int(cases_for_ICU)

def get_cases_requiring_ventilators(infectionsByRequestedTime, factor=0.02):
  cases_requiring_ventilators = factor * infectionsByRequestedTime
  return int(cases_requiring_ventilators)

def get_dollars_in_flight(infections_by_requested_time, avg_earners, avg_daily_income, days):
  expected_loss = (infections_by_requested_time * avg_earners * avg_daily_income) // days  
  return expected_loss