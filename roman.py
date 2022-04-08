#!/usr/bin/python3

#
# Convert between the Roman calendar and Julian Day
#

import months

cycle4 = 1465
epoch = 1446450

def tojd(day, month, year):
    day = int(day)
    month = month
    year = int(year)

    jday = epoch

    if year > 0:
        # positive dates
        y = 1
        cycles = (year - y) // 4
        y += (4 * cycles)
        jday += (cycle4 * cycles)
        while y < year:
            if y % 4 == 0:
                jday += 378
            elif y % 4 == 2:
                jday += 377
            else:
                jday += 355
            y += 1

        if year % 4 == 0:
            m = months.ROMAN_4
        elif year % 4 == 2:
            m = months.ROMAN_2
        else:
            m = months.ROMAN_NORMAL

    else:
        # negative dates
        y = 0
        cycles = (y - year) // 4
        y -= (4 * cycles)
        jday -= (cycle4 * cycles)
        while y > year:
            y -= 1
            if y % 4 == 3:
                jday -= 378
            elif y % 4 == 1:
                jday -= 377
            else:
                jday -= 355

        if abs(year) % 4 == 1:
            m = months.ROMAN_4
        elif abs(year) % 4 == 3:
            m = months.ROMAN_2
        else:
            m = months.ROMAN_NORMAL

    for i in m.keys():
        if i == month:
            jday += day - 1
            break
        else:
            jday += m[i]
    return jday

def fromjd(jday):
    day = 0
    month = 0
    year = 0

    jday = int(jday)
    nyd = epoch
    curryear = False

    if jday >= epoch:
        # positive dates
        year = 1
        cycles = (jday - nyd) // cycle4
        year += (4 * cycles)
        nyd += (cycle4 * cycles)
        while curryear == False:
            if year % 4 == 0:
                if jday - nyd < 378:
                    curryear = True
                else:
                    year += 1
                    nyd += 378
            elif year % 4 == 2:
                if jday - nyd < 377:
                    curryear = True
                else:
                    year += 1
                    nyd += 377
            else:
                if jday - nyd < 355:
                    curryear = True
                else:
                    year += 1
                    nyd += 355

        if year % 4 == 0:
            m = months.ROMAN_4
        elif year % 4 == 2:
            m = months.ROMAN_2
        else:
            m = months.ROMAN_NORMAL

    else:
        # negative years
        cycles = (nyd - jday) // cycle4
        year -= (4 * cycles)
        nyd -= (cycle4 * cycles)
        while jday < nyd:
            year -= 1
            if abs(year) % 4 == 1:
                nyd -= 378
            elif abs(year) % 4 == 3:
                nyd -= 377
            else:
                nyd -= 355

        if abs(year) % 4 == 1:
            m = months.ROMAN_4
        elif abs(year) % 4 == 3:
            m = months.ROMAN_2
        else:
            m = months.ROMAN_NORMAL

    delta = jday - nyd            
    for i in m.keys():
        if delta < m[i]:
            month = i
            day = delta + 1
            break
        else:
            delta -= m[i]

    return (day, month, year)
