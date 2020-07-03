#!/usr/bin/python

#
# Convert a date in the Parker Calendar to a Julian Day
#

import months

def convert(day, month, year):

    day = int(day)
    month = month.title()
    year = int(year)
    days = 0

    if year > 0:
        alpha = 1721424
        for y in range(1, year):
            if (y % 10000) in (2800,5600,8400):
                days += 365
            elif y % 400 == 0:
                days += 366
            elif y % 100 == 0:
                days += 365
            elif y % 4 == 0:
                days += 366
            else:
                days += 365

        if (year % 10000) in (2800,5600,8400):
            # not leap year
            m = months.CAESAR_MONTHS_NORMAL
        elif year % 400 == 0:
            # leap year
            m = months.CAESAR_MONTHS_LEAP
        elif year % 100 == 0:
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL
        elif year % 4 == 0:
            # leap year
            m = months.CAESAR_MONTHS_LEAP
        else:
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL
        for i in m.keys():
            if i == month:
                days += day
                break
            else:
                days += m[i]
    else:
        alpha = 1721425
        year = 0 - year

        if ((year - 1) % 10000) in(2800,5600,8400):
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL
        elif (year - 1) % 400 == 0:
            # leap year
            m = months.CAESAR_MONTHS_LEAP
        elif (year - 1) % 100 == 0:
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL
        elif (year - 1) % 4 == 0:
            # leap year
            m = months.CAESAR_MONTHS_LEAP
        else:
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL

        for i in m.keys():
            if i == month:
                days += day - 1
                break
            else:
                days += m[i]

        for y in range(0, year):
            if (y % 10000) in (2800,5600,8400):
                days -= 365
            elif y % 400 == 0:
                days -= 366
            elif y % 100 == 0:
                days -= 365
            elif y % 4 == 0:
                days -= 366
            else:
                days -= 365
    jday = alpha + days
    return jday
