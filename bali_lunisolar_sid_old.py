#!/usr/bin/python3

# Convert between Julian Days and dates in the Balinese lunisolar calendar
# This version uses methods from the Sūrya Siddhānta and the older leap year system

from math import floor, ceil
from fractions import Fraction
from months import BALINESE_LUNAR as MONTHS, NUM_BALINESE as MONTHNO
from surya_siddhanta import se, t_syn_month as syn_month, newmoon, dayof_sunrise as dayof

epoch = newmoon(se)
cycle = 235 * syn_month # mean cycle of 19 years
leap_rems = (0, 3, 6, 8, 11, 14, 16) # years in a Metonic cycle which are leap

def yeartype(year):
    '''Returns mean length of the year in question'''
    year = int(year)
    if (year % 19 in leap_rems):
        # leap year
        ans = 13 * syn_month
    else:
        # normal year
        ans = 12 * syn_month
    return ans

def fromjd(jday):
    '''Convert a Julian Day into a date in the Balinese lunisolar calendar'''
    jday = int(jday)

    # compute the year
    cycles = (jday - epoch) // cycle
    year = 19 * cycles
    crescent = epoch + (cycle * cycles)
    while (dayof(newmoon(crescent + cycle)) <= jday):
        year += 19
        crescent += cycle
    while (dayof(newmoon(crescent)) > jday):
        year -= 19
        crescent -= cycle
    while (dayof(newmoon(crescent + yeartype(year))) <= jday):
        crescent += yeartype(year)
        year += 1

    # compute the month
    m = (jday - crescent) // syn_month # number of the month
    crescent += (m * syn_month)
    while (dayof(newmoon(crescent)) > jday):
        crescent -= syn_month
        m -= 1
    while (dayof(newmoon(crescent + syn_month)) <= jday):
        crescent += syn_month
        m += 1
    
    if (not ((year % 19) in leap_rems)):
        # normal year
        month = MONTHS[m]
    elif (year % 19 in (0, 6, 11)):
        # leap year where Desta is the leap month
        if (m < 10):
            month = MONTHS[m]
        elif (m == 10):
            month = "Mengsa Desta 2"
        else:
            month = MONTHS[m - 1]
    else:
        # leap year where Sada is the leap month
        if (m < 11):
            month = MONTHS[m]
        elif (m == 11):
            month = "Mengsa Sada 2"
        else:
            month = "Mengsa Sada"

    # compute the day... that is, the tithi
    tithi = 1
    day = dayof(newmoon(crescent))
    while (day < jday):
        if ( (day - dayof(epoch)) % 63 == 8):
            tithi += 2
        else:
            tithi += 1
        day += 1
    
    return(tithi, month, year)

def tojd(tithi, month, year):
    '''Convert a date in the Balinese lunisolar calendar to a Julian Day'''
    tithi = int(tithi) - 1 # subtract 1 because computers count from 0
    month = str(month)
    year = int(year)

    # account for the year
    cycles = year // 19
    y = 19 * cycles
    jday = epoch + (cycle * cycles)
    while (y < year):
        jday += yeartype(y)
        y += 1

    # account for the month
    if (month[len(month) - 1:] == '2'):
        leap = True
        month = month[:len(month) - 2]
    else:
        leap = False

    if ( (not (year % 19 in leap_rems)) or (MONTHNO[month] < 10) ):
        # either it's a normal year or we haven't gotten to the leap month yet
        jday = dayof(newmoon(jday + (syn_month * MONTHNO[month])))
    else:
        if (year % 19 in (0, 6, 11)):
            # leap year where Desta is the leap month
            if (leap):
                m = 10
            else:
                m = MONTHNO[month] + 1
        else:
            # leap year where Sada is the leap month
            if (month == "Mengsa Desta"):
                m = 10
            elif (leap):
                m = 11
            else:
                m = 12
        jday = dayof(newmoon(jday + (syn_month * m)))

    # account for the tithi
    t = 0
    while (t < tithi):
        if ( (jday - ceil(epoch)) % 63 == 8):
            t += 2
        else:
            t += 1
        jday += 1

    return(int(jday))