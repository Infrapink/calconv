#!/usr/bin/python3

# Convert between Julian Days and dates in the modern traditional Borana calendar as described by Asmarom Legesse
# The main source here is chapter 7 of Legesse's book Gada: Three Approaches to the Study of African Society
# Additional information is drawn from On The Borana Calendrical System: A Preliminary Field Report. Marco Bassi, Current Anthropology 29:4 (1988), pp 619—624
from solun import sid_year, sid_month, syn_month, newmoon, fullmoon, dayof_arab, local_lunar_stellar_conjunction as llsc, get_solar_zpos, first_visible_crescent
from stars import MOTHALLA
from fractions import Fraction
from decimal import Decimal

lon = Decimal('-35.802778') # longitude of Namoratung'a II
lat = Decimal('3.422778') # latitude of Namoratung'a II
tz = Fraction(3,24) # Kenya and Ethiopia are both UTC+3
#solar_epoch = 1947986.852074074 + (sid_year / 2) + (917 * sid_year) # local Julian Day in the year 1537 AD when the sun was in conjunction with Mothalla (Lami)
solar_epoch = 2282913.335293403

spring_months = ("Birra", "Ciḳawa", "Sadassa", "Abrasa", "Ammaji", "Gurranḍala", "Gurranḍala 2")
autumn_months = ("Bittotessa", "Camsa", "Bufa", "Wacabajji", "Obora Gudda", "Obora Diḳḳa", "Obora Diḳḳa 2")

spring_nums = {"Birra":        0,
               "Ciḳawa":       1,
               "Sadassa":      2,
               "Abrasa":       3,
               "Ammaji":       4,
               "Gurranḍala":   5,
               "Gurranḍala 2": 6}

autumn_nums = {"Bittotessa":    0,
               "Camsa":         1,
               "Bufa":          2,
               "Wacabajji":     3,
               "Obora Gudda":   4,
               "Obora Diḳḳa":   5,
               "Obora Diḳḳa 2": 6}

def dayof(jday):
    '''Return the day associated with an astronomical event, per the Borana'''
    return dayof_arab(Fraction(jday), lon, lat, tz)

def fvc(jday):
    '''Returns the local time of the first visible crescent'''
    return first_visible_crescent(jday, tz)

def zeq(jday, opp):
    '''Compute when the sun is in conjunction or opposition to Sheratan (Lami)
    zeq is a contraction of zodiacal equinox
    This makes it easier to find the start and midpoint of the year'''
    jday = Fraction(jday)
    opp = bool(opp) # True for opposition, False for conjunction

    return get_solar_zpos(jday, MOTHALLA, opp, 0)

def spring_crescent(year):
    '''Compute the date of the first visible crescent of the month Birra'''
    year = int(year)

    equinox = zeq((solar_epoch + (year * sid_year) + (sid_year / 2)), False) # not the real equinox, but the conjunction the Borana use
    mid = fullmoon(equinox, tz) # midpoint of the month
    while (dayof(fullmoon(mid, tz)) < dayof(equinox)):
        mid += syn_month
    while (dayof(fullmoon((mid - syn_month), tz)) >= dayof(equinox)):
        mid -= syn_month

    crescent = fvc(mid - (syn_month / 2))
    return dayof(crescent)

def autumn_crescent(year):
    '''Compute the date of the first visible crescent of the month Bittotessa'''
    year = int(year)

    equinox = zeq((solar_epoch + (year * sid_year)), True) # not the real equinox, but the conjunction the Borana use
    crescent = fvc(equinox)
    while (dayof(fvc(crescent)) < dayof(equinox)):
        crescent += syn_month
    while (dayof(fvc(crescent - syn_month)) >= dayof(equinox)):
        crescent -= syn_month

    return dayof(crescent)

def fromjd(jday):
    '''Convert a Julian Day into a date in the modern Borana calendar'''
    jday = Fraction(jday)

    # compute the year
    year = int((jday - solar_epoch) // sid_year)
    while (autumn_crescent(year) > jday):
        year -= 1
    while (autumn_crescent(year + 1) <= jday):
        year += 1

    # compute the start of the month
    crescent = fvc(jday)
    while (dayof(fvc(crescent)) > jday):
        crescent -= syn_month
    while (dayof(fvc(crescent + syn_month)) <= jday):
        crescent += syn_month

    # compute the month
    if (spring_crescent(year) <= dayof(crescent)):
        month = spring_months[int(round((crescent - spring_crescent(year)) / syn_month))]
    else:
        month = autumn_months[int(round((crescent - autumn_crescent(year)) / syn_month))]

    # compute the day
    day = jday - dayof(fvc(crescent)) + 1 # add 1 because humans don't count from 0

    cycle = year // 8
    year = (year % 8) + 1 # add 1 because computers count from 0

    return (day, month, year, cycle)

def tojd(day, month, year, cycle):
    '''Convert a Borana date to a Julian Day'''
    day = int(day) - 1 # subtract 1 because humans don't count from 0
    month = str(month)
    year = int(year - 1) + (8 * int(cycle)) # subtract 1 from the year because humans don't count from 0

    if (month in spring_months):
        jday = spring_crescent(year)
        months = spring_nums
        if ( (month == "Gurranḍala 2") and (autumn_crescent(year + 1) - jday > 200) ):
            month = "Gurranḍala"
    else:
        jday = autumn_crescent(year)
        months = autumn_nums
        if ( (month == "Obora Diḳḳa 2") and (spring_crescent(year) - jday > 200) ):
            month = "Obora Diḳḳa"

    jday = dayof(fvc(jday + (syn_month * months[month]))) + day

    return jday
