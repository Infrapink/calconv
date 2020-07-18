#!/usr/bin/python

#
# Convert between the Ethiopian Calendar and Julian Day
#

import months

cycle4 = (4 * 365) + 1

def tojd(day, month, year):

    day = int(day)
    month = month.title()
    year = int(year)
    days = 0

    if year > 0:
        # positive years
        alpha = 1724221
        for y in range (1, year):
            if y % 4 == 0:
                days += 366
            else:
                days += 365

        if year % 4 == 0:
            # leap year
            m = months.ETHIOPIAN_LEAP
        else:
            # not a leap year
            m = months.ETHIOPIAN_NORMAL
        for i in m.keys():
            if i == month:
                days += day
                break
            else:
                days += m[i]
    else:
        # negative years
        alpha = 1724222
        year = 0 - year
        if (year - 1) % 4 == 0:
            # leap year
            m = months.ETHIOPIAN_LEAP
        else:
            # not a leap year
            m = months.ETHIOPIAN_NORMAL

        for i in m.keys():
            if i == month:
                days += day - 1
                break
            else:
                days += m[i]

        for y in range(0,year):
            if y % 4 == 0:
                days -= 366
            else:
                days -= 365

    jday = alpha + days
    return jday

def fromjd(jday):
    """Convert a Julian Day to a date in the Ethiopian calendar"""
    jday = int(jday)
    year = 0
    month = ""
    day = 0
    m = None
    d = 0

    if jday > 1724221:
        # positive date
        delta = jday - 1724221
        year_4 = delta // cycle4
        delta = delta % cycle4
        single_years = delta // 365
        delta = delta % 365
        year = (4 * year_4) + single_years + 1 # while there is a year 0, Ethiopians still reckon Jesus was born in the year 1
        if year % 4 == 0:
            # leap year
            m = months.ETHIOPIAN_LEAP
        else:
            # not a leap year
            m = months.ETHIOPIAN_NORMAL
        if delta == 0:
            delta = 365
            year -= 1
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    else:
        # negative date
        delta = 1724222 - jday

        while delta > 0:
            if year % 4 == 0:
                year += 1
                delta -= 366
            else:
                year += 1
                delta -= 365

        if (year %4) == 0:
            # leap year
            m = months.ETHIOPIAN_LEAP
        else:
            # not a leap year
            m = months.ETHIOPIAN_NORMAL

        year = 0 - year
        delta = 0 - delta + 1

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = [day, month, year]
    return(date)
