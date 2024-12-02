#!/usr/bin/python

# Convert between Julian Days and the nonspecific Kona variant of the traditional Hawai'ian calendar

from fractions import Fraction
from stars import PLEIADES
from solun import lunar_month as syn_month, sid_year, acronycal_rising, first_visible_crescent, dayof_arab
from months import HAWAIIAN as MONTHS, NUM_HAWAIIAN as MONTHNO

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

def lny(kupuku):
    '''Compute the first crescent of the year'''
    kupuku = int(kupuku) # acronycal rising of the Pleiades

    next_kupuku = acris(kupuku + sid_year)

    hilo = fvc(kupuku)
    while (dayof(fvc(hilo)) > kupuku):
        hilo -= syn_month
    while (dayof(fvc(hilo + syn_month)) <= kupuku):
        hilo += syn_month

    next_hilo = fvc(next_kupuku)
    while (dayof(fvc(next_hilo)) > next_kupuku):
        next_hilo -= syn_month
    while (dayof(fvc(next_hilo + syn_month)) <= next_kupuku):
        next_hilo += syn_month

    if (round( (next_hilo - hilo) / syn_month) == 13):
        # leap year
        l = True
        hilo -= syn_month
    else:
        l = False

    return(hilo, l)

def tojd(day, month, year):
    '''Convert a date in the traditional Hawai'ian calendar to a Julian Day'''
    day = int(day) - 1 # subtract 1 because computers count from 0
    month = str(month)
    year = int(year) # I figure that by the time of unification, the Hawai'ians knew about 0

    # account for the year
    kupuku = acris(epoch + (year * sid_year))

    # first new moon on or after that night
    nyd = lny(kupuku)
    hilo = nyd[0]
    l = nyd[1]
        
    # account for the month
    if (month == "Malama Pili"):
        m = 1
    elif(month == "ʻIkuā"):
        m = 0
    elif (l):
        # leap year
        m = (MONTHNO[month] + 2) % 12
    else:
        # normal year
        m = (MONTHNO[month] + 1) % 12

    jday = dayof(fvc(hilo + (m * syn_month))) + day

    return jday

def fromjd(jday):
    '''Convert a Julian Day to a date in the traditional Hawai'ian calendar'''
    jday = int(jday)

    # compute the year
    year = (jday - epoch) // sid_year
    kupuku = epoch + (year * sid_year)
    while (dayof(lny(acris(kupuku))[0]) > jday):
        kupuku -= sid_year
        year -= 1
    while(dayof(lny(acris(kupuku + sid_year))[0]) <= jday):
        kupuku += sid_year
        year += 1
    nyd = lny(acris(kupuku))
    firstmoon = nyd[0] # first crescent of the year
    l = nyd[1] # is it leap?

    # compute the crescent that starts the month
    hilo = fvc(jday)
    while (dayof(fvc(hilo)) > jday):
        hilo -= syn_month
    while (dayof(fvc(hilo + syn_month)) <= jday):
        hilo += syn_month

    # compute the month
    m = round((hilo - firstmoon) / syn_month)
    if (not l):
        # normal year
        month = MONTHS[(m - 1) % 12]
    else:
        # leap year
        if (m == 0):
            month = "ʻIkuā"
        elif (m == 1):
            month = "Malama Pili"
        else:
            month = MONTHS[(m - 2) % 12]

    day = jday - dayof(fvc(hilo)) + 1 # add 1 because humans don't count from 0

    return (day, month, year)
