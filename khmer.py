#!/usr/bin/python

# A programme to convert between the Khmer (Cambodian) lunisolar calendar and Julian Days
#
# There are two main sources:
## JC Eade, Calendrical Systems of Mainland Southeast Asia, EJ Brill, 1995
## https://khmer-calendar.tovnah.com/calendar/

from math import floor, ceil
from fractions import Fraction
from months import KHMER_NORMAL as NORMAL, KHMER_LEAP as LEAP
from sea import lny, sid_year, chulasakarat as epoch

MONTHDAYS = {354: (29, 30, 29, 30,     29, 30, 29, 30, 29, 30, 29, 30),
             355: (29, 30, 30, 30,     29, 30, 29, 30, 29, 30, 29, 30),
             384: (29, 30, 29, 30, 30, 29, 30, 29, 30, 29, 30, 29, 30)}

def tojd(day, month, year):
    '''Convert a date in the Khmer calendar to Julian Day'''
    day = int(day) - 1 # subtract 1 because computers count from 0
    month = str(month)
    year = str(year)

    if (year[len(year) - 1:] == '*'):
        # user has specified a time before solar new year
        if (month in ("Chaet", "Vesak")):
            year = int(year[:len(year)]) + 1
        else:
            year = int(year[:len(year)])
    else:
        year = int(year)
    year -= 1183 # Cambodians tend to use the Buddhist Era, but the functions in sea.py assume Chulasakarat

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
    '''Convert a Julian Day into a date in the Khmer calendar'''
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

    year += 1183 # convert from Chulasakarat to Buddhist Era
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
