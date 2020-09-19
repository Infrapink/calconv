#!/usr/bin/python

#
# Convert between the Assyrian Calendar and Julian Day
#

import months
import leap_years_assyrian

cycle4 = (4 * 365) + 1
cycle100 = (100 * 365) + 24
cycle400 = (400 * 365) + 97

epoch = (-13387)

def tojd(day,month,year):

    day = int(day)
    month = month
    year = int(year)
    jday = epoch

    if year > 0:
        # positive year
        y = 1
        cycles = (year - y) // 400
        y += (400 * cycles)
        jday += (cycle400 * cycles)
        while y < year:
            if y % 400 == 349:
                jday += 366
            elif y % 100 == 49:
                jday += 365
            elif y % 4 == 1:
                jday += 366
            else:
                jday += 365
            y += 1

        if year % 400 == 349:
            m = months.ASSYRIAN_LEAP
        elif year % 100 == 49:
            m = months.ASSYRIAN_NORMAL
        elif year % 4 == 1:
            m = months.ASSYRIAN_LEAP
        else:
            m = months.ASSYRIAN_NORMAL

    else:
        # negative years
        y = 0
        cycles = (y - year) // 400
        y -= (400 * cycles)
        jday -= (cycle400 * cycles)
        while y > year:
            if y - year > 400:
                y -= 400
                jday -= cycle400
            else:
                y -= 1
                if abs(y) % 400 == 51:
                    jday -= 366
                elif abs(y) % 100 == 51:
                    jday -= 365
                elif abs(y) % 4 == 3:
                    jday -= 366
                else:
                    jday -= 365
                
        if year % 400 == 51:
            m = months.ASSYRIAN_LEAP
        elif year % 100 == 51:
            m = months.ASSYRIAN_NORMAL
        elif year % 4 == 3:
            m = months.ASSYRIAN_LEAP
        else:
            m = months.ASSYRIAN_NORMAL
            
    for i in m.keys():
        if i == month:
            jday += day - 1
            break
        else:
            jday += m[i]

    return jday

def fromjd(jday):
    """Convert a Julian Day to a date in the Assyrian calendar."""
    jday = int(jday)
    day = 0
    month = ""
    year = 0
    akitu = epoch

    if jday >= epoch:
        # positive year
        year = 1
        cycles = (jday - akitu) // cycle400
        year += (400 * cycles)
        akitu += (cycle400 * cycles)
        curryear = False
        while curryear == False:
            if year % 400 == 349:
                if jday - akitu <= 366:
                    curryear = True
                else:
                    year += 1
                    akitu += 366
            elif year % 100 == 49:
                if jday - akitu <= 365:
                    curryear = True
                else:
                    year += 1
                    akitu += 365
            elif year % 4 == 1:
                if jday - akitu <= 366:
                    curryear = True
                else:
                    year += 1
                    akitu += 366
            else:
                if jday - akitu <= 365:
                    curryear = True
                else:
                    year += 1
                    akitu += 365

        if year % 400 == 349:
            m = months.ASSYRIAN_LEAP
        elif year % 100 == 49:
            m = months.ASSYRIAN_NORMAL
        elif year % 4 == 1:
            m = months.ASSYRIAN_LEAP
        else:
            m = months.ASSYRIAN_NORMAL
            
    else:
        # negative date
        cycles = (akitu - jday) // cycle400
        year -= (400 * cycles)
        akitu -= (cycle400 * cycles)
        while akitu > jday:
            year -= 1
            if abs(year) % 400 == 51:
                akitu -= 366
            elif abs(year) % 100 == 51:
                akitu -= 365
            elif abs(year) % 4 == 3:
                akitu -= 366
            else:
                akitu -= 365

        if abs(year) % 400 == 51:
            m = months.ASSYRIAN_LEAP
        elif abs(year) % 100 == 51:
            m = months.ASSYRIAN_NORMAL
        elif abs(year) % 4 == 3:
            m = months.ASSYRIAN_LEAP
        else:
            m = months.ASSYRIAN_NORMAL

    delta = jday - akitu
    for i in m.keys():
        if delta < m[i]:
            month = i
            day = delta + 1
            break
        else:
            delta -= m[i]

    return (day, month, year)
