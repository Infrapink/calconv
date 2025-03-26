#!/usr/bin/python3

# Convert between Meton's cyclic proposal and Julian Days, wherein months are assumed to hhave 30 days by default and a day is skipped every 63rd tithi.

from numpy import sign
from months import ATHENIAN as MONTHS, NUM_ATHENIAN as MONTHNO

epoch = 1563449
leaps = (1, 4, 7, 9, 12, 15, 17) # if the year gives a remainder in this tuple when divided by 19, it's a leap year. See Hannah, p. 57. This tuple is adjusted to count from 0 rather than 1.

def daysin(tithis):
    '''Compute the number of days in a given number of tithis'''
    tithis = int(tithis)

    days = tithis - ((tithis // 63) * sign(tithis))
    #days = tithis - (tithis // 63)
    return days

def leap(year):
    '''is the year leap?'''
    year = int(year)
    if (year > 0):
        year -= 1 # Ancient Greeks didn't recognise the number 0
    if (year % 19 in leaps):
        ans = True
    else:
        ans = False
    return ans

def nouthi(year):
    '''Compute the tithis that have passed since the epoch at the start of the year'''
    year = int(year)
    if (year > 0):
        year -= 1

    y = 19 * (year // 19)
    tithis = (year // 19) * 7050 # tithis that have passed since the epoch
    while (y < year):
        tithis += (30 * (12 + int((y % 19) in leaps)))
        y += 1

    return tithis

def fromjd(jday):
    '''Convert a Julian Day to a date in the variable Metonic Attic calendar'''
    jday = int(jday)

    # compute the year
    year = (jday - epoch) // 365
    while (epoch + daysin(nouthi(year + 1)) <= jday):
        year += 1
    while (epoch + daysin(nouthi(year)) > jday):
        year -= 1
    tithis = nouthi(year)

    # compute the month
    m = 0
    while (epoch + daysin(tithis + 30) <= jday):
        tithis += 30
        m += 1
    noumenia = epoch + daysin(tithis) # new moon.

    if (not(leap(year)) or (m < 6)):
        # normal year or before the leap month
        month = MONTHS[m]
    elif (m == 6):
        # leap month
        month = ("Poseideon 2")
    else:
        # after the leap month
        month = MONTHS[m - 1]

    # compute the day
    day = jday - noumenia + 1 # add 1 because humans don't count from 0

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a date in the Metonic Attic calendar to a Julian Day'''
    day = int(day) - 1 # subtact 1 because humans don't count from 0
    month = str(month)
    year = int(year)

    # account for the year
    tithis = nouthi(year)

    # account for the month
    if ( (month == "Poseideon 2") and not(leap(year)) ):
        month = "Poseidon"
    if (month == "Poseideon 2"):
        # leap month
        tithis += 180
    else:
        tithis += (30 * MONTHNO[month])
        if (leap(year) and (MONTHNO[month] > 5)):
            tithis += 30

    # account for the day
    jday = epoch + daysin(tithis) + day

    return jday
