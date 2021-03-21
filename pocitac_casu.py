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
	"1912" or "1924" or "1936" or "1948" or "1960" or "1972" or "1984" or "1996" or "2008" or "2020": "Rat",
	"1913" or "1925" or "1937" or "1949" or "1961" or "1973" or "1985" or "1997" or "2009" or "2021": "Ox",
	"1914" or "1926" or "1938" or "1950" or "1962" or "1974" or "1986" or "1998" or "2010" or "2022": "Tiger",
	"1915" or "1927" or "1939" or "1951" or "1963" or "1975" or "1987" or "1999" or "2011" or "2023": "Rabbit",
	"1916" or "1928" or "1940" or "1952" or "1964" or "1976" or "1988" or "2000" or "2012" or "2024": "Dragon",
	"1917" or "1929" or "1941" or "1953" or "1965" or "1977" or "1989" or "2001" or "2013" or "2025": "Snake",
	"1918" or "1930" or "1942" or "1954" or "1966" or "1978" or "1990" or "2002" or "2014" or "2026": "Horse",
	"1919" or "1931" or "1943" or "1955" or "1967" or "1979" or "1991" or "2003" or "2015" or "2027": "Goat",
	"1920" or "1932" or "1944" or "1956" or "1968" or "1980" or "1992" or "2004" or "2016" or "2028": "Monkey",
	"1921" or "1933" or "1945" or "1957" or "1969" or "1981" or "1993" or "2005" or "2017" or "2029": "Rooster",
	"1922" or "1934" or "1946" or "1958" or "1970" or "1982" or "1994" or "2006" or "2018" or "2030": "Dog",
	"1923" or "1935" or "1947" or "1959" or "1971" or "1983" or "1995" or "2007" or "2019" or "2031": "Pig",
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

zodiac = china_zodiac.get(age_date)
year_days = month_value.get(month_date) + int(day_date)
if int(Date.strftime("%j")) < year_days:
	Date_roz = year_days - int(Date.strftime("%j"))
	year_age -= 1
	print("you are", year_age, "years,", 365 - Date_roz, "days,", Date.strftime("%H"), "hours,", Date.strftime("%M"), "minutes and", Date.strftime("%S"), "seconds old.")
	print("there are", 365 - int(Date.strftime("%j")), "days remaining in this year")
	print(zodiac)
else:
	print("you are", year_age, "years,", int(Date.strftime("%j")) - year_days, "days,", Date.strftime("%H"), "hours,", Date.strftime("%M"), "minutes and", Date.strftime("%S"), "seconds old.")
	print("there are", 365 - int(Date.strftime("%j")), "days remaining in this year")
	print(zodiac)