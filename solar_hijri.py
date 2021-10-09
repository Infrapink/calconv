#!/usr/bin/python3

#
# Convert between the Solar Hijri calendar and Julian DAy
#

import months
from fractions import *
from math import floor

yearlen = 365 + Fraction(5,24) + Fraction(48,1440) + Fraction(45,86400)
epoch = 1948319 + Fraction(31379,43200)

YEARTYPE = {365: months.IRANIAN_NORMAL,
            366: months.IRANIAN_LEAP}

def tojd(day,month,year):
    """Convert a date in the Solar Hijri calendar into a Julian day."""
    day = int(day)
    month = month
    year = int(year)

    if year >= 1:
        equinox = epoch + (yearlen * (year - 1))
        nexteq = equinox + yearlen

        if equinox % 1 > Fraction(1,2):
            nowruz = int(equinox) + 1
        else:
            nowruz = int(equinox)

        if nexteq % 1 > Fraction(1,2):
            nextnowruz = int(nexteq) + 1
        else:
            nextnowruz = int(nexteq)

    else:
        # negative years
        equinox = (year * yearlen) + epoch
        nexteq = equinox + yearlen
        
        if equinox > 0:
            if equinox % 1 > Fraction(1,2):
                nowruz = int(equinox) + 1
            else:
                nowruz = int(equinox)
        else:
            if equinox % 1 < Fraction(1,2): # change sign to account for negative division
                nowruz = floor(equinox) - 1
            else:
                nowruz = floor(equinox)

        if nexteq > 0:
            if nexteq % 1 > Fraction(1,2):
                nextnowruz = int(nexteq) + 1
            else:
                nextnowruz = int(nexteq)
        else:
            if nexteq % 1 < Fraction(1,2): # change sign to account for negative division
                nextnowruz = floor(nexteq) - 1
            else:
                nextnowruz = floor(nexteq)

    jday = nowruz
    m = YEARTYPE[nextnowruz - nowruz]
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
        nexteq = equinox + yearlen

        if equinox % 1 > Fraction(1,2):
            nowruz = int(equinox) + 1
        else:
            nowruz = int(equinox)

        if nexteq % 1 > Fraction(1,2):
            nextnowruz = int(nexteq) + 1
        else:
            nextnowruz = int(nexteq)

    else:
        # negative dates
        y = (jday - epoch) // yearlen
        year = y
        equinox = epoch + (year * yearlen)
        
        nexteq = equinox + yearlen

        if equinox > 0:
            if equinox % 1 > Fraction(1,2):
                nowruz = int(equinox) + 1
            else:
                nowruz = int(equinox)
        else:
            if equinox % 1 < Fraction(1,2):  # change sign to account for negative division
                nowruz = floor(equinox)
            else:
                nowruz = floor(equinox) + 1

        if nexteq > 0:
            if nexteq % 1 > Fraction(1,2):
                nextnowruz = int(nexteq) + 1
            else:
                nextnowruz = int(nexteq)
        else:
            if nexteq % 1 < Fraction(1,2): # change sign to account for negative division
                nextnowruz = floor(nexteq)
            else:
                nextnowruz = floor(nexteq) + 1
            
    m = YEARTYPE[nextnowruz - nowruz]
    delta = jday - nowruz

    for i in m.keys():
        if delta < m[i]:
            month = i
            day = delta + 1
            break
        else:
            delta -= m[i]

    return (day, month, year)
