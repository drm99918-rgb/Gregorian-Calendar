def leap_year_bc_g(year):
    if (year % 4 == 3 and year % 100 != 3) or (year % 400 == 3):
        return True
    else:
        return False