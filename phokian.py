#!/usr/bin/python3

# Convert between Phokian dates and Julian Days

from solun import first_visible_crescent as fvc, trans, dayof_arab, tropical_year as trop_year, syn_month
from fractions import Fraction

lon = 0 - 22 - Fraction(15,60) - Fraction(0,3600) # longitude of Phokis
lat = 38 + Fraction(30,60) + Fraction(0,3600) # latitude of Phokis
tz = Fraction(2,24) # Greece is UTC+2
epoch = Fraction(2251499731, 1440) # solar epoch

def dayof(jday):
    '''Determine the day associated with an astronomical event'''
    ans = dayof_arab(Fraction(jday), lon, lat, tz)
    return ans

def nyd(year):
    '''Compute New Year's Day'''
    year = int(year)

    solstice = trans((epoch + (year * trop_year)), 180, tz)
    noumenia = fvc(solstice, tz)
    while (dayof(fvc((noumenia - syn_month), tz)) >= dayof(solstice)):
        noumenia -= syn_month
    while (dayof(fvc(noumenia, tz)) < dayof(solstice)):
        noumenia += syn_month

    return noumenia

def fromjd(jday):
    '''Convert a Julian Day into an Phokian date'''
    jday = int(jday)

    # compute the year
    year = int((jday - epoch) // trop_year)
    while (dayof(nyd(year + 1)) <= jday):
        year += 1
    while (dayof(nyd(year)) > jday):
        year -= 1
    crescent = nyd(year) # crescent moon marking the start of the year

    if (year >= 0):
        year += 1 # add 1 because the ancient Greeks didn't recognise 0

    # compute the start of the month
    noumenia = fvc(jday, tz)
    while (dayof(fvc(noumenia, tz)) > jday):
        noumenia -= syn_month
    while (dayof(fvc((noumenia + syn_month), tz)) <= jday):
        noumenia += syn_month

    # compute the month
    month = int(round((noumenia - crescent) / syn_month)) + 1

    # compute the day
    day = jday - dayof(fvc(noumenia, tz)) + 1 # add 1 because humans don't count from 0

    return (day, month, year)

def tojd(day, month, year):
    '''Convert an Phokian date to a Julian Day'''
    day = int(day) - 1 # subtract 1 because humans don't count from 0
    month = int(month) - 1
    year = int(year)

    # account for the year
    if (year > 0):
        year -= 1 # subtract 1 because the ancient Greeks didn't recognise 0
    jday = nyd(year)

    # account for the month
    jday += (month * syn_month)

    # account for the day
    jday = dayof(fvc(jday, tz)) + day

    return jday
