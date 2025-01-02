#!/usr/bin/python3

# Convert between Julian Days and the ISO-8601 week calendar

from solun import gregorian_nyd, gregorian_epoch
from months import WEEKDAYS_EN as WEEKDAYS

# new year's adjustment
adj = {"Monday":     0,
       "Tuesday":   -1,
       "Wednesday": -2,
       "Thursday":  -3,
       "Friday":     3,
       "Saturday":   2,
       "Sunday":     1}

def nym(year):
    '''Compute the Julian Day of the first Monday of the year'''

    nyd = gregorian_nyd(int(year), True)
    nyd = nyd + adj[WEEKDAYS[nyd % 7]]
    return nyd
       
def tojd(day, week, year):
    '''Convert a date in the week calendar into a Julian Day'''
    jday = nym(year) + (7 * (int(week) - 1)) + ((0 - adj[str(day)]) % 7) # subtract 1 from the week because humans don't count from 0
    return jday

def fromjd(jday):
    '''Convert a Julian Day into a date in the week calendar'''
    jday = int(jday)

    year = int((jday - gregorian_epoch) // 365.2425)
    while (nym(year) > jday):
        year -= 1
    while (nym(year + 1) <= jday):
        year += 1

    day = WEEKDAYS[jday % 7]
    week = ((jday - nym(year)) // 7) + 1 # add 1 because computers count from 0

    return (day, week, year)
