#!/usr/bin/python3

# Convert between the old Chinese calendar (Yao era) and Julian Day.

from fractions import *
from math import floor

solar_year = 365 + Fraction(5,24) + Fraction(48,1440) + Fraction(45,86400)
solar_term = Fraction(solar_year,24)

SOLAR_TERMS = ("Lìchūn", "Yǔshuı̌", "Jı̄ngzhé", "Chūnfēn", "Qı̄ngmíng", "Gǔyǔ", "Lìxià", "Xiǎomǎn", "Mángzhòng", "Xiàzhì", "Xiǎoshǔ", "Dàshǔ", "Lìqiū", "Chǔshǔ", "Báilù", "Qiūfēn", "Hánlù", "Shuāngjiàng", "Lìdōng", "Xiǎoxuě", "Dàxuě", "Dōngzhì", "Xiǎohán", "Dàhán")

solstice = Fraction(40346771441, 43200) + Fraction(8,24) # Southern solstice of 1 Anno Yao = 23 December 2699 BC = 30 Azar 3320 BH, with correction for Chinese Standard Time
epoch = solstice + (3 * solar_term) # moment when Lìchūn officially starts

def tojd(day, st, year):
    day = int(day)
    st = st
    year = int(year)

    if year > 0:
        # positive years
        jday = epoch + (solar_year * year)

    else:
        # negative years
        jday = epoch + (year * solar_year)

    for s in SOLAR_TERMS:
        if s == st:
            jday = floor(jday) + day - 1
            break
        else:
            jday += solar_term

    return jday

def fromjd(jday):
    jday = int(jday)
    day = 0
    st = ""
    year = 0

    if jday >= int(epoch):
        # positive dates
        year = ((jday - epoch) // solar_year)# + 1
        xin = epoch + (year * solar_year)
        while jday > int(xin + solar_year):
            year += 1
            xin += solar_year

    else:
        # negative dates
        year = 0 - ((epoch - jday) // solar_year)
        xin = epoch + (year * solar_year)
        while jday < floor(xin):
            year -= 1
            xin -= solar_year

    term = xin
    for s in SOLAR_TERMS:
        if floor(term + solar_term) > jday:
            st = s
            day = jday - floor(term) + 1
            break
        else:
            term += solar_term

    return(day, st, year)
