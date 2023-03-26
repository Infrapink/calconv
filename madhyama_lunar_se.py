#!/usr/bin/python

# Convert between the Old Hindu lunisolar calendar and Julian Day

from math import floor, ceil
from fractions import Fraction
from months import NUM_HINDU as NUMON
from months import HINDU_NUM as MONTHNO

solar_epoch = 1749623 + Fraction(343, 576) # in Julian Days
sid_year = 365 + Fraction(149,576) # mean sidereal year
rasi = sid_year * Fraction(1,12) # solar month
syn_month = Fraction(1577917500, 53433336)# synodic month
tithi = Fraction(syn_month, 30)
lunar_epoch = 1749608 + Fraction(6471437, 8905556)

def suncheck(inst):
    '''Get the official start date of a rasi, month, or tithi'''
    inst = Fraction(inst)
    if inst % 1 <= Fraction(6,24):
        return floor(inst)
    else:
        return ceil(inst)

def tojd(day, month, year):
    '''Convert a date in the Old Hindu lunisolar calendar to a Julian Day'''
    day = int(day) # technically this is a tithi
    month = str(month)
    year = int(year)

    # check for leap months
    if month[:5] == "Adhik":
        adhik = True
        month = month[6:]
    else:
        adhik = False
        
    mina = solar_epoch + (year * sid_year) - rasi # instant the sun enters Mīna/Pisces
    sankranti = mina + (rasi * ((MONTHNO[month] + 1) % 12)) # instant the sun enters the specified sign
    luns = (sankranti - lunar_epoch) // syn_month
    jday = lunar_epoch + (luns * syn_month)
    while (suncheck(jday) < suncheck(sankranti)):
        jday += syn_month
    while (suncheck(jday - syn_month) >= suncheck(sankranti)):
        jday -= syn_month

    if ((adhik == True) and (suncheck(jday + syn_month) < suncheck(sankranti + rasi))):
        jday += syn_month

    jday = suncheck(jday + ((day - 1) * tithi))
    return jday

def fromjd(jday):
    '''Convert a Julian Day to a date in the Old Hindu lunisolar calendar'''
    jday = int(jday)

    year = (jday - solar_epoch) // sid_year
    mesha = solar_epoch + (year * sid_year) # time the sun enters Meṡa/Aries
    mina = mesha - rasi # time the sun enters Mīna/Pisces
    while (suncheck(mina) > jday):
        mina -= 1
        year -= 1
    while (suncheck(mina + sid_year) <= jday):
        year += 1
        mina += sid_year

    luns = (mina - lunar_epoch) // syn_month
    firstmoon = lunar_epoch + (luns * syn_month)
    while(suncheck(firstmoon) < suncheck(mina)):
        firstmoon += syn_month

    while (suncheck(firstmoon) > jday):
        year -= 1
        mina -= sid_year
        firstmoon -= (12 * syn_month)
        while (suncheck(firstmoon - syn_month) >= suncheck(mina)):
            firstmoon -= syn_month

    chigra = (jday - mina) // rasi # which sign is jday in?
    sankranti = mina + (chigra * rasi) # instant the sun enters the sign
    while (suncheck(sankranti) > jday):
        chigra -= 1
        sankranti -= rasi
    while (suncheck(sankranti + rasi) <= jday):
        chigra += 1
        sankranti += rasi
    newmoon = firstmoon + (chigra * syn_month)
    while(suncheck(newmoon) < suncheck(sankranti)):
        newmoon += syn_month
    if (suncheck(newmoon) > jday):
        chigra -= 1
        sankranti -= rasi
        newmoon -= syn_month

    month = NUMON[(chigra - 1) % 12]
    if (suncheck(newmoon + syn_month) < suncheck(sankranti + chigra)):
        month = "Adhik " + month

    day =(jday - newmoon) // tithi
    while (suncheck(newmoon + (day * tithi)) > jday):
        day -= 1
    while (suncheck(newmoon + ((day + 1) * tithi)) <= jday):
        day += 1

    day += 1 # days are 1-indexed
    return(day, month, year)
