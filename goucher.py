#!/usr/bin/python

#
# Convert between the Goucher-Parker calendar and Julian day
#

import months

cycle128 = (128 * 365) + 31
cycle4 = (4 * 365) + 1

def tojd(day, month, year):

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
            m = months.CAESAR_NORMAL
        elif year % 4 == 0:
            # leap year
            m = months.CAESAR_LEAP
        else:
            # not a leap year
            m = months.CAESAR_NORMAL

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
            m = months.CAESAR_NORMAL
        elif (year - 1) % 4 == 0:
            # leap year
            m = months.CAESAR_LEAP
        else:
            # not a leap year
            m = months.CAESAR_NORMAL

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

def fromjd(jday):
    """Convert a Julian day to a date in the Goucher-Parker calendar."""
    jday = int(jday)
    year = 0
    month = ""
    day = 0

    if jday > 1721422:
        # positive date
        delta = jday - 1721422
        year_128 = delta // cycle128
        delta %= cycle128
        year_4 = delta // cycle4
        delta %= cycle4
        single_years = delta // 365
        delta %= 365
        year = (128 * year_128) + (4 * year_4) + single_years + 1 # need to add 1 to account for the lack of year 0
        if year % 128 == 0:
            # not a leap year
            m = months.CAESAR_NORMAL
        elif year % 4 == 0:
            # leap year
            m = months.CAESAR_LEAP
        else:
            # not a leap year
            m = months.CAESAR_NORMAL

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    else:
        # negative date
        delta = 1721423 - jday
        while delta > 0:
            if year % 128 == 0:
                delta -= 365
            elif year % 4 == 0:
                delta -= 366
            else:
                delta -= 365
            year += 1

        if (year - 1) % 128 == 0:
            # not a leap year
            m = months.CAESAR_NORMAL
        elif (year - 1) % 4 == 0:
            # leap year
            m = months.CAESAR_LEAP
        else:
            # not a leap yer
            m = months.CAESAR_NORMAL

        year = 0 - year
        delta = 0 - delta + 1
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = (day,month,year)
    return date
