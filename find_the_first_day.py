from leap_year import leap_year


def find_the_first_day(month, year):
    ans = 0
    cnt = 0
    for i in range(1, year):
        if leap_year(i):
            cnt += 1
    ans = (year - 1) * 365 + cnt
    mon = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    mon_leap = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if leap_year(year):
        for i in range(month - 1):
            ans += mon_leap[i + 1]
    else:
            for i in range(month - 1):
                ans += mon[i + 1]
    ans += 1
    ans %= 7
    return ans