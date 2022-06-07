#!/usr/bin/python

# Convert between the Old Hindu lunisolar calendar and Julian Day

from math import floor, ceil
from fractions import Fraction
from months import NUM_HINDU as NUMON
from months import HINDU_NUM as MONTHNO

solar_epoch = 1749623 + Fraction(343, 576)
sid_year = 365 + Fraction(149,576) # mean sidereal year
rasi = sid_year * Fraction(1,12) # solar month
syn_month = Fraction(1577917500, 53433336)# synodic month
tithi = Fraction(syn_month, 30)
lunar_epoch = 1749608 + Fraction(6471437, 8905556)

def start(inst):
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
    # it's easier to assume the user wants the month entered, regardless of whether it's leap or not.
    # hence, return the leap month if it's leap, otherwise return the corresponding normal month.

    if month[:5] == "Adhik":
        adhik = True
        month = month[6:]
    else:
        adhik = False

    mesha = solar_epoch + (year * sid_year) # solar new year
    zod = mesha - rasi # the start of the rasi prior to solar new year
    luns = (zod - lunar_epoch) // syn_month # lunations between lunar_epoch and rasi
    jday = lunar_epoch +(luns * syn_month) # Samvatsaradi
    while start(jday) > start(zod):
        jday -= syn_month
    while start(jday + syn_month) <= start(zod):
        jday += syn_month

    # OK, so we now have jday equal to 1 Chaitra, which starts before or instantaneously with
    # what is actually the last rasi of the previous solar year

    m = 11 # month number, starting at 11 because Chaitra
    
    while NUMON[m] != month:
        m = (m + 1) % 12
        jday += syn_month
        if jday <= zod:
            # leap month
            leap = True
        else:
            leap = False
            zod += rasi

    # OK, we're now at the desired month, but we need to be sure we're giving
    # the leap or normal month, as appropriate

    if (adhik == False) and (leap == True):
        jday += syn_month

    # right, now we should be at the right crescent moon.
    # just have to cover the days.

    jday += ((day - 1) * tithi)
    jday = start(jday)# - 1

    return jday

def fromjd(jday):
    '''Convert a Julian Day to a date in the Old Hindu lunisolar calendar'''
    jday = int(jday)

    year = (jday - solar_epoch) // sid_year
    zod = solar_epoch + (year * sid_year) - rasi # rasi prior to solar new year
    if start(zod + sid_year) <= jday:
        year += 1
        zod += sid_year
        
    luns = (zod - lunar_epoch) // syn_month # lunations from lunar_epoch to Samvatsaradi
    saradi = lunar_epoch + (luns * syn_month) # Samvatsaradi
    while (saradi + syn_month) <= zod:
        saradi += syn_month
    while saradi > zod:
        saradi -= syn_month

    m = 11 # number of the month, starting at 11 because Chaitra
    adhik = False # track the leap month
    #leapt = False # have we passed the leap month?
    crescent = saradi
    sign = zod # track which rasi we're in

    while start(crescent + syn_month) <= jday:
        crescent += syn_month
        if start(crescent) < start(sign):
            # this is the leap month
            m += 1
            adhik = True
        elif adhik == True:
            adhik = False
            #leapt = True
            sign += rasi
        else:
            m += 1
            sign += rasi

        # account for the rare possibility of a month being skipped
        while start(sign) < start(crescent):
            m += 1
            sign += rasi

    month = NUMON[m % 12]
    if adhik == True:
        month = "Adhik " + month

    # crescent is now the start of the month in which jday falls
    # I just need to get the day, which is technically the tithi

    #day = 0 # technically the tithi; for now, it's easier to count from 0
    day = (jday - crescent) // tithi
    while start(crescent + (day * tithi)) <= jday:
        day += 1
    while start(crescent + (day * tithi)) > jday:
        day -= 1
    day += 1 # days are 1-indexed

    return (day, month, year)
