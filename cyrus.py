#!/usr/bin/python

from math import floor, ceil
from fractions import Fraction
from months import IRANIAN_NORMAL, IRANIAN_LEAP
from solun import trans

trop = 365 + Fraction(5,24) + Fraction(48,1440) + Fraction(45,86400) # tropical year
epoch = 1516968 + Fraction(26,45)
tz = Fraction(7,48) # Iranian standard time is UTC+3:30

def fromjd(jday):
    '''Convert a Julian Day into a date in the new Bahá'í calendar'''
    jday = int(jday)

    day = 0
    month = ""

    year = (jday - floor(epoch)) // trop
    equinox = trans((epoch + (year * trop)), 0.0, tz)
    while round(equinox + trop) <= jday:
        equinox += trop
    while round(equinox) > jday:
        equinox -= trop

    nexteq = equinox + trop
    nowruz = round(equinox)
    next_nowruz = round(nexteq)

    if next_nowruz - nowruz == 366:
        MONTHS = IRANIAN_LEAP
    else:
        MONTHS = IRANIAN_NORMAL

    monstar = nowruz
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
    if (round(jday + trop) - round(jday)) == 366:
        MONTHS = IRANIAN_LEAP
    else:
        MONTHS = IRANIAN_NORMAL

    jday = round(jday)
    for m in MONTHS.keys():
        if m == month:
            break
        else:
            jday += MONTHS[m]

    jday = jday + day - 1
    return(jday)
            

    
