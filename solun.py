#!/usr/bin/python3

# algorithms to determine the exact ecliptic longitude of the sun and the moon

from fractions import Fraction
from decimal import Decimal
from math import floor, ceil, cos, acos, pi
import sunmoon
import numpy as np
import gregorian
from tdiff import DIFF
import stars

tropical_year = 365 + Fraction(5,24) + Fraction(48,1440) + Fraction(45,86400)
lunar_month = 29 + Fraction(12,24) + Fraction(44,1440) + Fraction(28,864000)
solar_term = tropical_year / 12 # time between major solar terms
year12 = 12 * lunar_month
year13 = 13 * lunar_month
r2d = 180 / pi # convert radians to degrees
d2r = pi / 180 # convert degrees to radians

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
        t = Decimal(year - 2000) / 100
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


def angsep(ra1, dec1, ra2, dec2):
    '''Determine the angular separation between two bodies, given their right ascensions and declinations'''
    # this function assumes input angles are in degrees
    # the answer is given in the zodiacal, not ecliptical, coordinate system
    ra1 = Decimal(ra1) # right ascension of 1st body
    dec1 = Decimal(dec1) # declination of 1st body
    ra2 = Decimal(ra2) # right ascension of 2nd body
    dec2 = Decimal(dec2) # declination of 2nd body

    cra = cos(d2r * (ra2 - ra1))
    cdec = cos(d2r * (dec2 - dec1))
    sigma = r2d * acos(cra + cdes - 1)
    return sigma

def sunrise(jday, lon, lat):
    '''Time of sunrise on a given day for a given longitude and latitude'''
    deltat = udt(int(jday))
    jday = float(jday) - 0.5 # Julian Day in question
    lon = float(lon) # observer's longitude
    lat = float(lat) # observer's latitude
    ra2000 = 281.29 # https://astronomy.stackexchange.com/questions/35779/ra-and-dec-of-the-sun-at-j2000
    dec2000 = 0 - 23 - (2/60) - (8.2/3600) # https://astronomy.stackexchange.com/questions/35779/ra-and-dec-of-the-sun-at-j2000

    r = sunmoon.sidereal.solar_riset(jday, lon, lat)
    return(r[0])

def sunset(jday, lon, lat):
    '''Time of sunset on a given day for a given longitude and latitude'''
    deltat = udt(int(jday))
    jday = int(jday) - 0.5 # Julian Day in question
    lon = float(lon) # observer's longitude
    lat = float(lat) # observer's latitude
    ra2000 = 281.29 # https://astronomy.stackexchange.com/questions/35779/ra-and-dec-of-the-sun-at-j2000
    dec2000 = 0	- 23 - (2/60) -	(8.2/3600) # https://astronomy.stackexchange.com/questions/35779/ra-and-dec-of-the-sun-at-j2000
    
    s =	sunmoon.sidereal.solar_riset(jday, lon, lat)
    return(s[1])

def starrise(jday, lon, lat, ra2000, dec2000, distance, rv, deltara, deltadec):
    '''Time of a star rising for a given longitude and latitude'''
    deltat = udt(int(jday))
    jday = int(jday) - 0.5
    lon = float(lon)
    lat = float(lat)
    ra2000 = float(ra2000)
    dec2000 = float(dec2000)
    distance = float(distance)
    rv = float(rv)
    deltara = float(deltara)
    deltadec = float(deltadec)

    s = sunmoon.sidereal.stellar_riset(jday, lon, lat, deltat, ra2000, dec2000, distance, rv, deltara, deltadec)
    return(s[0])
