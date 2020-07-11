#!/usr/bin/python

#
# Convert a date in the Coptic Calendar to a Julian Day

import months

cycle4 = (4 * 365) + 1

def tojd(day, month, year):

    day = int(day)
    month = month.title()
    year = int(year)
    days = 0

    if year > 0:
        # positive years. day 0 is 1825028
        alpha = 1825028
        for y in range(1, year):
            if y % 4 == 0:
                days += 366
            else:
                days += 365

        if year % 4 == 0:
            # leap year
            m = months.COPTIC_LEAP
        else:
            # not a leap year
            m = months.COPTIC_NORMAL
        for i in m.keys():
            if i == month:
                days += day
                break
            else:
                days += m[i]
    else:
        # negative years. day 0  is 1825029
        alpha = 1825029
        year = 0 - year

        if (year - 1) % 4 == 0:
            # leap year
            m = months.COPTIC_LEAP
        else:
            # not a leap year
            m = months.COPTIC_NORMAL

        for i in m.keys():
            if i == month:
                days += day - 1
                break
            else:
                days += m[i]

        for y in range(0, year):
            if y % 4 == 0:
                days -= 366
            else:
                days -= 365

    jday = alpha + days
    return jday

def fromjd(jday):
    """Convert a Julian Day to a date in the Coptic Calendar"""
    jday = int(jday)
    day = 0
    month = ""
    year = 0
    d = 0
    m = None

    if jday > 1825028:
        # positive date
        delta = jday - 1825028
        year_4 = delta // cycle4
        delta = delta % cycle4
        single_years = delta // 365
        delta = delta % 365
        year = (4 * year_4) + single_years + 1 # add 1 year to account for the lack of year 0
        if year % 4 == 0:
            # leap year
            m = months.COPTIC_LEAP
        else:
            # not a leap year
            m = months.COPTIC_NORMAL
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
        delta = 1825029 - jday

        while delta > 0:
            if year % 4 == 0:
                year += 1
                delta -= 366
            else:
                year += 1
                delta -= 365

        if (year - 1) % 4 == 0:
            # leap year
            m = months.COPTIC_LEAP
        else:
            # not a leap year
            m = months.COPTIC_NORMAL

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
