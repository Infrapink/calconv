#!/usr/bin/python3

#
# Convert between the Solar Hijri calendar and Julian DAy
#

import months
from fractions import *
from math import floor
from solun import trans

yearlen = 365 + Fraction(5,24) + Fraction(48,1440) + Fraction(45,86400)
epoch = 1948319 + Fraction(31379,43200)

YEARTYPE = {365: months.IRANIAN_NORMAL,
            366: months.IRANIAN_LEAP}

tz = Fraction(7,48) # Iran is 3hr 30 min ahead of UTC

def geteq(jday):
    '''Fire precise insteant of the northward equinox for a given day'''
    equinox = trans(jday, 0.0, tz)
    return equinox

def tojd(day,month,year):
    """Convert a date in the Solar Hijri calendar flooro a Julian day."""
    day = floor(day)
    month = month
    year = floor(year)

    if year >= 1:
        equinox = geteq(epoch + (yearlen * (year - 1)))
        nexteq = geteq(equinox + yearlen)

    else:
        equinox = geteq(epoch + (yearlen * year))
        nexteq = geteq(equinox + yearlen)

    nowruz = round(equinox)
    next_nowruz = round(nexteq)

    MONTHS = YEARTYPE[next_nowruz - nowruz]
    jday = nowruz
    for m in MONTHS.keys():
        if m == month:
            jday += day - 1
            break
        else:
            jday += MONTHS[m]

    return jday


def fromjd(jday):
    """Convert a Julian day to a date in the Solar Hijri calendar."""
    day = 0
    month = ""
    year = 0
    
    jday = floor(jday)
    current = False
    
    if jday >= floor(epoch):
        # positive dates
        y = (jday - epoch) // yearlen
        year = y + 1
        equinox = epoch + (y * yearlen)

    else:
        # negative dates
        y = (jday - epoch) // yearlen
        year = y
        equinox = epoch + (y * yearlen)

    while round(geteq(equinox)) > jday:
        year -= 1
        if year == 0:
            year = (-1)
        equinox -= yearlen

    while round(geteq(equinox + yearlen)) <= jday:
        equinox += yearlen
        year += 1
        if year == 0:
            year = 1

    if year == 0:
        year = (-1)

    nowruz = round(geteq(equinox))
    next_nowruz = round(geteq(equinox + yearlen))
    MONTHS = YEARTYPE[next_nowruz - nowruz]
    alpha = nowruz

    for m in MONTHS.keys():
        if alpha + MONTHS[m] > jday:
            month = m
            day = jday - alpha + 1
            break
        else:
            alpha += MONTHS[m]

    return (day, month, year)
