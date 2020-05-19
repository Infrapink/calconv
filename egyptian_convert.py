#!/usr/bin/python

import months

def convert(day, month, year):
    alpha = 160331
    day = int(day)
    month = month.title()
    year = int(year)
    days = 0
    m = months.EGYPTIAN_MONTHS

    year -= 1
    days = year * 365
    for i in m.keys():
        if i == month:
            days += day
            break
        else:
            days += m[i]
    jday = alpha + days
    return jday
