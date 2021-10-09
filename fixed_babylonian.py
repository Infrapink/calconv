#!/usr/bin/python3

#
# Convert between the Fixed Babylonian calendar and Julian Day
#

from fractions import *
from math import floor, ceil

leap_years_an = (3,6,8,11,14,17,19,0)
leap_years_bn = (1,3,6,9,12,14,17)
leap_years_zo = (0,2,5,8,11,13,16)

monlen = 29 + Fraction(12,24) + Fraction(44,1440) + Fraction(28,864000)
year12 = 12 * monlen
year13 = 13 * monlen
cycle19 = 235 * monlen

#solar_epoch = Fraction(125181054427,86400)
#lunar_epoch = Fraction(312955486723,216000)
solar_epoch = Fraction(62582469179,43200) + Fraction(3,24)
lunar_epoch = Fraction(7822931297,5400) + Fraction(3,24)

MONTHS_NORMAL = ("Nisānu", "Āru", "Simanu", "Dumuzu", "Abu", "Ulūlu", "Tišritum", "Samnu", "Kislimu", "Ṭebētum", "Šabaṭu", "Addaru")
MONTHS_LEAP = ("Nisānu", "Āru", "Simanu", "Dumuzu", "Abu", "Ulūlu", "Tišritum", "Samnu", "Kislimu", "Ṭebētum", "Šabaṭu", "Addaru", "Addaru Arku")
MONTHS_17 = ("Nisānu", "Āru", "Simanu", "Dumuzu", "Abu", "Ulūlu", "Ulūlu Arrku", "Tišritum", "Samnu", "Kislimu", "Ṭebētum", "Šabaṭu", "Addaru")

def tojd(day,month,year):
    """Convert a Babylonian date to a Julian Day."""
    day = int(day)
    month = month
    year = int(year)

    if year > 0:
        # positive years
        if month == "Ulūlu Arrku":
            if year % 19 != 17:
                month = "Ulūlu"
        elif month == "Addaru Arrku":
            if year % 19 not in leap_years_an:
                month = "Addaru"

        y = 1
        cycles = (year - y) // 19
        y += (19 * cycles)
        res = lunar_epoch + (cycle19 * cycles)
        
        while y < year:
            if y % 19 in leap_years_an:
                res += year13
            else:
                res += year12
            y += 1

        # res is now the new moon on which the year begins
        if year % 19 == 17:
            m = MONTHS_17
        elif year % 19 in leap_years_an:
            m = MONTHS_LEAP
        else:
            m = MONTHS_NORMAL

    else:
        # negative years
        if month == "Ulūlu Arrku":
            if abs(year) % 19 != 3:
                month =	"Ulūlu"
        elif month == "Addaru Arrku":
            if abs(year) % 19 not in leap_years_bn:
                month =	"Addaru"

        y = 0
        cycles = (y - year) // 19
        y -= (19 * cycles)
        res = lunar_epoch - (cycle19 * cycles)
        while y > year:
            y -= 1
            if abs(y) % 19 in leap_years_bn:
                res -= year13
            else:
                res -= year12

        if abs(year) % 19 == 3:
            m = MONTHS_17
        elif abs(year) in leap_years_bn:
            m = MONTHS_LEAP
        else:
            m = MONTHS_NORMAL

    jday = res
    for i in m:
        if i == month:
            jday = floor(jday) + day# - 1
            break
        else:
            jday = jday + monlen

    return jday

def fromjd(jday):
    """Convert a Julian Day into a date in the Seleucid calendar."""
    jday = int(jday)

    day = 0
    month = ""
    year = 0

    res = lunar_epoch
    curryear = False

    if jday >= floor(lunar_epoch):
        # positive dates

        year += 1
        cycles = (jday - lunar_epoch) // cycle19
        year += (19 * cycles)
        res = lunar_epoch + (cycle19 * cycles)
        
        while curryear == False:
            if year % 19 in leap_years_an:
                next_res = res + year13
            else:
                next_res = res + year12
                
            if floor(jday) < floor(next_res):
                curryear = True
            else:
                year += 1
                res = next_res

        if year % 19 == 17:
            m = MONTHS_17
        elif year % 19 in leap_years_an:
            m = MONTHS_LEAP
        else:
            m = MONTHS_NORMAL

    else:
        # negative dates

        cycles = (lunar_epoch - jday) // cycle19
        year -= (19 * cycles)
        res = lunar_epoch - (cycle19 * cycles)
        
        while floor(jday) < floor(res):
            year -= 1
            if abs(year) % 19 in leap_years_bn:
                res -= year13
            else:
                res -= year12

        if abs(year) % 19 == 3:
            m = MONTHS_17
        elif (abs(year) % 19) in leap_years_bn:
            m = MONTHS_LEAP
        else:
            m = MONTHS_NORMAL

    newmoon = res
    nextmoon = newmoon + monlen
    
    for i in m:
        crescent = ceil(newmoon)
        next_crescent = ceil(nextmoon)
        if floor(jday) < next_crescent:
            month = i
            day = floor(jday) - crescent + 1
            break
        else:
            newmoon += monlen
            nextmoon += monlen

    return (day, month, year)

