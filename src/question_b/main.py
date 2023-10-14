#add import
import question_b
KM = input ("enter KM")
MIN = input ("minutes")
KM = int (KM)
MIN = int (MIN)
MPH = question_b.get_miles_per_hour(KM,MIN)

print (MPH)