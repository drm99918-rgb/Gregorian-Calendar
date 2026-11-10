from leap_year_g import leap_year_g
from leap_year_j import leap_year_j
from leap_year_bc_g import leap_year_bc_g
from leap_year_bc_j import leap_year_bc_j


def day_difference(year):
    ans = 0
    if year in range(200, 300):
        return ans
    elif year > 299:
        for i in range(299, year + 1):
            if leap_year_j(i) and (not leap_year_g(i)):
                ans += 1
    elif year < 200:
        for i in range(year, 200):
            if (leap_year_j(i) and (not leap_year_g(i))) or (leap_year_bc_j(i) and (not leap_year_bc_g(i))):
                ans -= 1
    return ans