#!/usr/bin/python3

# A program to convert between Julian Days and the Nepali solar calendar

from months import NUM_NEPALI as MONTHS, NEPALI_NUM as MONTHNO

epoch = 2042401

cycle4 = (4 * 365) + 1 # 4-year cycle
cycle400 = (400 * 365) + 97 # 400-year cycle

def yeartype(year):
    '''Compute the number of days in a year'''
    year = int(year)

    if (year % 400  == 320):
        # leap year
        ans = 366
    elif (year % 100 == 20):
        # normal year
        ans = 365
    elif (year % 4 == 0):
        # leap year
        ans = 366
    else:
        # normal year
        ans = 365

    return ans

def qtype(year):
    '''Determine if there is a leap year within the next 4 year'''
    year = int(year)

    if (year % 400 == 320):
        # there is a leap year
        ans = cycle4
    elif (year % 100 == 20):
        # there is no leap year
        ans = cycle4 - 1
    else:
        # there is a leap year
        ans = cycle4

    return ans

def fromjd(jday):
    '''Convert a Julian Day into a date in the Nepali solar calendar'''
    jday = int(jday)

    cycles = (jday - epoch) // cycle400
    year = 400 * cycles
    mhapuja = epoch + (cycles * cycle400)

    if (jday - mhapuja >= (3 * 36524)):
        year += 300
        mhapuja += (3 * 36524)
    else:
        while (mhapuja + 36524 <= jday):
            year += 100
            mhapuja += 36524

    while( mhapuja + qtype(year) <= jday):
        mhapuja += qtype(year)
        year += 4

    while( mhapuja + yeartype(year) <= jday):
        mhapuja += yeartype(year)
        year += 1

    if (mhapuja + yeartype(year) - 186 > jday):
        # first six months of the year
        month = MONTHS[(jday - mhapuja) // 30]
        day = ((jday - mhapuja) % 30) + 1
    else:
        # last six months of the year
        month = MONTHS[6 + ((jday - (mhapuja + yeartype(year) - 186) ) // 31)]
        day = ( (jday - (mhapuja + yeartype(year) - 186)) % 31) + 1

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a day in the Nepali solar calendar to a Julian Day'''
    day = int(day)
    month = str(month)
    year = int(year)

    cycles = year // 400
    y = 400 * cycles
    jday = epoch + (cycles * cycle400)
    if (year - y >= 300):
        y += 300
        jday += (3 * 36524)
    else:
        while (year - y >= 100):
            y += 100
            jday += 36524
    

    while (year - y >= 4):
        jday += qtype(y)
        y += 4
    while (year > y):
        jday += yeartype(y)
        y += 1

    if (MONTHNO[month] < 6):
        # first six months of the year
        jday = jday + (30 * MONTHNO[month]) + day - 1
    else:
        # last six months of the year
        jday = jday + yeartype(year) - 186 + (31 * (MONTHNO[month] - 6)) + day - 1

    return jday
