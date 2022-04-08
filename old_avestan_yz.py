#!/usr/bin/python3

# Convert between the Old Avestan calendar and Julian Day, based on the Yazdegerdi Era

from months import OLD_AVESTAN_NUM as MONTHNO
from months import NUM_OLD_AVESTAN as NUMON

epoch = 1951953
sexan = (6 * 360) + 30 # six-year cycle
dozan = (20 * sexan) + 30 # 120-year cycle
f3 = (3 * sexan) + 30 # first three sexans of the dozan

def yearlen(year):
    '''Determine if a year is a normal, leap, or double-leap year'''
    year = int(year)

    if year > 0:
        if year % 120 == 13:
            # double-leap year
            length = 420
        elif year % 6 == 1:
            # leap year
            length = 390
        else:
            # normal year
            length = 360
    else:
         if year % 120 == 14:
             length = 420
         elif year % 6 == 2:
             length = 390
         else:
             length = 360

    return length

def fromjd(jday):
    '''Convert a Julian Day into a calendar date'''
    jday = int(jday)

    day = 0
    month = ""
    year = 0

    dozans = (jday - epoch) // dozan
    year = 120 * dozans
    nowruz = epoch + (dozans * dozan)

    while (nowruz + dozan) <= jday:
        year += 120
        nowruz += dozan

    while nowruz > jday:
        year -= 120
        nowruz -= dozan

    if year >= 0:
        year += 1

    y = year
    s = 0
    while (s < 2) and (jday - nowruz >= sexan):
        s += 1
        nowruz += sexan
        year += 6

    if (jday - nowruz >= 420) and (s == 2):
        year += 1
        nowruz += 420

    #if year - y >= 14:
    sexans = (jday - nowruz) // sexan
    nowruz += (sexans * sexan)
    year += (6 * sexans)

    while (nowruz + yearlen(year)) <= jday:
        nowruz += yearlen(year)
        year += 1
    while nowruz > jday:
        year -= 1
        nowruz -= yearlen(year)

    month = NUMON[(jday - nowruz) // 30]
    day = ((jday - nowruz) % 30) + 1

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a date in the Old Avestan calendar to a Julian Day'''
    day = int(day)
    month = str(month)
    year = int(year)

    jday = 0

    if year >= 0:
        dozans = (year - 1) // 120
    else:
        dozans = year // 120

    jday = epoch + (dozans * dozan)
    y = 120 * dozans
    if year > 0:
        y += 1

    if (year - y) >= 12:
        # get up to the double-leap year
        jday += (2 * sexan)
        y += 12

    if (y == 13) and (year - y > 13):
        # jump over the double-leap year
        y += 1
        jday += 420

    sexans = (year - y) // 6
    y += (6 * sexans)
    jday += (sexans * sexans)

    while y < year:
        jday += yearlen(y)
        y += 1

    # account for the user entering the leap month in a regular year
    if (month == "Kabizeh 2") and (yearlen(year) == 390):
        month = "Kabizeh"
    elif (month[:7] == "Kabizeh") and (yearlen(year) == 360):
        month = "Vixayana"

    jday = jday + (30 * MONTHNO[month]) + day - 1

    return jday
