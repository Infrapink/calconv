#!/usr/bin/python3

# A programme to convert between consecutive Julian Days and the tropical Nanakshahi calendar

from months import NUM_NANAKSHAHI as NUMON, NANAKSHAHI_NUM as MONTHNO

cycle4 = (365 * 4) + 1 # days in a normal 4-year cycle
cycle100 = 36524 # days in a normal century
cycle400 = (365 * 400) + 97 # days in a 400-year cycle

epoch = 2257309 # 1 Chet 0, equal to 14 March 1468

def yeartype(year):
    '''Determine if a given year is leap or not'''
    year = int(year)

    if (year % 400 == 131):
        # leap year
        ans = 366
    elif (year % 100 == 31):
        # normal year
        ans = 365
    elif (year % 4 == 3):
        # leap year
        ans = 366
    else:
        # normal year
        ans = 365

    return ans

def quadtype(year):
    '''Determine days in a 4-year cycle'''
    year = int(year)

    if (year % 4 != 0):
        print("ERROR! Invalid argument passed to quadtype()")
    elif (year % 400 == 128):
        ans = cycle4
    elif (year % 100 == 28):
        ans = 4 * 365
    else:
        ans = cycle4

    return ans

def fromjd(jday):
    '''Convert a Julian Day to a date in the Nanakshahi calendar'''
    jday = int(jday)

    # first, account for the 400-year cycle
    cycles = (jday - epoch) // cycle400
    year = 400 * cycles
    nyd = epoch + (cycles * cycle400)

    # next, account for the centuries
    if (jday - nyd >= cycle100): # normal century
        year += 100
        nyd += cycle100

    if (jday - nyd >= 36525): # the second century of a 400-year cycle has an extra leap year
        year += 100
        nyd += 36525

    while (jday - nyd >= cycle100): # the last two centuries of the 400-year cycle are normal
        year += 100
        nyd += cycle100

    # next, account for the 4-year cycle
    while (jday - nyd >= quadtype(year)):
        nyd += quadtype(year)
        year += 4

    # and now account for individual years
    while (jday - nyd >= yeartype(year)):
        nyd += yeartype(year)
        year += 1

    # now we have the year
    # and nyd is the Julian Day of the start of the year
    if (jday - nyd <= 155):
        # first five months of the year
        month = NUMON[(jday - nyd) // 31]
        day = ((jday - nyd) % 31) + 1
    else:
        # last seven months of the year
        month = NUMON[((jday - nyd - 155) // 30) + 4]
        day = ((jday - nyd - 155) % 30) + 1

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a date in the tropical Nanakshahi calendar to a Julian Day'''
    day = int(day)
    month = str(month)
    year = int(year)

    cycles = year // 400
    jday = epoch + (cycles * cycle400)
    y = 400 * cycles

    if (year - y >= 100): # first century in a 400-year cycle is normal
        jday += cycle100
        y += 100

    if (year - y >= 100): # second century in a 400-year cycle has an extra leap day
        jday += 36525
        y += 100

    while (year - y >= 100): # last two centuries in a 400-year cycle are normal
        jday += cycle100
        y += 100

    while (year - y >= 4):
        jday += quadtype(y)
        y += 4

    while (year > y):
        jday += yeartype(y)
        y += 1

    m = MONTHNO[month]
    if (m <= 4):
        jday = jday + (31 * m) + day - 1
    else:
        jday = jday + 155 + (30 * (m - 4)) + day - 1

    return jday
