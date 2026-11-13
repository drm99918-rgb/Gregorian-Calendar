from leap_year_bc_g import leap_year_bc_g


#reference day: 31/12/1BC
def find_the_first_day_bc_g(month, year):
    year_ = - year
    ans = 0
    mon = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    for i in range(year_): #loop to add all dates from the target yr until reference day
        if leap_year_bc_g(- i - 1):
            ans += 366
        else:
            ans += 365
    for i in range(month - 1):
        ans -= mon[i + 1] #minus off all dates before the target month in the target year
    if leap_year_bc_g(year) and month > 2:
        ans -= 1
    ans -= 1
    ans %= 7 #mod 7_a week to get the reminder
    return (7 - ans) % 7