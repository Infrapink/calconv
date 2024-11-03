#!/usr/bin/python3

# Convert between the Kaihuang calendar and Julian Day

from math import floor
from fractions import Fraction
from months import OLD_CHINESE as MONTHS, NUM_OLD_CHINESE as MONTHNO

sui = 365 + Fraction(25063, 102960) # tropical year
yue = 29 + Fraction(96529, 181920) # synodic month
zhongqi = sui / 12 # major solar term

solar_epoch = 1934351 + Fraction(775, 2574)
lunar_epoch = solar_epoch - Fraction(2218722317, 78043680)

def xinnian(year):
    '''Compute New Year's Day of a given year'''
    year = int(year)
    if (year > 0):
        year -= 1 # assuming there is no year 0

    solstice = solar_epoch + (year * sui)
    luns = (solstice - lunar_epoch) // yue
    solmoon = lunar_epoch + (yue * luns) # solstice moon
    while (floor(solmoon) > floor(solstice)):
        solmoon -= yue
    while (floor(solmoon + yue) <= floor(solstice)):
        solmoon += yue

    next_solstice = solstice + sui
    next_moon = solmoon + (12 * yue)
    if (floor(next_moon + yue) > floor(next_solstice)):
        # no leap month here
        ans = solmoon + (2 * yue)
    else:
        # there is a leap month somewhere
        if ( (solmoon + (2 * yue) < solstice + zhongqi) or (solmoon + (3 * yue) < solstice + (2 * zhongqi)) ):
            # leap month falls between the solstice and New Year's Day
            ans = solmoon + (3 * yue)
        else:
            # leap month falls during the year to come
            ans = solmoon + (2 * yue)

    return ans

def lny(year):
    '''Return the new moon of lunar new year, and whether the year is leap'''
    year = int(year)

    return ( xinnian(year), bool( (xinnian(year + 1) - xinnian(year)) / yue) )

def tojd(day, month, year):
    '''Convert a date in the Kaihuang li to a Julian Day'''
    day = int(day) - 1 # subtract 1 because computers count from 0
    month = str(month)
    year = int(year)

    # account for the year
    y = lny(year)
    jday = y[0]

    # account for the month
    # first, did the user specify the leap month?
    if (month[:3] == "Rùn"):
        month = month[4:]
        run = True
    else:
        run = False

    if (not(y[1])):
        # normal year
        jday += (MONTHNO[month] * yue)
    else:
        # leap year
        m = 0 # number of the month
        l = False # have we passed the leap month?
        z = solar_epoch + (year * sui) + (2 * zhongqi) # major solar term that the month contains
        if (year > 0):
            z -= sui
        while( floor(z) < floor(jday) ):
            z += zhongqi
        while( floor(z - zhongqi) >= floor(jday) ):
            z -= zhongqi

        while (MONTHS[m] != month):
            m += 1
            jday += yue
            if ( (not l) and (floor(jday + yue) < floor(z)) ):
                # we have not yet past the leap month
                l = True # now we are past the leap month
                jday += yue
            z += zhongqi

        if ( run and (not l) and (floor(jday + (2 * yue)) < floor(z + zhongqi)) ):
            # we are in the normal month, but the user specified the corresponding leap month
            jday += yue

    # compute the day
    jday = floor(jday) + day

    return jday
            
def fromjd(jday):
    '''Convert a Julian Day into a date in the Kaihuang li'''
    jday = int(jday)

    # compute the year
    year = (jday - solar_epoch) // sui
    while (floor(xinnian(year)) > jday):
        year -= 1
    while (floor(xinnian(year + 1)) <= jday):
        year += 1

    # compute the month
    y = lny(year)
    xinyue = y[0]
    if (not(y[1])):
        # normal year
        m = (jday - xinyue) // yue
        while (floor(xinyue + yue) <= jday):
            m += 1
            xinyue += yue
        month = MONTHS[m]
    else:
        # leap year
        m = 0 # number of the month
        l = False # have we passed the leap month?
        z = solar_epoch + (year * sui) + (2 * zhongqi) # marker of the major solar term

        if (year > 0):
            z -= sui
        while (floor(z) < floor(xinyue)):
            z += zhongqi
        while (floor(z - zhongqi) >= floor(xinyue)):
            z -= zhongqi

        while (floor(xinyue + yue) <= jday):
            xinyue += yue
            if(l):
                m += 1
            elif((not l) and (floor(xinyue) > floor(z))):
                m += 1
                z += zhongqi
            else:
                # this is the leap month
                l = True
                m -= 1 # the month has the same name as the previous month
        month = MONTHS[m]
        if ( (not l) and (floor(xinyue + yue) < floor(z)) ):
            # it's the leap month
            month = "Rùn " + month

    # compute the day
    day = jday - floor(xinyue) + 1 # add 1 because humans don't count from 0

    return (day, month, year)
