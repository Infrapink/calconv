#!/usr/bin/python3

# A programme to convert between Julian Days and dates in the traditional Malayam, using modern techniques and observations

# When reading these comments:
## Malayam days start at sunset
## Roman days start at midnight
## Ordinal numbers go 0th, 1st, 2nd, etc

from fractions import Fraction
from solun import sid_year, rasi, dayof_kerala as dayof, sankranti
from surya_siddhanta import ky
from months import INDIAN_SOLAR_NUM as MONTHNO, NUM_INDIAN_SOLAR as NUMON

epoch = ky + (3926 * sid_year) + (4 * rasi) # add 4 rasi because the year starts in Siṃha

def fromjd(jday):
    '''Convert a Julian Day into a date in the observational Malayam calendar'''
    jday = Fraction(jday) # Julian Day we are interested in

    # compute the year
    year = (jday - epoch) // sid_year
    simha = epoch + (year * sid_year) # 1st-order estimate of the time of Siṃha Saṃkrānti
    while (dayof(sankranti((simha + sid_year), 120)) <= jday):
        simha += sid_year
    while (dayof(sankranti(simha, 120)) > jday):
        simha -= sid_year

    # compute the month
    cigra = (jday - simha) // rasi # number of star signs the sun has traversed since Siṃha Saṃkrānti
    angle = 30 * ((cigra + 4) % 12) # zodiacal angle of the cusp of the rasi that the sun is in. add 4 and mod 12 to account for the fact that Siṃha is the 4th rasi
    while (dayof(sankranti((simha + (cigra * rasi)), angle)) > jday):
        # current saṃkrānti is later than jday
        cigra -= 1
        angle = (angle - 30) % 360
    while (dayof(sankranti((simha + ((cigra + 1) * rasi)), ((angle + 30) % 360))) <= jday):
        # There is at least one saṃkrānti between the current one and jday
        cigra += 1
        angle = (angle + 30) % 360
    month = MONTHNO[(cigra + 4) % 12]

    # compute the day
    day = jday - dayof(sankranti((simha + (cigra * rasi)), angle)) + 1

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a date in the observational Malayam calendar into a Julian Day'''
    day = int(day)
    month = str(month)
    year = int(year)

    cigra = (NUMON[month] - 4) % 12 # number of the rasi we're currently in; subtract 4 and mod 12 to account for the fact that Siṃha is the 4th zodiac sign
    angle = 30 * ((cigra + 4) % 12) # zodiacal angle of the cusp of the specified star sign

    jday = day + dayof(sankranti((epoch + (year * sid_year) + (cigra * rasi)), angle)) - 1
    return jday
