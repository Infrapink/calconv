#!/usr/bin/python3

# Convert between the Vietnamese lunisolar calendar and Julian Day.

from fractions import Fraction
from math import floor
from solun import conj, trans

MONTHS = ("Tháng Giêng", "Tháng Hai", "Tháng Ba", "Tháng Tư", "Tháng Năm", "Tháng Sáu", "Tháng Bảy", "Tháng Tám", "Tháng Chín", "Tháng Mười", "Tháng Mười Một", "Tháng Chạp")

# Global variables

solar_year = 365 + Fraction(5,24) + Fraction(49,1440) + Fraction(328,864000) # time between two southern solstices; differs by about a minute from the time between northward equinoxes due to orbital mechanics
lunar_month = 29 + Fraction(12,24) + Fraction(44,1440) + Fraction(28,864000) # length of 1 lunation
solar_term = solar_year / 12

year12 = 12 * lunar_month
year13 = 13 * lunar_month

solar_epoch = 669881 + Fraction(110, 1440)
lunar_epoch = 669853 + Fraction(17, 60)
timezone = Fraction(7, 24) # Vietnamese standard time is UTC+7

def truesun(day, angle):
    day = Fraction(day)
    return floor(trans(day, angle, timezone))

def truemoon(day):
    day = Fraction(day)
    return floor(conj(day, timezone))

