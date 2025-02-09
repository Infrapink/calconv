#!/usr/bin/python3

# Convert between Julian Days and an observational version of the Muisca agricultural calendar.
# The final release will also give zocam and acrotom dates.

from fractions import Fraction
from solun import dayof_arab, fullmoon as brightmoon, trans, tropical_year as trop_year, syn_month

solar_epoch = 2292289 + Fraction(547, 1440) # southern solstice at the end of 1563 AD, Colombian time
lat = 5 + Fraction(25,60) + Fraction(8,3600) # latitude of Colombian Altiplano
lon = 73 + Fraction(25,60) + Fraction(17,3600) # latitude of Colombian Altiplano
tz = 0 - Fraction(5,60)

def dayof(jday):
    '''Compute the Julian Day associated with an astronomical event, Colombian time'''
    return dayof_arab(Fraction(jday), lon, lat, tz)

def fullmoon(jday):
    '''Compute the day of the full moon, Colombian time'''
    return brightmoon(Fraction(jday), tz)

def solstice(jday):
    '''Compute the time of the southern solstice, Colombian time'''
    return trans(Fraction(jday), 270, tz)

def nyd(year):
    '''Compute New Year's Day for a given year'''
    year = int(year)

    sny = solstice(solar_epoch + (year * trop_year)) # solar new year, AKA solstice
    lny = fullmoon(sny) # full moon nearest the solstice
    while (dayof(fullmoon(lny)) < dayof(sny)):
        lny += syn_month
    while (dayof(fullmoon(lny - syn_month)) >= sny):
        lny -= syn_month

    return lny

def fromjd(jday):
    '''Convert a Julian Day into a date in the Muisca agricultural calendar'''
    jday = int(jday)

    # compute the year
    year = (jday - solar_epoch) // trop_year
    while (dayof(nyd(year)) > jday):
        year -= 1
    while (dayof(nyd(year + 1)) <= jday):
        year += 1

    # compute the month
    moon = fullmoon(jday)
    while (dayof(fullmoon(moon)) > jday):
        moon -= syn_month
    while (dayof(fullmoon(moon + syn_month)) <= jday):
        moon += syn_month
    month = int(round((moon - nyd(year)) // syn_month)) + 1 # add 1 becaue humans don't count from 0

    # compute the day
    day = jday - dayof(moon) + 1 # add 1 because humans don't count from 0

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a date in the Muisca agricultural calendar to a Julian Day'''
    day = int(day) - 1 # subtract 1 because computers count from 0
    month = int(month) - 1 # subtract 1 because computers count from 0
    year = int(year)

    jday = dayof(fullmoon(nyd(year) + (month * syn_month))) + day
    return jday
