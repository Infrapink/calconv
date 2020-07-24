#!/usr/bin/python

#
# Convert between the Assyrian Calendar and Julian Day
#

import months
import leap_years_assyrian

cycle4 = (4 * 365) + 1
cycle100 = (100 * 365) + 24
cycle400 = (400 * 365) + 97

def tojd(day,month,year):

    day = int(day)
    month = month
    year = int(year)
    days = 0

    if year > 0:
        # positive year
        alpha = -13388
        for y in range(1,year):
            if y % 400 == 349:
                days += 366
            elif y % 100 == 49:
                days += 365
            elif y % 4 == 1:
                days += 366
            else:
                days += 365

        if year % 400 == 349:
            m = months.ASSYRIAN_LEAP
        elif year % 100 == 49:
            m = months.ASSYRIAN_NORMAL
        elif year % 4 == 1:
            m = months.ASSYRIAN_LEAP
        else:
            m = months.ASSYRIAN_NORMAL

        for i in m.keys():
            if i == month:
                days += day
                break
            else:
                days += m[i]

    else:
        # negative years
        year = 0 - year
        alpha = -13388

        if year % 400 == 51:
            m = months.ASSYRIAN_LEAP
        elif year % 100 == 51:
            m = months.ASSYRIAN_NORMAL
        elif year % 4 == 3:
            m = months.ASSYRIAN_LEAP
        else:
            m = months.ASSYRIAN_NORMAL
            
        for i in m.keys():
            if i == month:
                days += day
                break
            else:
                days += m[i]

        for y in range(0,year):
            if y % 400 == 51:
                days -= 366
            elif y % 100 == 51:
                days -= 365
            elif y % 4 == 3:
                days -= 366
            else:
                days -= 365

    jday = alpha + days
    return jday

def fromjd(jday):
    """Convert a Julian Day to a date in the Assyrian calendar."""
    jday = int(jday)
    day = 0
    month = ""
    year = 0
    leap = None

    if jday > -13388:
        # positive year
        delta = jday - -13388
        cycles = delta // cycle400
        delta %= cycle400


        for y in range(1,401):
            if y % 400 == 349:
                if delta <= 366:
                    m = months.ASSYRIAN_LEAP
                    single_year = y
                    break
                else:
                    delta -= 366
            elif y % 100 == 49:
                if delta <= 365:
                    m = months.ASSYRIAN_NORMAL
                    single_year = y
                    break
                else:
                    delta -= 365
            elif y % 4 == 1:
                if delta <= 366:
                    m = months.ASSYRIAN_LEAP
                    single_year = y
                    break
                else:
                    delta -= 366
            else:
                if delta <= 365:
                    m = months.ASSYRIAN_NORMAL
                    single_year = y
                    break
                else:
                    delta -= 365

        year = (400 * cycles) + single_year
        if delta == 0:
            year -= 1
            if year % 400 == 349:
                m = months.ASSYRIAN_LEAP
                delta = 366
            elif year % 100 == 49:
                m = months.ASSYRIAN_NORMAL
                delta = 365
            elif year % 4 == 1:
                m = months.ASSYRIAN_LEAP
                delta = 366
            else:
                m = months.ASSYRIAN_NORMAL
                delta = 365
                
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]
    else:
        # negative date
        delta = -13388 - jday
        steps = 0

        while delta > 0:
            if year % 400 == 51:
                year += 1
                delta -= 366
            elif year % 100 == 51:
                year += 1
                delta -= 365
            elif year % 4 == 3:
                year += 1
                delta -= 366
            else:
                year += 1
                delta -= 365

        if year % 400 == 51:
            m = months.ASSYRIAN_LEAP
        elif year % 100 == 51:
            m = months.ASSYRIAN_NORMAL
        elif year % 4 == 3:
            m = months.ASSYRIAN_LEAP
        else:
            m = months.ASSYRIAN_NORMAL

        year = 0 - year
        delta = 0 - delta

        if delta == 0:
            year -= 1
            if year % 400 == 51:
                m = months.ASSYRIAN_LEAP
                delta = 366
            elif year % 100 == 51:
                m = months.ASSYRIAN_NORMAL
                delta = 365
            elif year % 4 == 3:
                m = months.ASSYRIAN_LEAP
                delta = 366
            else:
                m = months.ASSYRIAN_NORMAL
                delta = 365
                

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = (day,month,year)
    return date