def fromjd(jday):
    '''Convert a Julian Day into a date in the Vietnamese lunisolar calendar.'''
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
        trang = lunar_epoch + (lunations * lunar_month)

            
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
        trang = lunar_epoch - (lunations * lunar_month)

    dongchi = truesun(solstice, 270)
    while truemoon(trang + lunar_month) <= dongchi:
        trang += lunar_month
    while truemoon(trang) > dongchi:
        trang -= lunar_month

    prev_solstice = solstice - solar_year
    next_solstice = solstice + solar_year

    prev_dongchi = truesun(prev_solstice, 270)
    next_dongchi = truesun(next_solstice, 270)

    prev_trang = trang
    next_trang = trang

    while truemoon(prev_trang) > prev_dongchi:
        prev_trang -= lunar_month

    while truemoon(next_trang + lunar_month) <= next_dongchi:
        next_trang += lunar_month

    # now to check for leap years
    # I know this doesn't look right, but it consistently gives the correct date.
    # So screw it, it's what I'm going with even if it doesn't make sense.
    leap = None
    prev_leap = None
    next_leap = None

    if trang - prev_trang == year13:
        # 13 lunations between the new moon on or before the solstice moon preceding last year's tet year, and the solstice moon preceding this year's tet year
        # It's a leap sui, but is it a leap year?
        # The extra month probably belongs to this year, but it might possibly belong to last year

        # prev_trang is the new moon of the 11th month of two years ago
        if (truemoon(prev_trang + (2 * lunar_month)) <= truesun((solstice + solar_term), 300)) or (truemoon(prev_trang + (3 * lunar_month)) <= truesun(solstice + (2 * solar_term), 330)):
        #if (truemoon(prev_trang + (2 * lunar_month)) <= truesun((prev_solstice + solar_term), 300)) or (truemoon(prev_trang + (3 * lunar_month)) <= truesun(prev_solstice + (2 * solar_term), 330)):        
            # The first condition checks if there is a full lunation between Dongzhi and Dahan
            # The second condition checks if there is a full lunation between Dahan and Yushui
            # In either case, this is a leap sui, in which the leap month belongs to the previous year, which is a leap year
            prev_leap = True
            leap = False
            tet = prev_trang + (15 * lunar_month)
        else:
            prev_leap = False
            leap = True
            tet = prev_trang + (14 * lunar_month)
    else:
        # 12 lunations between the new moon on or before last year's solstice, and the new moon on or before this year's solstice.
        # Normal sui, probably a normal year
        prev_leap = False
        tet = prev_trang + (14 * lunar_month)

    
    if next_trang - trang == year13:
        # 13 lunations between the solstice moon preceding this tet year, and the solstice moon preceding next tet year
        # It's a leap sui, but is it a leap year?
        # The extra month probablt belongs to next year, but it might be part of this year

        # trang is the new moon of the 11th month of last year
        if (truemoon(trang + (2 * lunar_month)) <= truesun((next_solstice + solar_term), 300)) or (truemoon(trang + (3 * lunar_month)) <= truesun((next_solstice + (2 * solar_term)), 330)):
            # The first condition checks if there is a full lunation between Dongzhi and Dahan
            # The second condition checks if there is a full lunation between Dahan and Yushui
            # In either case, this is a leap sui, in which the leap month belongs to the previous year, which is a leap nean
            leap = True
            next_leap = False
            next_tet = trang + (15 * lunar_month)
        else:
            leap = False
            next_leap = True
            next_tet = trang + (14 * lunar_month)
    else:
        # 12 lunations between the solstice moon preceding this year's tet year, and the solstice moon preceding the next sin year
        # Normal sui, apparently a normal year
        #leap = False
        next_tet = trang + (14 * lunar_month)

    if leap != True:
        leap = False

    # OK
    # If my calculations are correct, this will give us the ACTUAL, PROPER, CORRECT date of tet year
    # tet is the time of the first new moon of the Vietnamese year, though the time of the new moon is in UTC.

    # But what if tet comes after jday?
    if truemoon(tet) > jday:
        year -= 1
        if year == 0:
            year = (-1)
            
        next_solstice = solstice
        next_dongchi = dongchi
        next_trang = trang
        next_tet = tet
        next_leap = leap

        solstice = prev_solstice
        dongchi = prev_dongchi
        trang = prev_trang
        leap = prev_leap

        if leap == True:
            tet = next_tet - year13
        else:
            tet = next_tet - year12

    newmoon = tet
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
        trungkhi = solstice + (2 * solar_term)
        # get the first major solar term which doesn't precede the new moon
        while truesun(trungkhi, angle) < truemoon(tet):
            trungkhi += solar_term
            angle = (angle + 30) % 360

        while truemoon(newmoon + lunar_month) <= jday:
            if leapt == True:
                # We're past the leap month so we don't need to worry about trungkhi any more
                m += 1
                newmoon += lunar_month
            elif truemoon(newmoon + lunar_month) <= truesun(trungkhi, angle):
                # this is the leap month
                newmoon += lunar_month
                leapt = True
            else:
                newmoon += lunar_month
                while truesun(trungkhi, angle) < truemoon(newmoon):
                    trungkhi += solar_term
                    angle = (angle + 30) % 360
                m += 1

        if (leapt == False) and (truemoon(newmoon + lunar_month) <= truesun(trungkhi, angle)):
            month = "Tháng Nhuận"
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

    trang = lunar_epoch + (lunations * lunar_month)
    dongchi = truesun(solstice, 270)
    while truemoon(trang) > dongchi:
        trang -= lunar_month
    while truemoon(trang + lunar_month) <= dongchi:
        trang += lunar_month

    next_solstice = solstice + solar_year
    next_dongchi = truesun(next_solstice, 270)
    
    prev_solstice = solstice - solar_year
    prev_dongchi = truesun(prev_solstice, 270)

    next_trang = trang + year12
    while truemoon(next_trang + lunar_month) <= next_dongchi:
        next_trang += lunar_month

    prev_trang = trang - year13
    while truemoon(prev_trang + lunar_month) <= prev_dongchi:
        prev_trang += lunar_month

    # now to check for leap years
    # as in fromjd(), this looks like it shouldn't work, but it does
    leap = None
    prev_leap = None
    next_leap = None

    if trang - prev_trang == year13:
        if (truemoon(prev_trang + (2 * lunar_month)) <= truesun((solstice + solar_term), 300)) or (truemoon(prev_trang + (3 * lunar_month)) <= truesun((solstice + (2 * solar_term)), 330)):
            prev_leap = True
            leap = False
            tet = prev_trang + (15 * lunar_month)
        else:
            prev_leap = False
            leap = True
            tet = prev_trang + (14 * lunar_month)
    else:
        prev_leap = False
        tet = prev_trang + (14 * lunar_month)
        
    if next_trang - trang == year13:
        if (truemoon(trang + (2 * lunar_month)) <= truesun((next_solstice + solar_term), 300)) or (truemoon(trang + (3 * lunar_month)) <= truesun((next_solstice + (2 * solar_term)), 330)):
            leap = True
            next_leap = False
            next_tet = trang + (15 * lunar_month)
        else:
            leap = False
            next_leap = True
            next_tet = trang + (14 * lunar_month)
    else:
        next_tet = trang + (14 * lunar_month)

    if leap != True:
        leap = False

    newmoon = tet
    m = 0
    #print(leap)
    
    if leap == False:
        # normal year
        if month == "Tháng Nhuận":
            month = "Tháng Giêng" # no way to determine which month the user actually meant

        while MONTHS[m] != month:
            m += 1
            newmoon += lunar_month

        jday = truemoon(newmoon) + day - 1
    else:
        # leap year
        if month == "Tháng Nhuận":
            nhuan = True # assuming that if the user enters a leap month, they want the actual leap month
        else:
            nhuan = False

        trungkhi = solstice + (2 * solar_term)
        angle = 330

        while truesun(trungkhi, angle) < truemoon(newmoon):
            trungkhi += solar_term
            angle = (angle + 30) % 360

        while MONTHS[m] != month:
            if (truemoon(newmoon + lunar_month) <= truesun(trungkhi, angle)) and (nhuan == True):
                # we're in the leap month, which is the month selected
                break
            elif (truemoon(newmoon + lunar_month) <= truesun(trungkhi, angle)):
                newmoon += lunar_month
            else:
                newmoon += lunar_month
                while truesun(trungkhi, angle) < truemoon(newmoon):
                    trungkhi += solar_term
                    angle = (angle + 30) % 360
                m += 1

        jday = truemoon(newmoon) + day - 1

    return jday
                
