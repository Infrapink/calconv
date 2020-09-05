#!/usr/bin/python

#
# Convert between the Fixed Babylonian calendar and Julian Day
#

from fractions import *
from math import floor

leap_years_an = (3,6,8,11,14,17,19,0)
leap_years_bn = (1,3,6,9,12,14,17)
leap_years_zo = (0,2,5,8,11,13,16)

monlen = 29 + Fraction(12,24) + Fraction(44,1440) + Fraction(28,864000)
year12 = 12 * monlen
year13 = 13 * monlen
cycle19 = 235 * monlen

lunar_epoch = 1448696 + Fraction(63379,72000)
solar_epoch = 1448668 + Fraction(16979,43200)

MONTHS_NORMAL = ("Nisānu", "Āru", "Simanu", "Dumuzu", "Abu", "Ulūlu", "Tišritum", "Samnu", "Kislimu", "Ṭebētum", "Šabaṭu", "Addaru")
MONTHS_LEAP = ("Nisānu", "Āru", "Simanu", "Dumuzu", "Abu", "Ulūlu", "Tišritum", "Samnu", "Kislimu", "Ṭebētum", "Šabaṭu", "Addaru", "Addaru Arku")
MONTHS_17 = ("Nisānu", "Āru", "Simanu", "Dumuzu", "Abu", "Ulūlu", "Ulūlu Arrku", "Tišritum", "Samnu", "Kislimu", "Ṭebētum", "Šabaṭu", "Addaru")

def tojd(day,month,year):
    """Convert a Babylonian date to a Julian Day."""
    day = int(day)
    month = month
    year = int(year)

    jday = lunar_epoch

    if year > 0:
        # positive years
        if month == "Ulūlu Arrku":
            if year % 19 != 17:
                month = "Ulūlu"
        elif month == "Addaru Arrku":
            if year % 19 not in leap_years_an:
                month = "Addaru"

        y = 1
        while y < year:
            if (year - y) >= 19:
                jday += cycle19
                y += 19
            elif y % 19 in leap_years_an:
                jday += year13
                y += 1
            else:
                jday += year12
                y += 1

        # jday is now the new moon on which the year begins
        if year % 19 == 17:
            m = MONTHS_17
        elif year % 19 in leap_years_an:
            m = MONTHS_LEAP
        else:
            m = MONTHS_NORMAL

        for i in m:
            if i == month:
                jday = floor(jday) + day# - 1
                break
            else:
                jday += monlen

    else:
        # negative years
        if month == "Ulūlu Arrku":
            if abs(year) % 19 != 3:
                month =	"Ulūlu"
        elif month == "Addaru Arrku":
            if abs(year) % 19 not in leap_years_bn:
                month =	"Addaru"

        y = 0
        while y > year:
            if y - year >= 19:
                y -= 19
                jday -= cycle19
            if abs(y - 1) % 19 in leap_years_bn:
                y -= 1
                jday -= year13
            else:
                y -= 1
                jday -= year12

        if abs(year) % 19 == 3:
            m = MONTHS_17
        elif abs(year) in leap_years_bn:
            m = MONTHS_LEAP
        else:
            m = MONTHS_NORMAL

        for i in m:
            if i == month:
                jday = floor(jday) + day - 1
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
        while curryear == False:
            if year % 19 in leap_years_an:
                next_res = res + year13
            else:
                next_res = res + year12
                
            if int(jday) < int(next_res):
                curryear = True
            elif jday - res >= cycle19:
                year += 19
                res += cycle19
            elif year % 19 in leap_years_an:
                year += 1
                res += year13
            else:
                year += 1
                res += year12

        if year % 19 == 17:
            m = MONTHS_17
        elif year % 19 in leap_years_an:
            m = MONTHS_LEAP
        else:
            m = MONTHS_NORMAL

        newmoon = res
        nextmoon = newmoon + monlen

        for i in m:
            crescent = floor(newmoon) + 1
            next_crescent = floor(nextmoon) + 1
            if floor(jday) < next_crescent:
                month = i
                day = floor(jday) - crescent + 1
                break
            else:
                newmoon += monlen
                nextmoon += monlen

    else:
        # negative dates

        while floor(jday) < floor(res):
            if res - jday >= cycle19:
                res -= cycle19
                year -= 19
            elif abs(year - 1) % 19 in leap_years_bn:
                res -= year13
                year -= 1
            else:
                res -= year12
                year -= 1

        if abs(year) % 19 == 3:
            m = MONTHS_17
        elif (abs(year) % 19) in leap_years_bn:
            m = MONTHS_LEAP
        else:
            m = MONTHS_NORMAL

        newmoon = res
        nextmoon = newmoon + monlen

        for i in m:
            crescent = floor(newmoon)
            next_crescent = floor(nextmoon)
            if floor(jday) < next_crescent:
                month = i
                day = int(jday) - crescent + 1
                #if jday < 0:
                    #day += 1
                break
            else:
                newmoon += monlen
                nextmoon += monlen

    return (day, month, year)

