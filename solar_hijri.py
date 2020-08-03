#!/usr/bin/python

#
# Convert between the French Republican calendar and Julian DAy
#

import months
from fractions import *

yearlen = 365 + Fraction(5,24) + Fraction(48,1440) + Fraction(45,86400)
day1 = 1948319 + Fraction(31379,43200)

YEARTYPE = {365: months.IRANIAN_NORMAL,
            366: months.IRANIAN_LEAP}

def tojd(day,month,year):
    """Convert a date in the French Republican calendar into a Julian day."""
    day = int(day)
    month = month
    year = int(year)

    days = 0
    equinox = day1
    nexteq = equinox + yearlen

    if year >= 1:
        for y in range(1, year):
            yeartype = int(nexteq) - int(equinox)
            days += yeartype
            equinox += yearlen
            nexteq += yearlen

        if equinox % 1 > Fraction(1,2):
            nowruz = int(equinox) + 1
        else:
            nowruz = int(equinox)

        if nexteq % 1 > Fraction(1,2):
            nextnowruz = int(nexteq) + 1
        else:
            nextnowruz = int(nexteq)

        m = YEARTYPE[nextnowruz - nowruz]
        for i in m.keys():
            if i == month:
                days += day - 1
                break
            else:
                days += m[i]

    else:
        # negative years
        equinox -= yearlen
        nexteq -= yearlen
        for y in range (0, year, -1):
#            equinox -= yearlen
 #           nexteq -= yearlen
            if equinox % 1 > Fraction(1,2):
                nowruz = int(equinox) + 1
            else:
                nowruz = int(equinox)

            if nexteq % 1 > Fraction(1,2):
                nextuz = int(nexteq) + 1
            else:
                nextuz = int(nexteq)
                
            if nowruz < 0 and nextuz > 0:
                yeartype = nextuz - nowruz - 1
            else:
                yeartype = nextuz - nowruz
            days -= yeartype
            equinox -= yearlen
            nexteq -= yearlen

        if equinox % 1 > Fraction(1,2):
            nowruz = int(equinox) + 1
        else:
            nowruz = int(equinox)

        if nexteq % 1 > Fraction(1,2):
            nextnowruz = int(nexteq) + 1
        else:
            nextnowruz = int(nexteq)

        if nowruz < 0 and nextnowruz > 0:
            m = YEARTYPE[nextnowruz - nowruz + 1]
        else:
            m = YEARTYPE[nextnowruz - nowruz]

        for i in m.keys():
            if i == month:
                days += day
                break
            else:
                days += m[i]

    days += int(day1)
    return days

def fromjd(jday):
    """Convert a Julian day to a date in the French Republican calendar."""
    day = 0
    month = ""
    year = 0
    
    jday = int(jday)
    current = False
    equinox = day1
    nexteq = day1 + yearlen
    
    if jday >= int(day1):
        # positive dates
        delta = jday - int(day1) + 1 # number of days since southward equinox of year 0
        while current == False:
            year += 1
            ytype = int(nexteq) - int(equinox)
            if delta <= ytype:
                current = True
            else:
                delta -= ytype
                equinox += yearlen
                nexteq += yearlen


        if equinox % 1 > Fraction(1,2):
            nowruz = int(equinox) + 1
        else:
            nowruz = int(equinox)

        if nexteq % 1 > Fraction(1,2):
            nextnowruz = int(nexteq) + 1
        else:
            nextnowruz = int(nexteq)
            
        m = YEARTYPE[nextnowruz - nowruz]

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    else:
        # negative dates
        while int(equinox) >= jday:
            year -= 1
            equinox -= yearlen

        # So now we have the year and the exact moment of the equinox
        nexteq = equinox + yearlen
#        print(equinox, equinox % 1)
 #       print(nexteq, nexteq % 1)

        if equinox % 1 > Fraction(1,2):
            nowruz = int(equinox) + 1
        else:
            nowruz = int(equinox)

        if nexteq % 1 > Fraction(1,2):
            nextuz = int(nexteq) + 1
        else:
            nextuz = int(nexteq)

        #print(nextuz - nowru)
        ytype = nextuz - nowruz
        if nowruz < 0:
            delta = jday - nowruz
        else:
            delta = jday - nowruz + 1
            
        if delta > ytype:
            delta -= ytype
            year += 1
            
        if nowruz < 0 and nextuz > 0:
            m = YEARTYPE[nextuz - (nowruz - 1)]
        else:
            m = YEARTYPE[nextuz - nowruz]
        #print(delta)
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    return (day, month, year)
