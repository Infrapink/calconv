#!/usr/bin/python

# Convert between the Fasli Zoroastrian calendar and Julian Day, according to the Zarathushtrian Religious Era

from months import NUM_ZOROASTRIAN as NUMON
from months import ZOROASTRIAN_NUM as MONTHNO
from math import floor
from solun import trans
from fractions import Fraction

epoch = 1086713 + Fraction(77,160)
tropical_year = 365 + Fraction(5,24) + Fraction(48,1440) + Fraction(45,86400)
tz = Fraction(7, 48) # Iranian standard time

def getnowruz(equinox):
    '''Determine the day which corresponds to 1 Farvardin'''
    equinox = Fraction(equinox)
    true_equinox = trans(equinox, 0.0, tz)
    if (true_equinox % 1) < Fraction(6,24):
        # equinox happens before sunrise
        nowruz = floor(true_equinox) - 1
    else:
        nowruz = floor(true_equinox)

    return nowruz

def fromjd(jday):
    '''Convert a Julian Day into a date in the Fasli calendar'''
    jday = int(jday)

    day = 0
    month = ""

    year = (jday - epoch) // tropical_year
    equinox = epoch + (year * tropical_year)

    while getnowruz(equinox + tropical_year) <= jday:
        year += 1
        equinox += tropical_year
    while getnowruz(equinox) > jday:
        year -= 1
        equinox -= tropical_year

    if year >= 0:
        year += 1

    nowruz = getnowruz(equinox)
    month = NUMON[(jday - nowruz) // 30]
    day = ((jday - nowruz) % 30) + 1

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a date in the Fasli calendar into a Julian Day.'''
    day = int(day)
    month = str(month)
    year = int(year)

    if year >= 0:
        year -= 1

    equinox = epoch + (year * tropical_year)
    jday = getnowruz(equinox)

    jday = jday + (30 * MONTHNO[month]) + day - 1

    return jday
