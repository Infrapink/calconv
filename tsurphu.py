#!/usr/bin/python3

# A programme to convert between Julian Days and the Tsurphu Tibetan calendar

from math import floor, ceil
from fractions import Fraction
from numpy import sign
from months import NUM_TIBETAN as MONTHS, TIBETAN_NUM as MONTHNO
import tibetan

def dayof(mcount, tithi):
    '''Compute the Julian Day corresponding to a given tithi in a given month'''
    mcount = floor(mcount)
    tithi = int(tithi)

    t = tibetan.tibetan.tsurphu(mcount, tithi)
    ans = t[0] + sign(sum(t) - t[0])
    return ans

# astronomical constants

epoch = 2397598 # epoch corresponding to the nominal new moon of 19 April 1852 AD
sid_year = 12 * Fraction(67,65) * Fraction(167025, 5656)

def tojd(tithi, month, year):
    '''Convert a date in the Phugpa Tibetan calendar to a Julian Day.'''
    tithi = int(tithi) - 1 # subtract 1 because computers count from 0
    month = str(month)
    year = int(year) - 825 # subtract 900 because the calculations take Tibetan year 825 as the epoch

    if (month[:4] == "Leap"):
        leap = True
        month = month[5:]
    else:
        leap = False

    mcount = (((year * 12) - 2) * Fraction(67,65)) + Fraction(14,65) # months since the epoch
    if (mcount % 1 > Fraction(1,65)):
        mcount += Fraction(67,65)
    # we are now at approximately Losar. next, step through the months until we get to the specified month.
    m = 0
    while (MONTHS[m] != month):
        if (mcount % 1 < (Fraction(2,65))):
            m += 0
        else:
            m += 1
        mcount += Fraction(67,65)
    if ( (leap == False) and (mcount % 1 in (Fraction(48,68), Fraction(49,65)))):
        mcount += 1

    jday = dayof(mcount, tithi)
    return jday

def fromjd(jday):
    '''Given a Julian Day, compute a date in the Phugpa Tibetan calendar'''
    jday = Fraction(jday)

    # compute the year
    year = round((jday - epoch) / sid_year)
    mcount = (((year * 12) - 2) * Fraction(67,65)) + Fraction(14,65)
    if (mcount % 1 > Fraction(1,65)):
        mcount += Fraction(67,65)
    while(dayof(  (mcount + (12 * Fraction(67,65))), 0) <= jday):
        year += 1
        mcount += (12 * Fraction(67,65))
    while(dayof(mcount, 0) > jday):
        year -= 1
        mcount -= (12 * Fraction(67,65))
    year = year + 825

    # compute the month
    m = 0
    while( dayof( (mcount + Fraction(67,65)), 0) <= jday):
        if (mcount % 1 < Fraction(2,65) ):
            m += 0
        else:
            m += 1
        mcount += Fraction(67,65)
    if (mcount % 1 < Fraction(2,65)):
        month = "Leap " + MONTHS[m]
    else:
        month = MONTHS[m]

    # compute the tithi
    tithi = 0
    while( dayof( mcount, (tithi + 1)) <= jday):
        tithi += 1

    return((tithi + 1), month, year)
