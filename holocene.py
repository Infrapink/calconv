#!/usr/bin/python3

#
# Convert between the Holocene Calendar and Julian Day
#

import months

cycle4 = (4 * 365) + 1
cycle100 = (100 * 365) + 24
cycle400 = (400 * 365) + 97

epoch = (-1931366)

def tojd(day, month, year):

    day = int(day)
    month = month.title()
    year = int(year)
    jday = epoch

    if year > 0:
        # positive dates
        y = 0
        cycles = (year - y) // 400
        y += (400 * cycles)
        jday += (cycles * cycle400)
        while y < year:
            if year - y > 400:
                y += 400
                jday += cycle400
#            elif year - y > 100:
 #               y += 100
  #              jday += cycle100
   #         elif year - y > 4:
    #            y += 4
     #           jday += cycle4
            elif y % 400 == 0:
                y += 1
                jday += 366
            elif y % 100 == 0:
                y += 1
                jday += 365
            elif y % 4 == 0:
                y += 1
                jday += 366
            else:
                y += 1
                jday += 365

        if year % 400 == 0:
            m = months.CAESAR_LEAP
        elif year % 100 == 0:
            m = months.CAESAR_NORMAL
        elif year % 4 == 0:
            m = months.CAESAR_LEAP
        else:
            m = months.CAESAR_NORMAL
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
                if abs(y) % 400 == 0:
                    jday -= 366
                elif abs(y) % 100 == 0:
                    jday -= 365
                elif abs(y) % 4 == 0:
                    jday -= 366
                else:
                    jday -= 365

        if abs(year) % 400 == 0:
            m = months.CAESAR_LEAP
        elif abs(year) % 100 == 0:
            m = months.CAESAR_NORMAL
        elif abs(year) % 4 == 0:
            m = months.CAESAR_LEAP
        else:
            m = months.CAESAR_NORMAL

    for i in m.keys():
        if i == month:
            jday += day - 1
            break
        else:
            jday += m[i]

    return jday

def fromjd(jday):
    """Convert a Julian Day to a date in the Holocene calendar"""
    jday = int(jday)
    year = 0
    month = ""
    nyd = epoch
    curryear = False

    if jday >= epoch:
        # positive date
        cycles = (jday - nyd) // cycle400
        year += (400 * cycles)
        nyd += (cycles * cycle400)
        while curryear == False:
            if jday - nyd > cycle400:
                year += 400
                nyd += cycle400
            else:
                #year += 1
                if year % 400 == 0:
                    if jday - nyd < 366:
                        curryear = True
                    else:
                        nyd += 366
                        year += 1
                elif year % 100 == 0:
                    if jday - nyd < 365:
                        curryear = True
                    else:
                        nyd += 365
                        year += 1
                elif year % 4 == 0:
                    if jday - nyd < 366:
                        curryear = True
                    else:
                        nyd += 366
                        year += 1
                else:
                    if jday - nyd < 365:
                        curryear = True
                    else:
                        nyd += 365
                        year +=1
        
        if year % 400 == 0:
            # leap year
            m = months.CAESAR_LEAP
        elif year % 100 == 0:
            # not a leap year
            m = months.CAESAR_NORMAL
        elif year % 4 == 0:
            # leap year
            m = months.CAESAR_LEAP
        else:
            # not a leap year
            m = months.CAESAR_NORMAL

    else:
        # negative date
        cycles = (nyd - jday) // cycle400
        year -= (400 * cycles)
        nyd -= (cycles * cycle400)

        while nyd > jday:
            year -= 1
            if abs(year) % 400 == 0:
                nyd -= 366
            elif abs(year) % 100 == 0:
                nyd -= 365
            elif abs(year) % 4 == 0:
                nyd -= 366
            else:
                nyd -= 365
           
        if abs(year) % 400 == 0:
            # leap year
            m = months.CAESAR_LEAP
        elif abs(year) % 100 == 0:
            # not a leap year
            m = months.CAESAR_NORMAL
        elif abs(year) % 4 == 0:
            # leap year
            m = months.CAESAR_LEAP
        else:
            # not leap year
            m = months.CAESAR_NORMAL

    delta = jday - nyd
    for i in m.keys():
        if delta < m[i]:
            month = i
            day = delta + 1
            break
        else:
            delta -= m[i]

    return (day, month, year)
