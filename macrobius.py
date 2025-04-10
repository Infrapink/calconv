#!/usr/bin/python3

#
# Convert between the corrected Roman calendar and Julian Day
#

from months import ROMAN as MONTHS, ROMAN_LENGTHS as DAYSIN

epoch = 1446015

def leap(year):
    '''Returns the number of days in the year, asssuming a year 0'''
    year = int(year)

    ans = 355 + (22 * int((year % 24) in (1,3,5,7,9,11,14,16.19,21,23))) + int((year % 24) in (1,5,9,21))
    return ans

def nyd(year):
    '''Compute New Year's Day for a given year, assuming a year 0'''
    year = int(year)

    y = 24 * (year // 24)
    ans = epoch + (8766 * (year // 24))
    while (y < year):
        ans += leap(y)
        y += 1
    return ans
    
def fromjd(jday):
    '''Convert a Julian Day into a (nominal) Roman date'''
    jday = int(jday)

    # compute the year
    year = int(round((jday - epoch) // 365.25))
    kalend = nyd(year) # first day of the month
    while (kalend + leap(year) <= jday):
        kalend += leap(year)
        year += 1
    while (kalend > jday):
        year -= 1
        kalend -= leap(year)

    # compute the month
    m = 0
    while (kalend + DAYSIN[leap(year)][m] <= jday):
        kalend += DAYSIN[leap(year)][m]
        m += 1
    month = MONTHS[m]

    # compute the day
    day = jday - kalend + 1 # add 1 because humans don't count from 0
    if (year < 1):
        year -= 1 # Romans didn't accept the number 0

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a Roman date to a Julian Day'''
    day = int(day) - 1 # subtract 1 because computers count from 0
    month = str(month)
    year = int(year)

    # account for the year
    if (year < 0):
        year += 1
    jday = nyd(year)

    # account for the month
    m = 0
    while (MONTHS[m] != month):
        jday += DAYSIN[leap(year)][m]
        m += 1

    # account for the day
    jday += day

    return jday
