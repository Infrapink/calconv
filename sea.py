#!/usr/bin/python

# A collection of useful constants and functions found in southeast Asian calendars

from fractions import Fraction
from math import floor, ceil

sid_year = Fraction(292207, 800) # sidereal year
rasi = Fraction(sid_year, 12) # rasi
chulasakarat = 1954168 + Fraction(373, 800) # chulasakarat
#southeast_asian_synodic_month = southeast_asian_rasi * Fraction(912,940)
syn_month = 30 * Fraction(692, 703) # synodic month

def lunar_figures(year):
    '''Compute lunar figures relating to the current solar new year'''
    year = int(year)

    songkran = chulasakarat + (year * sid_year) # solar new year
    t = songkran - floor(chulasakarat)
    ahargana = ceil(t) # Eade 6.1
    k = t % 1 # inverse of the kammacubala; Eade 6.2
    tithis = (ahargana * Fraction(11,692)) + Fraction(650,692) # Eade 6.4
    avoman = tithis % 1 # Eade 6.4
    masaken = Fraction( (floor(tithis) + 0 + ahargana), 30) # total elapsed months
    darkmoon = songkran - (syn_month * (masaken % 1))
    newmoon = ceil(darkmoon)

    return(newmoon, k, avoman)

def lny(year):
    '''Compute the new moon preceding a given solar new year'''
    year = int(year)

    curr_moon = lunar_figures(year)
    next_moon = lunar_figures(year + 1)
    prev_moon = lunar_figures(year - 1)

    if (next_moon[0] - curr_moon[0] > 380):
        # leap year
        year_length = 384
        newmoon = curr_moon[0]
    elif (curr_moon[0] - prev_moon[0] == 385):
        # last year would have had a leap day but it was a leap year, and so the leap day is added to this year
        year_length = 355
        newmoon = curr_moon[0] - 1
    elif ( (curr_moon[1] >= Fraction(593,800)) or (curr_moon[2] <= Fraction(126,692)) ):
        # long year
        year_length = 355
        newmoon = curr_moon[0]
    else:
        # normal year
        year_length = 354
        newmoon = curr_moon[0]


    return(year_length, newmoon)
