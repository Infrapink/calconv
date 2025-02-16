#!/usr/bin/python3

# Convert between Julian Days and Peter Meyer's Archetype calendar

epoch = 897474 # New Year's Day of year 443
arc_cycle = 658532 # total days in 1803 years

MONTHS = ("Apollo", "Diana", "Hermes", "Aphrodite", "Ares", "Zeus", "Chronos", "Prometheus", "Orpheus", "Sophia", "Dionysus", "Demeter", "Persephone")
MONTH_LENGTHS = {354: (30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29),     # normal regular year
                 355: (30, 29, 30, 29, 30, 29, 30, 29, 30, 30, 30, 29),     # normal leap year
                 384: (30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30), # long regular year
                 385: (30, 29, 30, 29, 30, 29, 30, 29, 30, 30, 30, 29, 30)} # long leap year

def year_length(year):
    '''Compute the number of days in the year'''
    pos = ((int(year) + 1360) % 1803) + 1 # position of the year in the cycle

    ans = 354 + (30 * int((((664 * pos) + 901) % 1803) < 664)) + int((((350 * pos) + 901) % 1803) < 350)

    return ans

def nyd(year):
    '''Compute New Year's Day for a given year'''
    year = int(year)
    cycles = (year - 443) // 1803
    y = 1803 * cycles
    ans = epoch + (cycles * arc_cycle)

    while (y + 1803 <= year):
        y += 1803
        ans += arc_cycle
    while (y < year):
        ans += year_length(y)
        y += 1

    return ans

def fromjd(jday):
    '''Convert a Julian Day to a date in the Archetypes calendar'''
    jday = int(jday)

    # compute the year
    year = int(round((jday - epoch) // 365.24237)) + 443 # add 443 because the epoch is for the year 443, not 0
    newmoon = nyd(year)
    while (newmoon > jday):
        year -= 1
        newmoon -= year_length(year)
    while (newmoon + year_length(year) <= jday):
        newmoon += nyd(year)
        year += 1

    # compute the month
    month_lengths = MONTH_LENGTHS[year_length(year)]
    m = 0
    while (newmoon + month_lengths[m] <= jday):
        newmoon += month_lengths[m]
        m += 1
    month = MONTHS[m]

    # compute the day
    day = (jday - newmoon) + 1 # add 1 because humans don't count from 0

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a date in the Archetypes calendar to a Julian Day'''
    day = int(day) - 1 # subtract 1 because computers count from 0
    month = str(month)
    year = int(year)

    # account for the year
    jday = nyd(year)

    # account for the month
    month_lengths = MONTH_LENGTHS[year_length(year)]
    m = 0
    while (MONTHS[m] != month):
        jday += month_lengths[m]
        m += 1

    # account for the day
    jday += day

    return jday
