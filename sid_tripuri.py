#!/usr/bin/python3

# A programme to convert between Julian Days and dates in the sidereal Tripuri

from fractions import Fraction
from math import floor, ceil
from solun import indian_spos as spos, sankranti, sid_year, rasi, dayof_hindi as dayof
from months import INDIAN_SOLAR_NUM as MONTHNO, NUM_INDIAN_SOLAR as NUMON

epoch = sankranti(1937753 - (3 * sid_year), 0)

def fromjd(jday):
    '''Given a Julian Day, compute a date in the sidereal Tripuri calendar'''
    jday = Fraction(jday)

    # get the year
    year = (jday - epoch) // sid_year
    bisu = epoch + (year * sid_year)
    while (dayof(sankranti((bisu + sid_year), 0)) <= jday):
        year += 1
        bisu += sid_year
    while (dayof(sankranti(bisu, 0)) > jday):
        year -= 1
        bisu -= sid_year

    # get the month
    cigra = int(spos(jday) // 30) # star sign we're in
    angle = cigra * 30 # zodiacal angle of the sun at saṁkrānti
    while (dayof(sankranti((bisu + ((cigra + 1) * rasi)), (angle + 30))) <= jday):
        cigra += 1
        angle += 30
    while (dayof(sankranti((bisu + (cigra * rasi)), angle)) > jday):
        cigra -= 1
        angle -= 30
    month = MONTHNO[cigra]

    # get the day
    day = jday - dayof(sankranti(jday, angle)) + 1

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a date in the sidereal Tripuri calendar to a Julian Day'''
    day = int(day)
    month = str(month)
    year = int(year)

    # get the number of the month
    cigra = NUMON[month]
    angle = cigra * 30 # zodiacal angle of the onset of the star sign corresponding to the given month

    jday = epoch + (year * sid_year)
    jday = sankranti((jday + (cigra * rasi)), angle)
    jday = dayof(jday) + day - 1

    return jday
