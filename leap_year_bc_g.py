def leap_year_bc_g(year):
    return ((year + 1) % 4 == 0 and (year + 1) % 100 != 0) or ((year + 1) % 400 == 0)