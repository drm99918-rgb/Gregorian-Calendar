from calendar_output_g import calendar_output_g
from calendar_output_bc_g import calendar_output_bc_g
from calendar_output_j import calendar_output_j
from calendar_output_bc_j import calendar_output_bc_j
from day_difference import day_difference
from leap_year_g import leap_year_g
from leap_year_j import leap_year_j
from leap_year_bc_g import leap_year_bc_g
from leap_year_bc_j import leap_year_bc_j
#final version for the task


while True:# while loop logic same as main_f_g.py
    try:
        month, year = map(int, input("Please enter your month and year (M/Y) in numbers (negative integers for BC years) : ").split('/'))
    except ValueError:
        print("Type in integers in M/Y form only")
        continue
    if month < 1 or month > 12:
        print("Please enter a valid month")
        continue
    elif year == 0:
        print("Please enter a valid year")
        continue
    if year > 0:
        print("***********Gregorian Calendar************")
        calendar_output_g(month, year)
        print("*************Julian Calendar*************")
        calendar_output_j(month, year)
    else:
        print("***********Gregorian Calendar************")
        calendar_output_bc_g(month, year)
        print("*************Julian Calendar*************")
        calendar_output_bc_j(month, year)
    d = day_difference(year)
    if (leap_year_j(year) and (not leap_year_g(year)) and year > 0) or ((leap_year_bc_j(year) and (not leap_year_bc_g(year)) and year < 0)): #output day difference based value d
        if d == 0:
            print("In this year, before February, Gregorian calendar is 1 day faster than Julian calendar, but after February, they two are exactly the same.")
        elif d == 1:
            print("In this year, before February, they two are exactly the same, but after February, Julian calendar is 1 day faster than Gregorian calendar.")
        elif d == 2:
            print("In this year, before February, Julian calendar is 1 day faster than Gregorian calendar, and after February, Julian calendar is 2 days faster than Gregorian calendar.")
        elif d == -1:
            print("In this year, before February, Gregorian calendar is 2 days faster than Julian calendar, and after February, Gregorian calendar is 1 day faster than Julian calendar.")
        elif d > 2:
            print("In this year, before February, Julian calendar is %d days faster than Gregorian calendar, and after February, Julian calendar is %d days faster than Gregorian calendar." % ((d - 1), d))
        elif d < -1:
            print("In this year, before February, Gregorian calendar is %d days faster than Julian calendar, and after February, Gregorian calendar is %d days faster than Julian calendar." % (-d, -(d + 1)))
    else:
        if d == 0:
            print("In this year, the two calendars are exactly the same.")
        elif d == 1:
            print("In this year, Julian calendar is 1 day faster than Gregorian calendar.")
        elif d == -1:
            print("In this year, Gregorian calendar is 1 day faster than Julian calendar.")
        elif d > 1:
            print("In this year, Julian calendar is %d days faster than Gregorian calendar." % d)
        elif d < -1:
            print("In this year, Gregorian calendar is %d days faster than Julian calendar." % -d)
    print("Try another?")
    while True:
        ask = input("Please enter yes or no (Y/N): ")
        ask = ask.lower()
        if ask != "y" and ask != "yes" and ask != "no" and ask != "n":
            print("Invalid input, please try again")
        else:
            break
    if ask == "y" or ask == "yes":
        continue
    else:
        break
print("***************Program Ended**************")