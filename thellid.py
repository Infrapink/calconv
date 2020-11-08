#!/usr/bin/python

#
# Convert between the Thellid calendar and Julian DAy
#

import months
from fractions import *
from math import floor

yearlen = 365 + Fraction(5,24) + Fraction(48,1440) + Fraction(45,86400)
epoch = Fraction(-83419488409, 43200) - yearlen # based on taking the southern solstice moment for 2020 AD and subtraction 12020 * yearlen
#epoch = 2375839 + Fraction(36877,86400)

YEARTYPE = {365: months.THELLID_NORMAL,
            366: months.THELLID_LEAP}

def tojd(day,month,year):
    """Convert a date in the Thellid calendar into a Julian day."""
    day = int(day)
    month = month
    year = int(year)

    equinox = epoch + (year * yearlen)
    nexteq = equinox + yearlen
    oyd = floor(equinox)
    noyd = floor(nexteq)
    
    jday = oyd
    m = YEARTYPE[noyd - oyd]

    for i in m.keys():
        if i == month:
            jday += day# - 1
            break
        else:
            jday += m[i]

    return jday

def fromjd(jday):
    """Convert a Julian day to a date in the Thellid calendar."""
    day = 0
    month = ""
    year = 0
    
    jday = int(jday)
    
    year = (jday - epoch) // yearlen
    equinox = epoch + (year * yearlen)
    nexteq = equinox + yearlen
    oyd = floor(equinox)
    noyd = floor(nexteq)
        
    m = YEARTYPE[noyd - oyd]
    delta = jday - oyd

    for i in m.keys():
        if delta <= m[i]:
            month = i
            day = delta
            break
        else:
            delta -= m[i]

    return (day, month, year)
