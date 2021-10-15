#!/usr/bin/python3

# Convert between the Chinese lunisolar calendar and Julian Day.

# I tested my algorithm against two websites with records of Chinese New Year over a century from 1930 to 2030:
## http://www.chinesenewyears.info/chinese-new-year-calendar.php
## https://chinese-year.com/
# The first one disagrees with me by 1 day in 1930, 1943, and 1946; the other agrees with me completely.
# Someone, somewhere, has made an error, and I have no choice but to assume it's the first site.

from fractions import Fraction
from math import floor
from solun import conj, trans

MONTHS = ("Zhēngyuè", "Èryuè", "Sānyuè", "Sìyuè", "Wǔyuè", "Liùyuè", "Qīyuè", "Bāyuè", "Jiǔyuè", "Shíyuè", "Shíyīyuè", "Làyuè")

# Global variables

solar_year = 365 + Fraction(5,24) + Fraction(49,1440) + Fraction(328,864000) # time between two southern solstices; differs by about a minute from the time between northward equinoxes due to orbital mechanics
lunar_month = 29 + Fraction(12,24) + Fraction(44,1440) + Fraction(28,864000) # length of 1 lunation
solar_term = solar_year / 12

year12 = 12 * lunar_month
year13 = 13 * lunar_month

solar_epoch = Fraction(708780574297, 432000) # instant of the southern solstice preceding the first year of the reign of Emperor Qin Shi Huang, gMT
lunar_epoch = Fraction(177192234937, 108000) # new moon immediately preceding solar_epoch, GMT
timezone = Fraction(8, 24) # Chinese standard time is UTC+8

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
        yue = lunar_epoch + (lunations * lunar_month)

            
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
        yue = lunar_epoch - (lunations * lunar_month)

    dongzhi = truesun(solstice, 270)
    while truemoon(yue + lunar_month) <= dongzhi:
        yue += lunar_month
    while truemoon(yue) > dongzhi:
        yue -= lunar_month

    prev_solstice = solstice - solar_year
    next_solstice = solstice + solar_year

    prev_dongzhi = truesun(prev_solstice, 270)
    next_dongzhi = truesun(next_solstice, 270)

    prev_yue = yue
    next_yue = yue

    while truemoon(prev_yue) > prev_dongzhi:
        prev_yue -= lunar_month

    while truemoon(next_yue + lunar_month) <= next_dongzhi:
        next_yue += lunar_month

    # now to check for leap years
    # I know this doesn't look right, but it consistently gives the correct date.
    # So screw it, it's what I'm going with even if it doesn't make sense.
    leap = None
    prev_leap = None
    next_leap = None

    if yue - prev_yue == year13:
        # 13 lunations between the new moon on or before the solstice moon preceding last year's xin nian, and the solstice moon preceding this year's xin nian
        # It's a leap sui, but is it a leap nian?
        # The extra month probably belongs to this year, but it might possibly belong to last year

        # prev_yue is the new moon of the 11th month of two years ago
        if (truemoon(prev_yue + (2 * lunar_month)) <= truesun((solstice + solar_term), 300)) or (truemoon(prev_yue + (3 * lunar_month)) <= truesun(solstice + (2 * solar_term), 330)):
        #if (truemoon(prev_yue + (2 * lunar_month)) <= truesun((prev_solstice + solar_term), 300)) or (truemoon(prev_yue + (3 * lunar_month)) <= truesun(prev_solstice + (2 * solar_term), 330)):        
            # The first condition checks if there is a full lunation between Dongzhi and Dahan
            # The second condition checks if there is a full lunation between Dahan and Yushui
            # In either case, this is a leap sui, in which the leap month belongs to the previous nian, which is a leap nian
            prev_leap = True
            leap = False
            xin = prev_yue + (15 * lunar_month)
        else:
            prev_leap = False
            leap = True
            xin = prev_yue + (14 * lunar_month)
    else:
        # 12 lunations between the new moon on or before last year's solstice, and the new moon on or before this year's solstice.
        # Normal sui, probably a normal nian
        prev_leap = False
        xin = prev_yue + (14 * lunar_month)

    
    if next_yue - yue == year13:
        # 13 lunations between the solstice moon preceding this xin nian, and the solstice moon preceding next xin nian
        # It's a leap sui, but is it a leap nian?
        # The extra month probablt belongs to next year, but it might be part of this year

        # yue is the new moon of the 11th month of last year
        if (truemoon(yue + (2 * lunar_month)) <= truesun((next_solstice + solar_term), 300)) or (truemoon(yue + (3 * lunar_month)) <= truesun((next_solstice + (2 * solar_term)), 330)):
            # The first condition checks if there is a full lunation between Dongzhi and Dahan
            # The second condition checks if there is a full lunation between Dahan and Yushui
            # In either case, this is a leap sui, in which the leap month belongs to the previous nian, which is a leap nean
            leap = True
            next_leap = False
            next_xin = yue + (15 * lunar_month)
        else:
            leap = False
            next_leap = True
            next_xin = yue + (14 * lunar_month)
    else:
        # 12 lunations between the solstice moon preceding this year's xin nian, and the solstice moon preceding the next sin nian
        # Normal sui, apparently a normal nian
        #leap = False
        next_xin = yue + (14 * lunar_month)

    if leap != True:
        leap = False

    # OK
    # If my calculations are correct, this will give us the ACTUAL, PROPER, CORRECT date of xin nian
    # xin is the time of the first new moon of the Chinese year, though the time of the new moon is in UTC.

    # But what if xin comes after jday?
    if truemoon(xin) > jday:
        year -= 1
        if year == 0:
            year = (-1)
            
        next_solstice = solstice
        next_dongzhi = dongzhi
        next_yue = yue
        next_xin = xin
        next_leap = leap

        solstice = prev_solstice
        dongzhi = prev_dongzhi
        yue = prev_yue
        leap = prev_leap

        if leap == True:
            xin = next_xin - year13
        else:
            xin = next_xin - year12

    newmoon = xin
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
        while truesun(zhongqi, angle) < truemoon(xin):
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
            month = "Rùn " + MONTHS[m - 1]
            if month == "Rùn Shíyīyuè":
                month = "Shíèryuè"
            elif month == "Rùn Làyuè":
                month = "Làyuè"
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

    yue = lunar_epoch + (lunations * lunar_month)
    dongzhi = truesun(solstice, 270)
    while truemoon(yue) > dongzhi:
        yue -= lunar_month
    while truemoon(yue + lunar_month) <= dongzhi:
        yue += lunar_month

    next_solstice = solstice + solar_year
    next_dongzhi = truesun(next_solstice, 270)
    
    prev_solstice = solstice - solar_year
    prev_dongzhi = truesun(prev_solstice, 270)

    next_yue = yue + year12
    while truemoon(next_yue + lunar_month) <= next_dongzhi:
        next_yue += lunar_month

    prev_yue = yue - year13
    while truemoon(prev_yue + lunar_month) <= prev_dongzhi:
        prev_yue += lunar_month

    # now to check for leap years
    # as in fromjd(), this looks like it shouldn't work, but it does
    leap = None
    prev_leap = None
    next_leap = None

    if yue - prev_yue == year13:
        if (truemoon(prev_yue + (2 * lunar_month)) <= truesun((solstice + solar_term), 300)) or (truemoon(prev_yue + (3 * lunar_month)) <= truesun((solstice + (2 * solar_term)), 330)):
            prev_leap = True
            leap = False
            xin = prev_yue + (15 * lunar_month)
        else:
            prev_leap = False
            leap = True
            xin = prev_yue + (14 * lunar_month)
    else:
        prev_leap = False
        xin = prev_yue + (14 * lunar_month)
        
    if next_yue - yue == year13:
        if (truemoon(yue + (2 * lunar_month)) <= truesun((next_solstice + solar_term), 300)) or (truemoon(yue + (3 * lunar_month)) <= truesun((next_solstice + (2 * solar_term)), 330)):
            leap = True
            next_leap = False
            next_xin = yue + (15 * lunar_month)
        else:
            leap = False
            next_leap = True
            next_xin = yue + (14 * lunar_month)
    else:
        next_xin = yue + (14 * lunar_month)

    if leap != True:
        leap = False

    newmoon = xin
    m = 0
    #print(leap)
    
    if leap == False:
        # normal year
        if month[0:3] == "Rùn":
            month = month[4:] # cut off the "Rùn " part.

        while MONTHS[m] != month:
            m += 1
            newmoon += lunar_month

        jday = truemoon(newmoon) + day - 1
    else:
        # leap year
        if month[0:3] == "Rùn":
            run = True # assuming that if the user enters a leap month, they want the actual leap month
        else:
            run = False

        zhongqi = solstice + (2 * solar_term)
        angle = 330

        while truesun(zhongqi, angle) < truemoon(newmoon):
            zhongqi += solar_term
            angle = (angle + 30) % 360

        while MONTHS[m] != month:
            if (truemoon(newmoon + lunar_month) <= truesun(zhongqi, angle)) and (run == True):
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
                
