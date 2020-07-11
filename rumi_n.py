#!/usr/bin/python

#
# Convert a date in the Rumi Calendar to a Julian Day
#

import months

def tojd(day, month, year):

    day = int(day)
    month = month.title()
    year = int(year)
    alpha = 0
    days = 0

    if year > 0:
        # positive years. day 0 is 1721422
        alpha = 1948242
        for y in range(1,year):
            if (y + 2) % 4 == 0:
                days += 366
            else:
                days += 365

        if (year + 2) % 4 == 0:
            # leap year
            m = months.TURKISH_LEAP
        else:
            # not a leap year
            m = months.TURKISH_NORMAL

        for i in m.keys():
            if i == month:
                days += day
                break
            else:
                days += m[i]

    else:
        # negative years. count backwards. day 0 is 1721423
        alpha = 1948243
        year = 0 - year

        if abs(year +2) % 4 == 0:
            # leap year
            m = months.TURKISH_LEAP
        else:
            # not a leap year
            m = months.TURKISH_NORMAL

        for i in m.keys():
            if i == month:
                days += day - 1
                break
            else:
                days += m[i]
                
        for y in range(0,year):
            if (y - 1) % 4 == 0:
                days -= 366
            else:
                days -= 365

    jday = alpha + days
    return jday

def fromjd(jday):
    """Convert a Julian day to a date in the Rumi calendar."""
    jday = int(jday)
    year = 0
    month = ""
    day = 0

    if jday > 1948242:
        # positive dates
        delta = jday - 1948242
        current = False
        while current == False:
            year += 1
            if (year + 2) % 4 == 0:
                if delta <= 366:
                    current = True
                else:
                    delta -= 366
            else:
                if delta <= 365:
                    current = True
                else:
                    delta -= 365

        if (year + 2) % 4 == 0:
            # leap year
            m = months.TURKISH_LEAP
        else:
            # not a leap year
            m = months.TURKISH_NORMAL

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    else:
        # negative dates
        delta = 1948243 - jday
        while delta > 0:
            if (year - 1) % 4 == 0:
                year += 1
                delta -= 366
            else:
                year += 1
                delta -= 365

        delta = abs(delta) + 1
        year = 0 - year

        if (abs(year) - 2) % 4 == 0:
            # leap year
            m = months.TURKISH_LEAP
        else:
            # not a leap year
            m = months.TURKISH_NORMAL

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = (day,month,year)
    return date
