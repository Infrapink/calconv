#!/usr/bin/python3

#
# Convert between the Old Babylonian calendar and Julian Day
#

from fractions import *
from math import floor, ceil

MONTHS_NORMAL = ("Nisānu", "Āru", "Simanu", "Dumuzu", "Abu", "Ulūlu", "Tišritum", "Samnu", "Kislimu", "Ṭebētum", "Šabaṭu", "Addaru")
MONTHS_LEAP = ("Nisānu", "Āru", "Simanu", "Dumuzu", "Abu", "Ulūlu", "Tišritum", "Samnu", "Kislimu", "Ṭebētum", "Šabaṭu", "Addaru", "Addaru Arku")
MONTHS_17 = ("Nisānu", "Āru", "Simanu", "Dumuzu", "Abu", "Ulūlu", "Ulūlu Arrku", "Tišritum", "Samnu", "Kislimu", "Ṭebētum", "Šabaṭu", "Addaru")

monlen = 29 + Fraction(12,24) + Fraction(44,1440) + Fraction(28,864000)
eqlen = 365 + Fraction(5,24) + Fraction(48,1440) + Fraction(45,86400)

year12 = 12 * monlen
year13 = 13 * monlen

solar_epoch = Fraction(-18513741167,86400) + Fraction(3,24)
lunar_epoch = Fraction(-46281244111,216000) + Fraction(3,24)

def tojd(day, month, year):
    """Convert a date in the Macedonian calendar to a Julian Day."""
    day = int(day)
    month = month
    year = int(year)

    curryear = False

    if year >= 0:
        # positive dates
        equinox = ((year - 1) * eqlen) + solar_epoch
        lunations = (equinox - lunar_epoch) // monlen
        jday = (lunations * monlen) + lunar_epoch
        while jday < equinox:
            jday += monlen

        # jday is now the new moon of the first month in the year in question. Is the year in question a leap year?

        if jday + year12 <= equinox + eqlen:
            # leap year
            if year % 19 == 18:
                m = MONTHS_17
            else:
                m = MONTHS_LEAP
        else:
            # not a leap year
            m = MONTHS_NORMAL

        if month not in m:
            if month == "Ulūlu Arrku":
                month = "Ulūlu"
            elif month == "Addaru Arku":
                month = "Addaru"

    else:
        # negative years
        equinox = (year * eqlen) + solar_epoch
        lunations = (lunar_epoch - equinox) // monlen
        jday = lunar_epoch - (lunations * monlen)
        while jday - equinox > monlen:
            jday -= monlen

        # jday is now the new moon of the first month of the year in questino. Is it a leap year?

        if jday + year12 <= equinox + eqlen:
            # leap year
            if abs(year % 19) == 2:
                m = MONTHS_18
            else:
                m = MONTHS_LEAP
        else:
            # not a leap year
            m = MONTHS_NORMAL

        if month not in m:
            if month == "Ulūlu Arrku":
                month = "Ulūlu"
            elif month == "Addaru Arrku":
                month = "Addaru"

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
    res = lunar_epoch
    metonic = 0

    if jday >= int(lunar_epoch):
        # positive dates
        year = 1
        while curryear == False:
            next_equinox = equinox + eqlen
            if res + year12 < next_equinox:
                next_res = res + year13
                metonic += 1
            else:
                next_res = res + year12

            if jday < int(next_res):
                curryear = True
            else:
                year += 1
                equinox = next_equinox
                res = next_res

        # check if it's a leap year
        if (res + year12) < (equinox + eqlen):
            # leap year
            if metonic % 6 == 0:
                m = MONTHS_17
            else:
                m = MONTHS_LEAP
        else:
            # not a leap year
            m = MONTHS_NORMAL

        newmoon = res
        nextmoon = newmoon + monlen

    else:
        # negative dates
        while res > jday:
            year -= 1
            equinox -= eqlen

            if res - year13 > equinox:
                res -= year13
            else:
                res -= year12

        # right, now what type of year is it?

        nexteq = equinox + eqlen
        if res + year12 < nexteq:
            # leap year
            if abs(year) % 19 == 2:
                m = MONTHS_17
            else:
                m = MONTHS_LEAP
        else:
            # not a leap year
            m = MONTHS_NORMAL

    newmoon = res
    nextmoon = newmoon + monlen
        
    for i in m:
        crescent = ceil(newmoon)
        next_crescent = ceil(nextmoon)
        if jday < next_crescent:
            month = i
            day = jday - crescent + 1
            break
        else:
            newmoon += monlen
            nextmoon += monlen

    return (day, month, year)
