#!/usr/bin/python3

# algorithms to determine the exact ecliptic longitude of the sun and the moon

from fractions import Fraction
from decimal import Decimal
from math import floor, ceil
import sunmoon
import numpy as np
import gregorian
from tdiff import DIFF

tropical_year = 365 + Fraction(5,24) + Fraction(48,1440) + Fraction(45,86400)
lunar_month = 29 + Fraction(12,24) + Fraction(44,1440) + Fraction(28,864000)
solar_term = tropical_year / 12 # time between major solar terms
year12 = 12 * lunar_month
year13 = 13 * lunar_month

def udt(jday):
    '''Get the difference between Universal Time and Dynamical Time for a given Julian Day'''
    jday = floor(jday)

    gdate = gregorian.fromjd(jday)
    year = gdate[2]

    if year in DIFF.keys():
        deltat = DIFF[year]
    elif year in range(1621,2000):
        deltat = Decimal('0.5') * (DIFF[year - 1] + DIFF[year + 1])
    else:
        # approximate value
        t = (year - 2000) / 100
        if year < 948:
            deltat = 2177 + (497 * t) + (t * t * Decimal('77.1'))
        elif (year <= 1600) or (year > 2000):
            deltat = 102 + (102 * t) + (t * t * Decimal('25.3'))
            if year <= 2100:
                deltat = deltat + (Decimal('0.37') * (year - 2100))

    return deltat

def spos(day):
    '''Ecliptic longitude of the sun'''
    day = floor(day) - 0.5
    return sunmoon.solar_coords.solar_longitude(day)

def mpos(day):
    '''Ecliptic longitude of the moon'''
    day = floor(day) - 0.5
    return sunmoon.lunar_coords.lunar_longitude(day)

def trans(day, angle, frtz):
    '''Time the sun hits a particular ecliptic longitude'''
    day = floor(day) - 0.5
    angle = float(angle)
    frtz = Fraction(frtz) # timezone
    
    minutes = int(sunmoon.solar_coords.solar_time(day, angle))
    time = ceil(day) + Fraction(minutes, 1440) + frtz
    return time

def conj(day, frtz):
    '''Julian Day and time of the new moon, UTC'''
    day = floor(day) - 0.5
    frtz = Fraction(frtz) # timezone

    minutes = int(sunmoon.lunar_coords.lunar_time(day))
    time = ceil(day) + Fraction(minutes, 1440) + frtz
    return time

def truesun(day, angle, timezone):
    day = Fraction(day)
    angle = int(angle)
    timezone = Fraction(timezone)
    return(floor(trans(day, angle, timezone)))

def truemoon(day, timezone):
    day = Fraction(day)
    timezone = Fraction(timezone)
    return(floor(conj(day, timezone)))

def sunrise(jday, lon, lat, deltat, ra0, dec0, ra1, dec1, ra2, dec2):
    jday = floor(jday) - 0.5
    lon = float(lon)
    lat = float(lat)
    deltat = float(deltat)
    yesterday = (float(ra0), float(dec0))
    today = (float(ra1), float(dec1))
    tomorrow = (float(ra2), float(dec2))

    return sunmoon.sidereal.riset(jday, lon, lat, deltat, yesterday, today, tomorrow, 0)
