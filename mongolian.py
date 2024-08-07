#!/usr/bin/python3

# A programme to convert between Julian Days and the traditional Mongolian calendar

from math import floor, ceil
from fractions import Fraction
from numpy import sign
import tibetan

# months constants
MONTHS = ("Negdugeer sar", "Khoyordugaar sar", "Guravdugaar sar", "Dörövdugeer sar", "Tarvdugaar sar", "Zurgadugaar sar", "Doldugaar sar", "Naĭmdugaar sar", "Yesdugeer sar", "Aravdugaar sar", "Arvannegdugeer sar", "Arvanchaërdugaar sar")
MONTHNO = {"Negdugeer sar": 0,
           "Khoyordugaar sar": 1,
           "Guravdugaar sar": 2,
           "Dörövdugeer sar": 3,
           "Tarvdugaar sar": 4,
           "Zurgadugaar sar": 5,
           "Doldugaar sar": 6,
           "Naĭmdugaar sar": 7,
           "Yesdugeer sar": 8,
           "Aravdugaar sar": 9,
           "Arvannegdugeer sar": 10,
           "Arvanchaërdugaar sar": 11}

def dayof(mcount, tithi):
    '''Compute the Julian Day corresponding to a given tithi in a given month'''
    mcount = floor(mcount)
    tithi = int(tithi)

    t = tibetan.tibetan.mongolian(mcount, tithi)
    ans = t[0] + sign(sum(t) - t[0])
    return ans

# astronomical constants
epoch = 2359237 # day of the nominal new moon of 9 April 1747 AD
syn_month = Fraction(167025, 5656)
sid_year = syn_month * Fraction(67,65) * 12

def tojd(tithi, month, year):
    '''Convert a date in the Mongolian traditional calendar to a Julian Day.'''
    tithi = int(tithi) - 1 # subtract 1 because computers count from 0
    month = str(month)
    year = int(year) - 720

    if (month[:4] == "Leap"):
        leap = True
        month = month[5:]
    else:
        leap = False

    mcount = (((year * 12) - 2) * Fraction(67,65)) + Fraction(10,65) # months since the epoch
    if (mcount % 1 > Fraction(47,65)):
        mcount += Fraction(67,65)
    # we are now at approximately Tsagaan Sar. next, step through the months until we get to the specified month.
    m = 0
    while (MONTHS[m] != month):
        if (mcount % 1 in (Fraction(46,65), Fraction(47,65))):
            m += 0
        else:
            m += 1
        mcount += Fraction(67,65)
    if ( (leap == False) and (mcount % 1 in (Fraction(46,68), Fraction(47,65)))):
        mcount += 1

    jday = dayof(mcount, tithi)
    return jday

def fromjd(jday):
    '''Given a Julian Day, compute a date in the Phugpa Tibetan calendar'''
    jday = Fraction(jday)

    # compute the year
    year = round((jday - epoch) / sid_year)
    mcount = (((year * 12) - 2) * Fraction(67,65)) + Fraction(10,65)
    if (mcount % 1 > Fraction(49,65)):
        mcount += Fraction(67,65)
    while(dayof(  (mcount + (12 * Fraction(67,65))), 0) <= jday):
        year += 1
        mcount += (12 * Fraction(67,65))
    while(dayof(mcount, 0) > jday):
        year -= 1
        mcount -= (12 * Fraction(67,65))
    year = year + 720

    # compute the month
    m = 0
    while( dayof( (mcount + Fraction(67,65)), 0) <= jday):
        if (mcount % 1 in ( Fraction(46,65), Fraction(47,65) )):
            m += 0
        else:
            m += 1
        mcount += Fraction(67,65)
    if (mcount % 1 in (Fraction(46,65), Fraction(47,65))):
        month = "Leap " + MONTHS[m]
    else:
        month = MONTHS[m]

    # compute the tithi
    tithi = 0
    while( dayof( mcount, (tithi + 1)) <= jday):
        tithi += 1

    return((tithi + 1), month, year)
