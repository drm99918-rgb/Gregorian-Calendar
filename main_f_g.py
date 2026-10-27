from calendar_output_g import calendar_output_g
from calendar_output_bc_g import calendar_output_bc_g

def main_g():
    print()
    print("*******Gregorian Calendar Calculator*******")
    while True:
        try:
            month, year = map(int, input("Please enter your month and year (M/Y) in numbers: ").split('/'))
        except ValueError:
            print("Type in positive integers in M/Y form only")
            continue
        if month < 1 or month > 12:
            print("Please enter a valid month")
            continue
        elif year == 0:
            print("Please enter a valid year")
            continue
        if year > 0:
            calendar_output_g(month, year)
        else:
            calendar_output_bc_g(month, year)
        print("Try another?")
        while True:
            ask = input("Please enter yes or no (Y/N): ")
            ask.lower()
            if ask != "y" and ask != "yes" and ask != "no" and ask != "n":
                print("Invalid input, please try again")
            else:
                break
        if ask == "y" or ask == "yes":
            continue
        else:
            break