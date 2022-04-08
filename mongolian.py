#!/usr/bin/python3

# Convert between the Mongolian traditional lunisolar calendar and Julian Day.

from fractions import Fraction
from math import ceil, floor
from solun import conj, trans

MONTHS = ("Negdugeer sar", "Khoyordugaar sar", "Guravdugaar sar", "Dörövdugeer sar", "Tarvdugaar sar", "Zurgadugaar sar", "Doldugaar sar", "Naĭmdugaar sar", "Yesdugeer sar", "Aravdugaar sar", "Arvannegdugeer sar", "Arvanchaërdugaar sar")

# Global variables

solar_year = 365 + Fraction(5,24) + Fraction(49,1440) + Fraction(328,864000) # time between two southern solstices; differs by about a minute from the time between northward equinoxes due to orbital mechanics
lunar_month = 29 + Fraction(12,24) + Fraction(44,1440) + Fraction(28,864000) # length of 1 lunation
solar_term = solar_year / 12

year12 = 12 * lunar_month
year13 = 13 * lunar_month

solar_epoch = 2161532 + Fraction(1247, 1440) # southern solstice preceding Temujin's ascension to Genghis Khan
lunar_epoch = 2161530 + Fraction(893, 1440) # first visible crescent preceding solar_epoch
timezone = Fraction(8, 24) # Mongolian standard time is UTC+8

def truesun(day, angle):
    day = Fraction(day)
    return floor(trans(day, angle, timezone))

def truemoon(day):
    day = Fraction(day)
    return ceil(conj(day, timezone))

def fromjd(jday):
    '''Convert a Julian Day into a date in the Chinese lunisolar calendar.'''
    jday = int(jday)

    if jday >= floor(solar_epoch):
        # positive dates... probably
        orbits = (jday - solar_epoch) // solar_year
        solstice = solar_epoch + (solar_year * orbits)
        year = orbits + 1
        while truesun((solstice + solar_year), 270) <= jday:
            solstice += solar_year
            year += 1
        while truesun(solstice, 270) > jday:
            solstice -= solar_year

        lunations = (solstice - lunar_epoch) // lunar_month
        sar = lunar_epoch + (lunations * lunar_month)

            
    else:
        # negative dates
        year = (solar_epoch - jday) // solar_year
        solstice = solar_epoch - (year * solar_year)
        while truesun(solstice, 270) > jday:
            year += 1
            solstice -= solar_year
        while truesun((solstice + solar_year), 270) <= jday:
            year -= 1
            solstice += solar_year
        year = 0 - year

        lunations = (lunar_epoch - solstice) // lunar_month
        sar = lunar_epoch - (lunations * lunar_month)

    dongzhi = truesun(solstice, 270)
    while truemoon(sar + lunar_month) <= dongzhi:
        sar += lunar_month
    while truemoon(sar) > dongzhi:
        sar -= lunar_month

    prev_solstice = solstice - solar_year
    next_solstice = solstice + solar_year

    prev_dongzhi = truesun(prev_solstice, 270)
    next_dongzhi = truesun(next_solstice, 270)

    prev_sar = sar
    next_sar = sar

    while truemoon(prev_sar) > prev_dongzhi:
        prev_sar -= lunar_month

    while truemoon(next_sar + lunar_month) <= next_dongzhi:
        next_sar += lunar_month

    # now to check for leap years
    # I know this doesn't look right, but it consistently gives the correct date.
    # So screw it, it's what I'm going with even if it doesn't make sense.
    leap = None
    prev_leap = None
    next_leap = None

    if sar - prev_sar == year13:
        if (truemoon(prev_sar + (2 * lunar_month)) <= truesun((solstice + solar_term), 300)) or (truemoon(prev_sar + (3 * lunar_month)) <= truesun(solstice + (2 * solar_term), 330)):
            prev_leap = True
            leap = False
            tsagaan = prev_sar + (15 * lunar_month)
        else:
            prev_leap = False
            leap = True
            tsagaan = prev_sar + (14 * lunar_month)
    else:
        prev_leap = False
        tsagaan = prev_sar + (14 * lunar_month)

    
    if next_sar - sar == year13:
        if (truemoon(sar + (2 * lunar_month)) <= truesun((next_solstice + solar_term), 300)) or (truemoon(sar + (3 * lunar_month)) <= truesun((next_solstice + (2 * solar_term)), 330)):
            leap = True
            next_leap = False
            next_tsagaan = sar + (15 * lunar_month)
        else:
            leap = False
            next_leap = True
            next_tsagaan = sar + (14 * lunar_month)
    else:
        next_tsagaan = sar + (14 * lunar_month)

    if leap != True:
        leap = False

    # But what if tsagaan comes after jday?
    if truemoon(tsagaan) > jday:
        year -= 1
        if year == 0:
            year = (-1)
            
        next_solstice = solstice
        next_dongzhi = dongzhi
        next_sar = sar
        next_tsagaan = tsagaan
        next_leap = leap

        solstice = prev_solstice
        dongzhi = prev_dongzhi
        sar = prev_sar
        leap = prev_leap

        if leap == True:
            tsagaan = next_tsagaan - year13
        else:
            tsagaan = next_tsagaan - year12

    crescent = tsagaan
    m = 0

    if leap == False:
        # normal year
        while truemoon(crescent + lunar_month) <= jday:
            crescent += lunar_month
            m += 1

        month = MONTHS[m]
        day = jday - truemoon(crescent) + 1
    else:
        # leap year
        leapt = False # have we passed the leap month?
        angle = 330
        zhongqi = solstice + (2 * solar_term)
        # get the first major solar term which doesn't precede the new moon
        while truesun(zhongqi, angle) < truemoon(tsagaan):
            zhongqi += solar_term
            angle = (angle + 30) % 360

        while truemoon(crescent + lunar_month) <= jday:
            if leapt == True:
                # We're past the leap month so we don't need to worry about zhongqi any more
                m += 1
                crescent += lunar_month
            elif truemoon(crescent + lunar_month) <= truesun(zhongqi, angle):
                # this is the leap month
                crescent += lunar_month
                leapt = True
            else:
                crescent += lunar_month
                while truesun(zhongqi, angle) < truemoon(crescent):
                    zhongqi += solar_term
                    angle = (angle + 30) % 360
                m += 1

        if (leapt == False) and (truemoon(crescent + lunar_month) <= truesun(zhongqi, angle)):
            month = "Shün " + MONTHS[m - 1]
        else:
            month = MONTHS[m]

        day = jday - truemoon(crescent) + 1

    return (day, month, year)

