#!/usr/bin/python3

# A programme to convert between Julian Days and the Javanese lunar calendar, where Amiswon is the short kurup.

from months import JAVANESE as MONTHS

epoch = 2317690 # 1 Sura 1555; years given will have to be modified by 1554 for the maths to work.
windu = 2835 # 8 years
kurup = (15 * windu) - 1 # 120 years
sk = (9 * windu) - 1 # short kurup; 72 years
cycle = (4 * kurup) + sk # cycle of 552 years; 4 kurups and 1 short kurup

MONTH_LENGTHS = {354: (30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29), # normal years
                 355: (30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 30)} # leap years
leap_rems = (0, 3, 6)

def yeartype(year):
    '''Compute the number of days in a year'''
    year = int(year)

    if (year % 552 in (120, 192, 312, 432, 0)):
        # would be leap but it's normal
        ans = 354
    elif (year % 8 in leap_rems):
        # leap year
        ans = 355
    else:
        # normal year
        ans = 354

    return ans

def tojd(day, month, year):
    '''Convert a date in the Javenese lunar calendar to a Julian Day'''
    day = int(day) - 1 # subtract 1 because humans don't count from 0
    month = str(month)
    year = int(year) - 1555 # assume the year of implementation is 0

    # step through the cycles
    cycles = year // 552
    jday = epoch + (cycles * cycle)
    y = 552 * cycles
    if (y + 120 <= year):
        y += 120
        jday += kurup
        print(jday)

        if (y + 72 <= year):
            y += 72
            jday += sk
            print(jday)

        while (y + 120 <= year):
            y += 120
            jday += kurup

    # we are now at the start of a kurup
    while (y + 8 <= year):
        y += 8
        jday += windu
    while (y < year):
        jday += yeartype(y)
        y += 1

    # we are now at the start of the year
    # account for the month
    m = 0
    month_lengths = MONTH_LENGTHS[yeartype(year)]
    while (MONTHS[m] != month):
        jday += month_lengths[m]
        m += 1

    # add the day and bring it home
    jday += day

    return jday

def fromjd(jday):
    '''Compute a date in the Javenese lunar calendar from a Julian Day'''
    jday = int(jday)

    # compute the year
    cycles = (jday - epoch) // cycle
    year = 552 * cycles
    nyd = epoch + (cycles * cycle) # new year's day

    if (nyd + kurup <= jday):
        nyd += kurup
        year += 120

        if (nyd + sk <= jday):
            nyd += sk
            year += 72
        while (nyd + kurup <= jday):
            nyd += kurup
            year += 120
    while (nyd + windu <= jday):
        nyd += windu
        year += 8
    while (nyd + yeartype(year) <= jday):
        nyd += yeartype(year)
        year += 1
    year += 1555 # add 1555 to make it agree with Javanese Śaka

    # compute the month
    m = 0
    while (nyd + MONTH_LENGTHS[yeartype(year)][m] <= jday):
        nyd += MONTH_LENGTHS[yeartype(year)][m]
        m += 1
    month = MONTHS[m]

    # compute the day
    day = jday - nyd + 1 # add 1 because humans count from 1

    return (day, month, year)
