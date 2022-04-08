#!/usr/hin/python3

# Convert between the mainstream Zoroastrian fixed calendar and Julian Day using the era of Zarathushtra

from months import NUM_ZOROASTRIAN as NUMONTHS
from months import ZOROASTRIAN_NUM as MONTHNO

epoch = 1579398

def fromjd(jday):
    '''Cionvert a Julian Day into a day in the Oshmurtik calendar'''
    jday = int(jday)

    day = 0
    month = ""
    year = 0

    year = (jday - epoch) // 365
    nowruz = epoch + (year * 365)
    
    while (nowruz + 365) <= jday:
        year += 1
        nowruz += 365
    while nowruz > jday:
        year -= 1
        nowruz -= 365

    if year >= 0:
        year += 1

    month = NUMONTHS[(jday - nowruz) // 30]
    day = 1 + ((jday - nowruz) % 30)

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a date in the Oshmurtik calendar into a Julian Day'''
    day = int(day)
    month = str(month)
    year = int(year)

    if year >= 0:
        jday = epoch + ((year - 1) * 365)
    else:
        jday = epoch + (year * 365)

    jday = jday + (30 * MONTHNO[month]) + day - 1

    return jday
