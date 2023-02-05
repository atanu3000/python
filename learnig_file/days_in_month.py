def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid Month"

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if leap_year(year):
        days[1] += 1
        return days[month-1]
    else:
        return days[month-1]


year = int(input("Enter a year: "))
months = int(input("Enter a month: "))
days = days_in_month(year, months)
print(days)