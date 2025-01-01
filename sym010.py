#!/usr/bin/python3

# Convert between Julian Days and Irv Bromberg's Symmetry 010 calendar

from months import CAESAR as MONTHS

epoch = 1721426 - 364 # 1st January of the year 0
cycle293 = (293 * 364) + (52 * 7) # length of a 293-year cycle with 52 leap weeks
month_lengths = {364: (30, 31, 30, 30, 31, 30, 30, 31, 30, 30, 31, 30), # normal years
                 371: (30, 31, 30, 30, 31, 30, 30, 31, 30, 30, 31, 37)} # leap years

def yearlen(year):
    '''Return the length of the year'''

    if ( ((52 * int(year)) + 146) % 293 < 52 ):
        ans = 371
    else:
        ans = 364

    return ans

def fromjd(jday):
    '''Convert a Julian Day into a date in Sym010'''
    jday = int(jday)

    # compute the year
    cycles = (jday - epoch) // cycle293
    year = cycles * 293
    nyd = epoch + (cycles * cycle293) # new year's day
    while (nyd + yearlen(year) <= jday):
        nyd += yearlen(year)
        year += 1

    # compute the month
    m = 0
    while (nyd + month_lengths[yearlen(year)][m] <= jday):
        nyd += month_lengths[yearlen(year)][m]
        m += 1
    month = MONTHS[m]

    # compute the day
    day = jday - nyd + 1 # add 1 because humans don't count from 0

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a date in Sym010 into a Julian Day'''
    day = int(day) - 1 # subtract 1 because computers count from 0
    month = str(month)
    year = int(year)

    # account for the year
    cycles = year // 293
    y = cycles * 293
    jday = epoch + (cycles * cycle293)
    while (y < year):
        jday += yearlen(y)
        y += 1

    # account for the month
    m = 0
    while (MONTHS[m] != month):
        jday += month_lengths[yearlen(year)][m]
        m += 1

    # account for the day
    jday += day

    return jday
