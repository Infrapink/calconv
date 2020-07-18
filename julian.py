#!/usr/bin/python

#
# Convert between the Julian Calendar and Julian Day
#

import months

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
            if y % 4 == 0:
                days += 366
            else:
                days += 365

        if year % 4 == 0:
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

        if (year - 1) % 4 == 0:
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
            if y % 4 == 0:
                days -= 366
            else:
                days -= 365

    jday = alpha + days
    return jday

def fromjd(jday):
    """Convert the Julian Day to a date in the Julian Calendar"""
    jday = int(jday)
    year = 0
    month = ""
    day = 0
    m = None
    d = 0

    if jday > 1721422:
        # positive date
        delta = jday - 1721422
        year_4 = delta // cycle4
        delta %= cycle4
        single_years = delta // 365
        delta %= 365
        year = (4 * year_4) + single_years + 1 # need to add 1 to account for the lack of year 0
        if year % 4 == 0:
            # leap year
            m = months.CAESAR_LEAP
        else:
            # not a leap year
            m = months.CAESAR_NORMAL
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
        delta = 1721423 - jday
        # This guarantees a nonzero value for delta
        # Because we are counting backwards, it is the first and not the fourth year of the 4-year cycle
        # that has 366 days in it.
        # But we're starting at year 0, which will be corrected later.

        while delta > 0:
            if year % 4 == 0:
                year += 1
                delta -= 366
            else:
                year += 1
                delta -= 365

        # delta is now 0 or negative, and year is the negative of the actual year.
        if (year - 1) % 4 == 0:
            # leap year
            m = months.CAESAR_LEAP
            delta = 0 - delta + 1
        else:
            # not a leap year
            m = months.CAESAR_NORMAL
            delta = 0 - delta + 1

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]
        year = 0 - year
        date = (day,month,year)
        return date

    date = (day,month,year)
    return date
