from calendar_output import calendar_output

print()
print("*******Gregorian Calendar Calculator*******")#41 chrs
while True:
    try:
        month, year = map(int, input("Please enter your month and year (M/Y) in numbers: ").split('/'))
    except ValueError:
        print("Type in integers in M/Y form only")
        continue
    if month < 1 or month > 12:
        print("Please enter a valid month")
        continue
    elif year < 1:
        print("Please enter a valid year")
        continue
    calendar_output(month, year)
    print("Try another?")
    while True:
        ask = input("Please enter yes or no (Y/N): ")
        if ask != "Y" and ask != "y" and ask != "Yes" and ask != "yes" and ask != "No" and ask != "no" and ask != "n" and ask != "N":
            print("Please enter yes or no")
        else:
            break
    if ask == "Y" or ask == "y" or ask == "Yes" or ask == "yes":
        continue
    else:
        print("**************Program Ended**************")
        break