def tojd(day, month, year):
    day = int(day)
    month = str(month)
    year = int(year)

    if year == 0:
        year = (-1)

    if year > 0:
        solstice = solar_epoch + ((year - 1) * solar_year)
        lunations = (solstice - solar_epoch) // lunar_month
    else:
        solstice = solar_epoch + (year * solar_year)
        lunations = (solar_epoch - solstice) // lunar_month

    sar = lunar_epoch + (lunations * lunar_month)
    dongzhi = truesun(solstice, 270)
    while truemoon(sar) > dongzhi:
        sar -= lunar_month
    while truemoon(sar + lunar_month) <= dongzhi:
        sar += lunar_month

    next_solstice = solstice + solar_year
    next_dongzhi = truesun(next_solstice, 270)
    
    prev_solstice = solstice - solar_year
    prev_dongzhi = truesun(prev_solstice, 270)

    next_sar = sar + year12
    while truemoon(next_sar + lunar_month) <= next_dongzhi:
        next_sar += lunar_month

    prev_sar = sar - year13
    while truemoon(prev_sar + lunar_month) <= prev_dongzhi:
        prev_sar += lunar_month

    # now to check for leap years
    # as in fromjd(), this looks like it shouldn't work, but it does
    leap = None
    prev_leap = None
    next_leap = None

    if sar - prev_sar == year13:
        if (truemoon(prev_sar + (2 * lunar_month)) <= truesun((solstice + solar_term), 300)) or (truemoon(prev_sar + (3 * lunar_month)) <= truesun((solstice + (2 * solar_term)), 330)):
            prev_leap = True
            leap = False
            tsagaan = prev_sar + (15 * lunar_month)
        else:
            prev_leap = False
            leap = True
            tsagaan = prev_sar + (14 * lunar_month)
    else:
        prev_leap = False
        tsagaan = prev_sar + (14 * lunar_month)
        
    if next_sar - sar == year13:
        if (truemoon(sar + (2 * lunar_month)) <= truesun((next_solstice + solar_term), 300)) or (truemoon(sar + (3 * lunar_month)) <= truesun((next_solstice + (2 * solar_term)), 330)):
            leap = True
            next_leap = False
            next_tsagaan = sar + (15 * lunar_month)
        else:
            leap = False
            next_leap = True
            next_tsagaan = sar + (14 * lunar_month)
    else:
        next_tsagaan = sar + (14 * lunar_month)

    if leap != True:
        leap = False

    crescent = tsagaan
    m = 0
    #print(leap)
    
    if leap == False:
        # normal year
        if month[0:3] == "Shün":
            month = month[4:] # cut off the "Shün " part.

        while MONTHS[m] != month:
            m += 1
            crescent += lunar_month

        jday = truemoon(crescent) + day - 1
    else:
        # leap year
        if month[0:3] == "Shün":
            run = True # assuming that if the user enters a leap month, they want the actual leap month
        else:
            run = False

        zhongqi = solstice + (2 * solar_term)
        angle = 330

        while truesun(zhongqi, angle) < truemoon(crescent):
            zhongqi += solar_term
            angle = (angle + 30) % 360

        while MONTHS[m] != month:
            if (truemoon(crescent + lunar_month) <= truesun(zhongqi, angle)) and (run == True):
                # we're in the leap month, which is the month selected
                break
            elif (truemoon(crescent + lunar_month) <= truesun(zhongqi, angle)):
                crescent += lunar_month
            else:
                crescent += lunar_month
                while truesun(zhongqi, angle) < truemoon(crescent):
                    zhongqi += solar_term
                    angle = (angle + 30) % 360
                m += 1

        jday = truemoon(crescent) + day - 1

    return jday
                
