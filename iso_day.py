#!/usr/bin/python3

# Convert between Julian Days and the ISO-8601 day calendar

from solun import gregorian_nyd, gregorian_epoch

def tojd(day, year):
    '''Convert a year in the ISO day calendar to a Julian Day'''
    jday = gregorian_nyd(int(year), True) + int(day) - 1 # subtract 1 because humans don't count from 0
    return jday

def fromjd(jday):
    '''Convert a Julian Day to a date in the ISO day calendar'''
    jday = int(jday)

    year = int((jday - gregorian_epoch) // 365.2424)
    while (gregorian_nyd(year, True) > jday):
        year -= 1
    while (gregorian_nyd((year + 1), True) <= jday):
        year += 1

    day = jday - gregorian_nyd(year, True) + 1 # add 1 because computers count from 0
    return (day, year)
