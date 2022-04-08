#!/usr/bin/python3

#
# Convert between Igbo dates and Julian Days
#

import months
epoch = 2087608
m = months.IGBO

def tojd(day, month, year):
    day = int(day)
    month = month
    year = int(year)
    jday = epoch
    
    if year > 0:
        # positive dates
        jday += (364 * (year - 1))
    else:
        # negative dates
        jday += (365 * year)

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

    if jday >= epoch:
        # positive dates
        year = ((jday - epoch) // 364) + 1
    else:
        # negative dates
        year = 0 - (((epoch - jday) // 364) + 1)

    delta = (jday - epoch) % 364

    for i in m.keys():
        if delta < m[i]:
            month = i
            day = delta + 1
            break
        else:
            delta -= m[i]

    return (day, month, year)
