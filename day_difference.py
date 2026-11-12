from leap_year_g import leap_year_g
from leap_year_j import leap_year_j


"""
I choose 200 to 300 as a reference.
Before 200, Julian should use more leap years to catch up with Gregorian.
"""
def day_difference(year):
    ans = 0
    if year in range(200, 300): #from 200AD to 300AD Gregorian and Julian calendars are the same
        return ans
    elif year > 299:
        for i in range(299, year + 1):
            if leap_year_j(i) and (not leap_year_g(i)):
                ans += 1 #Julian has a more leap year
    elif year < 200 and year > 0:
        for i in range(year, 201):
            if leap_year_j(i) and (not leap_year_g(i)):
                ans -= 1 #Julian has a less leap year
    elif year < 0:
        for i in range(year + 1, 201):
            if leap_year_j(i) and (not leap_year_g(i)):
                ans -= 1
    return ans