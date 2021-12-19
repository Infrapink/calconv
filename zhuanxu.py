#!/usr/bin/python3

# Convert between the Zhuanxu calendar and Julian Days

from math import floor
from fractions import Fraction

sui = 365 + Fraction(1,4) # solar year
yue = 29 + Fraction(499,940) # lunar month
nian12 = 12 * yue
nian13 = 13 * yue
cycle76 = 76 * sui # == 940 * yue

solar_epoch = 1581526 + Fraction(1,4)
lunar_epoch = 1581520 + Fraction(31,940)
cal_epoch = lunar_epoch - yue

MONTHS_NORMAL = ("Guìyuè", "Júyuè", "Lùyuè", "Dōngyuè", "Bīngyuè", "Zōuyuè", "Xìngyuè", "Táoyuè", "Méiyuè", "Liúyuè", "Héyuè", "Lányuè")
MONTHS_LEAP = ("Guìyuè", "Júyuè", "Lùyuè", "Dōngyuè", "Bīngyuè", "Zōuyuè", "Xìngyuè", "Táoyuè", "Méiyuè", "Liúyuè", "Héyuè", "Lányuè", "Rùnyuè")

def getxin(solstice):
    '''Given the solstice, get the date two new moons ago.'''
    solstice = Fraction(solstice)
    if floor(solstice) >= floor(lunar_epoch):
        luns = (solstice - lunar_epoch) // yue
        solstice_moon = lunar_epoch + (luns * yue)
        while floor(solstice_moon + yue) <= floor(solstice):
            solstice_moon += yue
    else:
        luns = (lunar_epoch - solstice) // yue
        solstice_moon = lunar_epoch - (luns * yue)
        while floor(solstice_moon) > floor(solstice):
            solstice_moon -= yue
    xin = solstice_moon - yue
    return(xin)

def tojd(day, month, year):
    '''Convert a date in the Xuanxu calendar into a Julian Day'''
    day = int(day)
    month = str(month)
    year = int(year)

    jday = 0
    solstice = 0

    if year > 0:
        # positive dates
        cycles = (year - 1) // 76
        solstice = solar_epoch + (cycle76 * cycles)
        y = (76 * cycles) + 1
        while y < year:
            y += 1
            solstice += sui
    else:
        # negative dates
        cycles = abs(year) // 76
        solstice = solar_epoch - (cycle76 * cycles)
        y = 0 - (19 * cycles)
        while y > year:
            y -= 1
            solstice -= sui

    xin = getxin(solstice)

    next_solstice = solstice + sui
    next_xin = getxin(next_solstice)

    if next_xin - xin == (13 * yue):
        leap = True
    else:
        leap = False

    jday = xin
    m = 0
    if leap == False:
        # normal year
        if month == "Rùnyuè":
            month = "Guìyuè"
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
    '''Convert a Julian Day into a date in the Xuanxu calendar'''
    jday = int(jday)
    day = 0
    month = ""
    year = 0

    if jday >= floor(cal_epoch):
        # positive dates
        y = (jday - solar_epoch) // sui
        year = y + 1
        solstice = solar_epoch + (y * sui)
        while floor(solstice + sui) <= jday:
            year += 1
            solstice += sui
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

    xin = getxin(solstice)

    next_solstice = solstice + sui
    next_xin = getxin(next_solstice)

    if floor(next_xin) <= jday:
        year += 1
        solstice = next_solstice
        xin = next_xin
        next_solstice = solstice + sui
        next_xin = getxin(next_solstice)

    if next_xin - xin == (13 * yue):
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
