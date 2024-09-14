#!/usr/bin/python3

#
# Convert between the new tropical Thai calendar and Julian Day
#

from months import THAI_TROPICAL_NORMAL as NORMAL, THAI_TROPICAL_LEAP as LEAP

cycle4 = (4 * 365) + 1
cycle100 = (100 * 365) + 24
cycle400 = (400 * 365) + 97

epoch = 1522734
MONTHSET = ("Mákàraa-khom", "Kumphaa-phan", "Miinaa-khom", "Meesaǎ-yon", "Phrɯ́tsaphaa-khom", "Míthùnaa-yon", "Kàrákàdaa-khom", "Sǐnghǎa-khom", "Kanyaa-yon", "Tùlaa-khom", "Phrɯ́tsacìkaa-yon", "Thanwaa-khom")

def yeartype(year):
    '''Return the number of days in a year'''
    year = int(year)

    if (year % 400 == 54):
        ans = 366
    elif (year % 100 == 54):
        ans = 365
    elif (year % 4 == 0):
        ans = 366
    else:
        ans = 365

    return ans

def qtype(year):
    '''Return number of days in a four-year period'''
    year = int(year)

    if (year % 400 == 52):
        # contains the 54th year of the cycle, which is a leap year
        ans = cycle4
    elif (year % 100 == 52):
        # contains a year which doesn't have leap day due to the century rule
        ans = cycle4 - 1
    else:
        ans = cycle4

    return ans

def monthtype(year):
    if yeartype(year) == 366:
        ans = LEAP
    else:
        ans = NORMAL

    return ans
        
def tojd(day, month, year):
    '''Convert a date in the new Thai tropical calendar to a Julian Day'''
    day = int(day) - 1 # subtract 1 because computers count from 0
    month = str(month)
    year = int(year)

    # compute new year's day
    cycles = year // 400
    jday = epoch + (cycle400 * cycles) # start of the 400-year cycle
    y = 400 * cycles
    if (year - y >= 100):
        y += 100
        jday += 36525
        while (y + 100 <= year):
            y += 100
            jday += 36524
    while (year - y >= 4):
        jday += qtype(y)
        y += 4
    while (y < year):
        jday += yeartype(y)
        y += 1

    # compute the start of the month
    m = 0
    MONTHS = monthtype(year)
    while (MONTHSET[m] != month):
        jday += MONTHS[MONTHSET[m]]
        m = (m + 1) % 12

    # account for the day
    jday = jday + day

    return jday

def fromjd(jday):
    """Convert a Julian Day to a date in the Thai tropical calendar"""
    jday = int(jday)

    # compute the year
    cycles = (jday - epoch) // cycle400
    songkran = epoch + (cycles * cycle400)
    year = 400 * cycles
    while (songkran > jday):
        year -= 400
        songkran -= cycle400
    while (songkran + cycle400 <= jday):
        year += 400
        songkran += cycle400

    if (songkran + 36525 <= jday):
        year += 100
        songkran += 36525
        while (songkran + 36524 <= jday):
            year += 100
            songkran += 36524

    while (songkran + qtype(year) <= jday):
        songkran += qtype(year)
        year += 4
    while (songkran + yeartype(year) <= jday):
        songkran += yeartype(year)
        year += 1

    # compute the month
    m = 0
    MONTHS = monthtype(year)
    while (songkran + MONTHS[MONTHSET[m]] <= jday):
        songkran += MONTHS[MONTHSET[m]]
        m = (m + 1) % 12
    month = MONTHSET[m]

    day = jday - songkran + 1 # add 1 because computers humans count from 1

    return (day, month, year)
