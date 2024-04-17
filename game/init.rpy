init python:

    # Since the date number changes and that affects the day of the week, defining a variable that performs that calculation.
    def get_day(a):
        dayCalc = a % 7
        calDate = dayOfWeek[dayCalc] + ", April " + str(a)
        return calDate