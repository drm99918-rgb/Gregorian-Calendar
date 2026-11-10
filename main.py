from main_f_g import main_g
from main_f_j import main_j


while True:
    type_calendar = input("Please enter the type of calendar ('g' for Goregorian Calendar and 'j' for Julian Calendar): ")
    type_calendar = type_calendar.lower()
    print()
    if type_calendar == "j" or type_calendar == "julian" or type_calendar == "julian calendar" or type_calendar == "g" or type_calendar == "gregorian" or type_calendar == "gregorian calendar":
        break
    else:
        print("Invalid input, please try again")
        continue
while True:
    match type_calendar:
        case "j" | "julian" | "julian calendar":
            main_j()
            while True:
                ask = input("Do you want to try another calendar? (Y/N): ")
                ask = ask.lower()
                if ask != "y" and ask != "yes" and ask != "no" and ask != "n":
                    print("Invalid input, please try again")
                else:
                    break
            if ask == "y" or ask == "yes":
                type_calendar = "g"
                continue
            else:
                break
        case "g" | "gregorian" | "gregorian calendar":
            main_g()
            while True:
                ask = input("Do you want to try another calendar? (Y/N): ")
                ask = ask.lower()
                if ask != "y" and ask != "yes" and ask != "no" and ask != "n":
                    print("Invalid input, please try again")
                else:
                    break
            if ask == "y" or ask == "yes":
                type_calendar = "j"
                continue
            else:
                break
print("**************Program Ended**************")