#!/usr/bin/python

#
# Convert a date in the Assyrian Calendar to a Julian Day
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
            if (y % 400) in leap_years_assyrian.PD:
                days += 366
            else:
                days += 365

        if (year % 400) in leap_years_assyrian.PD:
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
        alpha = -13387

        if (year % 400) in leap_years_assyrian.AD:
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
            if (y % 400) in leap_years_assyrian.ZO:
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
            if y in leap_years_assyrian.PD:
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
            if year in leap_years_assyrian.PD:
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
        delta = -13387 - jday

        while delta > 0:
            if (year % 400) in leap_years_assyrian.ZO:
                year += 1
                delta -= 366
            else:
                year += 1
                delta -= 365

        if (year % 400) in leap_years_assyrian.AD:
            m = months.ASSYRIAN_LEAP
        else:
            m = months.ASSYRIAN_NORMAL

        year = 0 - year
        delta = 0 - delta

        if delta == 0:
            year -= 1
            if (year % 400) in leap_years_assyrian.AD:
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
        


