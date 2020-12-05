#!/usr/bin/python

#
# Convert between the Goucher-Parker calendar and Julian day
#

import months

cycle128 = (128 * 365) + 31
cycle4 = (4 * 365) + 1
epoch = 1721423

def tojd(day, month, year):

    day = int(day)
    month = month.title()
    year = int(year)
    jday = epoch

    if year > 0:
        # positive years
        y = 1
        cycles = (year - y) // 128
        y += (128 * cycles)
        jday += (cycles * cycle128)

        while y < year:
            if y % 128 == 0:
                jday += 365
            elif y % 4 == 0:
                jday += 366
            else:
                jday += 365
            y += 1

        if year % 128 == 0:
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
        cycles = (y - year) // 128
        y -= (cycles * 128)
        jday -= (cycle128 * cycles)

        while y > year:
            y -= 1
            if abs(y) % 128 == 1:
                jday -= 365
            elif abs(y) % 4 == 1:
                jday -= 366
            else:
                jday -= 365

        if abs(year) % 128 == 1:
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
    """Convert a Julian day to a date in the Goucher-Parker calendar."""
    jday = int(jday)
    year = 0
    month = ""
    day = 0
    nyd = epoch
    curryear = False

    if jday >= epoch:
        # positive date
        year = 1
        cycles = (jday - nyd) // cycle128
        year += (128 * cycles)
        nyd += (cycles * cycle128)
        while curryear == False:
            if year % 128 == 0:
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
                
        if year % 128 == 0:
            # not a leap year
            m = months.CAESAR_NORMAL
        elif year % 4 == 0:
            # leap year
            m = months.CAESAR_LEAP
        else:
            # not a leap year
            m = months.CAESAR_NORMAL

    else:
        # negative date
        year = 0
        cycles = (nyd - jday) // cycle128
        year -= (128 * cycles)
        nyd -= (cycle128 * cycles)

        while nyd > jday:
            year -= 1
            if abs(year) % 128 == 1:
                nyd -= 365
            elif abs(year) % 4 == 1:
                nyd -= 366
            else:
                nyd -= 365

        if abs(year) % 128 == 1:
            # not a leap year
            m = months.CAESAR_NORMAL
        elif abs(year) % 4 == 1:
            # leap year
            m = months.CAESAR_LEAP
        else:
            # not a leap yer
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
