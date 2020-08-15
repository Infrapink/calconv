#!/usr/bin/python

#
# Convert between the skipping Rumi Calendar and Julian Day
#

import months

def tojd(day, month, year):

    day = int(day)
    month = month.title()
    year = int(year)
    alpha = 0
    days = 0
    skips = 0

    if year > 0:
        # positive years.
        alpha = 1948241
        for y in range(1,year):
            if y % 33 == 0:
                skips += 1
            elif (y - skips) % 4 == 2:
                days += 366
            else:
                days += 365

        if (year - skips) % 4 == 2:
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
        # negative years.
        alpha = 1948242

        for y in range(-1, (year - 1), -1):
            if abs(y) % 33 == 0:
                skips += 1
            elif (abs(y) - skips) % 4 == 1:
                days -= 366
            else:
                days -= 365

        if (abs(year) - skips) % 4 == 1:
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
                
    jday = alpha + days
    return jday

def fromjd(jday):
    """Convert a Julian day to a date in the Rumi calendar."""
    jday = int(jday)
    year = 0
    month = ""
    day = 0
    skips = 0

    if jday > 1948241:
        # positive dates
        delta = jday - 1948241
        current = False
        while current == False:
            year += 1
            if year % 33 == 0:
                skips += 1
            elif (year - skips) % 4 == 2:
                if delta <= 366:
                    current = True
                else:
                    delta -= 366
            else:
                if delta <= 365:
                    current = True
                else:
                    delta -= 365

        if (year - skips) % 4 == 2:
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
        delta = 1948242 - jday
        while delta > 0:
            year -= 1
            if abs(year) % 33 == 0:
                skips += 1
            elif (abs(year) - skips) % 4 == 1:
                delta -= 366
            else:
                delta -= 365


        delta = abs(delta) + 1

        if (abs(year) - skips) % 4 == 1:
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
