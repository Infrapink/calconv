#!/usr/bin/python3

#
# Convert between Samaritan Hebrew calendar and Julian Day
#

import months
from fractions import *
from math import floor

leap_years_ai = (3,6,8,11,14,17,19,0)
leap_years_bi = (1,3,6,9,12,14,17)
leap_years_zo = (0,2,5,8,11,13,16)
    
monlen = 29 + Fraction(12,24) + Fraction(793, (24 * 1080)) # formal mean synodic month length
yearlen12 = 12 * monlen # length of a 12-month year
yearlen13 = 13 * monlen # length of a 13-month year
cycle19 = 235 * monlen
molad_prime = 1122910 + Fraction(11,24) + Fraction(451,25920)

YEARTYPE = {353: months.SAMARITAN_DEFICIENT_NORMAL,
            354: months.SAMARITAN_REGULAR_NORMAL,
            355: months.SAMARITAN_ABUNDANT_NORMAL,
            383: months.SAMARITAN_DEFICIENT_LEAP,
            384: months.SAMARITAN_REGULAR_LEAP,
            385: months.SAMARITAN_ABUNDANT_LEAP}

def tojd(day, month, year):
    day = int(day)
    month = month
    year = int(year)
    
    hashanah = molad_prime

    if year >= 1:
        # positive years

        if month == "Veadar":
            if year % 19 not in leap_years_ai:
                month = "Adar"
                
        for y in range(1, year):
            if y % 19 in leap_years_ai:
                hashanah += yearlen13
            else:
                hashanah += yearlen12

        # the value of days is now the moment of the molad of Nisan for the year in question
        
        if year % 19 in leap_years_ai:
            next_hashanah = hashanah + yearlen13
        else:
            next_hashanah = hashanah + yearlen12

        rosh = floor(hashanah)
        molad = hashanah % 1

        next_rosh = floor(next_hashanah)
        next_molad = next_hashanah % 1

        m = YEARTYPE[next_rosh - rosh]
        days = rosh

        for i in m.keys():
            if i == month:
                days += day - 1
                break
            else:
                days += m[i]

    else:
        # negative dates
        
        for y in range(-1, (year - 1), -1):
            if abs(y) % 19 in leap_years_bi:
                hashanah -= yearlen13
            else:
                hashanah -= yearlen12

        if abs(year) % 19 in leap_years_bi:
            next_hashanah = hashanah + yearlen13
        else:
            next_hashanah = hashanah + yearlen12

        next_year = year + 1
        rosh = floor(hashanah)
        next_rosh = floor(next_hashanah)
        
        molad = hashanah % 1
        next_molad = next_hashanah % 1

        days = rosh
        m = YEARTYPE[next_rosh - rosh]

        for i in m.keys():
            if i == month:
                days += day - 1
                break
            else:
                days += m[i]
        days = int(days)

    return(days)

def fromjd(jday):
    """Convert a Julian day to a date in the Jewish calendar."""
    jday = int(jday)
    day = 0
    month = ""
    year = 0

    hashanah = molad_prime

    if jday >= floor(molad_prime):
        # positive dates

        current = False

        while current == False:
            year += 1
            if year % 19 in leap_years_ai:
                y = yearlen13
            else:
                y = yearlen12
                
            if jday - hashanah < y:
                current = True
            else:
                hashanah += y

        # now we have the current year, and hashanah gives the molad of Nisan
        if year % 19 in leap_years_ai:
            next_hashanah = hashanah + yearlen13
        else:
            next_hashanah = hashanah + yearlen12

        next_year = year + 1

        rosh = int(hashanah)
        molad = hashanah % 1

        next_rosh = int(next_hashanah)
        next_molad = next_hashanah % 1

        delta = jday - rosh + 1
        m = YEARTYPE[next_rosh - rosh]
        if delta <= 0:
            year -= 1
            month = "Elul"
            day = 29 + delta
        else:
            for i in m.keys():
                if delta <= m[i]:
                    month = i
                    day = delta
                    break
                else:
                    delta -= m[i]


    else:
        # negative dates
        while hashanah > jday:
            year -= 1
            if abs(year) % 19 in leap_years_bi:
                hashanah -= yearlen13
            else:
                hashanah -= yearlen12

        # This gives us the exact year, and hashanah gives the exact moment of the molad of Tishri for year
        next_year = year + 1

        if abs(year) % 19 in leap_years_bi:
            next_hashanah = hashanah + yearlen13
        else:
            next_hashanah = hashanah + yearlen12

        rosh = floor(hashanah)
        molad = hashanah % 1

        next_rosh = floor(next_hashanah)
        next_molad = next_hashanah % 1

        m = YEARTYPE[next_rosh - rosh]
        delta = jday - rosh + 1

        if jday == next_rosh:
            day = 1
            month = "Tishrei"
            year += 1
        elif delta <= 0:
            year -= 1
            month = "Elul"
            day = 29 + delta
        else:
            for i in m.keys():
                if delta <= m[i]:
                    month = i
                    day = delta
                    break
                else:
                    delta -= m[i]

    return (day,month,year)
