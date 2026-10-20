from leap_year_bc import leap_year_bc


def find_the_first_day_bc(month, year):
    year_ = - year
    ans = 0
    mon = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    for i in range(year_):
        if leap_year_bc(- i - 1):
            ans += 366
        else:
            ans += 365
    for i in range(month - 1):
        ans -= mon[i + 1]
    if leap_year_bc(year) and month > 2:
        ans -= 1
    ans %= 7
    return ans