#!/usr/bin/python

# Convert between the sidereal Thai calendar and Julian Days

from math import ceil
from fractions import Fraction
from months import THAI_SID as MONTHS, THAI_SID_NUM as MONTHNO
from constants import southeast_asian_sidereal_year as sid_year, chulasakarat as epoch, southeast_asian_rasi as rasi

def fromjd(jday):
    '''Convert a Julian Day into a date in the Thai sidereal calendar'''
    jday = Fraction(jday)

    r = (jday - epoch) // rasi
    while (ceil(epoch + (r * rasi)) > jday):
        r -= 1
    while (ceil(epoch + ( (r + 1) * rasi)) <= jday):
        r += 1

    year = r // 12
    month = MONTHS[r % 12]
    day = jday - ceil(epoch + (r * rasi)) + 1 # add 1 because humans don't count from 0

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a date in the Thai sidereal calendar into a Julian Day'''
    day = int(day) - 1 # subtract 1 because computers count from 0
    month = MONTHNO[str(month)]
    year = int(year)

    ans = ceil(epoch + (year * sid_year) + (month * rasi) + day)
    return ans
