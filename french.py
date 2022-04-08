#!/usr/bin/python3

#
# Convert between the French Republican calendar and Julian DAy
#

import months
from fractions import *

yearlen = 365 + Fraction(5,24) + Fraction(48,1440) + Fraction(45,86400)
day0 = 2375475 + Fraction(997,5400)
day1 = 2375840 + Fraction(36877,86400)

YEARTYPE = {365: months.FRENCH_NORMAL,
            366: months.FRENCH_LEAP}

def tojd(day,month,year):
    """Convert a date in the French Republican calendar into a Julian day."""
    day = int(day)
    month = month
    year = int(year)

    days = year * yearlen
    nyd = day0 + days # New Year's Day
    next_year = nyd + yearlen
    length = int(next_year) - int(nyd)
    m = YEARTYPE[length]
    days = int(days)# - 1 # subtract 1 to fix a fencepost error
    for i in m.keys():
        if i == month:
            days += day
            break
        else:
            days += m[i]
    days += int(day0)
    return days

def fromjd(jday):
    """Convert a Julian day to a date in the French Republican calendar."""
    day = 0
    month = ""
    year = 0
    equinox = day0
    
    jday = int(jday)
    current = False
    if jday >= 2375473:
        # positive dates
        delta = jday - 2375473 # number of days since southward equinox of year 0
        print("1:", delta)
        #year += 1
        while delta > yearlen:
            year += 1
            equinox += yearlen
            delta -= yearlen
            print("2:", delta)

        next_eq = equinox + yearlen


        if int(delta) == 0:
            equinox -= yearlen
            next_eq -= yearlen
            delta = int(next_eq) - int(equinox)
            print("X:", delta)
            
        m = YEARTYPE[int(next_eq) - int(equinox)]        
        
        delta = int(delta)# + 1 # delta will be fractional
        print("3:", delta)
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                print("5:", delta)
                break
            else:
                delta -= m[i]
                print("4:", delta)

        print("Year length:", int(next_eq) - int(equinox))
    else:
        # negative dates
        delta = day1 - jday # number of days prior to southward equinox of year 0
#        year -= 1
        while delta > yearlen:
            year -= 1
            equinox -= yearlen
            delta -= yearlen

        if delta < 0:
            delta = abs(int(delta - 1))
        else:
            delta = int(delta) + 1
            

        next_eq = equinox + yearlen
        y = int(next_eq) - int(equinox)
        delta = y - delta# + 1
        m = YEARTYPE[y]
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    return (day, month, year)
