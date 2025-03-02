#!/usr/bin/python3

# Convert between dates in the Hermetic Lunar Week calendar and Julian Days.

from math import floor, ceil
from solun import trans, newmoon, tropical_year as trop_year, syn_month, phasetime

epoch = 625413.8006944444

months = ("Artaud", "Benjamin", "Clark", "de Quincy", "Ellis", "Furst", "Goff", "Hofmann", "Izuni", "Janiger", "Kesey", "Lilly", "McKenna")
monthno = {"Artaud":    0,
           "Benjamin":  1,
           "Clark":     2,
           "de Quincy": 3,
           "Ellis":     4,
           "Furst":     5,
           "Goff":      6,
           "Hofmann":   7,
           "Izuni":     8,
           "Janiger":   9,
           "Kesey":    10,
           "Lilly":    11,
           "McKenna":  12}

def dayof(jday):
    '''Compute the Julian Day associated with the time of a given astronomical event'''
    jday = float(jday)

    if (jday % 1 <= 0.25):
        ans = floor(jday)
    else:
        ans = ceil(jday)

    return ans

def nyd(year):
    '''Compute New Year's Day of a specified year'''
    ans = dayof(newmoon(trans((epoch + (trop_year * int(year))), 0, 0), 0))
    return ans

def fromjd(jday):
    '''Convert a Julian Day into a date in the Hermetic Lunar Week calendar'''
    jday = int(jday)

    # compute the year
    year = int((jday - epoch) // trop_year)
    while (nyd(year) > jday):
        year -= 1
    while (nyd(year + 1) <= jday):
        year += 1
    n = nyd(year)
    
    # compute the month
    darkmoon = newmoon(jday, 0) # new moon marking the start of the month
    while (dayof(newmoon(darkmoon, 0)) > jday):
        darkmoon -= syn_month
    while (dayof(newmoon((darkmoon + syn_month), 0)) <= jday):
        darkmoon += syn_month
    month = months[int(round((darkmoon - n) / syn_month))]

    # compute the week
    week = 1
    while (dayof(phasetime((darkmoon + (syn_month + (week/4))), (week * 90), 0)) <= jday):
        print(week)
        week += 1
        

    # compute the day
    day = jday - dayof(phasetime((darkmoon + (syn_month * ((week - 1) / 4))), ((week - 1) * 90), 0)) + 1 # add 1 because humans don't count from 0

    return (day, week, month, year)

def tojd(day, week, month, year):
    '''Convert a day in the Hermetic Lunar Month calendar to a Julian Day'''
    day = int(day) - 1 # subtract 1 because computers count from 0
    week = int(week) - 1 # subtract 1 because computers count from 0
    month = monthno[str(month)]
    year = int(year)

    #ans = dayof(phasetime((nyd(year) + (month * syn_month) + (syn_month * (week / 4))), (week * 90), 0)) + day
    t = nyd(year) + (month * syn_month) + (syn_month * (week / 4))
    ans = dayof(phasetime(t, (week * 90), 0)) + day
    return ans
