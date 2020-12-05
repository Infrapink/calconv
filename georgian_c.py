#!/usr/bin/python

#
# Convert between the original Georgian calendar and Julian day
#

import months

cycle4 = (4 * 365) + 1
cycle132 = (cycle4 * 33) - 1

epoch = 2362414

def tojd(day, month, year):

    day = int(day)
    month = month.title()
    year = int(year)
    jday = epoch

    if year > 0:
        # positive years
        y = 1
        cycles = (year - y) // 132
        y += (132 * cycles)
        jday += (cycles * cycle132)

        while y < year:
            if y % 132 == 0:
                jday += 365
            elif y % 4 == 0:
                jday += 366
            else:
                jday += 365
            y += 1

        if year % 132 == 0:
            # not a leap year
            m = months.GEORGIAN_C_NORMAL
        elif year % 4 == 0:
            # leap year
            m = months.GEORGIAN_C_LEAP
        else:
            # not a leap year
            m = months.GEORGIAN_C_NORMAL

    else:
        # negative years
        y = 0
        cycles = (y - year) // 132
        y -= (cycles * 132)
        jday -= (cycle132 * cycles)

        while y > year:
            y -= 1
            if abs(y) % 132 == 1:
                jday -= 365
            elif abs(y) % 4 == 1:
                jday -= 366
            else:
                jday -= 365

        if abs(year) % 132 == 1:
            # not a leap year
            m = months.GEORGIAN_C_NORMAL
        elif abs(year) % 4 == 1:
            # leap year
            m = months.GEORGIAN_C_LEAP
        else:
            # not a leap year
            m = months.GEORGIAN_C_NORMAL

    for i in m.keys():
        if i == month:
            jday += day - 1
            break
        else:
            jday += m[i]
                
    return jday

def fromjd(jday):
    """Convert a Julian day to a date in the revised Georgian calendar."""
    jday = int(jday)
    year = 0
    month = ""
    day = 0
    nyd = epoch
    curryear = False

    if jday >= epoch:
        # positive date
        year = 1
        cycles = (jday - nyd) // cycle132
        year += (132 * cycles)
        nyd += (cycles * cycle132)
        while curryear == False:
            if year % 132 == 0:
                if jday - nyd < 365:
                    curryear = True
                else:
                    nyd += 365
                    year += 1
            elif year % 4 == 0:
                if jday - nyd < 366:
                    curryear = True
                else:
                    nyd += 366
                    year += 1
            else:
                if jday - nyd < 365:
                    curryear = True
                else:
                    nyd += 365
                    year += 1
                
        if year % 132 == 0:
            # not a leap year
            m = months.GEORGIAN_C_NORMAL
        elif year % 4 == 0:
            # leap year
            m = months.GEORGIAN_C_LEAP
        else:
            # not a leap year
            m = months.GEORGIAN_C_NORMAL

    else:
        # negative date
        year = 0
        cycles = (nyd - jday) // cycle132
        year -= (132 * cycles)
        nyd -= (cycle132 * cycles)

        while nyd > jday:
            year -= 1
            if abs(year) % 132 == 1:
                nyd -= 365
            elif abs(year) % 4 == 1:
                nyd -= 366
            else:
                nyd -= 365

        if abs(year) % 132 == 1:
            # not a leap year
            m = months.GEORGIAN_C_NORMAL
        elif abs(year) % 4 == 1:
            # leap year
            m = months.GEORGIAN_C_LEAP
        else:
            # not a leap yer
            m = months.GEORGIAN_C_NORMAL

    delta = jday - nyd
    for i in m.keys():
        if delta < m[i]:
            month = i
            day = delta + 1
            break
        else:
            delta -= m[i]

    return (day, month, year)
