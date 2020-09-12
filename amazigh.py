#!/usr/bin/python

#
# Convert between the Amazigh Calendar and Julian Day
#

import months

epoch = 1374435
cycle4 = (4*365) + 1

def tojd(day, month, year):

    day = int(day)
    month = month
    year = int(year)
    jday = epoch

    if year > 0:
        # positive years
        y = 1
        cycles = (year - y) // 4
        y += (cycles * 4)
        jday += (cycles * cycle4)
        while y < year:
            #if year - y > 4:
             #   y += 4
              #  jday += cycle4
            if y % 4 == 2:
                y += 1
                jday += 366
            else:
                y += 1
                jday += 365
                
        if year % 4 == 2:
            # leap year
            m = months.AMAZIGH_LEAP
        else:
            # not a leap year
            m = months.AMAZIGH_NORMAL

    else:
        # negative years.
        y = 0
        cycles = (y - year) // 4
        y -= (cycles * 4)
        jday -= (cycles * cycle4)
        while y > year:
            y -= 1
            if abs(y % 4) == 2:
                jday -= 366
            else:
                jday -= 365

        if abs(year) % 4 == 2:
            # leap yar
            m = months.AMAZIGH_LEAP
        else:
            # not a leap year
            m = months.AMAZIGH_NORMAL

    for i in m.keys():
        if i == month:
            jday += day - 1
            break
        else:
            jday += m[i]

    return jday

def fromjd(jday):
    """Convert a Julian day to a date in the Amazigh calendar."""
    jday = int(jday)
    year = 0
    month = ""
    day = 0
    yen = epoch

    if jday >= epoch:
        # positive dates
        curryear = False
        year = 1
        cycles = (jday - yen) // cycle4
        year += (4 * cycles)
        yen += (cycles * cycle4)
        while curryear == False:
            if year % 4 == 2:
                if jday - yen <= 366:
                    curryear = True
                else:
                    year += 1
                    yen += 366
            else:
                if jday - yen <= 365:
                    curryear = True
                else:
                    year += 1
                    yen += 365

        if year % 4 == 2:
            m = months.AMAZIGH_LEAP
        else:
            m = months.AMAZIGH_NORMAL

    else:
        # negative dates
        cycles = (yen - jday) // cycle4
        year -= (4 * cycles)
        yen -= (cycles * cycle4)
        while jday < yen:
            year -= 1
            if abs(year) % 4 == 2:
                yen -= 366
            else:
                yen -= 365
                
        if abs(year) % 4 == 2:
            # leap yar
            m = months.AMAZIGH_LEAP
        else:
            # not a leap year
            m = months.AMAZIGH_NORMAL

    delta = jday - yen
    for i in m.keys():
        if delta < m[i]:
            month = i
            day = delta + 1
            break
        else:
            delta -= m[i]

    return (day, month, year)
