from calendar_output_j import calendar_output_j


def main_j():
    print()
    print("*******Julian Calendar Calculator********")
    while True:
        try:
            month, year = map(int, input("Please enter your month and year (M/Y) in numbers: ").split('/'))
        except ValueError:
            print("Type in positive integers in M/Y form only")
            continue
        if month < 1 or month > 12:
            print("Please enter a valid month")
            continue
        elif year < 1:
            print("Please enter a valid year")
            continue
        if year > 0:
            calendar_output_j(month, year)
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