#!/usr/bin/python3

# Convert between the new Byzantine calendar and Julian Days

from months import CAESAR as MONTHS, CAESAR_LENGTHS as MONTH_LENGTHS

epoch = -290815
cycle900 = (900 * 365) + (900 // 4) - 7

def year_length(year):
    '''Returns number of days in a year'''
    year = int(year)

    if (year % 900 in (308, 708)):
        ans = 366
    elif (year % 100 == 8):
        ans = 365
    elif (year % 4) == 0:
        ans = 366
    else:
        ans = 365

    return ans

def century(year):
    '''Returns number of days in a century starting with year'''
    year = int(year)

    if (((year % 900 <= 308) and ((year + 100) % 900 > 308)) or ((year % 900 <= 708) and ((year + 100) % 900 > 708))):
        # the century year is a leap year
        ans = 36525
    else:
        # the century year is not a leap year
        ans = 36524

    return ans

def qtype(year):
    '''Returns number of days in a 4-year period starting with year'''
    year = int(year)

    if (((year % 900 <= 308) and ((year + 4) % 900 > 308)) or ((year % 900 <= 708) and ((year + 4) % 900 > 708))):
        # there is a leap year
        ans = (4 * 365) + 1
    elif ((year % 900 <= 8) and ((year + 4) % 900 > 8)):
        # no leap year
        ans = 4 * 365
    else:
        # there is a leap year
        ans = (4 * 365) + 1

    return ans

def nyd(year):
    '''Compute the Julian Day on which New Year's Day falls for a given year'''
    year = int(year)

    cycles = year // 900
    y = 900 * cycles
    ans = epoch + (cycles * cycle900)
    while (y + 100 <= year):
        ans += century(y)
        y += 100
    while (y + 4 <= year):
        ans += qtype(y)
        y += 4
    while (y < year):
        ans += year_length(y)
        y += 1
        
    return ans
    

def fromjd(jday, z):
    '''Convert a Julian Day into a Byzantine date'''
    jday = int(jday)
    z = bool(z) # is there a year 0?

    # compute the year
    year = int((jday - epoch) // 365.2422)
    while (nyd(year) > jday):
        year -= 1
    while (nyd(year + 1) <= jday):
        year += 1

    # compute the month
    m = 8
    alpha = nyd(year)
    while (alpha + MONTH_LENGTHS[year_length(year)][m] <= jday):
        alpha += MONTH_LENGTHS[year_length(year)][m]
        m = (m + 1) % 12
    month = MONTHS[m]

    # compute the day
    day = jday - alpha + 1 # add 1 because humans don't count from 0
    if (year < 1):
        year -= int(not(z))

    return (day, month, year)

def tojd(day, month, year, z):
    '''Convert a Byzantine date to a Julian Day'''
    day = int(day) - 1 # subtract 1 because computers count from 0
    month = str(month)
    year = int(year)
    z = bool(z) # is it a leap year?

    # account for the year
    if (year < 0):
        year += int(not(z))
    jday = nyd(year)

    # account for the month
    m = 8
    while (MONTHS[m] != month):
        jday += MONTH_LENGTHS[year_length(year)][m]
        m = (m + 1) % 12

    # account for the day
    jday += day

    return jday
