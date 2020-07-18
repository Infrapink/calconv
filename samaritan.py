#!/usr/bin/python

#
# Convert between the Samaritcan calendar and Julian day.
#

import months
from fractions import *

def tojd(day,month,year):
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
            m = months.SAMARITAN_LEAP
        else:
            m = months.SAMARITAN_NORMAL

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
            m = months.SAMARITAN_LEAP
        else:
            m = months.SAMARITAN_NORMAL
            
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
        test = fromjd(days)
        if test[0] != day:
            days -= 1

    return days

def fromjd(jday):
    """Convert a Julian Day to a date in the Samaritan calendar."""
    leap_years_ai = (3,6,8,11,14,17,19,0)
    leap_years_bi = (1,3,6,9,12,14,17)
    leap_years_zo = (0,2,5,8,11,13,16)
    monlen = 29 + Fraction(12,24) + Fraction(793, (24 * 1080))
    yearlen12 = 12 * monlen
    yearlen13 = 13 * monlen
    cycle19 = 235 * monlen
    #molad0 = Fraction(2,24) + Fraction(655,25920)
    #molad0 = Fraction(17,24) + Fraction(859,25920)
    molad0 = Fraction(11,24) + Fraction(451,25920)

    jday = int(jday)
    day = 0
    month = ""
    year = 0

    if jday > 1122908:
        # positive dates
        delta = jday - 1122908

        # First count 19-year cycles
        while delta > cycle19:
            year += 19
            delta -= cycle19

        # whole years
        for y in range(0, 19):
            y += 1
            if y in leap_years_ai:
                if delta <= yearlen13:
                    year += y
                    break
                else:
                    delta -= yearlen13
            else:
                if delta <= yearlen12:
                    year += y
                    break
                else:
                    delta -= yearlen12

        # delta now gives the exact position in the current year.
        delta = int(delta)
        if delta == 0:
            year -= 1
            if (year % 19) in leap_years_ai:
                delta = 384
            else:
                delta = 354
                
        if (year % 19) in leap_years_ai:
            m = months.SAMARITAN_LEAP
        else:
            m = months.SAMARITAN_NORMAL

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    else:
        # negative years
        delta = 1122909 - jday
        flag = False

        while flag == False:
            year -= 1
            if (abs(year) % 19) in leap_years_bi:
                if delta <= yearlen13:
                    flag = True
                else:
                    delta -= yearlen13
            else:
                if delta <= yearlen12:
                    flag = True
                else:
                    delta -= yearlen12

        # year now gives us the current year year and delta the exact position within that year.
        delta = int(delta)
        if delta == 0:
            year -= 1
#            if (abs(year) % 19) in leap_years_bi:
 #               delta = 384
  #          else:
   #             delta = 354
                
        if (abs(year) % 19) in leap_years_bi:
            m = months.SAMARITAN_LEAP
            delta = 384 - delta
        else:
            m = months.SAMARITAN_NORMAL
            delta = 354 - delta

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = (day,month,year)
    return date
