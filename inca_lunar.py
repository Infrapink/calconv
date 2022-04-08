#!/usr/bin/python3

#
# Convert between the Inca civil calendar and Julian Day
#

from fractions import *
from math import floor, ceil

MONTHS_NORMAL = ("Intiraymipacha", "Pachacyahuarllamapacha", "Yapuypacha", "Coyaraymipacha", "Paramañaypacha", "Ayamarcaypacha", "Capacintiraymipacha", "Huacapacha", "Huarachicuypacha", "Paraypacha", "Rinrituccinapacha", "Aymuraypacha")
MONTHS_LEAP = ("Intiraymipacha", "Pachacyahuarllamapacha", "Yapuypacha", "Coyaraymipacha", "Paramañaypacha", "Ayamarcaypacha", "Capacintiraymipacha", "Huacapacha", "Huarachicuypacha", "Paraypacha", "Rinrituccinapacha", "Aymuraypacha", "Intihuatapacyapanapacha")


monlen = 29 + Fraction(12,24) + Fraction(44,1440) + Fraction(28,864000)
eqlen = 365 + Fraction(5,24) + Fraction(48,1440) + Fraction(45,86400)

year12 = 12 * monlen
year13 = 13 * monlen

solar_epoch = Fraction(6065414981, 2700) - Fraction(5,24) + 1 # southern solstice in 1438 AD, corrected for Peruvian time
lunar_epoch = Fraction(485229140243, 216000) + Fraction(5,24) + 1 # new moon before the souther solstice of 1438 AD, corrected for Peruvian time

def tojd(day, month, year):
    """Convert a date in the Inca civil calendar to a Julian Day."""
    day = int(day)
    month = month
    year = int(year)

    curryear = False

    if year >= 0:
        # positive dates
        equinox = ((year - 1) * eqlen) + solar_epoch
        lunations = (equinox - lunar_epoch) // monlen
        jday = (lunations * monlen) + lunar_epoch
        while ceil(jday + monlen) < floor(equinox):
            jday += monlen

        # jday is now the new moon of the first month in the year in question. Is the year in question a leap year?

        if ceil(jday + year13) <= floor(equinox + eqlen):
            # leap year
            m = MONTHS_LEAP
        else:
            # not a leap year
            m = MONTHS_NORMAL

        if month not in m:
            month = "Aymuraypacha"

    else:
        # negative years
        equinox = (year * eqlen) + solar_epoch
        lunations = (lunar_epoch - equinox) // monlen
        jday = lunar_epoch - (lunations * monlen)
        while ceil(jday) > floor(equinox):
            jday -= monlen

        # jday is now the new moon of the first month of the year in question. Is it a leap year?

        if ceil(jday + year13) <= floor(equinox + eqlen):
            # leap year
            m = MONTHS_LEAP
        else:
            # not a leap year
            m = MONTHS_NORMAL

        if month not in m:
            month = "Aymuraypacha"

    for i in m:
        if i == month:
            jday = ceil(jday) + day - 1
            break
        else:
            jday += monlen
    return jday

def fromjd(jday):
    """Convert a Julian Day to a date in the Babylonian calendar"""
    jday = int(jday)

    day = 0
    month = ""
    year = 0

    curryear = False
    equinox = solar_epoch
    raymi = lunar_epoch

    if jday >= ceil(lunar_epoch):
        # positive dates
        year = 1
        while curryear == False:
            nexteq = equinox + eqlen
            if ceil(raymi + year13) < floor(nexteq):
                next_raymi = raymi + year13
            else:
                next_raymi = raymi + year12

            if jday < int(next_raymi):
                curryear = True
            else:
                year += 1
                equinox = nexteq
                raymi = next_raymi

        # check if it's a leap year
        if int(raymi + year13) <= int(equinox + eqlen):
            # leap year
            m = MONTHS_LEAP
        else:
            # not a leap year
            m = MONTHS_NORMAL

    else:
        # negative dates
        while ceil(raymi) > jday:
            year -= 1
            equinox -= eqlen

            if raymi - year12 < equinox:
                raymi -= year12
            else:
                raymi -= year13

        # right, now what type of year is it?

        nexteq = equinox + eqlen
        if raymi + year13 < nexteq:
            # leap year
            m = MONTHS_LEAP
        else:
            # not a leap year
            m = MONTHS_NORMAL

    newmoon = raymi
    nextmoon = newmoon + monlen
        
    for i in m:
        crescent = ceil(newmoon)
        next_crescent = ceil(nextmoon)
        if jday < next_crescent:
            month = i
            day = floor(jday) - crescent + 1
            break
        else:
            newmoon += monlen
            nextmoon += monlen

    return (day, month, year)
