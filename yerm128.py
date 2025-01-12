#!/usr/bin/python3

# Convert between Julian Days and the Yerm 128 lunisolar calendar

from array import array

solar_epoch = 1721426 - 375
s4 = (4 * 365) + 1
s128 = (32 * s4) - 1

lunar_epoch = 2450399
m17 = (9 * 30) + (8 * 29)
m15 = (8 * 30) + (7 * 29)
mc3 = m17 + m17 + m15
mc52 = (17 * mc3) + m17

MONTHS = ("Chang'e", "Sîn", "Tecciztecatl", "Hina", "Chía", "Quilla", "Khonsu", "Gleti", "Küyen", "Mayari", "Dalnim", "Olapa", "Anumati")

def syl(year):
    '''Compute the length of the solar year'''
    year = int(year)

    if (year % 128 == 0):
        # not a leap year
        ans = 365
    elif (year % 4 == 0):
        # leap year
        ans = 366
    else:
        # not a leap year
        ans = 365

    return ans

def sny(year):
    '''Compute solar new year for a given year'''
    year = int(year)

    cycles = year // 128
    y = 128 * cycles
    nyd = solar_epoch + (s128 * cycles)

    if (y + 4 <= year):
        nyd += (4 * 365)
        y += 4

    while (y + 4 <= year):
        y += 4
        nyd += s4

    while (y < year):
        nyd += syl(year)
        y += 1

    return nyd

def newmoon(jday):
    '''Find the first of the month which contains a given Julian Day, as well as the number of days in that month'''
    jday = int(jday)

    cycles = (jday - lunar_epoch) // mc52
    darkmoon = array('l', [lunar_epoch + (cycles * mc52), 0])
    while (darkmoon[0] + mc3 <= jday):
        darkmoon[0] += mc3
    while (darkmoon[0] + m17 <= jday):
        darkmoon[0] += m17

    while (darkmoon[0] + 59 <= jday):
        darkmoon[0] += 59
    if (darkmoon[0] + 30 <= jday):
        darkmoon[0] += 30
        darkmoon[1] = 29
    else:
        darkmoon[1] = 30

    return darkmoon

def lny(year):
    '''Compute the date of lunar new year'''
    # lunar new year falls on the first of the month which is closest to solar new year
    # if the first of the month before and after are equal,
    # it is the first of the month which contains solar new year
    year = int(year)

    solstice = sny(year)
    moon_before = newmoon(solstice)
    if (moon_before[0] + moon_before[1] - solstice < solstice - moon_before[0]):
        ans = moon_before[0] + moon_before[1]
    else:
        ans = moon_before[0]

    return ans

def fromjd(jday):
    '''Convert a Julian Day into a date in the Yerm 128 calendar'''
    jday = int(jday)

    # Compute the year
    year = int((jday - solar_epoch) // 365.2421875)
    while (lny(year) > jday):
        year -= 1
    while (lny(year + 1) <= jday):
        year += 1

    # compute the month
    darkmoon = newmoon(lny(year))
    m = 0
    while (darkmoon[0] + darkmoon[1] <= jday):
        darkmoon = newmoon(darkmoon[0] + darkmoon[1])
        m += 1
    month = MONTHS[m]

    # compute the day
    day = jday - darkmoon[0] + 1 # add 1 because humans don't count from 0

    return (day, month, year)

def tojd(day, month, year):
    ''' Convert a date in the Yerm 128 calendar into a Julian Day'''
    day = int(day) - 1 # subtract 1 because computers count from 0
    month = str(month)
    year = int(year)

    # account for the year
    darkmoon = newmoon(lny(year)) # new year's day

    # account for the month
    # first, check if the user entered Anumati as the month in a non-leap year
    if ( (month == "Anumati") and (lny(year + 1) - darkmoon[0] < 380) ):
        month = "Olapa"
    # now count through the months
    m = 0
    while (month != MONTHS[m]):
        darkmoon = newmoon(darkmoon[0] + darkmoon[1])
        m += 1

    # account for the day
    darkmoon[0] = darkmoon[0] + day

    return darkmoon[0]
