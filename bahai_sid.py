#!/usr/bin/python

# Convert between the sidereal Bahá'í calendar and Julian Day

from fractions import Fraction
from decimal import Decimal
from math import floor, ceil
from months import BAHAI_NUM as MONTHNO
from months import NUM_BAHAI as NUMON
from stars import ARIES
from solun import sunset
import sunmoon

sid_year = 365 + Fraction(6,24) + Fraction(9,1440) + Fraction(95,864000)
lon =  -51 - Fraction(23,60) - Fraction(20,3600) # longitude of Tehran
lat = 35 + Fraction(41,60) + Fraction(21,3600) # latitude of Tehran
tz = Fraction(7,48) # Iran's timezone

epoch = 2394673 + Fraction(69103,86400) # instant when the sun crossed Aries on 27 Farvardin 1223, UTC

def sunra(jday):
    '''Determine the right ascension of the sun'''
    jday = float(jday) - 0.5
    radec = sunmoon.pub.pub_solar_radec(jday)
    return radec[0]

def starra(jday):
    '''Determine the right ascension of 4 Arietis'''
    jday = float(jday) - 0.5
    ra = ARIES.ra
    dec = ARIES.dec
    distance = ARIES.distance
    rv = ARIES.rv
    dra = ARIES.dra
    ddec = ARIES.ddec

    radec = sunmoon.pub.pub_precession(jday, ra, dec, distance, rv, dra, ddec)
    return radec[0]

def dusk(jday):
    '''local time of sunset'''
    jday = int(jday)
    frac = sunset(jday, lon, lat)
    ans = jday + frac + tz
    return ans

def sep(jday):
    '''Angula separation between the sun and 4 Arieti; only right ascensions considered.'''
    jday = float(jday)
    sun = sunra(jday)
    aries = starra(jday)
    ans = aries - sun
    return ans

def crosstime(jday):
    '''Time the sun enters Aries'''
    jday = float(jday)
    p = 0
    while sep(jday) < 0:
        jday -= 1

    while (sep(jday) > 0) and (p <= 6):
        if sep(jday + (10 ** p)) <= 0:
            jday += (10 ** p)
        else:
            p -= 1

    frac = jday % 1
    frac = round(frac * 86400)
    ans = floor(jday) + Fraction(frac, 86400)
    return ans

def getnowruz(jday):
    '''Calculate day of Nowruz.'''
    jday = float(jday)
    cross = crosstime(jday) + float(tz)
    dusk = sunset(floor(cross), lon, lat) + tz
    if cross < dusk:
        nowruz = floor(cross)
    else:
        nowruz = ceil(cross)
    return nowruz

def fromjd(jday):
    '''Convert a Julian Day into a date in the sidereal Bahá'í calendar'''
    jday = int(jday)

    year = (jday - epoch) // sid_year
    cross = epoch + (year * sid_year)
    while getnowruz(cross) > jday:
        year -= 1
        cross -= sid_year
    while getnowruz(cross + sid_year) <= jday:
        year += 1
        cross += sid_year

    if year >= 0:
        year += 1
    next_cross = cross + sid_year
    nowruz = getnowruz(cross)
    next_nowruz = getnowruz(next_cross)

    if jday >= next_nowruz - 19:
        month = "ʻAláʼ"
        day = 1 + jday + 19 - next_nowruz
    else:
        month = NUMON[(jday - nowruz) // 19]
        day = 1 + ((jday - nowruz) % 19)

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a date in the sidereal Bahá'í calendar into a Julian Day.'''
    day = int(day)
    month = str(month)
    year = int(year)
    if year >= 0:
        year -= 1

    jday = epoch + (year * sid_year)
    cross = crosstime(jday)
    next_cross = crosstime(cross + sid_year)
    nowruz = getnowruz(cross)
    next_nowruz = getnowruz(next_cross)

    if month == "ʻAláʼ":
        jday = next_nowruz - 19 + day - 1
    else:
        jday = nowruz + (19 * MONTHNO[month]) + day - 1
    return jday
