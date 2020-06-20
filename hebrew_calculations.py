#!/usr/bin/python

#
# This does various calculations involved in the Hebrew calendar.
# Splitting it off like this is necessary because the algorithm
# always turns up the correct moment for the molad of Tishri
# in the year being examined, but for some reason consistently
# gives the wrong molad of Tishri for the next year if the
# current year is a leap year.

from fractions import *

def calc(jday):
    leap_years_am = (3,6,8,11,14,17,19,0)
    leap_years_bc = (1,3,6,9,12,14,17)
    leap_years_zo = (0,2,5,8,11,13,16)
    
    monlen = 29 + Fraction(12,24) + Fraction(793, (24 * 1080)) # formal mean synodic month length
    yearlen12 = 12 * monlen # length of a 12-month year
    yearlen13 = 13 * monlen # length of a 13-month year
    cycle19 = 235 * monlen
    molad_tohu = Fraction(5,24) + Fraction(204,(24 * 1080))
    
    day = 0
    month = ""
    year = 0

    if jday > 347996:
        # positive dates
        delta = jday - 347996
        cycles = 0

        # First, let's see how many 19-yaer cycles have passed
        while delta > cycle19:
            cycles += 1
            delta -= cycle19

        # Now let's get the number of whole years that have passed
        for y in range(0,19):
            y += 1
            if y in leap_years_am:
                if delta <= yearlen13:
                    single_years = y
                    break
                else:
                    delta -= yearlen13
            else:
                if delta <= yearlen12:
                    single_years = y
                    break
                else:
                    delta -= yearlen12

        # delta now gives us the exact position in the current year.
        rosh = int(jday - delta + molad_tohu) + 1 # add 1 to avoid a fencepost error

        # Work out the molad of Tishri
        days = 235 * monlen * cycles
        for z in range(1, single_years):
            if z in leap_years_am:
                days += yearlen13
            else:
                days += yearlen12
        molad = (days % 1) + molad_tohu
        if molad >= 1:
            molad -= 1

        year = (19 * cycles) + y

        # Is it a leap year?
        if year in leap_years_am:
            leap = True
        else:
            leap = False

        # So to recap:
        # delta is the current position within the year
        # rosh  is the Julian Day on which the molad of Tishri falls
        # molad is the moment of the molad of Tishri
        # year  is the current year number
        # leap  tells us whether or not it's a leap year

    else:
        # negative dates
        delta = 347997 - jday
        cycles = 0
        flag = False

        # Unlike the other algorithms, this one is going to work with negative numbers a lot.

        # calculate the year
        while flag == False:
            year += 1
            if (year % 19) in leap_years_bc:
                if delta < yearlen13:
                    flag = True
                else:
                    delta -= yearlen13
            else:
                if delta < yearlen12:
                    flag = True
                else:
                    delta -= yearlen12

        # year now gives us the current year

        # calculate the molad of Tishri and the date on which it falls
        position = 347997 + molad_tohu
        for y in range(0, year):
            if (y % 19) in leap_years_zo:
                position -= yearlen13
            else:
                position -= yearlen12

        rosh = int(position)
        molad = position % 1


    results = (rosh,molad,year)
    return results
