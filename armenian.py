#!/usr/bin/python

#
# Convert between the Armenian Calendar and Julian Day
#

import months
epoch = 1922867
m = months.ARMENIAN

def tojd(day, month, year):
    day = int(day)
    month = month
    year = int(year)
    jday = epoch

    if year > 0:
        # positive years
        jday = jday + (365 * (year - 1))
    else:
        # negative dates
        jday = jday + (365 * year)

    for i in m.keys():
        if i == month:
            jday += day - 1
            break
        else:
            jday += m[i]
                
def fromjd(jday):
    """Convert a Julian Day to a date in the Armenian calendar"""
    jday = int(jday)
    day = 0
    month = ""
    year = 0

    if jday >= epoch:
        year = ((jday - epoch) // 365) + 1
    else:
        year = 0 - (((epoch - jday) // 365) + 1)

    delta = (jday - epoch) % 365

    for i in m.keys():
        if delta < m[i]:
            month = i
            day = delta + 1
            break
        else:
            delta -= m[i]

    return (day, month, year)
