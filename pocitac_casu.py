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

china_zodiac = {
	"1912": "Rat",
	"1913": "Ox",
	"1914": "Tiger",
	"1915": "Rabbit",
	"1916": "Dragon",
	"1917": "Snake",
	"1918": "Horse",
	"1919": "Goat",
	"1920": "Monkey",
	"1921": "Rooster",
	"1922": "Dog",
	"1923": "Pig",
}
age_date = input("what year were you born in?: ")
year_age = (Date.year) - int(age_date)
ag = year_age - 1
#for element in china_zodiac:
	#if (int(age_date) - int(element)) % 12 == 0:
		#zodiac = china_zodiac.get(element)

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

if month_value.get(month_date) > 31:
	for element in china_zodiac:
		if (int(age_date) - int(element)) % 12 == 0:
			zodiac = china_zodiac.get(element)
else:
	for element in china_zodiac:
		if (int(age_date) -1 - int(element)) % 12 == 0:
			zodiac = china_zodiac.get(element)


year_days = month_value.get(month_date) + int(day_date)
if int(Date.strftime("%j")) < year_days:
	Date_roz = year_days - int(Date.strftime("%j"))
	year_age -= 1
	print("you are", year_age, "years,", 365 - Date_roz, "days,", Date.strftime("%H"), "hours,", Date.strftime("%M"), "minutes and", Date.strftime("%S"), "seconds old.")
	print("there are", 365 - int(Date.strftime("%j")), "days remaining in this year")
	print("your chinese zodiac is:", zodiac)
	print("you are alive for:",((year_age + 1)* 365.25) - Date_roz + 1, "days")
else:
	Date_roz = year_days - int(Date.strftime("%j"))
	print("you are", year_age, "years,", int(Date.strftime("%j")) - year_days, "days,", Date.strftime("%H"), "hours,", Date.strftime("%M"), "minutes and", Date.strftime("%S"), "seconds old.")
	print("there are", 365 - int(Date.strftime("%j")), "days remaining in this year")
	print("your chinese zodiac is:", zodiac)
	print("you are alive for:",(year_age * 365.25) - Date_roz, "days")