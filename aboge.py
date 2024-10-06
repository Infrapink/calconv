#!/usr/bin/python3

# A programme to convert between Julian Days and the Javanese Aboge calendar

from months import JAVANESE as MONTHS

epoch = 2385728 # 1 Sura 1555; years given will have to be modified by 1555 for the maths to work.
windu = 2835 # 8 years
kurup = (15 * windu) - 1 # 120 years

MONTH_LENGTHS = {354: (30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29), # normal years
                 355: (30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 30)} # leap years
leap_rems = (0, 3, 6)

def yeartype(year):
    '''Compute the number of days in a year'''
    year = int(year)

    if (year % 120 == 0):
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
    year = int(year) - 1747 # assume the year of implementation is 0

    # step through the cycles
    k = year // 120 # kurups past
    y = 120 * k
    jday = epoch + (k * kurup)

    while (y + 120 <= year):
        y += 120
        jday += kurup
    while (y > year):
        y -= 120
        jday -= kurup

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
    k = (jday - epoch) // kurup # total kurups past
    year = 120 * k
    nyd = epoch + (k * kurup)

    while (nyd + kurup <= jday):
        nyd += kurup
        year += 120
    while (nyd > jday):
        nyd -= kurup
        year -= 120
    while (nyd + windu <= jday):
        nyd += windu
        year += 8
    while (nyd + yeartype(year) <= jday):
        nyd += yeartype(year)
        year += 1
    year += 1747 # add 1747 to make it agree with Javanese Śaka

    # compute the month
    m = 0
    while (nyd + MONTH_LENGTHS[yeartype(year)][m] <= jday):
        nyd += MONTH_LENGTHS[yeartype(year)][m]
        m += 1
    month = MONTHS[m]

    # compute the day
    day = jday - nyd + 1 # add 1 because humans count from 1

    return (day, month, year)
