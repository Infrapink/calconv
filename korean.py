#!/usr/bin/python3

#
# Convert between the Gregorian Calendar and Julian Day
#

import months

cycle4 = (4 * 365) + 1
cycle100 = (100 * 365) + 24
cycle400 = (400 * 365) + 97

epoch = 869314

def tojd(day, month, year):

    day = int(day)
    month = month.title()
    year = int(year)
    jday = epoch

    if year > 0:
        # positive dates
        y = 1
        cycles = (year - y) // 400
        y += (400 * cycles)
        jday += (cycles * cycle400)
        while y < year:
            if year - y > 400:
                y += 400
                jday += cycle400
            elif year - y > 100:
                y += 100
                jday += cycle100
            elif year - y > 4:
                y += 4
                jday += cycle4
            elif y % 400 == 333:
                y += 1
                jday += 366
            elif y % 100 == 33:
                y += 1
                jday += 365
            elif y % 4 == 1:
                y += 1
                jday += 366
            else:
                y += 1
                jday += 365

        if year % 400 == 333:
            m = months.KOREAN_LEAP
        elif year % 100 == 33:
            m = months.KOREAN_NORMAL
        elif year % 4 == 1:
            m = months.KOREAN_LEAP
        else:
            m = months.KOREAN_NORMAL
    else:
        # negative years
        y = 0
        cycles = (y - year) // 400
        y -= (400 * cycles)
        jday -= (cycles * cycle400)
        
        while y > year:
            if y - year > 400:
                y -= 400
                jday -= cycle400
            else:
                y -= 1
                if abs(y) % 400 == 267:
                    jday -= 366
                elif abs(y) % 100 == 67:
                    jday -= 365
                elif abs(y) % 4 == 3:
                    jday -= 366
                else:
                    jday -= 365

        if abs(year) % 400 == 267:
            m = months.KOREAN_LEAP
        elif abs(year) % 100 == 67:
            m = months.KOREAN_NORMAL
        elif abs(year) % 4 == 3:
            m = months.KOREAN_LEAP
        else:
            m = months.KOREAN_NORMAL

    for i in m.keys():
        if i == month:
            jday += day - 1
            break
        else:
            jday += m[i]

    return jday

def fromjd(jday):
    """Convert a Julian Day to a date in the Gregorian calendar"""
    jday = int(jday)
    year = 0
    month = ""
    seollal = epoch
    curryear = False

    if jday >= epoch:
        # positive date
        year = 1
        cycles = (jday - seollal) // cycle400
        year += (400 * cycles)
        seollal += (cycles * cycle400)
        while curryear == False:
            if jday - seollal > cycle400:
                year += 400
                seollal += cycle400
            else:
                #year += 1
                if year % 400 == 333:
                    if jday - seollal < 366:
                        curryear = True
                    else:
                        seollal += 366
                        year += 1
                elif year % 100 == 33:
                    if jday - seollal < 365:
                        curryear = True
                    else:
                        seollal += 365
                        year += 1
                elif year % 4 == 1:
                    if jday - seollal < 366:
                        curryear = True
                    else:
                        seollal += 366
                        year += 1
                else:
                    if jday - seollal < 365:
                        curryear = True
                    else:
                        seollal += 365
                        year +=1
        
        if year % 400 == 333:
            # leap year
            m = months.KOREAN_LEAP
        elif year % 100 == 33:
            # not a leap year
            m = months.KOREAN_NORMAL
        elif year % 4 == 1:
            # leap year
            m = months.KOREAN_LEAP
        else:
            # not a leap year
            m = months.KOREAN_NORMAL

    else:
        # negative date
        cycles = (seollal - jday) // cycle400
        year -= (400 * cycles)
        seollal -= (cycles * cycle400)

        while seollal > jday:
            year -= 1
            if abs(year) % 400 == 267:
                seollal -= 366
            elif abs(year) % 100 == 67:
                seollal -= 365
            elif abs(year) % 4 == 3:
                seollal -= 366
            else:
                seollal -= 365
           
        if abs(year) % 400 == 267:
            # leap year
            m = months.KOREAN_LEAP
        elif abs(year) % 100 == 67:
            # not a leap year
            m = months.KOREAN_NORMAL
        elif abs(year) % 4 == 4:
            # leap year
            m = months.KOREAN_LEAP
        else:
            # not leap year
            m = months.KOREAN_NORMAL

    delta = jday - seollal
    for i in m.keys():
        if delta < m[i]:
            month = i
            day = delta + 1
            break
        else:
            delta -= m[i]

    return (day, month, year)
