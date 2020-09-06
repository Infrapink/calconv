#!/usr/bin/python

#
# Convert between the Ethiopian Calendar and Julian Day
#

import months

cycle4 = (4 * 365) + 1
epoch = 1724222

def tojd(day, month, year):

    day = int(day)
    month = month.title()
    year = int(year)
    jday = epoch

    if year > 0:
        # positive years
        y = 1
        while y < year:
            if year - y > 4:
                y += 4
                jday += cycle4
            elif y % 4 == 0:
                y += 1
                jday ++ 366
            else:
                y += 1
                jday += 365

        if year % 4 == 0:
            # leap year
            m = months.ETHIOPIAN_LEAP
        else:
            # not a leap year
            m = months.ETHIOPIAN_NORMAL

    else:
        # negative years
        y = 0
        while y > year:
            if y - year > 4:
                y -= 4
                jday -= cycle4
            else:
                y -= 1
                if abs(y) % 4 == 1:
                    jday -= 366
                else:
                    jday -= 365

        if abs(year) % 4 == 1:
            # leap year
            m = months.ETHIOPIAN_LEAP
        else:
            # not a leap year
            m = months.ETHIOPIAN_NORMAL

    for i in m.keys():
        if i == month:
            jday += day - 1
            break
        else:
            jday += m[i]

    return jday

def fromjd(jday):
    """Convert a Julian Day to a date in the Ethiopian calendar"""
    jday = int(jday)
    year = 0
    month = ""
    day = 0
    nyd = epoch

    if jday >= epoch:
        # positive date
        curryear = False
        year = 1
        while curryear == False:
            if jday - nyd > cycle4:
                year += 4
                nyd += cycle4
            elif year % 4 == 0:
                if jday - nyd <= 366:
                    curryear = True
                else:
                    year += 1
                    nyd += 366
            else:
                if jday - nyd <= 365:
                    curryear = True
                else:
                    year += 1
                    nyd += 365

        if year % 4 == 0:
            # leap year
            m = months.ETHIOPIAN_LEAP
        else:
            # not a leap year
            m = months.ETHIOPIAN_NORMAL

    else:
        # negative date
        while jday < nyd:
            if nyd - jday > cycle4:
                year -= 4
                nyd -= cycle4
            else:
                year -= 1
                if abs(year) % 4 == 1:
                    nyd -= 366
                else:
                    nyd -= 365

        if abs(year) % 4 == 1:
            # leap year
            m = months.ETHIOPIAN_LEAP
        else:
            # not a leap year
            m = months.ETHIOPIAN_NORMAL

    delta = jday - nyd
    for i in m.keys():
        if delta < m[i]:
            month = i
            day = delta + 1
            break
        else:
            delta -= m[i]

    return (day, month, year)
