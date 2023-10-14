#add import
import question_b

get_kilometers = input("Please enter a number that isn't a negative for kilometers: ")

get_minutes = input("Please enter a number that isn't a negative for minutes: ")



result = question_b.get_miles_per_hour(int(get_kilometers), int(get_minutes))

hour = float(60)
time_in_hours = float(get_minutes) / hour
get_km_per_hr = float(get_kilometers) / time_in_hours

print(str(int(get_kilometers)) + " km in " + str(int(get_minutes)) + " min. In kilometers per hour it is: " + str(int(get_km_per_hr)) + " km/hr.\nTherefore, " + str(int(get_km_per_hr)) + " km/hr converted into mph is: " + str(float(result)) + " mph. ")