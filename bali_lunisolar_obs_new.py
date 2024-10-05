#!/usr/bin/python3

# Convert between Julian Days and dates in the Balinese lunisolar calendar
# This version uses modern methods and the newer leap year system

from math import floor, ceil
from fractions import Fraction
from months import BALINESE_LUNAR as MONTHS, NUM_BALINESE as MONTHNO
from solun import se, newmoon as darkmoon, lunar_month as syn_month, year12, year13, local_sunrise as sunrise

tz = Fraction(8,24) # Bali's timezone is UTC+8
lon = 0 - (8 + Fraction(20,60) + Fraction(6,3600)) # Bali is 8°20'06" south of the equator
lat = 115 + Fraction(5,60) + Fraction(17,3600) # Bali is 115°5'17" east of Greenwich
epoch = darkmoon(se, tz)
cycle = 235 * syn_month # mean cycle of 19 years
leap_rems = (2, 4, 7, 10, 13, 15, 18) # years in a Metonic cycle which are leap
leap_months = {2:  1,
               4:  5,
               7:  3,
               10: 1,
               13: 0,
               15: 4,
               18: 2}

def yeartype(year):
    '''Returns mean length of the year in question'''
    year = int(year)
    if (year % 19 in leap_rems):
        # leap year
        ans = 13 * syn_month
    else:
        # normal year
        ans = 12 * syn_month
    return ans

def newmoon(jday):
    '''Compute the time of the new moon, in local time'''
    return darkmoon(Fraction(jday), tz)

def dayof(jday):
    '''Compute the Julian Day associated with a given instant'''
    jday = Fraction(jday)

    ans = round(jday)
    while (sunrise(ans, lon, lat, tz) < jday):
        ans += 1
    while (sunrise((ans - 1), lon, lat, tz) >= jday):
        ans -= 1

    return ans

def fromjd(jday):
    '''Convert a Julian Day into a date in the Balinese lunisolar calendar'''
    jday = int(jday)

    # compute the year
    cycles = (jday - epoch) // cycle
    year = 19 * cycles
    crescent = epoch + (cycle * cycles)
    while (dayof(newmoon(crescent + cycle)) <= jday):
        year += 19
        crescent += cycle
    while (dayof(newmoon(crescent)) > jday):
        year -= 19
        crescent -= cycle
    while (dayof(newmoon(crescent + yeartype(year))) <= jday):
        crescent += yeartype(year)
        year += 1

    # compute the month
    if (not (year % 19 in leap_rems)):
        # normal year
        m = round((jday - crescent) / syn_month) # number of the month
        crescent += (m * syn_month)
        while (dayof(newmoon(crescent + syn_month)) <= jday):
            m += 1
            crescent += syn_month
        while (dayof(newmoon(crescent)) > jday):
            m -= 1
            crescent -= syn_month
        month = MONTHS[m]
    else:
        m = 0 # number of the month
        l = False # have we passed the leap month?

        while (dayof(newmoon(crescent + syn_month)) <= jday):
            crescent += syn_month
            if ( (m == leap_months[year % 19]) and (not l)):
                # this is the leap month
                l = True
            else:
                # normal month
                m += 1
        month = MONTHS[m]
        if ( (m == leap_months[year % 19]) and l ):
            # we are in the leap month
            month += " 2"

    # compute the day... that is, the tithi
    tithi = 1
    day = dayof(newmoon(crescent))
    while (day < jday):
        if ( (day - dayof(epoch)) % 63 == 8):
            tithi += 2
        else:
            tithi += 1
        day += 1
    
    return(tithi, month, year)

def tojd(tithi, month, year):
    '''Convert a date in the Balinese lunisolar calendar to a Julian Day'''
    tithi = int(tithi) - 1 # subtract 1 because computers count from 0
    month = str(month)
    year = int(year)

    # account for the year
    cycles = year // 19
    y = 19 * cycles
    jday = epoch + (cycle * cycles)
    while (y < year):
        jday += yeartype(y)
        y += 1

    # account for the month
    if (month[len(month) - 1:] == '2'):
        leap = True
        month = month[:len(month) - 2]
    else:
        leap = False

    if (not (year % 19 in leap_rems)):
        # normal year
        jday = dayof(newmoon(jday + (syn_month * MONTHNO[month])))
    else:
        m = 0 # number of the month
        l = False # have we passed the leap month?
        while (MONTHS[m] != month):
            jday += syn_month
            if ( (m == leap_months[year % 19]) and (not l) ):
                l = True
            else:
                m += 1
        if ( leap and (not l) and (m == leap_months[year % 19]) ):
            jday += syn_month
        jday = dayof(newmoon(jday))

    # account for the tithi
    t = 0
    while (t < tithi):
        if ( (jday - ceil(epoch)) % 63 == 8):
            t += 2
        else:
            t += 1
        jday += 1

    return(int(jday))
