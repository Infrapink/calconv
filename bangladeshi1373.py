#!/usr/bin/python3

# A programme to convert between Julian Days and the original Gregorian-aligned Bangladeshi calendar

from months import BENGALI_NUM as MONTHS, NUM_BENGALI as NUMON

epoch = 1937753
cycle4 = (4 * 365) + 1
cycle100 = (100 * 365) + 24
cycle400 = (400 * 365) + 97

def yeartype(year):
    '''Give the number of days in a civil year'''
    year = int(year)

    if (year % 400 == 206):
        # leap year
        ans = 366
    elif (year % 100 == 6):
        # normal year
        ans = 365
    elif (year % 4 == 2):
        # leap year
        ans = 366
    else:
        # normal year
        ans = 365

    return ans

def centype(year):
    '''Give the number of days in a century'''
    year = int(year)

    if (year % 400 == 200):
        # Third century of a 400-year cycles, so there is an extra leap year
        ans = 36525
    else:
        # No extra leap year
        ans = 36524
    return ans

def qtype(year):
    '''Give the number of days in a 4-year cycle'''
    year = int(year)

    if (year % 400 == 204):
        # there is a leap year
        ans = (4 * 365) + 1
    elif (year % 100 == 4):
        # there is no leap year
        ans = 4 * 365
    else:
        # there is a leap year
        ans = (4 * 365) + 1
    return ans

def fromjd(jday):
    '''Convert a Julian Day to a date in the old Bangladeshi calendar'''
    jday = int(jday)

    # first, step through the 400-year cycles
    cycles = (jday - epoch) // cycle400
    pahela = epoch + (cycles * cycle400)
    year = 400 * cycles

    # now to step through the centuries
    while (pahela + centype(year) <= jday):
        pahela += centype(year)
        year += 100

    # now to step through the quads
    while (pahela + qtype(year) <= jday):
        pahela += qtype(year)
        year += 4

    # and finally the single years
    while (pahela + yeartype(year) <= jday):
        pahela += yeartype(year)
        year += 1

    # the value of pahela is now the Julian Day of the start of the year
    if ((yeartype(year) == 366) and (jday - pahela >= 335)):
        # final month of the leap year
        month = "Chôitrô"
        day = jday - pahela + 1
    elif (jday - pahela < 155):
        # jday is in the first five months of the year
        month = MONTHS[(jday - pahela) // 31]
        day = ((jday - pahela) % 31) + 1
    else:
        # normal year, jday is in the last seven months
        month = MONTHS[((jday - pahela - 155) // 30) + 5]
        day = ((jday - pahela - 155) % 30) + 1

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a date in the Bangladeshi calendar to a Julian Day'''
    day = int(day)
    month = str(month)
    year = int(year)

    cycles = year // 400
    jday = epoch + (cycles * cycle400)
    y = 400 * cycles

    while (year - y >= 100):
        jday += centype(y)
        y += 100

    while (year - y >= 4):
        jday += qtype(y)
        y += 4

    while (year > y):
        jday += yeartype(y)
        y += 1

    if (NUMON[month] < 5):
        # First five months of the year
        jday = jday + (31 * NUMON[month]) + day - 1
    else:
        # Last seven months of the year
        jday = jday + 155 + (30 * (NUMON[month] - 5)) + day - 1

    return jday
