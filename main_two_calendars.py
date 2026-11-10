from calendar_output_g import calendar_output_g
from calendar_output_bc_g import calendar_output_bc_g
from calendar_output_j import calendar_output_j
from calendar_output_bc_j import calendar_output_bc_j


while True:
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
        print("*******Gregorian Calendar Calculator*******")
        calendar_output_g(month, year)
        print("*******Julian Calendar Calculator********")
        calendar_output_j(month, year)
    else:
        print("*******Gregorian Calendar Calculator*******")
        calendar_output_bc_g(month, year)
        print("*******Julian Calendar Calculator********")
        calendar_output_bc_j(month, year)
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
print("**************Program Ended**************")