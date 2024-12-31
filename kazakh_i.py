#!/usr/bin/python3

# Convert between Julian Days and the Kazakh nomad calendar, wherein days start at midnight.

from fractions import Fraction
from stars import PLEIADES
from solun import sid_month, syn_month, local_lunar_stellar_conjunction, newmoon, phase, dayof_arab

epoch = 1948379 # first conjunction of the new moon with the Pleiades in the year of Muhammad's flight to Mecca
tz = Fraction(5, 24) # Kazakhstan is UTC+5
lat = 51 + Fraction(10, 60) # latitude of Almaty
lon = 0 - (76 + Fraction(53,60) + Fraction(45,60)) # longitude of Almaty
cycle19 = 254 * sid_month # 254 sidereal months is almost exactly 19 solar years

def llsc(jday):
    return local_lunar_stellar_conjunction(Fraction(jday), PLEIADES, tz)

def darkmoon(jday):
    return newmoon(jday, tz)

def dayof(jday):
    return dayof_arab(Fraction(jday), lon, lat, tz)

def firstmoon(jday):
    '''Compute the first month of the year'''
    jday = Fraction(jday)

    conj = llsc(jday)

    if (phase(llsc(conj), tz) < phase(llsc(conj + sid_month), tz)):
        # this is the first month of the year
        a = False
    else:
        # this is not the first month of the year
        a = True

    while (a):
        if (phase(llsc(conj - sid_month), tz) < phase(llsc(conj), tz)):
            # previous month is the first
            a = False
        conj -= sid_month

    return llsc(conj)

def fromjd(jday):
    '''Convert a Julian Day to a date in the Kazakh nomad lunar calendar'''
    jday = Fraction(jday)

    # compute the start of the month
    conj = llsc(jday) # the moon in conjunction with the Pleiades
    while (dayof(llsc(conj)) > jday):
        conj -= sid_month
    while (dayof(llsc(conj + sid_month)) <= jday):
        conj += sid_month

    # compute the number of the month
    crescent = darkmoon(conj)
    while (dayof(darkmoon(crescent)) > dayof(llsc(conj))):
        crescent -= syn_month
    togys = dayof(llsc(conj)) - dayof(darkmoon(crescent)) + 1 # add 1 because humans don't count from 0

    # compute the number of the year
    ny = llsc(firstmoon(conj))
    cycles = (conj - epoch) // cycle19
    year = 19 * cycles
    ny0 = llsc(epoch + (cycles * cycle19))
    while (dayof(llsc(ny0)) > dayof(ny)):
        ny0 -= cycle19
        year -= 19
    while (dayof(llsc(ny0 + cycle19)) <= dayof(ny)):
        ny0 += cycle19
        year += 19
    while (dayof(llsc(ny0)) < dayof(ny)):
        ny0 += (12 * sid_month)
        while (phase((ny0 + sid_month), tz) < phase(ny0, tz)):
            ny0 += sid_month
        year += 1

    day = jday - dayof(llsc(conj)) + 1 # add 1 because humans don't count from 0

    return (day, togys, int(year))
        
def tojd(day, togys, year):
    '''Convert a date in the Kazakh nomad calendar to a Julian Day'''
    day = int(day) - 1 # subtract 1 because computers count from 0
    togys = int(togys) - 1 # subtract 1 because computers count from 0
    year = int(year)

    # account for the year
    cycles = year // 19
    y = 19 * cycles
    jday = llsc(epoch + (cycles * cycle19))
    while (y < year):
        jday += (12 * sid_month)
        while (phase((jday + sid_month), tz) < phase(jday, tz)):
            jday += sid_month
        y += 1

    # account for the togys
    crescent = newmoon(llsc(jday), tz)
    if (togys > dayof(llsc(jday)) - dayof(crescent)):
        jday += sid_month
        while ((dayof(llsc(jday)) - dayof(newmoon(crescent, tz))) > togys):
            jday += sid_month
            crescent += syn_month

    # account for the day
    jday = dayof(llsc(jday)) + day

    return jday
