#!/usr/bin/python

# A programme to convert between the Thai lunisolar calendar and Julian Days, assuming Central Thai reckoning of month
# this is almost entirely based on JC Eade, Calendrical Systems of Mainland Southeast Asia, EJ Brill, 1995
# Internet sources for the names of the months:
## http://world.clndr.org/calendars/thai-lunar-calendar/
## https://www.thaipod101.com/blog/2019/10/24/thai-numbers/

from math import floor, ceil
from fractions import Fraction
from months import THAI_LUNAR_NORMAL as NORMAL, THAI_LUNAR_LEAP as LEAP
from sea import lny, chulasakarat as epoch, sid_year

MONTHDAYS = {354: (29, 30, 29, 30,     29, 30, 29, 30, 29, 30, 29, 30),
             355: (29, 30, 30, 30,     29, 30, 29, 30, 29, 30, 29, 30),
             384: (29, 30, 29, 30, 30, 29, 30, 29, 30, 29, 30, 29, 30)}

def tojd(day, month, year):
    '''Convert a date in the Thai lunisolar calendar to Julian Day'''
    day = int(day) - 1 # subtract 1 because computers count from 0
    month = str(month)
    year = str(year)

    if (year[len(year) - 1:] == '*'):
        # user has specified a time before solar new year
        if (month[6:] in ("hâa", "hòk")):
            year = int(year[:len(year)]) + 1
        else:
            year = int(year[:len(year)])
    else:
        year = int(year)

    # compute lunar new year
    moonums = lny(year)
    if (moonums[0] == 384):
        MONTHS = LEAP
    else:
        MONTHS = NORMAL
    monthdays = MONTHDAYS[moonums[0]]
    jday = moonums[1]

    # account for the month
    m = 0
    while (MONTHS[m] != month):
        jday += monthdays[m]
        m += 1

    # account for the days
    jday += day

    return jday

def fromjd(jday):
    '''Convert a Julian Day into a date in the Thai lunisolar calendar'''
    jday = int(jday)

    # compute the year
    year = (jday - epoch) // sid_year
    while (lny(year)[1] > jday):
        year -= 1
    while (lny(year + 1)[1] <= jday):
        year += 1

    moonums = lny(year)
    if (moonums[0] == 384):
        MONTHS = LEAP
    else:
        MONTHS = NORMAL
    monthdays = MONTHDAYS[moonums[0]]
    newmoon = moonums[1]
    
    songkran = ceil(epoch + (year * sid_year))
    if (jday < songkran):
        year = str(year - 1) + '*'

    # compute the month
    m = 0
    while (newmoon + monthdays[m] <= jday):
        newmoon += monthdays[m]
        m += 1
    month = MONTHS[m]

    # compute the day
    day = jday - newmoon + 1 # add 1 because humans don't count from 0

    return(day, month, year)
