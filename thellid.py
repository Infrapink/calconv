#!/usr/bin/python

#
# Convert between the Thellid calendar and Julian DAy
#

import months
from fractions import *

yearlen = 365 + Fraction(5,24) + Fraction(48,1440) + Fraction(45,86400)
day0 = Fraction(-83419488409, 43200) - yearlen # based on taking the southern solstice moment for 2020 AD and subtraction 12020 * yearlen
day1 = 2375839 + Fraction(36877,86400)

YEARTYPE = {365: months.THELLID_NORMAL,
            366: months.THELLID_LEAP}

def tojd(day,month,year):
    """Convert a date in the French Republican calendar into a Julian day."""
    day = int(day)
    month = month
    year = int(year)

    days = 0
    equinox = day0
    nexteq = equinox + yearlen

    if year >= 0:
        for y in range(0, year):
            yeartype = int(nexteq) - int(equinox)
            days += yeartype
            equinox += yearlen
            nexteq += yearlen

        m = YEARTYPE[int(nexteq) - int(equinox)]
        for i in m.keys():
            if i == month:
                days += day# - 1
                break
            else:
                days += m[i]

    else:
        equinox -= yearlen
        nexteq -= yearlen
        for y in range (0, year, -1):
            if equinox < 0 and nexteq > 0:
                yeartype = int(nexteq) - int(equinox - 1)
            else:
                yeartype = int(nexteq) - int(equinox)
            days -= yeartype
            equinox -= yearlen
            nexteq -= yearlen

        if equinox < 0 and nexteq > 0:
            m = YEARTYPE[int(nexteq) - int(equionx - 1)]
        else:
            m = YEARTYPE[int(nexteq) - int(equinox)]

        for i in m.keys():
            if i == month:
                days += day# - 1
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
    equinox = day0
    nexteq = day0 + yearlen
    
    if jday >= int(day0):
        # positive dates
        delta = jday - int(day0)# + 1 # number of days since southward equinox of year 0
        while current == False:
            ytype = int(nexteq) - int(equinox)
            if delta <= ytype:
                current = True
            else:
                year += 1
                delta -= ytype
                equinox += yearlen
                nexteq += yearlen

#        if delta == 0:
 #           year -= 1
  #          equinox -= yearlen
   #         nexteq -= yearlen
    #        delta = int(nexteq) - int(yearlen)
            
        m = YEARTYPE[int(nexteq) - int(equinox)]

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    else:
        # negative dates
        delta = int(day0) - jday
        while current == False:
            year -= 1
            equinox -= yearlen
            nexteq -= yearlen
            ytype = int(nexteq) - int(equinox)
            #
            # THIS BIT MIGHT CAUSE A BUG
            # 
            if equinox < 0 and nexteq > 0:
                ytype += 1
            #
            # THIS BIT MIGHT CAUSE A BUG
            #
            if delta <= ytype:
                current = True
            else:
                delta -= ytype

        m = YEARTYPE[int(nexteq) - int(equinox)]
        delta = int(nexteq) - int(equinox) - delta# + 1
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    return (day, month, year)
