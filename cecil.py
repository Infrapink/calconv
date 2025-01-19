#!/usr/bin/python3

# Convert between the Dee-Cecil calendar and Julian Days

from months import CAESAR as MONTHS, CAESAR_LENGTHS as MONTH_LENGTHS

epoch = 1721426 - 365 # 1 January of the year 0
cycle = (33 * 365) + 8 # days in a 33-year cycle
quad = (4 * 365) + 1 # days in a normal 4-year cycle

def leap(year):
    '''Return number of days in a year'''
    year = int(year)

    if (year % 33 == 0):
        # normal year
        ans = 365
    elif ((year % 33) % 4 == 0):
        # leap year
        ans = 366
    else:
        ans = 365

    return ans

def nyd(year):
    '''Compute the Julian Day corresponding to 1 January of year'''
    year = int(year)

    cycles = year // 33
    y = 33 * cycles
    ans = epoch + (cycles * cycle)

    if (y + 5 <= year):
        y += 5
        ans = ans + quad + 365

        while (y + 4 <= year):
            y += 4
            ans += quad

    while (y < year):
        ans += leap(y)
        y += 1

    return ans

def fromjd(jday):
    '''Convert a Julian Day into a date in the Dee-Cecil calendar'''
    jday = int(jday)

    # compute the year
    year = int((jday - epoch) // 365.2424)
    n = nyd(year)
    while (n > jday):
        year -= 1
        n -= leap(year)
    while (n + leap(year) <= jday):
        n += leap(year)
        year += 1

    # compute the month
    m = 0
    month_lengths = MONTH_LENGTHS[leap(year)]
    while (n + month_lengths[m] <= jday):
        n += month_lengths[m]
        m += 1
    month = MONTHS[m]

    # compute the day
    day = jday - n + 1 # add 1 because humans don't count from 0

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a date in the Dee-Cecil calendar to a Julian Day'''
    day = int(day) - 1 # subtract 1 because computers count form 0
    month = str(month)
    year = int(year)

    # account for the year
    jday = nyd(year)

    # account for the month
    m = 0
    month_lengths = MONTH_LENGTHS[leap(year)]
    while (MONTHS[m] != month):
        jday += MONTHS[m]
        m += 1

    # account for the day
    jday += day

    return jday
