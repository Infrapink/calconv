#!/usr/bin/python

#
# Convert a date in the Goucher-Parker calendar to a Julian day
#

import months

def convert(day, month, year):

    day = int(day)
    month = month.title()
    year = int(year)
    alpha = 0
    days = 0

    if year > 0:
        # positive years. day 0 is 1721422
        alpha = 1721422
        for y in range(1,year):
            if y % 128 == 0:
                days += 365
            elif y % 4 == 0:
                days += 366
            else:
                days += 365

        if year % 128 == 0:
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
        # negative years. count backwards. day 0 is 1721423
        alpha = 1721423
        year = 0 - year

        if (year - 1) % 128 == 0:
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
                
        for y in range(0,year):
            if y % 128 == 0:
                days -= 365
            elif y % 4 == 0:
                days -= 366
            else:
                days -= 365

    jday = alpha + days
    return jday
