from datetime import date

year = int(input("Enter birth year: "))
month = int(input("Enter birth month: "))
day = int(input("Enter birth day: "))

today = date.today()

birth_date = date(year, month, day)

age_years = today.year - birth_date.year

if (today.month, today.day) < (birth_date.month, birth_date.day):
    age_years -= 1

print("Your age is:", age_years, "years")