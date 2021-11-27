#!/usr/bin/python3

# Convert between the Chinese Quarter-Remainder calendar (Sifen li) and Julian Days

# Note that the epoch used here is Christian year 85, which is apparently the one use by Martzloff.
# This is year 17 of the 76-year Callipic cycle, and thus the mean sun and mean moon are NOT equal at the epoch.

from math import floor
from fractions import Fraction

sui = 365 + Fraction(1,4) # solar year
yue = 29 + Fraction(499,940) # lunar month
nian12 = 12 * yue
nian13 = 13 * yue
cycle76 = 76 * sui # == 940 * yue

solar_epoch = Fraction(7008381, 4) + 1 # 23 December 84 AD = 537 BH, based on data from Mertzloff, p 249
lunar_epoch = Fraction(164696223, 94) +1 # 16 December 84 AD = 537 BH, based on data from Mertzloff, p 249

# Martzloff uses the modern system of inserting the leap month at the point where a full lunation passes
# without a major solar term. However, every source I can find says that this is a later innovation,
# so I am taking it that the leap month falls before the 11th month.
MONTHS_NORMAL = ("Dōngyuè", "Bīngyuè", "Zōuyuè", "Xìngyuè", "Táoyuè", "Méiyuè", "Liúyuè", "Héyuè", "Lányuè", "Guìyuè", "Júyuè", "Lùyuè")
MONTHS_LEAP = ("Dōngyuè", "Bīngyuè", "Zōuyuè", "Xìngyuè", "Táoyuè", "Méiyuè", "Liúyuè", "Héyuè", "Lányuè", "Guìyuè","Rùnyuè",  "Júyuè", "Lùyuè")



def tojd(day, month, year):
    '''Convert a date in the Sifen li into a Julian Day'''
    day = int(day)
    month = str(month)
    year = int(year)

    jday = 0
    solstice = 0

    if year > 0:
        # positive dates
        cycles = (year - 1) // 76
        solstice = solar_epoch + (cycle76 * cycles)
        solstice_moon = lunar_epoch + (cycles * cycle76)
        y = (76 * cycles) + 1
        while y < year:
            y += 1
            solstice += sui
            if floor(solstice_moon + nian13) <= floor(solstice):
                solstice_moon += nian13
            else:
                solstice_moon += nian12
    else:
        # negative dates
        cycles = abs(year) // 76
        solstice = solar_epoch - (cycle76 * cycles)
        solstice_moon = lunar_epoch - (cycle76 * cycles)
        y = 0 - (19 * cycles)
        while y > year:
            y -= 1
            solstice -= sui
            if floor(solstice_moon - nian12) > floor(solstice):
                solstice_moon -= nian13
            else:
                solstice_moon -= nian12

    prev_solstice = solstice - sui
    if floor(solstice_moon - nian12) > floor(prev_solstice):
        prev_moon = solstice_moon - nian13
        prev_leap = True
        jday = prev_moon + (15 * yue)
    else:
        prev_moon = solstice_moon - nian12
        prev_leap = False
        jday = prev_moon + (14 * yue)

    next_solstice = solstice + sui
    if floor(solstice_moon + nian13) <= floor(next_solstice):
        leap = True
        next_moon = solstice_moon + (15 * yue)
    else:
        leap = False
        next_moon = solstice_moon + (14 * yue)

    m = 0
    if leap == False:
        # normal year
        if month == "Rùnyuè":
            month = "Júyuè"
        while MONTHS_NORMAL[m] != month:
            m += 1
            jday += yue
    else:
        # leap year
        while MONTHS_LEAP[m] != month:
            m += 1
            jday += yue

    jday = floor(jday) + day - 1
    return(jday)


def fromjd(jday):
    '''Convert a Julian Day into a date in the Sifen li'''
    jday = int(jday)
    day = 0
    month = ""
    year = 0

    if jday >= floor(lunar_epoch + (2 * yue)):
        # positive dates... probably
        y = (jday - solar_epoch) // sui
        year = y + 1
        solstice = solar_epoch + (y * sui)
        while floor(solstice + sui) <= jday:
            #y += 1
            year += 1
            solstice += sui
        luns = (solstice - lunar_epoch) // yue
        solstice_moon = lunar_epoch + (luns * yue)
        while floor(solstice_moon + yue) <= floor(solstice):
            solstice_moon += yue

    else:
        # negative dates
        year = 0 - ((solar_epoch - jday) // sui)
        solstice = solar_epoch + (year * sui)
        while floor(solstice) > jday:
            year -= 1
            solstice -= sui
        while floor(solstice + sui) <= jday:
            year += 1
            solstice += sui
        luns = (lunar_epoch - solstice) // yue
        solstice_moon = lunar_epoch - (luns * yue)
        while floor(solstice_moon) > floor(solstice):
            solstice_moon -= yue
        while floor(solstice_moon + yue) <= jday:
            solstice_moon += yue

    # now we have the solstice preceding Xin Nian, as well as its corresponding new moon. Let's get New Year's Day.
    prev_solstice = solstice - sui
    if floor(solstice_moon - nian12) > floor(prev_solstice):
        # leap year
        prev_moon = solstice_moon - nian13
        prev_leap = True
        xin = prev_moon + (15 * yue)
    else:
        # regular year
        prev_moon = solstice_moon - nian12
        prev_leap = False
        xin = prev_moon + (14 * yue)

    next_solstice = solstice + sui
    if floor(solstice_moon + nian13) <= floor(next_solstice):
        # leap year
        next_moon = solstice_moon + nian13
        leap = True
        next_xin = solstice_moon + (15 * yue)
    else:
        # regular year
        next_moon = solstice_moon + nian12
        leap = False
        next_xin = solstice_moon + (14 * yue)

    if floor(xin) > jday:
        year -= 1
        if year == 0:
            year = (-1)

        next_solstice = solstice
        next_moon = solstice_moon
        next_xin = xin
        
        solstice = prev_solstice
        solstice_moon = prev_moon
        leap = prev_leap

        prev_solstice = solstice - sui
        if floor(solstice_moon - nian12) > floor(prev_solstice):
            prev_moon = solstice_moon - nian13
            prev_leap = True
            xin = prev_moon + (15 * yue)
        else:
            prev_moon = solstice_moon - nian12
            prev_leap = False
            xin = prev_moon + (14 * yue)
            
    newmoon = xin
    m = 0
    if leap == False:
        # normal year
        while floor(newmoon + yue) <= jday:
            newmoon += yue
            m += 1
        month = MONTHS_NORMAL[m]
    else:
        # leap year
        while floor(newmoon + yue) <= jday:
            newmoon += yue
            m += 1
        month = MONTHS_LEAP[m]

    day = jday - floor(newmoon) + 1
    return (day, month, year)
