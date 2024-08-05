#!/usr/bin/python3

# A programme to convert between Julian Days and the Sarnath reform of the Tibetan calendar

from math import floor, ceil
from fractions import Fraction
from numpy import sign
from months import NUM_TIBETAN as MONTHS, TIBETAN_NUM as MONTHNO
import tibetan

def dayof(mcount, tithi):
    '''Compute the Julian Day corresponding to a given tithi in a given month'''
    mcount = floor(mcount)
    tithi = int(tithi) - 15 # subtract 15 to make the month start on the full moon

    t = tibetan.tibetan.sherab_ling(mcount, tithi)
    ans = t[0] + sign(sum(t) - t[0])
    return ans

# astronomical constants
epoch = 2446885 # nominal epoch corresponding to the new moon that fell on 29 March 1987 AD
syn_month = Fraction(637861, 21600)
sid_year = syn_month * 12 * Fraction(67,65)

def tojd(tithi, month, year):
    '''Convert a date in the Sarnath calendar to a Julian Day.'''
    tithi = int(tithi) - 1 # subtract 1 because computers count from 0
    month = str(month)
    year = int(year) - 960 # subtract 960 because the calculations take Tibetan year 960 as the epoch

    if (month[:4] == "Leap"):
        leap = True
        month = month[5:]
    else:
        leap = False

    mcount = (((year * 12) - 3) * Fraction(67,65)) + Fraction(55,65) # months since the epoch
    if (mcount % 1 > Fraction(17,65)):
        mcount += Fraction(67,65)
    # we are now at approximately Losar. next, step through the months until we get to the specified month.
    m = 0
    while (MONTHS[m] != month):
        if (mcount % 1 in (Fraction(16,65), Fraction(17,65))):
            m += 0
        else:
            m += 1
        mcount += Fraction(67,65)
    if ( (leap == False) and (mcount % 1 in (Fraction(16,68), Fraction(17,65)))):
        mcount += 1

    jday = dayof(mcount, tithi)
    return jday

def fromjd(jday):
    '''Given a Julian Day, compute a date in the Sarnath calendar'''
    jday = Fraction(jday)

    # compute the year
    year = round((jday - epoch) / sid_year)
    mcount = (((year * 12) - 3) * Fraction(67,65)) + Fraction(55,65)
    if (mcount % 1 > Fraction(17,65)):
        mcount += Fraction(67,65)
    while(dayof(  (mcount + (12 * Fraction(67,65))), 0) <= jday):
        year += 1
        mcount += (12 * Fraction(67,65))
    while(dayof(mcount, 0) > jday):
        year -= 1
        mcount -= (12 * Fraction(67,65))
    year = year + 960

    # compute the month
    m = 0
    while( dayof( (mcount + Fraction(67,65)), 0) <= jday):
        if (mcount % 1 in ( Fraction(16,65), Fraction(17,65) )):
            m += 0
        else:
            m += 1
        mcount += Fraction(67,65)
    if (mcount % 1 in (Fraction(16,65), Fraction(17,65))):
        month = "Leap " + MONTHS[m]
    else:
        month = MONTHS[m]

    # compute the tithi
    tithi = 0
    while( dayof( mcount, (tithi + 1)) <= jday):
        tithi += 1

    return((tithi + 1), month, year)
