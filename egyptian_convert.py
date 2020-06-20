#!/usr/bin/python

#
# Convert a date in the Egyptian Calendar to a Julian Day
#

import months

def convert(day, month, year):
    day = int(day)
    month = month.title()
    year = int(year)
    days = 0
    m = months.EGYPTIAN_MONTHS

    if year > 0:
        # positive years
        alpha = 160331
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
        alpha = 160332
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

            
