#!/usr/bin/python

# Convert between the Egyptian observational calendar and Julian Day.

from fractions import Fraction
from decimal import Decimal
from math import floor, ceil, pi, sin, cos, acos, asin
from solun import sunrise, starrise
from stars import SIRIUS
from months import EGYPTIAN_NUM as MONTHNO
from months import NUM_EGYPTIAN as NUMON
import sunmoon

#epoch = 160539 + Fraction(17251, 17280) # worked out in Stellarium
epoch = 160572 + Fraction(4,24) + Fraction(26,1440) + Fraction(18,86400)
sothic_year = 365 + Fraction(6,24) + Fraction(1,1440)

lon = 0 - (31 + Fraction(8,60) + Fraction(3,3600)) # longitude of the Great Pyramid
lat = 29 + Fraction(58,60) + Fraction(45,3600) # latitude of the Great Pyramid
tz = Fraction(2,24) # Egypt's timezone is UTC+2

d2r = pi/180 # convert degrees to radians
r2d = 180/pi # convert radians to degrees

def dawn(jday):
    '''Local sunrise in UTC'''
    jday = int(jday)
    frac = sunrise(jday, lon, lat)
    ans = jday + frac
    return ans

def sirise(jday):
    '''Local Sirius rising in UTC'''
    jday = int(jday)
    ra = SIRIUS.ra
    dec = SIRIUS.dec
    distance = SIRIUS.distance
    rv = SIRIUS.rv
    dra = SIRIUS.dra
    ddec = SIRIUS.ddec
    frac = starrise(jday, lon, lat, ra, dec, distance, rv, dra, ddec)
    rise = jday + frac
    return rise

def rdiff(jday):
    '''Different in time between the times that Sirius and the sun rise'''
    jday = int(jday)
    sun = dawn(jday)
    star = sirise(jday)
    diff = sun - star
    diff = round(diff * 86400) # convert to seconds
    diff = Fraction(diff, 86400)
    #return (24 * diff) # return the difference in hours
    return diff

def fromjd(jday):
    '''Convert a Julian Day into a date in the Egyptian observational calendar'''
    jday = int(jday)
    year = (jday - epoch) // sothic_year
    madjet = epoch + (year * sothic_year)
    prev_madjet = madjet - sothic_year
    next_madjet = madjet + sothic_year

    sopdet = floor(madjet)
    next_sopdet = floor(next_madjet)
    prev_sopdet = floor(prev_madjet)

    # since I can't properly calculate celestial bodies' altitudes,
    # I'm operating on the basis that when the rise times of the sun and Sirius
    # are separated by 30 minutes (Tetley, p. 42), we have the heliacal rising
    while rdiff(sopdet) > Fraction(1800,86400):
        sopdet -= 1
    while rdiff(prev_sopdet) > Fraction(1800,86400):
        prev_sopdet -= 1
    while rdiff(next_sopdet) > Fraction(1800,86400):
        next_sopdet -= 1
    while rdiff(sopdet) < Fraction(1800,86400):
        sopdet += 1
    while rdiff(prev_sopdet) < Fraction(1800,86400):
        prev_sopdet += 1
    while rdiff(next_sopdet) < Fraction(1800,86400):
        next_sopdet += 1

    if jday < sopdet:
        sopdet = prev_sopdet
        year -= 1
    elif jday >= next_sopdet:
        sopdet = next_sopdet
        year += 1

    if year >= 0:
        year += 1

    month = NUMON[(jday - sopdet) // 30]
    day = ((jday - sopdet) % 30) + 1

    return(day, month, year)

def tojd(day, month, year):
    '''Convert a date in the Egyptian observational calendar to a Julian Day'''
    day = int(day)
    month = str(month)
    year = int(year)

    if year >= 0:
        year -= 1

    jday = floor(epoch + (year * sothic_year))
    # since I can't properly calculate celestial bodies' altitudes,                                       
    # I'm operating on the basis that when the rise times of the sun and Sirius                                     
    # are separated by 30 minutes (Tetley, p. 42), we have the heliacal rising
    while rdiff(jday) > Fraction(1800,86400):
        jday -= 1
    while rdiff(jday) < Fraction(1800,86400):
        jday += 1

    jday = jday + (30 * MONTHNO[month])
    jday = jday + day - 1
    return jday
    
