#!/usr/bin/python3

#
# Convert between the Seleucid Macedonian calendar and Julian Day
#

from fractions import *
from math import floor

leap_years_ag = (4,7,9,12,15,18,1)
leap_years_bg = (19,0,2,5,8,11,13,16)

monlen = 29 + Fraction(12,24) + Fraction(44,1440) + Fraction(28,864000)
year12 = 12 * monlen
year13 = 13 * monlen
cycle19 = 235 * monlen

epoch = 1607743 + Fraction(14107, 17280) + Fraction(1,4) # Time of first noumenia of the calendar, Iran Standard
                                                         # Time, starting the day at 18:00

MONTHS_NORMAL = ("Dios", "Apellaiios", "Audunaios", "Peritios", "Dystros", "Xanthikos", "Artemisios", "Daisios", "Panamos", "Lōios", "Gorpiaios", "Hyperberetaios")
MONTHS_LEAP = ("Dios", "Apellaiios", "Audunaios", "Peritios", "Dystros", "Xanthikos", "Xandikos Embolimos", "Artemisios", "Daisios", "Panamos", "Lōios", "Gorpiaios", "Hyperberetaios")
MONTHS_18 = ("Dios", "Apellaiios", "Audunaios", "Peritios", "Dystros", "Xanthikos", "Artemisios", "Daisios", "Panamos", "Lōios", "Gorpiaios", "Hyperberetaios", "Hyperberetaios Embolimos")

def tojd(day,month,year):
    """Convert a Seleucid date to a Julian Day."""
    day = int(day)
    month = month
    year = int(year)

    jday = epoch

    if year > 0:
        # positive years
        if month == "Hyperberetaios Embolimos":
            if year % 19 != 18:
                month = "Hyperberetaios"

        if month == "Xandikos Embolimos":
            if year % 19 not in (1,4,7,9,12,15):
                month = "Xanthikos"

        y = 1
        cycles = (year - y) // 19
        y += (19 * cycles)
        noumenia = epoch + (cycles * cycle19)

        while y < year:
            if y % 19 in leap_years_ag:
                noumenia += year13
            else:
                noumenia += year12
            y += 1

        # jday is now the new moon on which the year begins
        if year % 19 == 18:
            m = MONTHS_18
        elif year % 19 in leap_years_ag:
            m = MONTHS_LEAP
        else:
            m = MONTHS_NORMAL

    else:
        # negative years
        if month == "Hyperberetaios Embolimos":
            if abs(year) % 19 != 2:
                month =	"Hyperberetaios"

        if month == "Xandikos Embolimos":
            if abs(year) % 19 not in (19,0,5,8,11,13,16):
                month =	"Xanthikos"

        y = 0
        cycles = (y - year) // 19
        y -= (19 * cycles)
        noumenia = epoch - (cycle19 * cycles)
        while y > year:
            y -= 1
            if abs(y) % 19 in leap_years_bg:
                noumenia -= year13
            else:
                noumenia -= year12

        if abs(year) % 19 == 2:
            m = MONTHS_18
        elif abs(year) in leap_years_bg:
            m = MONTHS_LEAP
        else:
            m = MONTHS_NORMAL

    jday = noumenia
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

    curryear = False

    if jday >= int(epoch):
        # positive dates
        year += 1
        cycles = (jday - epoch) // cycle19
        year += (19 * cycles)
        noumenia = epoch + (cycle19 * cycles)
        
        while curryear == False:
            if year % 19 in leap_years_ag:
                next_noumenia = noumenia + year13
            else:
                next_noumenia = noumenia + year12
                
            if floor(jday) < floor(next_noumenia):
                curryear = True
            else:
                year += 1
                noumenia = next_noumenia

        if year % 19 == 18:
            m = MONTHS_18
        elif year % 19 in leap_years_ag:
            m = MONTHS_LEAP
        else:
            m = MONTHS_NORMAL

    else:
        # negative dates

        cycles = (epoch - jday) // cycle19
        year -= (19 * cycles)
        noumenia = epoch - (cycle19 * cycles)

        while floor(jday) < floor(noumenia):
            year -= 1
            if abs(year) % 19 in leap_years_bg:
                noumenia -= year13
            else:
                noumenia -= year12

        if abs(year) % 19 == 2:
            m = MONTHS_18
        elif (abs(year) % 19) in leap_years_bg:
            m = MONTHS_LEAP
        else:
            m = MONTHS_NORMAL

    newmoon = noumenia
    nextmoon = newmoon + monlen
    
    for i in m:
        if floor(jday) < floor(nextmoon):
            month = i
            day = floor(jday) - floor(newmoon) + 1
            break
        else:
            newmoon += monlen
            nextmoon += monlen

    return (day, month, year)

