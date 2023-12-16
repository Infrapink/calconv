#!/usr/bin/python

# Convert between the traditional Bengali calendar and Julian Day

# When reading the comments, Indian days run from sunrise to sunrise, and Roman days run from midnight to midnight.

from fractions import Fraction
from math import floor, ceil
from surya_siddhanta import sunrise, sankranti, t_sid_year as sid_year, t_rasi as rasi, dayof_sunrise as dayof
from months import BENGALI_NUM as MONTHNO, NUM_BENGALI as NUMON

epoch = sankranti(1937753, 0)

def fromjd(jday):
    '''Convert a Julian Day into a date in the Bengali calendar'''
    jday = Fraction(jday) # Julian Day we are interested in

    # compute the year
    year = (jday - epoch) // sid_year
    pohela = epoch + (year * sid_year) # estimated time of Pohela Boisak
    while (dayof(sankranti((pohela + sid_year), 0)) <= jday):
        pohela += sid_year
        year += 1
    while (dayof(sankranti(pohela, 0)) > jday):
        pohela -= sid_year
        year -= 1

    # compute the month
    cigra = (jday - sankranti(pohela, 0)) // rasi # number of the zodiacal month, starting from 0
    angle = cigra * 30 # solar zodiacal longitude, in degrees
    while (dayof(sankranti(pohela + ((cigra + 1) * rasi), (angle + 30))) <= jday):
        cigra += 1
        angle += 30
    while (dayof(sankranti((pohela + (cigra * rasi)), angle)) > jday):
        cigra -= 1
        angle -= 30
    month = MONTHNO[cigra]

    # compute the day
    day = jday - dayof(sankranti((pohela + (rasi * cigra)), angle)) + 1

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a date in the Bengali calendar into a Julian Day'''
    day = int(day)
    month = str(month)
    year = int(year)

    cigra = NUMON[month] # number of the month, starting from 0
    angle = 30 * cigra # zodiacal angle at which the month begins

    jday = dayof(sankranti((epoch + (year * sid_year) + (cigra * rasi)), angle)) + day - 1
    return jday
