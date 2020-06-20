#!/usr/bin/python

#
# Convert a date in the Assyrian Calendar to a Julian Day
#

import months
import leap_years_assyrian

def convert(day,month,year):

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
            m = months.ASSYRIAN_MONTHS_LEAP
        else:
            m = months.ASSYRIAN_MONTHS_NORMAL

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
            m = months.ASSYRIAN_MONTHS_LEAP
        else:
            m = months.ASSYRIAN_MONTHS_NORMAL
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
