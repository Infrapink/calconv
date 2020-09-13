#!/usr/bin/python

#
# Convert between the non-skipping Rumi Calendar and Julian Day
#

import months

epoch = 1948301
cycle4 = (4 * 365) + 1

def tojd(day, month, year):

    day = int(day)
    month = month.title()
    year = int(year)
    jday = epoch

    if year > 0:
        # positive years
        y = 1
        cycles = (year - y) // 4
        y += (cycles * 4)
        jday += (cycles * cycle4)
        while y < year:
            if y % 4 == 2:
                jday += 366
            else:
                jday += 365
            y += 1

        if year % 4 == 2:
            # leap year
            m = months.TURKISH_LEAP
        else:
            # not a leap year
            m = months.TURKISH_NORMAL

    else:
        # negative years
        y = 0
        cycles = (y - year) // 4
        y -= (4 * cycles)
        jday -= (cycles * cycle4)
        while y > year:
            y -= 1
            if y % 4 == 2:
                jday -= 366
            else:
                jday -= 365

        if abs(year) % 4 == 2:
            # leap year
            m = months.TURKISH_LEAP
        else:
            # not a leap year
            m = months.TURKISH_NORMAL

    for i in m.keys():
        if i == month:
            jday += day - 1
            break
        else:
            jday += m[i]
                
    return jday

def fromjd(jday):
    """Convert a Julian day to a date in the Rumi calendar."""
    jday = int(jday)
    year = 0
    month = ""
    day = 0
    nyd = epoch

    if jday >= epoch:
        # positive dates
        curryear = False
        year = 1
        cycles = (jday - nyd) // cycle4
        year += (4 * cycles)
        nyd += (cycles * cycle4)

        while curryear == False:
            if year % 4 == 2:
                if nyd - jday <= 366:
                    curryear = True
                else:
                    jday += 366
            else:
                if nyd - jday <= 365:
                    curryear = True
                else:
                    jday += 365
            year += 1

        if year % 4 == 2:
            # leap year
            m = months.TURKISH_LEAP
        else:
            # not a leap year
            m = months.TURKISH_NORMAL

    else:
        # negative dates
        cycles = (nyd - jday) // cycle4
        year -= (4 * cycles)
        nyd -= (cycles * cycle4)
        while jday < nyd:
            year -= 1
            if abs(year) % 4 == 2:
                nyd -= 365
            else:
                nyd -= 365

        if abs(year) % 4 == 2:
            # leap year
            m = months.TURKISH_LEAP
        else:
            # not a leap year
            m = months.TURKISH_NORMAL

    delta = nyd - jday
    for i in m.keys():
        if delta < m[i]:
            month = i
            day = delta + 1
            break
        else:
            delta -= m[i]

    return (day, month, year)
