#!/usr/bin/python

#
# Convert between the Pax calendar and Julian day
#

import months

cycle400 = (400 * 365) + 97
#epoch = 1721059
epoch = 1721061

leap_digits_ad = (0,6,12,18,24,30,36,42,48,54,60,66,72,78,84,90,96,99)
leap_digits_bc = (0,94,88,82,76,70,64,58,52,46,40,34,28,22,16,10,4,1)

def tojd(day, month, year):
    day = int(day)
    month = month
    year = int(year)
    lear = abs(year) % 100 # use to check leap years
    jday = epoch
    y = 0

    if year >= 0:
        # positive dates
        cycles = year // 400
        y += (400 * cycles)
        jday += (cycle400 * cycles)

        while y < year:
            if y % 400 == 0:
                jday += 364
            elif y % 100 in leap_digits_ad:
                jday += 371
            else:
                jday += 364
            y += 1

        if year % 400 == 0:
            # not a leap year
            m = months.PAX_NORMAL
        elif year % 100 in leap_digits_ad:
            # leap year
            m = months.PAX_LEAP
        else:
            # not a leap year
            m = months.PAX_NORMAL

    else:
        # negative dates
        cycles = abs(year) // 400
        y -= (400 * cycles)
        jday -= (cycles * cycle400)
        
        while y > year:
            y -= 1
            if y % 400 == 0:
                jday -= 364
            elif abs(y) % 100 in leap_digits_bc:
                jday -= 371
            else:
                jday -= 364
        
        if year % 400 == 0:
            m = months.PAX_NORMAL
        elif abs(year) % 100 in leap_digits_bc:
            m = months.PAX_LEAP
        else:
            m = months.PAX_NORMAL

    for i in m.keys():
        if i == month:
            jday += day - 1
            break
        else:
            jday += m[i]

    return jday

def fromjd(jday):
    """Convert a Julian day to a date in the Pax calendar."""
    jday = int(jday)
    year = 0
    month = ""
    day = 0
    nyd = epoch
    curryear = False
    
    if jday >= epoch:
        # positive dates
        cycles = (jday - nyd) // cycle400
        year += (400 * cycles)
        nyd += (cycle400 * cycles)
        
        while curryear == False:
            if year % 400 == 0:
                if jday - nyd < 364:
                    curryear = True
                    break
                else:
                    nyd += 364
            elif year % 100 in leap_digits_ad:
                if jday - nyd < 371:
                    curryear = True
                    break
                else:
                    nyd += 371
            else:
                if jday - nyd < 364:
                    curryear = True
                    break
                else:
                    nyd += 364
            year += 1
            
        if year % 400 == 0:
            # not a leap year
            m = months.PAX_NORMAL
        elif year % 100 in leap_digits_ad:
            # leap year
            m = months.PAX_LEAP
        else:
            # not a leap year
            m = months.PAX_NORMAL

    else:
        # negative dates
        cycles = (nyd - jday) // cycle400
        year -= (400 * cycles)
        nyd -= (cycle400 * cycles)

        while nyd > jday:
            year -= 1
            if abs(year) % 400 == 0:
                nyd -= 364
            elif abs(year) % 100 in leap_digits_bc:
                nyd -= 371
            else:
                nyd -= 364
            #year -= 1
        
        if abs(year) % 400 == 0:
            # not a leap year
            m = months.PAX_NORMAL
        elif abs(year) % 100 in leap_digits_bc:
            # leap year
            m = months.PAX_LEAP
        else:
            # not a leap yer
            m = months.PAX_NORMAL

    delta = jday - nyd
    for i in m.keys():
        if delta < m[i]:
            month = i
            day = delta + 1
            break
        else:
            delta -= m[i]

    return (day, month, year)

