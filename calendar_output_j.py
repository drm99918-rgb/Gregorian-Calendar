from find_the_first_day_j import find_the_first_day_j
from leap_year_j import leap_year_j


def calendar_output_j(month, year):
    mon_name = {1: "Ianuarius", 2: "Februarius", 3: "Martius", 4: "Aprilis", 5: "Maius", 6: "Iunius", 7: "Quintilis", 8: "Sextilis",
                9: "September", 10: "October", 11: "November", 12: "December"}
    print(year)
    print(mon_name[month])
    print("S   M   T   W   T   F   S")
    mon = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    mon_leap = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    day_list = []
    if month == 1:
        day_list.extend([31 - i for i in range(find_the_first_day_j(month, year))])
        day_list.sort()
        day_list.extend([i + 1 for i in range(mon[month])])
    else:
        if leap_year_j(year):
            day_list.extend([mon_leap[month - 1] - i for i in range(find_the_first_day_j(month, year))])
            day_list.sort()
            day_list.extend([i + 1 for i in range(mon_leap[month])])
        else:
            day_list.extend([mon[month - 1] - i for i in range(find_the_first_day_j(month, year))])
            day_list.sort()
            day_list.extend([i + 1 for i in range(mon[month])])
    if len(day_list) % 7 != 0:
        day_list.extend([i + 1 for i in range(7 - len(day_list) % 7)])
    for i in range(len(day_list) // 7):
        for j in range(i * 7, i * 7 + 7):
            print("%-2d" % day_list[j], end="  ")
        print()