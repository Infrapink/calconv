#!/usr/bin/python

#
# Convert between the Parker Calendar and Julian Day
#

import months

cycle4 = (4 * 365) + 1
cycle100 = (100 * 365) + 24
cycle400 = (400 * 365) + 97
cycle10000 = (25 * cycle400) - 3

epoch = 1721425

def tojd(day, month, year):

    day = int(day)
    month = month.title()
    year = int(year)
    jday = epoch

    if year > 0:
        # positive dates
        y = 1
        cycles = (year - y) // 10000
        y += (10000 * cycles)
        jday += (cycle10000 * cycles)

        while y < year:
            if (y % 10000) in (2800,5600,8400):
                jday += 365
            elif y % 400 == 0:
                jday += 366
            elif y % 100 == 0:
                jday += 365
            elif y % 4 == 0:
                jday += 366
            else:
                jday += 365
            y += 1

        if (year % 10000) in (2800,5600,8400):
            # not leap year
            m = months.CAESAR_NORMAL
        elif year % 400 == 0:
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
        y = 0
        while y - year > 10000:
            y -= 10000
            jday -= cycle10000

        while y > year:
            y -= 1
            if abs(y) % 10000 in (1600,4400,7200):
                jday -= 365
            elif abs(y) % 400 == 1:
                jday -= 366
            elif abs(y) % 100 == 1:
                jday -= 365
            elif abs(y) % 4 == 1:
                jday -= 366
            else:
                jday -= 365

        if abs(year) % 10000 in (1600, 4400, 7200):
            # not a leap year
            m = months.CAESAR_NORMAL
        elif abs(year) % 400 == 1:
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
    """Convert a Julian day to a date in the Parker calendar."""
    jday = int(jday)
    year = 0
    month = ""
    day = 0
    nyd = epoch

    if jday >= epoch:
        # positive date
        curryear = False
        year = 0
        cycles = (jday - nyd) // cycle10000
        year += (10000 * cycles)
        nyd += (cycle10000 * cycles)

        while curryear == False:
            year += 1
            if (year % 10000) in (2800, 5600, 8400):
                if jday - nyd <= 365:
                    curryear = True
                else:
                    nyd += 365
            elif year % 400 == 0:
                if jday - nyd <= 366:
                    curryear = True
                else:
                    nyd += 366
            elif year % 100 == 0:
                if jday - nyd <= 365:
                    curryear = True
                else:
                    nyd += 365
            elif year % 4 == 0:
                if jday - nyd <= 366:
                    curryear = True
                else:
                    nyd += 366
            else:
                if jday - nyd <= 365:
                    curryear = True
                else:
                    nyd += 365

        if (year % 10000) in (2800,5600,8400):
            # not a leap year
            m = months.CAESAR_NORMAL
        elif year % 400 == 0:
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
        cycles = (nyd - jday) // cycle10000
        year -= (cycles * 10000)
        nyd -= (cycle10000 * cycles)

        while nyd > jday:
            year -= 1
            if abs(year) % 10000 in (1600, 4400, 7200):
                nyd -= 365
            elif abs(year) % 400 == 1:
                nyd -= 366
            elif abs(year) % 100 == 1:
                nyd -= 365
            elif abs(year) % 4 == 1:
                nyd -= 366
            else:
                nyd -= 365

        if abs(year) % 10000 in (1600, 4400, 7200):
            # not a leap year
            m = months.CAESAR_NORMAL
        elif abs(year) % 400 == 1:
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
