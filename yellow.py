#!/usr/bin/python3

# A programme to convert between Julian Days and the Yellow Tibetan calendar

from math import floor, ceil
from fractions import Fraction
from numpy import sign
from months import NUM_TIBETAN as MONTHS, TIBETAN_NUM as MONTHNO
import tibetan

def newmoon(mcount):
    '''Compute the Julian Day on which the new moon of a given month falls'''
    mcount = floor(mcount)

    t = tibetan.tibetan.phugpa(mcount, 0)
    ans = t[0] + sign(sum(t) - t[0])
    return ans

# astronomical constants
epoch = 2424972 # nominal epoch corresponding to the new moon that fell on 1 April 1927 AD
syn_month = Fraction(167025, 5656)
sid_year = syn_month * 12 * Fraction(67,65)

def tojd(day, month, year):
    '''Convert a date in the Phugpa Tibetan calendar to a Julian Day.'''
    day = int(day) - 1 # subtract 1 because computers count from 0
    month = str(month)
    year = int(year) - 900 # subtract 900 because the calculations take Tibetan year 900 as the epoch

    if (month[:4] == "Leap"):
        leap = True
        month = month[5:]
    else:
        leap = False

    mcount = (((year * 12) - 2) * Fraction(67,65)) + Fraction(55,65) # months since the epoch
    if (mcount % 1 > Fraction(49,65)):
        mcount += Fraction(67,65)
    # we are now at approximately Losar. next, step through the months until we get to the specified month.
    m = 0
    while (MONTHS[m] != month):
        if (mcount % 1 in (Fraction(48,65), Fraction(49,65))):
            m += 0
        else:
            m += 1
        mcount += Fraction(67,65)
    if ( (leap == False) and (mcount % 1 in (Fraction(48,68), Fraction(49,65)))):
        mcount += 1

    jday = newmoon(mcount) + day
    return jday

def fromjd(jday):
    '''Given a Julian Day, compute a date in the Phugpa Tibetan calendar'''
    jday = Fraction(jday)

    # compute the year
    year = round((jday - epoch) / sid_year)
    mcount = (((year * 12) - 2) * Fraction(67,65)) + Fraction(55,65)
    if (mcount % 1 > Fraction(49,65)):
        mcount += Fraction(67,65)
    while(newmoon(mcount + (12 * Fraction(67,65))) <= jday):
        year += 1
        mcount += (12 * Fraction(67,65))
    while(newmoon(mcount) > jday):
        year -= 1
        mcount -= (12 * Fraction(67,65))
    year = year + 900

    # compute the month
    m = 0
    while(newmoon(mcount + Fraction(67,65)) <= jday):
        if (mcount % 1 in ( Fraction(48,65), Fraction(49,65) )):
            m += 0
        else:
            m += 1
        mcount += Fraction(67,65)
    if (mcount % 1 in (Fraction(48,65), Fraction(49,65))):
        month = "Leap " + MONTHS[m]
    else:
        month = MONTHS[m]

    # compute the day
    day = jday - newmoon(mcount) + 1

    return(day, month, year)
