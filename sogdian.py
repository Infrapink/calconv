#!/usr/bin/sogdian

# Convert between the Sogdian calendar and Julian Day

from months import SOGDIAN_NUM as MONTHNO
from months import NUM_SOGDIAN as NUMON

epoch = 1951702

def fromjd(jday):
    '''Convert Julian Day into a date in hte Sogdian calendar'''
    jday = int(jday)

    day = 0
    month = ""

    year = (jday - epoch) // 365
    nogroc = epoch + (year * 365)
    while (nogroc + 365) <= jday:
        year += 1
        nogroc += 365
    while nogroc > jday:
        year -= 1
        nogroc -= 365

    if year >= 0:
        year += 1

    month = NUMON[(jday - nogroc) // 30]
    day = ((jday - nogroc) % 30) + 1
    return (day, month, year)

def tojd(day, month, year):
    '''Convert a date in the Sogdian calendar to a Julian Day'''
    day = int(day)
    month = str(month)
    year = int(year)

    if year >= 0:
        year -= 1

    jday = epoch + (year * 365)
    jday = jday + (30 * MONTHNO[month])
    jday = jday + day - 1

    return jday
