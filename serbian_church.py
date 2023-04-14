#!/usr/bin/python3

#
# Convert between the Serbian church calendar and Julian day
#

from months import CAESAR_NORMAL, CAESAR_LEAP

epoch = 1721426 # New Year's Day of the year 1 AD
cycle900 = (900 * 365) + (900 // 4) - 7
century = (100 * 365) + 24
quad = (4 * 365) + 1 # 4-year cycle
y400 = (4 * century) + 1 # first 400 years of a 900-year cycle

def yeartype(year):
    '''Determine number of days in the year'''
    year = int(year)

    if (year % 900) in (0, 400):
        # leap year
        ans = 366
    else:
        # normal year
        ans = 365

    return ans

def centype(year):
    '''Determine number of days in a century.'''
    year = int(year)

    if (year % 900) in (301, 801):
        # last year of the century is a leap year
        ans = century + 1
    else:
        # last year of the century is a normal year
        ans = century

    return ans

def qtype(year):
    '''Determine number of days in a four-year period.'''
    year = int(year)

    if (year % 900) in (397, 897):
        # last year of the group is a leap year
        ans = quad
    elif (year % 100 == 7):
        # last year of the group is a normal year
        ans = quad - 1
    else:
        # last year of the group is a leap year
        ans = quad

    return ans

def tojd(day, month, year):

    day = int(day)
    month = month.title()
    year = int(year)

    cycles = (year - 1) // 900
    y = (900 * cycles) + 1
    jday = epoch + (cycles * cycle900) # start of the current 900-year cycle
    while (y > year):
        jday -= cycle900
        y -= 900
    while (y + 900 <= year):
        jday  += cycle900
        y += 900

    if (year - y > 400):
        y += 400
        jday += y400

    while (y + 100 <= year):
        jday += centype(year)
        y += 100

    while (y + 4 <= year):
        jday += qtype(year)
        y += 4

    while (y < year):
        jday += yeartype(y)
        y += 1

    if yeartype(year) == 366:
        # leap year
        MONTHS = CAESAR_LEAP
    else:
        # normal year
        MONTHS = CAESAR_NORMAL

    for m in MONTHS.keys():
        if (m == month):
            jday = jday + day - 1
            break
        else:
            jday += MONTHS[m]

    return(jday)

def fromjd(jday):
    """Convert a Julian day to a date in the Serbian church calendar."""
    jday = int(jday)

    cycles = (jday - epoch) // cycle900
    nyd = epoch + (cycles * cycle900)
    year = (900 * cycles) + 1
    while (nyd + cycle900 <= jday):
        year += 900
        nyd += cycle400
    while (nyd > jday):
        year -= 900
        nyd -= cycle900

    if (nyd + y400 <= jday):
        year += 400
        nyd += y400

    while (nyd + centype(year) <= jday):
        nyd += centype(year)
        year += 100

    while (nyd + qtype(year) <= jday):
        nyd += qtype(year)
        year += 4

    while (nyd + yeartype(year) <= jday):
        nyd += yeartype(year)
        year += 1

    if yeartype(year) == 366:
        # leap year
        MONTHS = CAESAR_LEAP
    else:
        # normal year
        MONTHS = CAESAR_NORMAL

    d = nyd

    for m in MONTHS.keys():
        if (d + MONTHS[m] > jday):
            break
        else:
            d += MONTHS[m]

    month = m
    day = jday - d + 1

    return (day, month, year)
