#!/usr/bin/python3

#
# Convert between the Solar Hijri calendar and Julian DAy
#

import months
from fractions import *
from math import floor

yearlen = 365 + Fraction(5,24) + Fraction(48,1440) + Fraction(45,86400)
epoch = Fraction(6065414981, 2700) - Fraction(5,24) + 1 # southern solstice in 1438 AD, corrected for Peruvian time

YEARTYPE = {365: months.INCA_SOLAR_NORMAL,
            366: months.INCA_SOLAR_LEAP}

def tojd(day,month,year):
    """Convert a date in the Solar Hijri calendar into a Julian day."""
    day = int(day)
    month = month
    year = int(year)

    if year >= 1:
        equinox = epoch + (yearlen * (year - 1))
        nexteq = equinox + yearlen

    else:
        # negative years
        equinox = (year * yearlen) + epoch
        nexteq = equinox + yearlen

    raymi = floor(equinox)
    next_raymi = floor(nexteq)

    jday = raymi
    m = YEARTYPE[next_raymi - raymi]
    for i in m.keys():
        if i == month:
            jday += day - 1
            break
        else:
            jday += m[i]

    return jday


def fromjd(jday):
    """Convert a Julian day to a date in the Solar Hijri calendar."""
    day = 0
    month = ""
    year = 0
    
    jday = int(jday)
    current = False
    
    if jday >= int(epoch):
        # positive dates
        y = (jday - epoch) // yearlen
        year = y + 1
        equinox = epoch + (y * yearlen)
        while floor(equinox + yearlen) <= jday:
            equinox += yearlen
        nexteq = equinox + yearlen

    else:
        # negative dates
        y = (jday - epoch) // yearlen
        year = y
        equinox = epoch + (year * yearlen)
        while floor(equinox + yearlen) <= jday:
            equinox += yearlen
        nexteq = equinox + yearlen

    raymi = floor(equinox)
    next_raymi = floor(nexteq)

    m = YEARTYPE[next_raymi - raymi]
    delta = jday - raymi

    for i in m.keys():
        if delta < m[i]:
            month = i
            day = delta + 1
            break
        else:
            delta -= m[i]

    return (day, month, year)
