#!/usr/bin/python

# Convert between Julian Days and the traditional calendar of the Tūhoe Māori

from math import floor
from fractions import Fraction
from stars import PLEIADES
from solun import lunar_month as syn_month, sid_year, heliacal_rising, first_visible_crescent, dayof_arab
from months import TUHOE as MONTHS, NUM_TUHOE as MONTHNO

lon = -177 - Fraction(3,60) # longitude of Te Urewera
lat = 0 - 38 - Fraction(27,60) # latitude of Te Urewera
tz = Fraction(12,24) # Aotearoa's timezone
epoch = 2188710 # heliacal rising of the Pleiades in the year that the first settlers arrived on Aotearoa

def fvc(jday):
    '''Compute the time of first visible crescent'''
    return first_visible_crescent(Fraction(jday), tz)

def dayof(jday):
    '''Compute which midnight-indexed Julian Day corresponds to a given astronomical event (which in this case is the new moon)'''
    return dayof_arab(Fraction(jday), lon, lat, tz)

def helris(jday):
    '''Compute the day of the acronycal rising of the Pleiades'''
    return heliacal_rising(Fraction(jday), lon, lat, PLEIADES, tz)

def tojd(day, month, year):
    '''Convert a date in the Tūhoe calendar to a Julian Day'''
    day = int(day) - 1 # subtract 1 because computers count from 0
    month = str(month)
    year = int(year)

    # account for the year
    sny = helris(epoch + (year * sid_year))

    # first new moon on or after that night
    whiro = fvc(sny)
    while (dayof(fvc(whiro)) < sny):
        whiro += syn_month
    while (dayof(fvc(whiro - syn_month)) >= sny):
        whiro -= syn_month
        
    # account for the month
    if (month == "Te Tahi o Pipiri"):
        m = 12
    else:
        m = MONTHNO[month]

    jday = dayof(fvc(whiro + (m * syn_month))) + day

    return jday

def fromjd(jday):
    '''Convert a Julian Day to a date in the traditional Tūhoe calendar'''
    jday = int(jday)

    # compute the crescent that starts the month
    whiro = fvc(jday)
    while (dayof(fvc(whiro)) > jday):
        whiro -= syn_month
    while (dayof(fvc(whiro + syn_month)) <= jday):
        whiro += syn_month

    # compoute the year
    year = (whiro - epoch) // sid_year
    while ( helris(epoch + (year * sid_year)) > dayof(fvc(whiro)) ):
        year -= 1
    while (helris(epoch + ((year + 1) * sid_year)) <= dayof(fvc(whiro)) ):
        year += 1

    # compute the month
    sny = helris(epoch + (year * sid_year))
    firstmoon = fvc(sny)
    while (dayof(fvc(firstmoon)) < sny):
        firstmoon += syn_month
    while (dayof(fvc(firstmoon - syn_month)) >= sny):
        firstmoon -= syn_month
    m = round((whiro - firstmoon) / syn_month)
    if (m == 12):
        month = "Te Tahi o Pipiri"
    else:
        month = MONTHS[m]

    day = jday - dayof(fvc(whiro)) + 1 # add 1 because humans don't count from 0

    return (day, month, year)
