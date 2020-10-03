#!/usr/bin/python

#
# Convert between the algorithmic Kurdish Calendar and Julian Day
#

import months

cycle4 = (4 * 365) + 1
cycle5 = (365 * 5) + 1
cycle33 = (7 * cycle4) + cycle5

leap_years_an = (17,21,25,29,33,4,8,12)
leap_years_bn = (17,13,9,5,1,30,26,22)

epoch = 1497975

def tojd(day, month, year):
    day = int(day)
    month = month
    year = int(year)
    jday = epoch

    if year > 0:
        # positive years
        y = 1
        cycles = (year - y) // 33
        y += (33 * cycles)
        jday += (cycle33 * cycles)
        while y < year:
            if y % 33 in leap_years_an:
                y += 1
                jday += 366
            else:
                y += 1
                jday += 365

        if (year % 33) in leap_years_an:
            # leap year
            m = months.KURDISH_LEAP
        else:
            # not a leap eyar
            m = months.KURDISH_NORMAL

    else:
        # negative years
        y = 0
        cycles = (y - year) // 33
        y -= (33 * cycles)
        jday -= (cycle33 * cycles)
        while y > year:
            y -= 1
            if abs(y) % 33 in leap_years_bn:
                jday -= 366
            else:
                jday -= 365

        if abs(year) % 33 in leap_years_bn:
            # leap year
            m = months.KURDISH_LEAP
        else:
            # nto a leap year
            m = months.KURDISH_NORMAL

    for i in m.keys():
        if i == month:
            jday += day - 1
            break
        else:
            jday += m[i]

    return jday

def fromjd(jday):
    """Convert a Julian Day into a date in the algorithmic Kurdish calendar."""
    jday = int(jday)
    day = 0
    month = 0
    year = 0
    nowruz = epoch

    if jday >= epoch:
        # positive date
        year = 1
        cycles = (jday - nowruz) // cycle33
        year += (33 * cycles)
        nowruz += (cycle33 * cycles)
        curryear = False
        while curryear == False:
            if year % 33 in leap_years_an:
                if jday - nowruz < 366:
                    curryear = True
                else:
                    year += 1
                    nowruz += 366
            else:
                if jday - nowruz < 365:
                    curryear = True
                else:
                    year += 1
                    nowruz += 365
                
        if year % 33 in leap_years_an:
            m = months.KURDISH_LEAP
        else:
            m = months.KURDISH_NORMAL

    else:
        # negative dates
        cycles = (nowruz - jday) // cycle33
        year -= (33 * cycles)
        nowruz -= (cycle33 * cycles)
        while nowruz > jday:
            year -= 1
            if abs(year) % 33 in leap_years_bn:
                nowruz -= 366
            else:
                nowruz -= 365

        if abs(year) % 33 in leap_years_bn:
            # leap year
            m = months.KURDISH_LEAP
        else:
            # not a leap year
            m = months.KURDISH_NORMAL

    delta = jday - nowruz
    for i in m.keys():
        if delta < m[i]:
            month = i
            day = delta + 1
            break
        else:
            delta -= m[i]

    return (day, month, year)

