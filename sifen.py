#!/usr/bin/python3

# Convert between the Taichu calendar and Julian Day

from math import floor
from fractions import Fraction

sui = 365 + Fraction(1,4) # tropical year
yue = 29 + Fraction(499,940) # synodic month
zhongqi = sui / 12 # major solar term
nian12 = 12 * yue
nian13 = 13 * yue

MONTHS = ("Dōngyuè", "Bīngyuè", "Zōuyuè", "Xìngyuè", "Táoyuè", "Méiyuè", "Liúyuè", "Héyuè", "Lányuè", "Guìyuè", "Júyuè", "Lùyuè")

solar_epoch = Fraction(7008389, 4)
lunar_epoch = Fraction(1647269459, 940)

def getxin(solstice):
    solstice = Fraction(solstice)
    if floor(solstice) >= floor(solar_epoch):
        luns = (solstice - lunar_epoch) // yue
        moon = lunar_epoch + (luns * yue)
    else:
        luns = (lunar_epoch - solstice) // yue
        moon = lunar_epoch - (luns * yue)
        
    while floor(moon) > floor(solstice):
        moon -= yue
    while floor(moon + yue) <= floor(solstice):
        moon += yue

    prev_solstice = solstice - sui
    if floor(prev_solstice) >= floor(solar_epoch):
        luns = (prev_solstice - lunar_epoch) // yue
        prev_moon = lunar_epoch + (luns * yue)
    else:
        luns = (lunar_epoch - solstice) // yue
        prev_moon = lunar_epoch - (luns * yue)
        
    while floor(prev_moon) > floor(prev_solstice):
        prev_moon -= yue
    while floor(prev_moon + yue) <= floor(prev_solstice):
        prev_moon += yue

    if moon - prev_moon == nian12:
        # previous year was normal
        xin = prev_moon + (14 * yue)
    elif (floor(prev_moon + (2 * yue)) <= floor(solstice + zhongqi)) or (floor(prev_moon + (3 * yue)) <= floor(solstice + (2 * zhongqi))):
        # previous year was leap
        xin = prev_moon + (15 * yue)
    else:
        # previous year was normal
        xin = prev_moon + (14 * yue)

    return xin

def fromjd(jday):
    jday = int(jday)

    day = 0
    month = ""
    year = 0

    if jday >= floor(solar_epoch):
        # positice dates... probably
        orbits = (jday - solar_epoch) // sui
        year = orbits + 1
        solstice = solar_epoch + (orbits * sui)
        while floor(solstice + sui) <= jday:
            year += 1
            solstice += sui
        luns = (solstice - lunar_epoch) // yue
        solstice_moon = lunar_epoch + (luns * yue)
        while floor(solstice_moon + yue) <= floor(solstice):
            solstice_moon += yue
    else:
        # negative dates
        year = 0 - ((solar_epoch - jday) // sui)
        solstice = solar_epoch + (year * sui)
        while floor(solstice) > jday:
            year -= 1
            solstice -= sui
        luns = (lunar_epoch - solstice) // yue
        solstice_moon = lunar_epoch - (luns * yue)
        while floor(solstice_moon) > floor(solstice):
            solstice_moon -= yue

    next_solstice = solstice + sui
    prev_solstice = solstice - sui
    xin = getxin(solstice)
    next_xin = getxin(next_solstice)

    if floor(xin) > jday:
        year -= 1
        if year == 0:
            year = (-1)

        next_solstice = solstice
        next_xin = xin

        solstice = prev_solstice

        xin = getxin(solstice)

    if next_xin - xin == nian13:
        leap = True
    else:
        leap = False

    newmoon = xin
    m = 0

    if leap == False:
        # normal year
        while floor(newmoon + yue) <= jday:
            newmoon += yue
            m += 1
        month = MONTHS[m]
        day = jday - floor(newmoon) + 1
    else:
        # leap year
        leapt = False # have we past the leap month?
        st = solstice # solar term
        while floor(st) < floor(newmoon):
            st += zhongqi

        while floor(newmoon + yue) <= jday:
            if (floor(newmoon + yue) <= floor(st)) and (leapt == False):
                leapt = True
            else:
                st += zhongqi
                m += 1
            newmoon += yue

        if m == 12:
            month = "Rùnyuè"
        elif (leapt == False) and (floor(newmoon + yue) <= floor(st)):
            month = "Rùnyuè"
        else:
            month = MONTHS[m]
        
        day = jday - floor(newmoon) + 1

    return(day, month, year)

def tojd(day, month, year):
    day = int(day)
    month = str(month)
    year = int(year)

    if year == 0:
        year = (-1)

    if year > 0:
        solstice = solar_epoch + ((year - 1) * sui)
    else:
        solstice = solar_epoch + (year * sui)

    next_solstice = solstice + sui
    xin = getxin(solstice)
    next_xin = getxin(next_solstice)
    if (next_xin - xin) == nian13:
        leap = True
    else:
        leap = False

    jday = xin
    m = 0

    if leap == False:
        # normal year
        if month == "Rùnyuè":
            month = "Dōngyuè"
        while MONTHS[m] != month:
            m += 1
            jday += yue
    else:
        # leap year
        leapt = False # have we passed the leap month?
        st = solstice # major solar term
        while floor(st) < floor(jday):
            st += zhongqi

        while MONTHS[m] != month:
            if (month == "Rùnyuè") and (floor(jday + yue) <= st):
                break
            else:
                jday += yue
                if (floor(jday) < floor(st)) and (leapt == False):
                    leapt = True
                else:
                    st += zhongqi
                    m += 1

    jday = floor(jday) + day - 1

    return jday
