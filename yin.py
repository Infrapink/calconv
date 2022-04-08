#!/usr/bin/python3

# Convert between the Yin calendar (Sifen li) and Julian Days

from math import floor
from fractions import Fraction

sui = 365 + Fraction(1,4) # solar year
yue = 29 + Fraction(499,940) # lunar month
nian12 = 12 * yue
nian13 = 13 * yue
cycle76 = 76 * sui # == 940 * yue

solar_epoch = 1567282 + Fraction(1,4)
lunar_epoch = 1567286 + Fraction(429,470)

MONTHS_NORMAL = ("Lùyuè", "Dōngyuè", "Bīngyuè", "Zōuyuè", "Xìngyuè", "Táoyuè", "Méiyuè", "Liúyuè", "Héyuè", "Lányuè", "Guìyuè", "Júyuè")
MONTHS_LEAP = ("Lùyuè", "Dōngyuè", "Bīngyuè", "Zōuyuè", "Xìngyuè", "Táoyuè", "Méiyuè", "Liúyuè", "Héyuè", "Lányuè", "Guìyuè", "Júyuè", "Rùnyuè")

def getxin(solstice):
    solstice = Fraction(solstice)
    if solstice == solar_epoch:
        xin = lunar_epoch
    elif solstice > solar_epoch:
        luns = (solstice - lunar_epoch) // yue
        xin = lunar_epoch + (luns * yue)
        while floor(xin) <= floor(solstice):
            xin += yue
    else:
        luns = (lunar_epoch - solstice) // yue
        xin = lunar_epoch - (luns * yue)
        while floor(xin - yue) > floor(solstice):
            xin -= yue
    return xin

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
        xin = lunar_epoch + (cycles * cycle76)
        y = (76 * cycles) + 1
        while y < year:
            y += 1
            solstice += sui
    else:
        # negative dates
        cycles = abs(year) // 76
        solstice = solar_epoch - (cycle76 * cycles)
        xin = lunar_epoch - (cycle76 * cycles)
        y = 0 - (19 * cycles)
        while y > year:
            y -= 1
            solstice -= sui

    xin = getxin(solstice)
    prev_solstice = solstice - sui
    prev_xin = getxin(prev_solstice)

    next_solstice = solstice + sui
    next_xin = getxin(next_solstice)

    if (next_xin - xin) == nian13:
        leap = True
    else:
        leap = False

    jday = xin
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

    if jday >= floor(lunar_epoch):
        # positive dates
        y = (jday - solar_epoch) // sui
        year = y + 1
        solstice = solar_epoch + (y * sui)
    else:
        # negative dates
        year = 0 - ((solar_epoch - jday) // sui)
        solstice = solar_epoch + (year * sui)
        while floor(solstice) > jday:
            year -= 1
            solstice -= sui

    xin = getxin(solstice)
    if floor(xin) > jday:
        year -= 1
        if year == 0:
            year = (-1)
        solstice -= sui
        xin = getxin(solstice)

    next_solstice = solstice + sui
    next_xin = getxin(next_solstice)
    if next_xin - xin == nian13:
        leap = True
    else:
        leap = False

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
