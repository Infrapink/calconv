#!/usr/bin/python3

# Convert between the Korean lunisolar calendar and Julian Day.

from fractions import Fraction
from math import floor
from solun import conj, trans

MONTHS = ("Il-wol", "I-wol", "Sam-wol", "Sa-wol", "O-wol", "Yu-wol", "Chil-wol", "Pal-wol", "Gu-wol", "Si-wol", "Sibil-wol", "Sibi-wol")

# Global variables

solar_year = 365 + Fraction(5,24) + Fraction(49,1440) + Fraction(328,864000) # time between two southern solstices; differs by about a minute from the time between northward equinoxes due to orbital mechanics
lunar_month = 29 + Fraction(12,24) + Fraction(44,1440) + Fraction(28,864000) # length of 1 lunation
solar_term = solar_year / 12

nyeon2 = 12 * lunar_month
nyeon3 = 13 * lunar_month

solar_epoch = 869303 + Fraction(95,144)
lunar_epoch = 869302 + Fraction(122,480)
timezone = Fraction(9, 24) # Korean standard time is UTC+9

def truesun(day, angle):
    day = Fraction(day)
    return floor(trans(day, angle, timezone))

def truemoon(day):
    day = Fraction(day)
    return floor(conj(day, timezone))

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
        dal = lunar_epoch + (lunations * lunar_month)

            
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
        dal = lunar_epoch - (lunations * lunar_month)

    dongji = truesun(solstice, 270)
    while truemoon(dal + lunar_month) <= dongji:
        dal += lunar_month
    while truemoon(dal) > dongji:
        dal -= lunar_month

    prev_solstice = solstice - solar_year
    next_solstice = solstice + solar_year

    prev_dongji = truesun(prev_solstice, 270)
    next_dongji = truesun(next_solstice, 270)

    prev_dal = dal
    next_dal = dal

    while truemoon(prev_dal) > prev_dongji:
        prev_dal -= lunar_month

    while truemoon(next_dal + lunar_month) <= next_dongji:
        next_dal += lunar_month

    # now to check for leap years
    # I know this doesn't look right, but it consistently gives the correct date.
    # So screw it, it's what I'm going with even if it doesn't make sense.
    leap = None
    prev_leap = None
    next_leap = None

    if dal - prev_dal == nyeon3:
        # 13 lunations between the new moon on or before the solstice moon preceding last year's seollal nyeon, and the solstice moon preceding this year's seollal nyeon
        # It's a leap sui, but is it a leap nyeon?
        # The extra month probably belongs to this year, but it might possibly belong to last year

        # prev_dal is the new moon of the 11th month of two years ago
        if (truemoon(prev_dal + (2 * lunar_month)) <= truesun((solstice + solar_term), 300)) or (truemoon(prev_dal + (3 * lunar_month)) <= truesun(solstice + (2 * solar_term), 330)):
        #if (truemoon(prev_dal + (2 * lunar_month)) <= truesun((prev_solstice + solar_term), 300)) or (truemoon(prev_dal + (3 * lunar_month)) <= truesun(prev_solstice + (2 * solar_term), 330)):        
            # The first condition checks if there is a full lunation between Dongzhi and Dahan
            # The second condition checks if there is a full lunation between Dahan and Yushui
            # In either case, this is a leap sui, in which the leap month belongs to the previous nyeon, which is a leap nyeon
            prev_leap = True
            leap = False
            seollal = prev_dal + (15 * lunar_month)
        else:
            prev_leap = False
            leap = True
            seollal = prev_dal + (14 * lunar_month)
    else:
        # 12 lunations between the new moon on or before last year's solstice, and the new moon on or before this year's solstice.
        # Normal sui, probably a normal nyeon
        prev_leap = False
        seollal = prev_dal + (14 * lunar_month)

    
    if next_dal - dal == nyeon3:
        # 13 lunations between the solstice moon preceding this seollal nyeon, and the solstice moon preceding next seollal nyeon
        # It's a leap sui, but is it a leap nyeon?
        # The extra month probablt belongs to next year, but it might be part of this year

        # dal is the new moon of the 11th month of last year
        if (truemoon(dal + (2 * lunar_month)) <= truesun((next_solstice + solar_term), 300)) or (truemoon(dal + (3 * lunar_month)) <= truesun((next_solstice + (2 * solar_term)), 330)):
            # The first condition checks if there is a full lunation between Dongzhi and Dahan
            # The second condition checks if there is a full lunation between Dahan and Yushui
            # In either case, this is a leap sui, in which the leap month belongs to the previous nyeon, which is a leap nean
            leap = True
            next_leap = False
            next_seollal = dal + (15 * lunar_month)
        else:
            leap = False
            next_leap = True
            next_seollal = dal + (14 * lunar_month)
    else:
        # 12 lunations between the solstice moon preceding this year's seollal nyeon, and the solstice moon preceding the next sin nyeon
        # Normal sui, apparently a normal nyeon
        #leap = False
        next_seollal = dal + (14 * lunar_month)

    if leap != True:
        leap = False

    # OK
    # If my calculations are correct, this will give us the ACTUAL, PROPER, CORRECT date of seollal nyeon
    # seollal is the time of the first new moon of the Chinese year, though the time of the new moon is in UTC.

    # But what if seollal comes after jday?
    if truemoon(seollal) > jday:
        year -= 1
        if year == 0:
            year = (-1)
            
        next_solstice = solstice
        next_dongji = dongji
        next_dal = dal
        next_seollal = seollal
        next_leap = leap

        solstice = prev_solstice
        dongji = prev_dongji
        dal = prev_dal
        leap = prev_leap

        if leap == True:
            seollal = next_seollal - nyeon3
        else:
            seollal = next_seollal - nyeon2

    newmoon = seollal
    m = 0

    if leap == False:
        # normal year
        while truemoon(newmoon + lunar_month) <= jday:
            newmoon += lunar_month
            m += 1

        month = MONTHS[m]
        day = jday - truemoon(newmoon) + 1
    else:
        # leap year
        leapt = False # have we passed the leap month?
        angle = 330
        zhongqi = solstice + (2 * solar_term)
        # get the first major solar term which doesn't precede the new moon
        while truesun(zhongqi, angle) < truemoon(seollal):
            zhongqi += solar_term
            angle = (angle + 30) % 360

        while truemoon(newmoon + lunar_month) <= jday:
            if leapt == True:
                # We're past the leap month so we don't need to worry about zhongqi any more
                m += 1
                newmoon += lunar_month
            elif truemoon(newmoon + lunar_month) <= truesun(zhongqi, angle):
                # this is the leap month
                newmoon += lunar_month
                leapt = True
            else:
                newmoon += lunar_month
                while truesun(zhongqi, angle) < truemoon(newmoon):
                    zhongqi += solar_term
                    angle = (angle + 30) % 360
                m += 1

        if (leapt == False) and (truemoon(newmoon + lunar_month) <= truesun(zhongqi, angle)):
            month = "Yun " + MONTHS[m - 1]
        else:
            month = MONTHS[m]

        day = jday - truemoon(newmoon) + 1

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

    dal = lunar_epoch + (lunations * lunar_month)
    dongji = truesun(solstice, 270)
    while truemoon(dal) > dongji:
        dal -= lunar_month
    while truemoon(dal + lunar_month) <= dongji:
        dal += lunar_month

    next_solstice = solstice + solar_year
    next_dongji = truesun(next_solstice, 270)
    
    prev_solstice = solstice - solar_year
    prev_dongji = truesun(prev_solstice, 270)

    next_dal = dal + nyeon2
    while truemoon(next_dal + lunar_month) <= next_dongji:
        next_dal += lunar_month

    prev_dal = dal - nyeon3
    while truemoon(prev_dal + lunar_month) <= prev_dongji:
        prev_dal += lunar_month

    # now to check for leap years
    # as in fromjd(), this looks like it shouldn't work, but it does
    leap = None
    prev_leap = None
    next_leap = None

    if dal - prev_dal == nyeon3:
        if (truemoon(prev_dal + (2 * lunar_month)) <= truesun((solstice + solar_term), 300)) or (truemoon(prev_dal + (3 * lunar_month)) <= truesun((solstice + (2 * solar_term)), 330)):
            prev_leap = True
            leap = False
            seollal = prev_dal + (15 * lunar_month)
        else:
            prev_leap = False
            leap = True
            seollal = prev_dal + (14 * lunar_month)
    else:
        prev_leap = False
        seollal = prev_dal + (14 * lunar_month)
        
    if next_dal - dal == nyeon3:
        if (truemoon(dal + (2 * lunar_month)) <= truesun((next_solstice + solar_term), 300)) or (truemoon(dal + (3 * lunar_month)) <= truesun((next_solstice + (2 * solar_term)), 330)):
            leap = True
            next_leap = False
            next_seollal = dal + (15 * lunar_month)
        else:
            leap = False
            next_leap = True
            next_seollal = dal + (14 * lunar_month)
    else:
        next_seollal = dal + (14 * lunar_month)

    if leap != True:
        leap = False

    newmoon = seollal
    m = 0
    #print(leap)
    
    if leap == False:
        # normal year
        if month[0:3] == "Yun":
            month = month[4:]

        while MONTHS[m] != month:
            m += 1
            newmoon += lunar_month

        jday = truemoon(newmoon) + day - 1
    else:
        # leap year
        if month[0:3] == "Yun":
            yun = True # assuming that if the user enters a leap month, they want the actual leap month
        else:
            yun = False

        zhongqi = solstice + (2 * solar_term)
        angle = 330

        while truesun(zhongqi, angle) < truemoon(newmoon):
            zhongqi += solar_term
            angle = (angle + 30) % 360

        while MONTHS[m] != month:
            if (truemoon(newmoon + lunar_month) <= truesun(zhongqi, angle)) and (yun == True):
                # we're in the leap month, which is the month selected
                break
            elif (truemoon(newmoon + lunar_month) <= truesun(zhongqi, angle)):
                newmoon += lunar_month
            else:
                newmoon += lunar_month
                while truesun(zhongqi, angle) < truemoon(newmoon):
                    zhongqi += solar_term
                    angle = (angle + 30) % 360
                m += 1

        jday = truemoon(newmoon) + day - 1

    return jday
                
