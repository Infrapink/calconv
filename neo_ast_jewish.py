#!/usr/bin/python3

# Convert between Julian Days and Irv Bromborg's astronomical Jewish calendar system

from math import floor, ceil
from fractions import Fraction
from months import HEBREW as MONTHS
from solun import newmoon, trans, local_sunset, tropical_year as trop_year, syn_month

tz = Fraction(2,24) # Israeli Standard Time
lon = 0 - (35 + Fraction(14,60) + Fraction(9, (60 ** 2))) # longitude of Jerusalem
lat = 32 + Fraction(46, 60) + Fraction(40, (60 ** 2)) # latitude of Jerusalem

solar_epoch = 347836 + Fraction(427, 480) # northward equinox closest to 1 Nisan of the year 0; thus, the Nisan prior to the molad tohu

def sunset(jday):
    return local_sunset(Fraction(jday), lon, lat, tz)

def dayof(jday):
    '''Compute the day associated with a new moon'''
    jday = Fraction(jday)

    darkmoon = newmoon(jday, tz)
    dusk = sunset(jday)

    if (dusk - darkmoon > 0.5):
        ans = ceil(dusk)
    else:
        ans = ceil(dusk) + 1

    return ans

def aviv(year):
    '''Compute the 1st of Nisan for a given year'''
    year = int(year)

    equinox = trans((solar_epoch + (year * trop_year)), 0, tz) # northward equinox
    darkmoon = newmoon(equinox, tz)
    if (equinox < sunset(equinox)):
        eqday = ceil(equinox)
    else:
        eqday = ceil(equinox) + 1
    while (dayof(darkmoon) > eqday):
        darkmoon -= syn_month
    while (dayof(darkmoon + syn_month) <= eqday):
        darkmoon += syn_month

    if (eqday - dayof(darkmoon) > 15):
        # Nisan must be moved forward a month lest the full moon fall after the equinox
        darkmoon += syn_month

    return darkmoon

def rosh_hashanah(year):
    '''Compute Rosh Hashanah of a given year'''
    year = int(year)

    nisan = aviv(year)
    prev_nisan = aviv(year - 1)

    if (round((nisan - prev_nisan) / syn_month) == 13):
        # leap year
        rosh = nisan - (7 * syn_month)
    else:
        # normal year
        rosh = nisan - (6 * syn_month)

    if (dayof(rosh) % 7 in (2, 4, 6)): # Rosh Hashanah can't fall on a Wednesday, Friday, or Sunday
        if (dayof(rosh) - dayof(rosh - syn_month) == 30):
            rosh = dayof(rosh) - 1
        else:
            rosh = dayof(rosh) + 1
    else:
        rosh = dayof(rosh)

    return (rosh)

def fromjd(jday):
    '''Convert a Julian Day into a date in the astronomical Jewish calendar'''
    jday = int(jday)

    # compute the year
    year = (jday - solar_epoch - 183) // trop_year
    while (rosh_hashanah(year) > jday):
        year -= 1
    while (rosh_hashanah(year + 1) <= jday):
        year += 1


    # compute the month
    if (dayof(aviv(year)) <= jday):
        m = 7
        rosh = aviv(year)
    else:
        m = 0
        rosh = rosh_hashanah(year)
    while (dayof(rosh + syn_month) <= jday):
        m += 1
        rosh += syn_month
    month = MONTHS[m]

    # compute the day
    if (m > 0):
        rosh = dayof(rosh)
    day = jday - rosh + 1 # add 1 because computers count from 0

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a date in the astronomical Jewish calendar to a Julian Day'''
    day = int(day) - 1 # subtract 1 because humans don't count from 0
    month = str(month)
    year = int(year)

    # account for the year
    if (month in ("Nisan", "Iyar", "Sivan", "Tammuz", "Av", "Elul")):
        jday = aviv(year)
        m = 7
    else:
        jday = rosh_hashanah(year)
        m = 0

    # account for the month
    if ( (month == "Veadar") and (round((aviv(year) - rosh_hashanah(year)) / syn_month) == 7) ):
        # user specfied Veadar in a normal year
        month = "Adar"
    while (month != MONTHS[m]):
        jday += syn_month
        m += 1

    # account for the day
    jday = dayof(jday) + day

    return jday
