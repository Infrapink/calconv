#!/usr/bin/python

#
# Convert a date in the Armenian Calendar to a Julian Day
#

import months

def tojd(day, month, year):
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
                
def fromjd(jday):
    """Convert a Julian Day to a date in the Armenian calendar"""
    jday = int(jday)
    day = 0
    month = ""
    year = 0
    m = months.ARMENIAN_MONTHS

    if jday > 1922866:
        # positive year
        delta = jday - 1922866
        year = (delta // 365) + 1 # add 1 to account for the lack of year 0
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
        delta = 1922867 - jday
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
