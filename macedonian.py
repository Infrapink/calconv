#!/usr/bin/python

#
# Convert between the Macedonian calendar and Julian Day
#

from months import *
from fractions import *
from math import floor, ceil

MONTHS_NORMAL = ("Dios", "Apellaiios", "Audunaios", "Peritios", "Dystros", "Xanthikos", "Artemisios", "Daisios", "Panamos", "Lōios", "Gorpiaios", "Hyperberetaios")
MONTHS_LEAP = ("Dios", "Apellaiios", "Audunaios", "Peritios", "Dystros", "Xanthikos", "Xandikos Embolimos", "Artemisios", "Daisios", "Panamos", "Lōios", "Gorpiaios", "Hyperberetaios")
MONTHS_18 = ("Dios", "Apellaiios", "Audunaios", "Peritios", "Dystros", "Xanthikos", "Artemisios", "Daisios", "Panamos", "Lōios", "Gorpiaios", "Hyperberetaios", "Hyperberetaios Embolimos")

monlen = 29 + Fraction(12,24) + Fraction(44,1440) + Fraction(28,864000)
eqlen = 365 + Fraction(5,24) + Fraction(48,1440) + Fraction(45,86400)

year12 = 12 * monlen
year13 = 13 * monlen
cycle235 = 235 * monlen
cycle19 = 19 * eqlen

lunar_epoch = 1598617 + Fraction(427549,432000)
solar_epoch = 1598604 + Fraction(26077,86400)

def tojd(day, month, year):
    """Convert a date in the Macedonian calendar to a Julian Day."""
    day = int(day)
    month = month
    year = int(year)

    curryear = False

    if year >= 0:
        # positive dates
        equinox = ((year - 1) * eqlen) + solar_epoch
        lunations = (equinox - lunar_epoch) // monlen
        jday = (lunations * monlen) + lunar_epoch
        while jday < equinox:
            jday += monlen

        # jday is now Noumenia of Dios in the year in question. Is the year in question a leap year?

        if jday + year12 <= equinox + eqlen:
            # leap year
            if year % 19 == 18:
                m = MONTHS_18
            else:
                m = MONTHS_LEAP
        else:
            # not a leap year
            m = MONTHS_NORMAL

        if month not in m:
            if month == "Xandikos Embolimos":
                month = "Xandikos"
            elif month == "Hyperberetaios Embolimos":
                month = "Hyperberetaios"

    else:
        # negative years
        equinox = (year * eqlen) + solar_epoch
        lunations = (lunar_epoch - equinox) // monlen
        jday = lunar_epoch - (lunations * monlen)
        while jday - equinox > monlen:
            jday -= monlen

        # jday is now Noumenia of Dios of the year in questino. Is it a leap year?

        if jday + year12 <= equinox + eqlen:
            # leap year
            if abs(year % 19) == 2:
                m = MONTHS_18
            else:
                m = MONTHS_LEAP
        else:
            # not a leap year
            m = MONTHS_NORMAL

        if month not in m:
            if month == "Xandikos Embolimos":
                month = "Xandikos"
            elif month == "Hyperberetaios Embolimos":
                month = "Hyperberetaios"

    for i in m:
        if i == month:
            jday = floor(jday) + day - 1
            break
        else:
            jday += monlen
            
    return jday

def fromjd(jday):
    """Convert a Julian Day to a date in the Macedonian calendar"""
    jday = int(jday)

    day = 0
    month = ""
    year = 0

    curryear = False
    equinox = solar_epoch
    noumenia = lunar_epoch
    metonic = 0

    if jday >= int(lunar_epoch):
        # positive dates
        year = 1

        while curryear == False:
            next_equinox = equinox + eqlen
            if noumenia + year12 < next_equinox:
                next_noumenia = noumenia + year13
                metonic += 1
            else:
                next_noumenia = noumenia + year12

            if jday < int(next_noumenia):
                curryear = True
            else:
                year += 1
                equinox = next_equinox
                noumenia = next_noumenia

        # check if it's a leap year
        if (noumenia + year12) < (equinox + eqlen):
            # leap year
            if metonic % 6 == 0:
                m = MONTHS_18
            else:
                m = MONTHS_LEAP
        else:
            # not a leap year
            m = MONTHS_NORMAL

    else:
        # negative dates
        while noumenia > jday:
            year -= 1
            equinox -= eqlen

            if noumenia - year13 > equinox:
                noumenia -= year13
            else:
                noumenia -= year12

        # right, now what type of year is it?

        nexteq = equinox + eqlen
        if noumenia + year12 < nexteq:
            # leap year
            if abs(year) % 19 == 2:
                m = MONTHS_18
            else:
                m = MONTHS_LEAP
        else:
            # not a leap year
            m = MONTHS_NORMAL

    newmoon = noumenia
    nextmoon = newmoon + monlen
        
    for i in m:
        if jday < floor(nextmoon):
            month = i
            day = floor(jday) - floor(newmoon) + 1
            #if jday < 0:
             #   day += 1
            break
        else:
            newmoon += monlen
            nextmoon += monlen

    return (day, month, year)
