from leap_year_g import leap_year_g


def find_the_first_day_g(month, year):
    ans = 0
    cnt = 0
    for i in range(1, year):
        if leap_year_g(i):
            cnt += 1
    ans = (year - 1) * 365 + cnt
    mon = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    mon_leap = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if leap_year_g(year):
        for i in range(month - 1):
            ans += mon_leap[i + 1]
    else:
            for i in range(month - 1):
                ans += mon[i + 1]
    ans += 1
    ans %= 7
    return ans