#!/usr/bin/python

#
# Convert a date in the Hebrew calendar to a Julian day.
#

import months
from fractions import *
import julian_day_conversions

def convert(day,month,year):
    day = int(day)
    month = month.title()
    year = int(year)
    days = 0

    leap_years_ai = (3,6,8,11,14,17,19,0)
    leap_years_bi = (1,3,6,9,12,14,17)
    leap_years_zo = (0,2,5,8,11,13,16)

    monlen = 29 + Fraction(12,24) + Fraction(793,25920)
    yearlen12 = 12 * monlen
    yearlen13 = 13 * monlen
    cycle19 = 235 * monlen

    molad0 = Fraction(11,24) + Fraction(451,25920)

    if year > 0:
        # positive dates
        if month == "Veadar":
            if (year % 19) not in leap_years_ai:
                month = "Adar"

        for y in range(1,year):
            if (y % 19) in leap_years_ai:
                days += yearlen13
            else:
                days += yearlen12

        days = int(days + 1122908 + molad0)
        if (year % 19) in leap_years_ai:
            m = months.SAMARITAN_MONTHS_LEAP
        else:
            m = months.SAMARITAN_MONTHS_NORMAL

        for i in m.keys():
            if i == month:
                days += day + 1
                break
            else:
                days += m[i]

        test = julian_day_conversions.samaritan(days)
        if test[0] != day:
            days -= 1

    else:
        # negative dates
        if month == "Veadar":
            if (abs(year) % 19) not in leap_years_bi:
                month = "Adar"

        if (abs(year) % 19) in leap_years_bi:
            m = months.SAMARITAN_MONTHS_LEAP
        else:
            m = months.SAMARITAN_MONTHS_NORMAL
            
        for i in m.keys():
            if i == month:
                days += day
                break
            else:
                days += m[i]
                
        for y in range(0, abs(year)):
            if (y % 19) in leap_years_zo:
                days -= yearlen13
            else:
                days -= yearlen12

        days = int(days + molad0 + 1122909)
        test = julian_day_conversions.samaritan(days)
        if test[0] != day:
            days -= 1

    return days
