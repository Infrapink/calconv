#!/usr/bin/python3

# algorithms to determine the exact ecliptic longitude of the sun and the moon

from fractions import Fraction
from decimal import Decimal
from math import floor
import sunmoon
import numpy as np
import gregorian

tropical_year = 365 + Fraction(5,24) + Fraction(48,1440) + Fraction(45,86400)
lunar_month = 29 + Fraction(12,24) + Fraction(44,1440) + Fraction(28,864000)
solar_term = tropical_year / 12 # time between major solar terms
year12 = 12 * lunar_month
year13 = 13 * lunar_month

def spos(day):
    '''Ecliptic longitude of the sun'''
    day = floor(day) + 0.5
    return sunmoon.solar_coords.solar_longitude(day)

def mpos(day):
    '''Ecliptic longitude of the moon'''
    day = floor(day) + 0.5
    return sunmoon.lunar_coords.lunar_longitude(day)

def trans(day, angle, frtz):
    '''Time the sun hits a particular ecliptic longitude'''
    day = floor(day) + 0.5
    angle = float(angle)
    frtz = Fraction(frtz) # timezone
    
    minutes = int(sunmoon.solar_coords.solar_time(day, angle))
    time = int(day) + Fraction(minutes, 1440) + frtz
    return time

def conj(day, frtz):
    '''Julian Day and time of the new moon, UTC'''
    day = floor(day) + 0.5
    frtz = Fraction(frtz) # timezone

    minutes = int(sunmoon.lunar_coords.lunar_time(day))
    time = int(day) + Fraction(minutes, 1440) + frtz
    return time

def truesun(day, angle, timezone):
    day = Fraction(day)
    angle = int(angle)
    timezone = Fraction(timezone)
    return(floor(suntime(day, angle, timezone)))

def truemoon(day, timezone):
    day = Fraction(day)
    timezone = Fraction(timezone)
    return(floor(conj(day, timezone)))
