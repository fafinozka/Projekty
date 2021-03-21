import datetime
# seconds passed since epoch
Date = datetime.datetime.now()
FullDate = []
month_value = {
  "january": 0,
  "february": 31,
  "march": 59,
  "april": 90,
  "may": 120,
  "june": 151,
  "july": 181,
  "august": 212,
  "september": 243,
  "october": 273,
  "november": 304,
  "december": 334
}


age_date = input("what year were you born in?: ")
year_age = (Date.year) - int(age_date)

while True:
	month_date = input("what month were you born in? (word january-december): ")
	if month_date not in ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']:
		print("your input is not valid, try checking if your input is in lowercase and spelled correctly.")
	else:
		break
while True:
	day_date = input("what day of the month were you born in?(number 1-31): ")
	if int(day_date) > 31:
		print("your number is too big! try again.")
	else:
		break
	if int(day_date) < 1:
		print("your number is too small! try again.")
	else:
		break


year_days = month_value.get(month_date) + int(day_date)
print(year_days)

