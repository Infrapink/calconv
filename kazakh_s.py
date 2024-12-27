#!/usr/bin/python3

# convert between the traditional Kazakh nomad calendar and Julian Days
# The Kazakh nomad calendar is unique in that its months are sidereal; the year begins when the new month coïncides with the new moon
# 254 sidereal months is very close to 19 years, a fact which I use in computing the year number
# In this version, days start at sunset

from fractions import Fraction
from solun import sid_month, syn_month, phase, local_lunar_stellar_conjunction, newmoon, dayof_arab
from stars import PLEIADES

epoch = 1948379 # first conjunction of the moon with the Pleiades at new moon in the year of Muhammad's flight from Mecca
tz = Fraction(5, 24) # Kazakhstan is 5 hours ahead of UTC.
lat = 51 + Fraction(10, 60) # latitude of Almaty
lon = 0 - (76 + Fraction(53,60) + Fraction(45,60)) # longitude of Almaty
cycle19 = 254 * sid_month # 19 years

def llsc(jday):
    return local_lunar_stellar_conjunction(Fraction(jday), PLEIADES, tz)

def dayof(jday):
    return dayof_arab(Fraction(jday), lon, lat, tz)

def firstmoon(jday):
    '''Given the first day of the sidereal month, find the beginning of the year'''
    jday = Fraction(jday)
    
    #if (phase(llsc(jday - sid_month), tz) < phase(llsc(jday), tz)):
        # this is the first month of the year
        #a = False
    #else:
        #a = True
    #while (a):
    a = True
    while (a):
        if ( (phase(llsc(jday), tz) > 270) and (phase(llsc(jday - sid_month), tz) < 90) ):
            a = False
        else:
            #print(phase(llsc(jday), tz))
            jday -= sid_month

    return jday

def fromjd(jday):
    '''Convert a Julian Day into a date in the Kazakh nomad calendar'''
    jday = Fraction(jday)

    # first, compute the month
    conj = llsc(jday) # conjunction of the moon with the Pleiades; beginning of the month
    while (dayof(llsc(conj)) > jday):
        conj -= sid_month

    # day of the month
    day = jday - dayof(conj) + 1 # add 1 because humans don't count from 0

    # number of the month
    darkmoon = newmoon(conj, tz)
    while (dayof(newmoon(darkmoon, tz)) > dayof(conj)):
        darkmoon -= syn_month
    while (dayof(newmoon((darkmoon + syn_month), tz)) <= dayof(conj)):
        darkmoon += syn_month
    togys = dayof(conj) - dayof(darkmoon)

    # start of the year
    nyd = dayof(firstmoon(llsc(conj)))

    # compute the year number
    cycles = (conj - epoch) // cycle19
    year = int(19 * cycles)
    crescent = firstmoon(llsc(epoch + (cycles * cycle19)))
    while (dayof(firstmoon(llsc(crescent + cycle19))) <= nyd):
        year += 19
        crescent += cycle19
    while (dayof(firstmoon(llsc(crescent))) > nyd):
        year -= 19
        crescent -= cycle19
    # we are now at the star of a 19-year cycle

    while (dayof(llsc(crescent)) < nyd):
        crescent += (12 * sid_month)
        while (phase(llsc(crescent + sid_month), tz) > phase(llsc(crescent), tz)):
            crescent += sid_month
        year += 1

    if (year >= 0):
        year += 1 # add 1 because humans don't count from 0

    return (day, togys, year)

def tojd(day, togys, year):
    '''Convert a Kazakh date into a Julian Day'''
    day = int(day) - 1 # subtract 1 because humans count from 0
    togys = int(togys)
    year = int(year)
    if (year > 0):
        year -= 1 # subtract 1 because computers count from 0

    # account for the year, and get up to the new moon which begins the year
    cycles = year // 19
    y = cycles * 19
    crescent = firstmoon(llsc(epoch + (cycles * cycle19)))
    while (y < year):
        crescent += (12 * sid_month)
        while (phase(llsc(crescent + sid_month), tz) > phase(llsc(crescent), tz)):
            crescent += sid_month
        y += 1

    # crescent is now the new moon which begins the year
    # now account for the month
    
    if (togys > 1):
        jday = llsc(crescent + sid_month)
        while (dayof(llsc(jday)) - dayof(newmoon(crescent, tz)) > togys):
            jday += sid_month
            crescent += syn_month

    jday = dayof(jday) + day

    return jday
