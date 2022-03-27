#!/usr/hin/python3

# Convert between the Young Avestan calendar and Julian Day using the era of Zarathushtra

from months import NUM_YOUNG_AVESTAN as NUMONTHS
from months import YOUNG_AVESTAN_NUM as MONTHNO

epoch = 1579397

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

    monstar = nowruz
    if jday - monstar >= (8 * 30) + 5:
        m = 9
        monstar = monstar + (8 * 30) + 5
    else:
        m = 0

    m = m + ((jday - monstar) // 30)
    month = NUMONTHS[m]
    day = 1 + ((jday - monstar) % 30)

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

    if MONTHNO[month] <= 8:
        jday = jday + (30 * MONTHNO[month]) + day - 1
    else:
        jday = jday + (30 * MONTHNO[month]) + day - 26

    return jday
