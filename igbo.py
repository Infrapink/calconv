#!/usr/bin/python

#
# Convert between Igbo dates and Julian Days
#

import months

def tojd(day, month, year):
    day = int(day)
    month = month
    year = int(year)
    jday = 2087607
    m = months.IGBO
    
    if year > 0:
        # positive dates
        jday += (364 * (year - 1))
        for i in m.keys():
            if i == month:
                jday += day - 1 # subtract 1 to account for the fencepost error
                break
            else:
                jday += m[i]
    else:
        # negative dates
        jday += (364 * year)
        for i in m.keys():
            if i == month:
                jday += day - 1
                break
            else:
                jday += m[i]

    return jday

def fromjd(jday):
    jday = int(jday)
    day = 0
    month = ""
    year = 0
    m = months.IGBO

    if jday >= 2087607:
        # positive dates
        delta = jday - 2087607
        year = (delta // 364) + 1
        delta %= 364
        for i in m.keys():
            if delta < m[i]:
                month = i
                day = delta + 1
                break
            else:
                delta -= m[i]
    else:
        # negative dates
        delta = jday - 2087607
        year = (abs(delta) // 364) + 1
        year = 0 - year
        delta %= 364

        for i in m.keys():
            if delta < m[i]:
                month = i
                day = delta + 1
                break
            else:
                delta -= m[i]

    return (day, month, year)
