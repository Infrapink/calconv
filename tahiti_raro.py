#!/usr/bin/python

# Convert between Julian Days and the traditional Tahitian lunisolar calendar, starting with the heliacal rising of the Pleiades

from math import floor
from fractions import Fraction
from stars import PLEIADES
from solun import lunar_month as syn_month, sid_year, heliacal_rising, first_visible_crescent, dayof_arab
from months import TAHITIAN as MONTHS, NUM_TAHITIAN as MONTHNO

lon = -149 - Fraction(25,60) # longitude of Tahiti
lat = -17 - Fraction(40,60) # latitude of Tahiti
tz = 0 - Fraction(10,24) # Tahiti's timezone
epoch = 2374066 # heliacal rising of the year that Pomare I united Tahiti

def fvc(jday):
    '''Compute the time of first visible crescent'''
    return first_visible_crescent(Fraction(jday), tz)

def dayof(jday):
    '''Compute which midnight-indexed Julian Day corresponds to a given astronomical event (which in this case is the new moon)'''
    return dayof_arab(Fraction(jday), lon, lat, tz)

def helris(jday):
    '''Compute the day of the heliacal rising of the Pleiades'''
    return heliacal_rising(Fraction(jday), lon, lat, PLEIADES, tz)

def tojd(day, month, year):
    '''Convert a date in the Tahitian calendar to a Julian Day'''
    day = int(day) - 1 # subtract 1 because computers count from 0
    month = str(month)
    year = int(year)

    # account for the year
    sny = helris(epoch + (year * sid_year))
    next_sny = helris(sny + sid_year)

    # first new moon on or after that night
    whiro = fvc(sny)
    while (dayof(fvc(whiro)) < sny):
        whiro += syn_month
    while (dayof(fvc(whiro - syn_month)) >= sny):
        whiro -= syn_month

    # first new moon of the next year
    next_whiro = fvc(next_sny)
    while (dayof(fvc(next_whiro)) < next_sny):
        next_whiro += syn_month
    while (dayof(fvc(next_whiro - syn_month)) >= next_sny):
        next_whiro -= syn_month

    # is it a leap year?
    if (round((next_whiro - whiro) / syn_month) == 13):
        leap = True
    else:
        leap = False

    if ( (not leap) and (month == "Aununu")):
        m = 11
    else:
        m = (MONTHNO[month] - 7) % 13

    jday = dayof(fvc(whiro + (m * syn_month))) + day

    return jday

def fromjd(jday):
    '''Convert a Julian Day to a date in the Tahitian calendar'''
    jday = int(jday)

    # compute the crescent that starts the month
    whiro = fvc(jday)
    while (dayof(fvc(whiro)) > jday):
        whiro -= syn_month
    while (dayof(fvc(whiro + syn_month)) <= jday):
        whiro += syn_month

    # compute the year
    year = (whiro - epoch) // sid_year
    while ( helris(epoch + (year * sid_year)) > dayof(fvc(whiro)) ):
        year -= 1
    while (helris(epoch + ((year + 1) * sid_year)) <= dayof(fvc(whiro)) ):
        year += 1

    # is it a leap year?
    sny = helris(epoch + (year * sid_year))
    next_sny = helris(sny + sid_year)
    firstmoon = fvc(sny)
    nextmoon = fvc(next_sny)
    while (dayof(fvc(firstmoon)) < sny):
        firstmoon += syn_month
    while (dayof(fvc(firstmoon - syn_month)) >= sny):
        firstmoon -= syn_month
    while (dayof(fvc(nextmoon)) < next_sny):
        nextmoon += syn_month
    while (dayof(fvc(nextmoon - syn_month)) >= next_sny):
        nextmoon -= syn_month
    if (round((nextmoon - firstmoon) / syn_month) == 13):
        leap = True
    else:
        leap = False

    # compute the month
    m = round((whiro - firstmoon) / syn_month)
    if ( (not leap) and (m == 11) ):
        month = "Aununu"
    else:
        month = MONTHS[(m + 7) % 13]

    # compute the day
    day = jday - dayof(fvc(whiro)) + 1 # add 1 because humans don't count from 0

    return (day, month, year)
