#!/usr/bin/python3

# Convert between the Zhou calendar and Julian Day

from fractions import Fraction
from math import floor
from solun import truemoon, truesun

MONTHS_NORMAL = ("Dōngyuè", "Bīngyuè", "Zōuyuè", "Xìngyuè", "Táoyuè", "Méiyuè", "Liúyuè", "Héyuè", "Lányuè", "Guìyuè", "Júyuè", "Lùyuè")
MONTHS_LEAP = ("Dōngyuè", "Bīngyuè", "Zōuyuè", "Xìngyuè", "Táoyuè", "Méiyuè",	"Liúyuè", "Héyuè", "Lányuè", "Guìyuè", "Júyuè", "Lùyuè", "Rùnyuè")

solar_year = 365 + Fraction(5,24) + Fraction(49,1440) + Fraction(328,864000) # time between two southern solstices; differs by about a minute from the time between northward equinoxes due to orbital mechanics
lunar_month = 29 + Fraction(12,24) + Fraction(44,1440) + Fraction(28,864000) # length of 1 lunation

year12 = 12 * lunar_month
year13 = 13 * lunar_month

solar_epoch = Fraction(578608061497, 432000) # instant of the southern solstice which heralds the start of the Western Zhou, corresponding to 21 December 1047 BC
lunar_epoch = Fraction(289303542653, 216000) # new moon immediately preceding solar_epoch

timezone = Fraction(7,24) + Fraction(14,1440) + Fraction(528,864000) # Fenghao, the original capital of Western Zhou, is located 108.72ºE, which corresponds to a local time 7 hours 14 minutes 52.8 seconds ahead of UTC.

def fromjd(jday):
    '''Convert a Julian Day into a date in the Zhou calendar'''
    jday = int(jday)

    if jday >= truemoon(lunar_epoch, timezone):
        # positive years
        if jday <= truesun(solar_epoch, 270, timezone):
            year = 1
            solstice = solar_epoch
            yue = lunar_epoch
        else:
            orbits = (jday - solar_epoch) // solar_year
            year = orbits + 1
            solstice = solar_epoch + (orbits * solar_year)
            lunations = (solstice - lunar_epoch) // lunar_month
            yue = lunar_epoch + (lunations * lunar_month)
    else:
        # negative years
        orbits = (solar_epoch - jday) // solar_year
        year = 0 - orbits - 1
        solstice = solar_epoch + (year * solar_year)
        lunations = (lunar_epoch - solstice) // lunar_month
        yue = lunar_epoch - (lunations * lunar_month)

    while truemoon((yue + lunar_month), timezone) <= truesun(solstice, 270, timezone):
        yue += lunar_month
    while truemoon(yue, timezone) > truesun(solstice, 270, timezone):
        yue -= lunar_month

    next_solstice = solstice + solar_year
    next_yue = yue + year12
    while truemoon((next_yue + lunar_month), timezone) <= truesun(next_solstice, 270, timezone):
        next_yue += lunar_month

    if truemoon(next_yue, timezone) <= jday:
        yue = next_yue
        solstice = next_solstice
        next_solstice += solar_year
        next_yue += year12
        while truemoon((next_yue + lunar_month), timezone) <= truesun(next_solstice, 270, timezone):
            next_yue += lunar_month

    if next_yue - yue == year13:
        # leap year
        months = MONTHS_LEAP
    else:
        # normal year
        months = MONTHS_NORMAL

    newmoon = yue
    m = 0

    while truemoon((newmoon + lunar_month), timezone) <= jday:
        newmoon += lunar_month
        m += 1

    month = months[m]
    day = jday - truemoon(newmoon, timezone) + 1
    return(day, month, year)

def tojd(day, month, year):
    '''Convert a date in the Zhou calendar to a Julian Day'''
    day = int(day)
    month = str(month)
    year = int(year)

    if year > 0:
        # positive dates
        solstice = solar_epoch + ((year - 1) * solar_year)
        lunations = (solstice - lunar_epoch) // lunar_month
        yue = lunar_epoch + (lunations * lunar_month)
    else:
        # negative dates
        solstice = solar_epoch + (year * solar_year)
        lunations = (lunar_epoch - solstice) // lunar_month
        yue = lunar_epoch - (lunations * lunar_month)

    while truemoon((yue + lunar_month), timezone) <= truesun(solstice, 270, timezone):
        yue += lunar_month
    while truemoon(yue, timezone) > truesun(solstice, 270, timezone):
        yue -= lunar_month

    next_solstice = solstice + solar_year
    next_yue = yue + year12
    while truemoon((next_yue + lunar_month), timezone) <= truesun(next_solstice, 270, timezone):
        yue += lunar_month

    if next_yue - yue == year13:
        # leap year
        months = MONTHS_LEAP
    else:
        # normal year
        months = MONTHS_NORMAL
        if month == "Rùnyuè":
            month = "Lùyuè"

    jday = yue
    m = 0
    while months[m] != month:
        m += 1
        jday += lunar_month

    jday = truemoon(jday, timezone) + day - 1
    return jday
