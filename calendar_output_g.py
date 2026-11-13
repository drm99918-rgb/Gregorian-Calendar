from find_the_first_day_g import find_the_first_day_g
from leap_year_g import leap_year_g


def calendar_output_g(month, year):
    mon_name = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
                9: "September", 10: "October", 11: "November", 12: "December"}
    print(year) #interface
    print(mon_name[month]) #print month
    print("S   M   T   W   T   F   S") #header
    mon = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31} #nums of days in each month in non-leap years
    mon_leap = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31} #nums of days in each month in leap years
    day_list = [] #pack everything in a list before filling in
    if month == 1:
        day_list.extend([31 - i for i in range(find_the_first_day_g(month, year))]) #December so 31 days - i
        day_list.sort() #arrange the dates
        day_list.extend([i + 1 for i in range(mon[month])]) #fill in January calendar
    else:
        if leap_year_g(year):
            day_list.extend([mon_leap[month - 1] - i for i in range(find_the_first_day_g(month, year))]) #leap years so month - 1 - i
            day_list.sort() #arrange the dates
            day_list.extend([i + 1 for i in range(mon_leap[month])]) #fill in current month calendar
        else:
            day_list.extend([mon[month - 1] - i for i in range(find_the_first_day_g(month, year))])
            day_list.sort()
            day_list.extend([i + 1 for i in range(mon[month])])
    if len(day_list) % 7 != 0: #check the last week is full or not
        day_list.extend([i + 1 for i in range(7 - len(day_list) % 7)]) #if not full then continue to fill the following dates
    for i in range(len(day_list) // 7): #column = 7
        for j in range(i * 7, i * 7 + 7):
            print("%-2d" % day_list[j], end="  ") #output
        print()