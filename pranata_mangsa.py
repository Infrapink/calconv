#!/usr/bin/python3

# Convert between Pranata Mangsa and Julian Days

epoch = 2398849
cycle400 = (400 * 365) + 97

MONTHS = ("Mangsa Kasa", "Mangsa Karo", "Mangsa Katelu", "Mangsa Kapat", "Mangsa Kalima", "Mangsa Kanem", "Mangsa Kapitu", "Mangsa Kawolu", "Mangsa Kasanga", "Mangsa Kasadasa", "Mangsa Desta", "Mangsa Saddha")
MONTHDAYS = {365: (41, 23, 24, 25, 27, 43, 43, 26, 25, 24, 23, 41),
             366: (41, 23, 24, 25, 27, 43, 43, 27, 25, 24, 23, 41)}


def yeartype(year):
    '''Compute the days in a year'''
    year = int(year)

    if (year % 400 == 145):
        ans = 366
    elif (year % 100 == 45):
        ans = 365
    elif (year % 4 == 1):
        ans = 366
    else:
        ans = 365

    return ans

def qtype(year):
    '''Compute the days in a 4-year period starting with year'''
    year = int(year)

    if (year % 400 == 145):
        ans = (4 * 365) + 1
    elif (year % 100 == 45):
        ans = 4 * 365
    else:
        ans = (4 * 365) + 1

    return ans

def tojd(day, month, year):
    '''Convert a date in the Pranata Mangsa to Julian Days'''
    day = int(day) - 1 # subtract 1 because computers count from 0
    month = str(month)
    year = int(year)

    # account for the year
    cycles = year // 400
    y = 400 * cycles
    jday = epoch + (cycles * cycle400)

    while (y + 4 <= year):
        jday += qtype(y)
        y += 4

    while (y < year):
        jday += yeartype(y)
        y += 1

    # account for the month
    m = 0
    while (MONTHS[m] != month):
        jday += MONTHDAYS[yeartype(y)][m]
        m += 1

    # account for the day
    jday += day

    return jday

def fromjd(jday):
    '''Convert a Julian Day into a date in Pranata Mangsa'''
    jday = int(jday)

    # cover the 400-year cycles
    cycles = (jday - epoch) // cycle400
    year = 400 * cycles
    nyd = epoch + (cycles * cycle400)
    while (nyd + cycle400 <= jday):
        year += 400
        nyd += cycle400
    while (nyd > jday):
        year -= 400
        nyd -= cycle400

    # cover the 4-year cycles
    while (nyd + qtype(year) <= jday):
        nyd += qtype(year)
        year += 4

    # compute the year and new year's day
    while (nyd + yeartype(year) <= jday):
        nyd += yeartype(year)
        year += 1

    
    # compute the month
    m = 0
    while (nyd + MONTHDAYS[yeartype(year)][m] <= jday):
        nyd += MONTHDAYS[yeartype(year)][m]
        m += 1
    month = MONTHS[m]

    # finally, the day
    day = jday - nyd + 1 # add 1 because humans don't count from 0

    return (day, month, year)
