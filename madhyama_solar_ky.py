#!/usr/bin/python

# Convert between the Old Hindu solar calendar and Julian Day

from math import floor, ceil
from fractions import Fraction
from months import NUM_HINDU as NUMON
from months import HINDU_NUM as MONTHNO

epoch = 588466 + Fraction(6,24)# in Julian Days
sid_year = 365 + Fraction(149,576) # mean sidereal year
rasi = sid_year * Fraction(1,12) # solar month

def monstar(inst):
    '''Determine when a month begins'''
    inst = Fraction(inst)
    if (inst % 1) <= Fraction(6,24):
        return floor(inst)
    else:
        return ceil(inst)

def tojd(day, month, year):
    '''Convert a date in the Hindu solar calendar to a Julian Day'''
    day = int(day)
    month = str(month)
    year = int(year)

    jday = epoch + (year * sid_year) + (rasi * MONTHNO[month])
    jday = monstar(jday) + day - 1
    return jday

def fromjd(jday):
    '''Convert a Julian Day to a date in the Hindu solar calendar'''
    jday = int(jday)
    year = (jday - epoch) // sid_year
    mesha = epoch + (year * sid_year)

    while monstar(mesha + sid_year) <= jday:
        year += 1
        mesha += sid_year
    while monstar(mesha) > jday:
        year -= 1
        mesha -= sid_year

    m = (jday - mesha) // rasi
    while monstar(mesha + (rasi * (m + 1))) <= jday:
        m += 1
    while monstar(mesha + (rasi * m)) > jday:
        m -= 1
    month = NUMON[m]
    day = jday - monstar(mesha + (m * rasi)) + 1

    return(day, month, year)
