import calendar

year = int(input("Enter a year: "))
month_number = int(input("Enter a month (1-12): "))

cal = calendar.month(year, month_number)
print(cal)
