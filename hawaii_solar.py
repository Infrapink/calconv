#!/usr/bin/python3

# Convert between the Hawai'ian solar calendar and Julian Days

from fractions import Fraction
from solun import sid_year, acronycal_rising
from months import HAWAIIAN as MONTHS, NUM_HAWAIIAN as MONTHNO
from stars import PLEIADES

epoch = 2376621 - 365 # November 1793 AD, the approximate start of year 0
tz = Fraction(-10,24) # Hawai'i's timezone
lon = -155 - Fraction(30,60) # longitude of the centre of Hawai'i Island
lat = 19 + Fraction(36,60) # latitude of the centre of Hawai'i Island

def acris(jday):
    '''Compute the day of the acronycal rising of the Pleiades'''
    return acronycal_rising(int(jday), lon, lat, PLEIADES, tz)

def tojd(day, month, year):
    '''Convert a year in the Hawai'ian solar calendar to a Julian Day'''
    day = int(day) - 1 # subtract 1 because humans don't count from 0
    month = str(month)
    year = int(year)

    if (month == "Extra Days"):
        m = 12
    else:
        m = MONTHNO[month]

    jday = acris(epoch + (year * sid_year)) + (30 * m) + day

    return jday

def fromjd(jday):
    '''Convert a Julian Day to a date in the Hawai'ian solar calendar'''
    jday = int(jday)

    # compute the year
    year = (jday - epoch) // sid_year
    while (acris(epoch + ((year + 1) * sid_year)) <= jday):
        year += 1
    while (acris(epoch + (year * sid_year)) > jday):
        year -= 1
    kupuku = acris(epoch + (year * sid_year))

    # compute the month and day
    if ((jday - kupuku) // 30 == 12):
        month = "Extra days"
    else:
        month = MONTHS[(jday - kupuku) // 30]
    day = ((jday - kupuku) % 30) + 1 # add 1 because computers count from 0

    return (day, month, year)
