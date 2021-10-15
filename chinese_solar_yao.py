#!/usr/bin/python3

# Convert between the old Chinese calendar (Huangdi era) and Julian Day.

from fractions import Fraction
from math import floor
from months import JIEQI, SOLAR_TERMS
from solun import truesun

solar_year = 365 + Fraction(5,24) + Fraction(49,1440) + Fraction(328,864000)
solar_term = solar_year / 24
solstice = Fraction(403466862457, 432000) # instant of the southern solstice preceding the first year of the reign of Emperor Yao, GMT
epoch = solstice + (3 * solar_term)
timezone = Fraction(8,24)

def tojd(day, st, year):
    day = int(day)
    st = str(st)
    year = int(year)

    if year > 0:
        # positive years
        jday = epoch + (solar_year * (year - 1))

    else:
        # negative years
        jday = epoch + (year * solar_year)

    for s in JIEQI.keys():
        if s == st:
            jday = truesun(jday, JIEQI[s], timezone) + day - 1
            break
        else:
            jday += solar_term

    return jday

def fromjd(jday):
    jday = int(jday)
    day = 0
    st = ""
    year = 0

    if jday >= truesun(epoch + (3 * solar_term), 315, timezone):
        # positive dates
        orbits = ((jday - epoch) // solar_year)
        dongzhi = solstice + (orbits * solar_year)
        year = orbits + 1
        xin = dongzhi + (3 * solar_term)
        while jday >= truesun(xin + solar_year, 315, timezone):
            year += 1
            xin += solar_year


    else:
        # negative dates
        year = 0 - ((epoch - jday) // solar_year)
        dongzhi = solstice + (year * solar_year)
        xin = dongzhi + (3 * solar_term)
        while jday < truesun(xin, 315, timezone):
            year -= 1
            xin -= solar_year

    term = xin
    angle = 315

    while truesun((term + solar_term), ((angle + 15) % 360), timezone) <= jday:
        term += solar_term
        angle = (angle + 15) % 360

    st = SOLAR_TERMS[angle]
    day = jday - truesun(term, angle, timezone) + 1    

    return(day, st, year)
