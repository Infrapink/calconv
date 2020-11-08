#!/usr/bin/python

#
# Convert between the French Republican calendar and Julian DAy
#

import months
from fractions import *
from math import floor

yearlen = 365 + Fraction(5,24) + Fraction(48,1440) + Fraction(45,86400)
epoch = 2375474 + Fraction(997,5400)
#day1 = 2375839 + Fraction(36877,86400)

YEARTYPE = {365: months.FRENCH_NORMAL,
            366: months.FRENCH_LEAP}

def tojd(day,month,year):
    """Convert a date in the French Republican calendar into a Julian day."""
    day = int(day)
    month = month
    year = int(year)

    equinox = epoch + (year * yearlen)
    nexteq = equinox + yearlen

    jday = floor(equinox)
    m = YEARTYPE[floor(nexteq) - floor(equinox)]

    for i in m.keys():
        if i == month:
            jday += day - 1
            break
        else:
            jday += m[i]

    return jday

def fromjd(jday):
    """Convert a Julian day to a date in the French Republican calendar."""
    jday = int(jday)
    
    day = 0
    month = ""

    year = (jday - epoch) // yearlen
    equinox = epoch + (year * yearlen)
    nexteq = equinox + yearlen

    m = YEARTYPE[floor(nexteq) - floor(equinox)]
    delta = jday - floor(equinox)

    for i in m.keys():
        if delta < m[i]:
            month = i
            day = delta + 1
            break
        else:
            delta -= m[i]

    return (day, month, year)

