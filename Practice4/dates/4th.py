from datetime import date, timedelta, datetime

year1, month1, day1 = int(input("Year for first date: ")), int(input("Month for first date: ")), int(input("Day for first date: "))

year2, month2, day2 = int(input("Year for second date: ")), int(input("Month for second date: ")), int(input("Day for second date: "))

first_date = date(year1, month1, day1)
second_date = date(year2, month2, day2)

print((second_date - first_date).total_seconds())