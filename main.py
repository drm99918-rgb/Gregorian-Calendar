from calendar_output import calendar_output

while True:
    print("Please enter a month and year in the form mm/yyyy:")
    month, year = map(int, input().split('/'))
    if month < 1 or month > 12:
        print("Please enter a valid month")
        continue
    calendar_output(month, year)
    break