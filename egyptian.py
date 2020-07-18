#!/usr/bin/python

#
# Convert between the Egyptian Calendar and Julian Day
#

import months

def tojd(day, month, year):
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

def fromjd(jday):
    """Convert a Julian Day to a date in the Egyptian calendar."""
    jday = int(jday)
    m = months.EGYPTIAN_MONTHS
    year = 0
    month = ""
    day = 0

    if jday > 160331:
        # positive year
        delta = jday - 160331
        year = (delta // 365) + 1 # if delta is positive, year > 1 even if less than one full year has passed since day 0
        delta %= 365
        if delta == 0:
            delta = 365
            year -= 1
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]
    else:
        # negative year
        delta = 160332 - jday

        while delta > 0:
            year -= 1
            delta -= 365

        delta = 0 - delta + 1
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = [day, month, year]
    return date
