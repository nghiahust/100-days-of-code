age = int(input("What is your current age? "))

year_left = 90 - age
month_left = year_left * 12
weeks_left = year_left * 52
day_left = year_left * 365

print(f"You have {day_left} days, {weeks_left} weeks, and {month_left} months left.")