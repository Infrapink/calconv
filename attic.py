#!/usr/bin/python3

# Convert between Attic dates and Julian Days

from solun import first_visible_crescent as fvc, trans, dayof_arab, tropical_year as trop_year, syn_month
from months import ATHENIAN as MONTHS, NUM_ATHENIAN as MONTHNO
from fractions import Fraction

lon = 0 - 23 - Fraction(43,60) - Fraction(41,3600) # longitude of Athens
lat = 37 + Fraction(59,60) + Fraction(3,3600) # latitude of Athens
tz = Fraction(2,24) # Greece is UTC+2
epoch = Fraction(281420887, 180) # solar epoch

def dayof(jday):
    '''Determine the day associated with an astronomical event'''
    ans = dayof_arab(Fraction(jday), lon, lat, tz)
    return ans

def nyd(year):
    '''Compute New Year's Day'''
    year = int(year)

    solstice = trans((epoch + (year * trop_year)), 90, tz)
    noumenia = fvc(solstice, tz)
    while (dayof(fvc((noumenia - syn_month), tz)) >= dayof(solstice)):
        noumenia -= syn_month
    while (dayof(fvc(noumenia, tz)) < dayof(solstice)):
        noumenia += syn_month

    return noumenia

def fromjd(jday):
    '''Convert a Julian Day into an Attic date'''
    jday = int(jday)

    # compute the year
    year = int((jday - epoch) // trop_year)
    while (dayof(nyd(year + 1)) <= jday):
        year += 1
    while (dayof(nyd(year)) > jday):
        year -= 1
    crescent = nyd(year) # crescent moon marking the start of the year

    # is it leap?
    if (nyd(year + 1) - nyd(year) > 370):
        leap = True
    else:
        leap = False

    if (year >= 0):
        year += 1 # add 1 because the ancient Greeks didn't recognise 0

    # compute the start of the month
    noumenia = fvc(jday, tz)
    while (dayof(fvc(noumenia, tz)) > jday):
        noumenia -= syn_month
    while (dayof(fvc((noumenia + syn_month), tz)) <= jday):
        noumenia += syn_month

    # compute the month
    if ( (not(leap)) or (round((noumenia - crescent) / syn_month) < 6) ):
        # either it's not a leap year or it's before the leap month
        month = MONTHS[int(round((noumenia - crescent) / syn_month))]
    elif (round((noumenia - crescent) / syn_month) == 6):
        # leap month
        month = "Poseideon 2"
    else:
        # after the leap month
        month = MONTHS[int(round((noumenia - crescent) / syn_month)) + 1]

    # compute the day
    day = jday - dayof(fvc(noumenia, tz)) + 1 # add 1 because humans don't count from 0

    return (day, month, year)

def tojd(day, month, year):
    '''Convert an Attic date to a Julian Day'''
    day = int(day) - 1 # subtract 1 because humans don't count from 0
    month = str(month)
    year = int(year)

    # account for the year
    if (year > 0):
        year -= 1 # subtract 1 because the ancient Greeks didn't recognise 0
    jday = nyd(year)

    # is it leap?
    if (nyd(year + 1) - nyd(year) > 370):
        leap = True
    else:
        leap = False
        if (month == "Poseideon 2"):
            month = "Poseideon"

    # account for the month
    if (month == "Poseideon 2"):
        jday += (6 * syn_month)
    else:
        jday += (MONTHNO[month] * syn_month)
        if (leap and (MONTHNO[month] > 5)):
            # account for the leap month
            jday += syn_month

    # account for the day
    jday = dayof(fvc(jday, tz)) + day

    return jday
