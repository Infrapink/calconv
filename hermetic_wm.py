#!/usr/bin/python

# Convert between the Hermetic Leap Week calendar and Julian Days

from months import WEEKDAYS_EN as weekdays, DAYNO_EN as dayno

epoch = 1721419 - 364 # First Monday of the year 0, rather than 1 as Meyer has it
cycle400 = (400 * 365) + 97 # days in 400 years

months = ("Arcturus", "Bellatrix", "Canopus", "Deneb", "Elanth", "Formalhaut", "Girtab", "Hadar", "Izar", "Jabbah", "Kochab", "Lesath")

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
    while (n > jday):
        year -= 1
        n -= leap(year)

    # compute the month and day
    if (jday - n > 364):
        # leap week
        month = "Lesath"
        day = jday - n + 337
    else:
        q = (jday - n) // 91
        m = 3 * q
        n += (91 * q)
        if (jday - n >= 35):
            m += 1
            n += 35
            while (jday - n >= 28):
                n += 28
                m += 1
        month = months[m]
        day = (jday - n) + 1

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a date in the Hermetic Leap Week calendar to a Julian Day'''
    day = int(day) - 1
    month = str(month)
    year = int(year)

    jday = nyd(year)
    m = 0
    while (months[m] != month):
        if (not(month in (months[m], months[m + 1], months[m + 2]))):
            m += 91
        elif (m % 3 == 0):
            jday += 35
        else:
            jday += 28
        m += 1
    jday += day
    return jday
