#!/usr/bin/python3

#
# Convert between the Serbian church calendar and Julian day
#

import months

epoch = 1721426
cycle900 = (900 * 365) + (900 // 4) - 7

def tojd(day, month, year):

    day = int(day)
    month = month.title()
    year = int(year)
    jday = epoch

    if year > 0:
        # positive years
        y = 1
        cycles = (year - y) // 900
        y += (900 * cycles)
        jday += (cycle900 * cycles)
        while y < year:
            if (y % 900) in (0, 400):
                jday += 366
            elif y % 100 == 0:
                jday += 365
            elif y % 4 == 0:
                jday += 366
            else:
                jday += 365
            y += 1

        if (year % 900) in (0 ,400):
            # leap year
            m = months.CAESAR_LEAP
        elif year % 100 == 0:
            # not a leap year
            m = months.CAESAR_NORMAL
        elif year % 4 == 0:
            # leap year
            m = months.CAESAR_LEAP
        else:
            # not a leap year
            m = months.CAESAR_NORMAL

    else:
        # negative years
        y = 0
        cycles = (y - year) // 900
        y -= (900 * cycles)
        jday -= (cycle900 * cycles)

        while y > year:
            y -= 1
            if abs(y) % 900 in (1, 601):
                jday -= 366
            elif abs(y) % 100 == 1:
                jday -= 365
            elif abs(y) % 4 == 1:
                jday -= 366
            else:
                jday -= 365

        if abs(year) % 900 in (1, 601):
            # leap year
            m = months.CAESAR_LEAP
        elif abs(year) % 100 == 1:
            # not a leap year
            m = months.CAESAR_NORMAL
        elif abs(year) % 4 == 1:
            # leap year
            m = months.CAESAR_LEAP
        else:
            # not a leap year
            m = months.CAESAR_NORMAL

    for i in m.keys():
        if i == month:
            jday += day - 1
            break
        else:
            jday += m[i]
                
    return jday

def fromjd(jday):
    """Convert a Julian day to a date in the Serbian church calendar."""
    jday = int(jday)
    day = 0
    month = ""
    year = 0
    nyd = epoch

    if jday >= epoch:
        # positive date
        curryear = False
        year = 1
        cycles = (jday - nyd) // cycle900
        year += (900 * cycles)
        nyd += (cycle900 * cycles)
        
        while curryear == False:
            if (year % 900) in (0, 400):
                if jday - nyd < 366:
                    curryear = True
                else:
                    nyd += 366
                    year += 1
            elif year % 100 == 0:
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

        if (year % 900) in (0,400):
            # leap year
            m = months.CAESAR_LEAP
        elif year % 100 == 0:
            # not a leap year
            m = months.CAESAR_NORMAL
        elif year % 4 == 0:
            # leap year
            m = months.CAESAR_LEAP
        else:
            # not a leap year
            m = months.CAESAR_NORMAL

    else:
        # negative dates
        cycles = (nyd - jday) // cycle900
        nyd -= (cycle900 * cycles)
        year -= (900 * cycles)

        while nyd > jday:
            year -= 1
            if abs(year) % 900 in (1, 601):
                nyd -= 366
            elif abs(year) % 100 == 1:
                nyd -= 365
            elif abs(year) % 4 == 1:
                nyd -= 366
            else:
                nyd -= 365
                
        if abs(year) % 900 in (1,601):
            # leap year
            m = months.CAESAR_LEAP
        elif abs(year) % 100 == 1:
            # not a leap year
            m = months.CAESAR_NORMAL
        elif abs(year) % 4 == 1:
            # leap year
            m = months.CAESAR_LEAP
        else:
            # not a leap year
            m = months.CAESAR_NORMAL

    delta = jday - nyd
    for i in m.keys():
        if delta < m[i]:
            month = i
            day = delta + 1
            break
        else:
            delta -= m[i]

    return (day, month, year)
