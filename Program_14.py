#Leap year

def check_leap_year(year):
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        flag=True
    else:
        flag=False
    return flag

year = int(input("Enter a year: "))
if check_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")