#!/usr/bin/python3

from fractions import Fraction
from solun import dayof_hindi as dayof, solar_term as rasi, trans, tropical_year, spos, tropical_sankranti as sankranti
from surya_siddhanta import se
from months import INDIAN_LUNAR_NUM as NUMON, NUM_INDIAN_LUNAR as MONTHNO # the tropical solar calendar uses the lunar month names

tz = Fraction(11, 48) # India is 5hr 30min ahead of UTC
epoch = trans(se, (23 + Fraction(15,60)), tz)

def tojd(day, month, year):
    '''Convert a date in the tropical Indian solar calendar to Julian Day'''
    day = int(day)
    month = str(month)
    year = int(year)

    # compute Meṣa Saṃkrānti
    jday = epoch + (year * tropical_year)

    # account for months
    m = (MONTHNO[month] - 1) % 12
    jday = dayof(sankranti((jday + (m * rasi)), (m * 30))) + day - 1

    return jday

def fromjd(jday):
    '''Convert a Julian Day to a date in the tropical Indian solar calendar'''
    jday = Fraction(jday)

    # compute the year
    year = (jday - epoch) // tropical_year
    mesha = epoch + (year * tropical_year) # estimated time of Meṣ Saṃkrānti
    while (dayof(sankranti(mesha, 0)) > jday):
        year -= 1
        mesha -= tropical_year
    while (dayof(sankranti((mesha + tropical_year), 0)) <= jday):
        year += 1
        mesha += 1

    # compute the month
    m = (jday - mesha) // rasi
    angle = m * 30
    r = mesha + (m * rasi)

    while (dayof(sankranti(r, angle)) > jday):
        r -= rasi
        angle -= 30
        m -= 1
    while (dayof(sankranti((r + rasi), (angle + 30))) <= jday):
        r += rasi
        m += 1
        angle += 30
    month = NUMON[(m + 1) % 12]

    # compute the day
    day = jday - dayof(sankranti(r, angle)) + 1

    return (day, month, year)
