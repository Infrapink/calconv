#!/usr/bin/python

##
## Conveart between Lunar Hijri calendar and Julian Day.
##

import months

cycle30 = (30 * 354) + 11
epoch = 1948439

leap_years_ah = (2,5,7,10,13,16,18,21,24,26,29)
leap_years_bh = (1,4,6,9,12,15,17,20,23,25,28)
leap_years_zo = (1, 4, 6, 9, 12, 14, 17, 20, 23, 25, 28)
    
def tojd(day, month, year):
    day = int(day)
    month = month
    year = int(year)
    jday = epoch

    if year > 0:
        y = 1
        cycles = (year - y) // 30
        y += (30 * cycles)
        jday += (cycle30 * cycles)
        while y < year:
            if year - y >= 30:
                y += 30
                jday += cycle30
            elif y % 30 in leap_years_ah:
                y += 1
                jday += 355
            else:
                y += 1
                jday += 354

        if year in leap_years_ah:
            # leap year
            m = months.ARAB_LEAP
        else:
            # not a leap year
            m = months.ARAB_NORMAL

    else:
        # negative years
        y = 0
        cycles = (y - year) // 30
        y -= (30 * cycles)
        jday -= (cycle30 * cycles)
        while y > year:
            if y - year > 30:
                y -= 30
                jday -= cycle30
            else:
                y -= 1
                if abs(y) % 30 in leap_years_bh:
                    jday -= 355
                else:
                    jday -= 354

        if year in leap_years_bh:
            # leap year
            m = months.ARAB_LEAP
        else:
            # not a leap year
            m = months.ARAB_NORMAL
    for i in m.keys():
        if i == month:
            jday += day - 1
            break
        else:
            jday += m[i]

    return jday

def fromjd(jday):
    """Convert a Julian Day to a date in the Lunar Hijri calendar."""
    jday = int(jday)
    day = 0
    month = ""
    year = 0
    nyd = epoch

    if jday >= epoch:
        # positive year
        curryear = False
        year = 1
        cycles = (jday - nyd) // cycle30
        year += (30 * cycles)
        nyd += (cycle30 * cycles)
        while curryear == False:
            if jday - nyd > cycle30:
                year += 30
                nyd += cycle30
            elif year % 30 in leap_years_ah:
                if jday - nyd <= 355:
                    curryear = True
                else:
                    year += 1
                    nyd += 355
            else:
                if jday - nyd <= 354:
                    curryear = True
                else:
                    year += 1
                    nyd += 354

        if year % 30 in leap_years_ah:
            m = months.ARAB_LEAP
        else:
            m = months.ARAB_NORMAL

    else:
        # negative year
        cycles = (nyd - jday) // cycle30
        year -= (30 * cycles)
        nyd -= (cycle30 * cycles)
        while nyd > jday:
            if nyd - jday > cycle30:
                nyd -= cycle30
                year -= 30
            else:
                year -= 1
                if abs(year) % 30 in leap_years_bh:
                    nyd -= 355
                else:
                    nyd -= 354

        if abs(year) % 30 in leap_years_bh:
            m = months.ARAB_LEAP
        else:
            m = months.ARAB_NORMAL
                    
    delta = jday - nyd
    for i in m.keys():
        if delta < m[i]:
            month = i
            day = delta + 1
            break
        else:
            delta -= m[i]

    return (day, month, year)
