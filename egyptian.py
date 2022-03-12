#!/usr/bin/python3

#
# Convert between the Egyptian Calendar and Julian Day
#

import months
epoch = 160550
m = months.EGYPTIAN

def tojd(day, month, year):
    day = int(day)
    month = month.title()
    year = int(year)
    jday = epoch

    if year > 0:
        # positive years
        jday = jday + (365 * (year - 1))

    else:
        # negative years
        jday = jday + (365 * year)

    for i in m.keys():
        if i == month:
            jday += day - 1
            break
        else:
            jday += m[i]

    return jday

def fromjd(jday):
    """Convert a Julian Day to a date in the Egyptian calendar."""
    jday = int(jday)

    year = 0
    month = ""
    day = 0

    if jday >= epoch:
        # positive year
        year = ((jday - epoch) // 365) + 1
        delta = (jday - epoch) % 365

    else:
        # negative year
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
