#!/usr/bin/python3

# Convert between the Shahanshahi Zoroastrian calendar and Julian Days, according to the Yazdegerdi era

from months import ZOROASTRIAN_NUM as MONTHNO
from months import NUM_ZOROASTRIAN as NUMON

epoch = 1951943 # 1951972
cycle = (120 * 365) + 30
l = 8 # position of the leap month

def yearlen(y):
    '''Leap or normal year?'''
    y = int(y)
    if (y < 0) and (y % 120 == 14):
        ans = 395
    elif (y > 0) and (y % 120 == 13):
        ans = 395
    else:
        ans = 365

    return ans

def fromjd(jday):
    '''Convert a Julian Day into a date in the Shahanshahi calendar'''

    jday = int(jday)
    lpos = l

    day = 0
    month = ""

    cycles = (jday - epoch) // cycle
    nowruz = epoch + (cycle * cycles)
    year = 120 * cycles
    lpos = (lpos + cycles) % 12

    while nowruz > jday:
        nowruz -= cycle
        year -= 120
        lpos = (lpos - 1) % 12
    while nowruz + cycle <= jday:
        nowruz += cycle
        year += 120
        lpos = (lpos + 1) % 12
    if year >= 0:
        year += 1

    while nowruz + yearlen(year) <= jday:
        if yearlen(year) == 395:
            lpos = (lpos + 1) % 12
        nowruz += yearlen(year)
        year += 1
        if year == 0:
            year = 1
    # We now have the year and the Julian Day on which Nowruz falls

    if yearlen(year) == 365:
        # normal year
        month = NUMON[(jday - nowruz) // 30]
        day = ((jday - nowruz) % 30) + 1
    else:
        # leap year
        if jday < nowruz + (30 * (lpos + 1)):
            # before the leap month
            month = NUMON[(jday - nowruz) // 30]
            day = ((jday - nowruz) % 30) + 1
        elif jday < nowruz + (30 * (lpos + 2)):
            # leap month
            month = "Kabizeh"
            day = jday - (nowruz + (30 * (lpos + 1))) + 1
        else:
            # after the leap month
            alpha = nowruz + (30 * (lpos + 2))
            month = NUMON[1 + lpos + ((jday - alpha) // 30)]
            day = ((jday - alpha) % 30) + 1

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a day in the Shahanshahi calendar into a Julian Day'''
    day = int(day)
    month = str(month)
    year = int(year)

    jday = 0
    lpos = l
        
    if year == 0:
        year = (-1)

    if year > 0:
        cycles = (year - 1) // 120
    else:
        cycles = year // 120

    jday = epoch + (cycles * cycle)
    lpos = (lpos + cycles) % 12
    y = 120 * cycles
    if y >= 0:
        y += 1

    while y < year:
        jday += yearlen(y)
        if yearlen(y) == 395:
            lpos = (lpos + 1) % 12
        y += 1

    while y > year:
        y -= 1
        if year == 0:
            year = (-1)
        jday -= yearlen(y)
        if yearlen(y) == 395:
            lpos = (lpos - 1) % 12

    if yearlen(year) == 365:
        # normal year
        if month == "Kabizeh":
            # account for the user entering the leap month
            month = NUMON[lpos]
        jday = jday + (30 * MONTHNO[month]) + day - 1
    else:
        # leap year
        if month == "Kabizeh":
            # leap month
            jday = jday + (30 * (lpos + 1)) + day - 1
        elif lpos >= MONTHNO[month]:
            # not yet at the leap month
            jday = jday + (30 * MONTHNO[month]) + day - 1
        else:
            # after the leap month
            jday = jday + (30 * (lpos + 1))
            jday = jday + (30 * (MONTHNO[month] - lpos)) + day - 1

    return jday
