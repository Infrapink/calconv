#!/usr/bin/python

# Convert between the Hermetic Leap Week calendar and Julian Days

from months import WEEKDAYS_EN as weekdays, DAYNO_EN as dayno

epoch = 1721419 - 364 # First Monday of the year 0, rather than 1 as Meyer has it
cycle400 = (400 * 365) + 97 # days in 400 years

def leap(year):
    '''Return the number of days in a year'''
    year = int(year)

    if ((((year * 71) + 203) % 400)  < 71):
        # leap year
        ans = 371
    else:
        ans = 364

    return ans

def nyd(year):
    '''Return New Year's Day of a given year'''
    year = int(year)
    y = 400 * (year // 400)
    ans = epoch + (cycle400 * (year // 400))
    while (y < year):
        ans += leap(y)
        y += 1
    return ans

def fromjd(jday):
    '''Convert a Julian Day into a date in the Hermetic Leap Week calendar'''
    jday = int(jday)

    # compute the year
    year = (int(round((jday - epoch) // 365.2425)))
    n = nyd(year)
    while (n + leap(year) <= jday):
        n += leap(year)
        year += 1
    while (n > year):
        year -= 1
        n -= leap(year)

    # compute the week and day
    week = ((jday - n) // 7) + 1 # add 1 because humans don't count from 0
    day = weekdays[(jday - n) % 7]

    return (day, week, year)

def tojd(day, week, year):
    '''Convert a date in the Hermetic Leap Week calendar to a Julian Day'''
    day = dayno[str(day)]
    week = int(week) - 1 # subtract 1 because computers count from 0
    year = int(year)

    jday = nyd(year) + (7 * week) + day
    return jday
