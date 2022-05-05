# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# There are 365 days in a year, 52 weeks in a year and 12 months in a year.

age_int = int(age)
years_left = 90
years_left -= age_int

days = 365 * years_left
weeks = 52 * years_left
months = 12 * years_left

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
