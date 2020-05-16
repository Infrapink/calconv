#!/usr/bin/python

import months

def convert(day, month, year):

    day = int(day)
    month = month.title()
    year = int(year)
    alpha = 1724221
    days = 0

    if year > 0:
        for y in range (1, year):
            if y % 4 == 0:
                days += 366
            else:
                days += 365

        if year % 4 == 0:
            # leap year
            m = months.ETHIOPIAN_MONTHS_LEAP
        else:
            # not a leap year
            m = months.ETHIOPIAN_MONTHS_NORMAL
        for i in m.keys():
            if i == month:
                days += day
                break
            else:
                days += m[i]
    else:
        year = 0 - year
        for i in range (0, year):
            if year % 4 == 0:
                days -= 366
            else:
                days -= 365
        if year % 4 == 0:
            # leap year
            m = months.ETHIOPIAN_MONTHS_LEAP
        else:
            # not a leap year
            m = months.ETHIOPIAN_MONTHS_NORMAL
        for i in m.keys():
            if i == month:
                days -= day
                break
            else:
                days -= m[i]
    jday = alpha + days
    return jday
