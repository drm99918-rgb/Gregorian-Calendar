from calendar_output import calendar_output

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
    elif year < 1:
        print("Do not enter a BC year")
        continue
    calendar_output(month, year)
    print("Try another?")
    while True:
        ask = input("Please enter yes or no (Y/N): ")
        ask.lower()
        if ask != "y" and ask != "yes" and ask != "no" and ask != "n":
            print("Invalid input, please try again")
        else:
            break
    if ask == "Y" or ask == "y" or ask == "Yes" or ask == "yes" or ask == "YES":
        continue
    else:
        print("**************Program Ended**************")
        break