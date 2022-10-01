#!/usr/bin/python

# Convert between the True Hindu solar calendar and Julian Day

from math import floor, ceil
from fractions import Fraction
from months import NUM_HINDU as NUMON
from months import HINDU_NUM as MONTHNO
from hindu_functions import uj_lon as lon
from hindu_functions import uj_lat as lat
from hindu_functions import sunrise, solar_longitude, zodiac, solar_convergence

ky = 588466 # Beginning of the Kali Yuga in Julian Days; note that the epoch actually happens at sunrise, but I haven't figured out how to calculate that just yet
sid_year = 365 + Fraction(279547, 1080000)
sid_month = 27 + Fraction(4644439, 14438334)
syn_month = 29 + Fraction(7087771, 13358334)
rasi = sid_year / 12

creation = ky - (1955880000 * sid_year)
solar_epoch = ky
anom_year = Fraction(1577917828000, (4320000000 - 387)) # anomalistic year
anom_month = Fraction(1577917828, (57753336 - 488199)) # anomalistic month

def suncheck(time):
    time = Fraction(time)

    dawn = sunrise(time, lon, lat)
    if (dawn > time):
        ans = ceil(dawn)
    else:
        ans = floor(dawn)

    return ans

def fromjd(jday):
    '''Convert a Julian Day into a date'''
    jday = Fraction(jday)

    year = (jday - solar_epoch) // sid_year
    sankranti = solar_epoch + (year * sid_year)
    next_sankranti = sankranti + sid_year
    prev_sankranti = sankranti - sid_year

    sankranti = solar_convergence(sankranti, 0)
    next_sankranti = solar_convergence(next_sankranti, 0)
    prev_sankranti = solar_convergence(prev_sankranti, 0)

    if suncheck(next_sankranti) <= suncheck(jday):
        sankranti = next_sankranti
        year += 1
    elif suncheck(sankranti) > suncheck(jday):
        sankranti = prev_sankranti
        year -= 1

    m = zodiac(jday)
    month = NUMON[m]

    r = solar_convergence((sankranti + (m * rasi)), (m * 30)) # instant the sun enters the mth rasi
    day = floor(jday - suncheck(r)) + 1

    return (day, month, year)

    
def tojd(day, month, year):
    '''Convert a date into a Julian Day'''
    day = int(day)
    m = MONTHNO[str(month)]
    year = int(year)

    jday = solar_epoch + (year * sid_year) + (m * rasi)
    jday = solar_convergence(jday, (m * 30)) # instant the sun enters the mth rasi
    jday = suncheck(jday) + day - 1

    return jday
    
