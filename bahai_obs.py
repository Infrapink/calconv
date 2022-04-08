#!/usr/bin/python

from math import floor, ceil
from fractions import Fraction
from months import BAHAI_NORMAL, BAHAI_LEAP
from solun import trans

trop = 365 + Fraction(5,24) + Fraction(48,1440) + Fraction(45,86400) # tropical year
epoch = 2394281 + Fraction(572, 1440) # northward equinox of 0 BE
tz = Fraction(7,48) # Iranian standard time is UTC+3:30

def getnawruz(equinox):
    '''Figure out the actual date of Nawruz'''
    equinox = Fraction(equinox)
    if equinox % 1 >= Fraction(18,24): # Bahá'í days start at sunset
        nawruz = ceil(equinox)
    else:
        nawruz = floor(equinox)
    return nawruz

def fromjd(jday):
    '''Convert a Julian Day into a date in the new Bahá'í calendar'''
    jday = int(jday)

    day = 0
    month = ""

    year = (jday - floor(epoch)) // trop
    equinox = trans((epoch + (year * trop)), 0.0, tz)
    while getnawruz(equinox + trop) <= jday:
        equinox += trop
    while getnawruz(equinox) > jday:
        equinox -= trop

    nexteq = equinox + trop
    nawruz = getnawruz(equinox)
    next_nawruz = getnawruz(nexteq)

    if next_nawruz - nawruz == 366:
        MONTHS = BAHAI_LEAP
    else:
        MONTHS = BAHAI_NORMAL

    monstar = nawruz
    for m in MONTHS.keys():
        if monstar + MONTHS[m] > jday:
            break
        else:
            monstar += MONTHS[m]

    month = m
    day = jday - monstar + 1

    return(day, month, year)

def tojd(day, month, year):
    '''Convert a day in the new Bahá'í calendar into a Julian Day'''
    day = int(day)
    month = str(month)
    day = int(day)

    jday = epoch + (year * trop)
    if (getnawruz(jday + trop) - getnawruz(jday)) == 366:
        MONTHS = BAHAI_LEAP
    else:
        MONTHS = BAHAI_NORMAL

    jday = getnawruz(jday)
    for m in MONTHS.keys():
        if m == month:
            break
        else:
            jday += MONTHS[m]

    jday = jday + day - 1
    return(jday)
            

    
