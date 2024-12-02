#!/usr/bin/python

# Convert between Julian Days and the Kaua'i version of the traditional Hawai'ian calendar.

from fractions import Fraction
from stars import PLEIADES
from solun import lunar_month as syn_month, sid_year, acronycal_rising, first_visible_crescent, dayof_arab
from months import KAUAI as MONTHS, NUM_KAUAI as MONTHNO

lon = 155 - Fraction(30,60) # longitude of the centre of Hawai'i Island
lat = 19 + Fraction(36,60) # latitude of the centre of Hawai'i Island
tz = Fraction(-10,24) # Hawai'i's timezone
epoch = 2376621 - 365 # year 1 is 1795 AD, starting in November 1794; this is the start of year 0

def fvc(jday):
    '''Compute the time of first visible crescent'''
    return first_visible_crescent(Fraction(jday), tz)

def dayof(jday):
    '''Compute which midnight-indexed Julian Day corresponds to a given astronomical event (which in this case is the new moon)'''
    return dayof_arab(Fraction(jday), lon, lat, tz)

def acris(jday):
    '''Compute the day of the acronycal rising of the Pleiades'''
    return acronycal_rising(Fraction(jday), lon, lat, PLEIADES, tz)

def tojd(day, month, year):
    '''Convert a date in the Kaua'ian calendar to a Julian Day'''
    day = int(day) - 1 # subtract 1 because computers count from 0
    month = str(month)
    year = int(year) # I figure that by the time of unification, the Hawai'ians knew about 0

    # account for the year
    kupuku = acris(epoch + (year * sid_year))

    # first new moon on or after that night
    hilo = fvc(kupuku)
    while (dayof(fvc(hilo)) < kupuku):
        hilo += syn_month
    while (dayof(fvc(hilo - syn_month)) >= kupuku):
        hilo -= syn_month
        
    # account for the month
    if (month == "Malama Pili"):
        m = 12
    else:
        m = MONTHNO[month]

    jday = dayof(fvc(hilo + (m * syn_month))) + day

    return jday

def fromjd(jday):
    '''Convert a Julian Day to a date in the Kaua'ian calendar'''
    jday = int(jday)

    # compute the crescent that starts the month
    hilo = fvc(jday)
    while (dayof(fvc(hilo)) > jday):
        hilo -= syn_month
    while (dayof(fvc(hilo + syn_month)) <= jday):
        hilo += syn_month

    # compoute the year
    year = (hilo - epoch) // sid_year
    while ( acris(epoch + (year * sid_year)) > dayof(fvc(hilo)) ):
        year -= 1
    while (acris(epoch + ((year + 1) * sid_year)) <= dayof(fvc(hilo)) ):
        year += 1

    # compute the month
    kupuku = acris(epoch + (year * sid_year))
    firstmoon = fvc(kupuku)
    while (dayof(fvc(firstmoon)) < kupuku):
        firstmoon += syn_month
    while (dayof(fvc(firstmoon - syn_month)) >= kupuku):
        firstmoon -= syn_month
    m = round((hilo - firstmoon) / syn_month)
    if (m == 12):
        month = "Malama Pili"
    else:
        month = MONTHS[m]

    day = jday - dayof(fvc(hilo)) + 1 # add 1 because humans don't count from 0

    return (day, month, year)
