#!/usr/bin/python3

# A programme to convert between Julian Days and dates in the modern Indian sidereal calendar (Śaka era)

from fractions import Fraction
from math import floor, ceil
from solun import indian_spos as spos, sankranti, indian_sunrise as sunrise, indian_sunset as sunset, sid_year, rasi
from surya_siddhanta import ky
from months import INDIAN_SOLAR_NUM as MONTHNO, NUM_INDIAN_SOLAR as NUMON

epoch = ky + (3179 * sid_year) - Fraction(11,48) # ensure epoch is given in IST

def dayof(jday):
    '''Determine the day which begins within an astronomical even'''
    # if the sun is already in a star sign at sunrise, the month is that star sign
    # if the sun enters a sign after rising, the day belongs to the previous sign
    jday = Fraction(jday)

    if (sunrise(jday) <= (jday % 1)):
        ans = floor(jday)
    else:
        ans = ceil(jday)

    return ans

def fromjd(jday):
    '''Given a Julian Day, compute a date in the modern Indian sidereal solar'''
    jday = Fraction(jday)

    # get the year
    year = (jday - epoch) // sid_year
    mesha = epoch + (year * sid_year)
    while (dayof(sankranti((mesha + sid_year), 0)) <= dayof(jday)):
        year += 1
        mesha += sid_year
    while (dayof(sankranti(mesha, 0)) > dayof(jday)):
        year -= 1
        mesha -= sid_year

    # get the month
    cigra = spos(jday) // 30 # star sign we're in
    angle = cigra * 30 # zodiacal angle of the sun at saṁkrānti
    while (dayof(sankranti((mesha + ((cigra + 1) * rasi)), (angle + 30))) <= dayof(jday)):
        cigra += 1
        angle += 30
    while (dayof(sankranti((mesha + (cigra * rasi)), angle)) > dayof(jday)):
        cigra -= 1
        angle -= 30
    month = MONTHNO[cigra]

    # get the day
    day = jday - dayof(sankranti(jday, angle)) + 1

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a date in the modern Indian sidereal calendar to a Julian Day'''
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
