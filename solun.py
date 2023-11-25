#!/usr/bin/python3

# algorithms to determine the exact ecliptic longitude of the sun and the moon

from fractions import Fraction
from decimal import Decimal
from math import floor, ceil, cos, acos, pi, sin, asin, tan, atan
import sunmoon
import numpy as np
import gregorian
from tdiff import DIFF
import stars

tropical_year = 365 + Fraction(5,24) + Fraction(48,1440) + Fraction(45,86400)
lunar_month = 29 + Fraction(12,24) + Fraction(44,1440) + Fraction(28,864000)
solar_term = tropical_year / 12 # time between major solar terms
sid_year = 365 + Fraction(6, 24) + Fraction(9, 1440) + Fraction(954, 8640000)
rasi = sid_year / 12 # time for the sun to transit one zodiac sign
year12 = 12 * lunar_month
year13 = 13 * lunar_month
r2d = 180 / pi # convert radians to degrees
d2r = pi / 180 # convert degrees to radians
eqm = 0.6749121716696571 # Difference between the celestial longitudes of the sun and counterspica when the sun hit an ecliptic angle of 23°15' in 1955. This is used in computing the instant of Meṣa Saṁkrānti

def dsin(angle):
    '''sine of an angle in degrees'''
    angle = float(angle)
    ans = sin(angle * d2r)
    return ans

def dcos(angle):
    '''cosine of an angle in degrees'''
    angle = float(angle)
    ans = cos(angle * d2r)
    return ans

def dtan(angle):
    angle = float(angle)
    ans = tan(angle * d2r)
    return ans


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


def starrise2(jday, lon, lat, star):
    '''Time of a star rising for a given longitude and latitude.'''
    deltat = udt(int(jday))
    jday = int(jday) - 0.5
    lon = float(lon)
    lat = float(lat)

    s = sunmoon.sidereal.stellar_riset(jday, lon, lat, deltat, star.ra, star.dec, star.distance, star.rv, star.dra, star.ddec)
    return(s[0])

def starpos(jday, star):
    '''Determine the right ascension and declination of a given star as of jday. See Meeus, chapter 23'''
    jday = Fraction(jday) - Fraction(12,24) # convert from midnight-to-midnight to noon-to-noon denotation

    # first, the effect of proper motion
    radec = sunmoon.stellar_coords.propmot(jday, star.ra, star.dec, star.distance, star.rv, star.dra, star.ddec)
    ra = radec[0]
    dec = radec[1]

    # next, apply the effect of nutation
    nut = sunmoon.stellar_coords.nutation(jday)
    epsilon = nut[0]
    delta_psi = nut[1]
    delta_epsilon = nut[2]
    delta_ra1 = ((dcos(epsilon) + (dsin(epsilon) * dsin(ra) * dtan(dec))) * delta_psi) - ((dcos(ra) * dtan(dec)) * delta_epsilon)
    delta_dec1 = (dsin(epsilon) * dcos(ra) * delta_psi) + (dsin(ra) * delta_epsilon)

    # next, the effect of aberration
    T = (jday - 2451545 + Fraction(12,24)) / 36525 # Julian Centuries since J2000.0
    ecc = 0.016708634 - (0.000042037 * T) - (0.0000001267 * T * T) # eccentricity of Earth's orbit
    per = 102.93735 + (1.71946 * T) + (0.00046 * T * T) # longitude of perihelion, in DEGREES
    kappa = 20.49552 / 3600 # constant of aberration, in DEGREES

    solar_radec = sunmoon.solar_coords.solar_radec(jday)
    solar_ra = solar_radec[0]
    solar_dec = solar_radec[1]

    delta_ra2a = (0 - kappa) * (((dcos(ra) * dcos(solar_ra) * dcos(epsilon)) + (dsin(ra) * dsin(epsilon))) / dcos(dec))
    delta_ra2b = (ecc * kappa) * (((dcos(ra) * dcos(per) * dcos(epsilon)) + (dsin(ra) * dsin(per))) / dcos(dec))
    delta_ra2 = delta_ra2a + delta_ra2b

    delta_dec2a = (dcos(solar_ra) * dcos(epsilon) * ((dtan(epsilon) * dcos(dec)) - (dsin(ra) * dsin(dec)))) + (dcos(ra) * dsin(dec) * dsin(solar_ra))
    delta_dec2b = ((((dtan(epsilon) * dtan(dec)) - (dsin(ra) + dsin(dec)))) * dcos(per) * dcos(epsilon)) + (dcos(ra) * dsin(dec) * dsin(per))
    delta_dec2 = ((0 - kappa) * delta_dec2a) + (ecc * kappa * delta_dec2b)

    delta_ra = (delta_ra1 + delta_ra2) / 3600 # divide by 3600 to convert from seconds to degrees
    delta_dec = (delta_dec1 + delta_dec2) / 3600 # divide by 3600 to convert from seconds to degrees

    ra += delta_ra
    dec += delta_dec
    
    return(ra, dec)

def counterstar(jday, star):
    '''Calculate the point exactly opposite a given star, in the celestial coördinate system'''
    jday = Fraction(jday)
    coords = starpos(jday, star)
    counter_ra = (coords[0] + 180) % 360
    counter_dec = 0 - coords[1]
    return(counter_ra, counter_dec)

def solar_cel_coords(jday):
    '''Get the right ascension and declination of the sun'''
    ans = sunmoon.solar_coords.solar_radec(jday)
    return ans

def solar_zpos(jday, star, opp):
    '''Compute the sun's zodiacal position'''
    jday = Fraction(jday) # time under consideration
    opp = bool(opp) # False means the zodiac starts at a given star, True means it starts opposite that star
    
    solar_radec = solar_cel_coords(jday)
    solar_ra = solar_radec[0]
    if (opp == False):
        # zodiac starts at the star
        zero = starpos(jday, star)
    else:
        # zodiac starts opposite the star
        zero = counterstar(jday, star)
        
    stellar_ra = zero[0]
    sep = solar_ra - stellar_ra # angular separation of the sun from the star
    while (sep < 0):
        sep += 360

    return sep

def get_solar_zpos(jday, star, opp, angle):
    '''Zero in on the time the sun hits a given zodiacal angle'''
    jday = Fraction(jday)
    opp = bool(opp) # False means the zodiac starts at a given star, True means it starts opposite that star
    angle = float(angle)

    p = 0

    while (p < 4):
        if (solar_zpos(jday, star, angle) == angle):
            p = 4
        else:
            f = Fraction(1, (60 ** p))
            while ((solar_zpos(jday, star, opp) <= 90) and (angle >= 270)):
                jday -= f
            while ((solar_zpos(jday, star, opp) >= 270) and (angle <= 90)):
                jday += f
            while (solar_zpos(jday, star, opp) + f <= angle):
                jday += Fraction(1, (60 ** p))
            while (solar_zpos(jday, star, opp) - f >= angle):
                jday -= f
            p += 1

    return jday

def indian_spos(jday):
    '''Compute the zodiacal position of the sun for modern Indian calendars'''
    jday = Fraction(jday) - Fraction(11,48) # convert IST to UTC
    ans = (solar_zpos(jday, SPICA, True) - eqm) % 360
    return ans

def get_indian_spos(jday, angle):
    '''Zero in on the time the sun hits a given zodiacal longitude as used in modern Indian calendars'''
    jday = Fraction(jday)
    angle = float(angle)

    ans = get_solar_zpos(jday, SPICA, True, ((angle - eqm) % 360)) # time in UTC
    ans += Fraction(11,48) # convert from UTC to IST
    return ans
