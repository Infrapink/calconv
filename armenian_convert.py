#!/usr/bin/python

#
# Convert a date in the Armenian Calendar to a Julian Day
#

import months

def convert(day, month, year):
    day = int(day)
    month = month
    year = int(year)
    days = 0
    m = months.ARMENIAN_MONTHS

    if year > 0:
        # positive years
        alpha = 1922866
        for y in range(1,year):
            days += 365
        for i in m.keys():
            if i == month:
                days += day
                break
            else:
                days += m[i]
    else:
        # negative years
        alpha = 1922867
        year = 0 - year
        for i in m.keys():
            if i == month:
                days += day - 1
                break
            else:
                days += m[i]
        for y in range(0,year):
            days -= 365
    jday = alpha + days
    return jday
                
