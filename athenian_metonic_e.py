#!/usr/bin/python

# Convert between Julian Days and the Metonic Athenian calendar which correlates with the Egyptian calendar

from months import ATHENIAN as MONTHS, NUM_ATHENIAN as MONTHNO

epoch = 1563449
leaps = (1, 4, 7, 9, 12, 15, 17) # if the year gives a remainder in this tuple when divided by 19, it's a leap year. See Hannah, p. 57. This tuple is adjusted to count from 0 rather than 1.

def nyd(year):
    '''Compute the Julian Day on which a given year begins'''
    year = int(year)
    if (year > 0):
        # ancient Greeks did not accept the number 0
        year -= 1

    y = 19 * (year // 19)
    noumenia = epoch + (6936 * (year // 19))
    while (y < year):
        noumenia += (354 + (30 * int(y % 19 in leaps)))
        y += 1

    return noumenia

def leap(year):
    '''Is the year leap?'''
    year = int(year)
    if (year > 0):
        year -= 1
    if (year % 19 in leaps):
        ans = True
    else:
        ans = False
    return ans

def daysin(m):
    '''Returns days in a month, given the number of the month in the year (starting from 0)'''
    ans = 30 - (m % 2)
    return ans

def fromjd(jday):
    '''Convert a Julian Day to a date in the Metonic calendar with fixed month lengths'''
    jday = int(jday)

    # compute the year
    year = (jday - epoch) // 365
    noumenia = nyd(year) # New Year's Day, for now
    while (noumenia > jday):
        year -= 1
        noumenia -= (354 + (30 * int(leap(year))))
    while (noumenia + 354 + (30 * int(leap(year))) <= jday):
        noumenia += 354 + (30 * int(leap(year)))
        year += 1

    # compute the month
    m = 0
    if (not(leap(year)) or (jday - noumenia < 177)):
        # normal year, or it's before the leap month
        while (noumenia + 59 <= jday):
            noumenia += 59
            m += 2
        while (noumenia + daysin(m) <= jday):
            noumenia += daysin(m)
            m += 1
        month = MONTHS[m]
    elif (jday - noumenia < 207):
        # leap month
        noumenia += 177
        month = "Poseideon 2"
    else:
        # after the leap month
        noumenia += 207
        m = 6
        while (noumenia + 59 <= jday):
            noumenia += 59
            m += 2
        while (noumenia + daysin(m) <= jday):
            noumenia += daysin(m)
            m += 1
        month = MONTHS[m]

    # compute the day
    day = jday - noumenia + 1 # add 1 because humans don't count from 0

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a date in the Metonic calendar to a Julian Day.'''
    day = int(day) - 1 # subtract 1 because humans don't count from 0
    month = str(month)
    year = int(year)

    # account for the year
    jday = nyd(year)

    # account for the month
    if (not(leap(year)) and (month == "Poseideon 2")):
        month = "Poseideon"
    if (month == "Poseideon 2"):
        jday += 177
    else:
        if (not(leap(year)) or (MONTHNO[month] < 6)):
            m = 0
        else:
            m = 6
            jday += 207
        while (MONTHS[m] != month):
            jday += daysin(m)
            m += 1

    # account for the day
    jday += day

    return jday
                
            
