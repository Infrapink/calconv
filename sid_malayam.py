#!/usr/bin/python

# Convert between the tradition Indian solar calendar and Julian Day, dating from the start of the Kali Yuga, using methods described in the Sūrya Siddhānta

# When reading the comments, Indian days run from sunset to sunset, and Roman days run from midnight to midnight.

from fractions import Fraction
from math import floor, ceil
from surya_siddhanta import ky, sunset, sankranti, t_sid_year as sid_year, t_rasi as rasi, dayof_sunset as dayof
from months import INDIAN_SOLAR_NUM as MONTHNO, NUM_INDIAN_SOLAR as NUMON

epoch = ky + (3926 * sid_year) + (4 * rasi) # add 4 rasi because they year starts in Siṃha

def fromjd(jday):
    '''Convert a Julian Day into a date in the traditional Malayam calendar'''
    jday = Fraction(jday) # Julian Day we are interested in

    # compute the year
    year = (jday - epoch) // sid_year
    simha = epoch + (year * sid_year) # 1st-order estimate of the time of Siṃha Saṃkrānti
    while (dayof(sankranti((simha + sid_year), 120)) <= jday):
        simha += sid_year
    while (dayof(sankranti(simha, 120)) > jday):
        simha -= sid_year

    # sankranti(simha, 120) is the exact time of Siṃha Saṃkrānti
    cigra = (jday - simha) // rasi # how many star signs has the sun traversed since Siṃha Saṃkrānti?
    angle = 30 * ((cigra + 4) % 12) # zodiacal angle of the cusp of the current star sign. Add 4 and mod 12 to account for the fact that Siṃha is the 5th star sign (4th if you start counting from 0 instead of 1)

    while (dayof(sankranti((simha + (cigra * rasi)), angle)) > jday):
        # current sankranti is later than jday
        cigra -= 1
        angle = (angle - 30) % 360
    while (dayof(sankranti((simha + ((cigra + 1) * rasi)), ((angle + 30) % 360))) <= jday):
        # there is a sankranti between the current one and jday
        cigra += 1
        angle = (angle + 30) % 360

    month = MONTHNO[(cigra + 4) % 12]

    day = jday - dayof(sankranti((simha + (cigra * rasi)), angle)) + 1

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a date in the traditional Malayam calendar into a Julian Day'''
    day = int(day)
    month = str(month)
    year = int(year)

    cigra = (NUMON[month] - 4) % 12 # number of the month; subtract 4 and mod 12 to account for the fact that Siṃha is the 5th sign of the zodiac, or 4th if you start counting from 0 instead of 1
    angle = 30 * ((cigra + 4) % 12) # zodiacal angle at which the month begins
    

    jday = dayof(sankranti((epoch + (year * sid_year) + (((cigra * rasi) - 4) % 12)), angle)) + day - 1
    return jday
