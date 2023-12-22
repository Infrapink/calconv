#!/usr/bin/python3

# A programme to convert between Julian Days and the (proposed) tropical Tripuri calendar

from fractions import Fraction
from solun import tropical_year as trop_year, solar_term, spos, trans, indian_sunrise as sunrise, dayof_hindi as dayof
from months import INDIAN_SOLAR_NUM as NUMON, NUM_INDIAN_SOLAR as MONTHNO

tz = Fraction(11,48) # Indian standard time is UTC + 5hr 30 min
epoch = trans(1936544, 270, tz) # startpoint of the calendar

def fromjd(jday):
    '''Convert a Julian Day into a date in the tropical Tripuri calendar'''
    jday = Fraction(jday) # Julian Day in question

    # compute the year
    year = (jday - epoch) // trop_year
    bisu = epoch + (year * trop_year)
    while (dayof(trans(bisu, 270, tz)) > jday):
        bisu -= trop_year
        year -= 1
    while (dayof(trans((bisu + trop_year), 270, tz)) <= jday):
        bisu += trop_year
        year += 1

    # compute the month
    m = ((spos(sunrise(jday)) // 30) - 1) % 12 # subtract 1 and mod 12 because Dhanu by convention is the 8th section of the zodiac but the 9th section of the ecliptic.
    month = NUMON[m]
    
    # compute the day
    n = (m + 4) % 12 # ordinal number of the current month, starting from the southern solstice
    angle = 30 * ((n + 9) % 12)
    day = jday - dayof(trans((bisu + (n * solar_term)), angle, tz)) + 1

    return(day, month, year)

def tojd(day, month, year):
    '''Convert a date in the tropical Tripuri calendar to a Julian Day'''
    day = int(day)
    month = str(month)
    year = int(year)

    jday = epoch + (year * trop_year)

    m = (MONTHNO[month] + 4) % 12 # ordinal number of the current month, starting from 0 at the southern solstice
    angle = 30 * ((m + 9) % 12)
    jday = dayof(trans((jday + (m * solar_term)), angle, tz)) + day - 1
    return jday
