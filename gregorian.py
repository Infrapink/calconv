#!/usr/bin/python

#
# Convert between the Gregorian Calendar and Julian Day
#

import months

cycle4 = (4 * 365) + 1
cycle100 = (100 * 365) + 24
cycle400 = (400 * 365) + 97

def tojd(day, month, year):

    day = int(day)
    month = month.title()
    year = int(year)
    days = 0

    if year > 0:
        alpha = 1721424
        for y in range(1, year):
            if y % 400 == 0:
                days += 366
            elif y % 100 == 0:
                days += 365
            elif y % 4 == 0:
                days += 366
            else:
                days += 365
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
            
        for i in m.keys():
            if i == month:
                days += day
                break
            else:
                days += m[i]
    else:
        alpha = 1721425
        year = 0 - year

        if (year - 1) % 400 == 0:
            # leap year
            m = months.CAESAR_LEAP
        elif (year - 1) % 100 == 0:
            # not a leap year
            m = months.CAESAR_NORMAL
        elif (year - 1) % 4 == 0:
            # leap year
            m = months.CAESAR_LEAP
        else:
            # not a leap year
            m = months.CAESAR_NORMAL

        for i in m.keys():
            if i == month:
                days += day - 1
                break
            else:
                days += m[i]

        for y in range(0, year):
            if y % 400 == 0:
                days -= 366
            elif y % 100 == 0:
                days -= 365
            elif y % 4 == 0:
                days -= 366
            else:
                days -= 365

    jday = alpha + days
    return jday

def fromjd(jday):
    """Convert a Julian Day to a date in the Gregorian calendar"""
    jday = int(jday)
    year = 0
    month = ""
    day = 0
    current = False

    if jday > 1721424:
        # positive date
        delta = jday - 1721424
        current = False

        while delta > cycle400:
            year += 400
            delta -= cycle400

        while delta > cycle100:
            year += 100
            delta -= cycle100

        while delta > cycle4:
            year += 4
            delta -= cycle4

        while current == False:
            year += 1
            if year % 400 == 0:
                if delta <= 366:
                    current = True
                else:
                    delta -= 366
            elif year % 100 == 0:
                if delta <= 365:
                    current = True
                else:
                    delta -= 365
            elif year % 4 == 0:
                if delta <= 366:
                    current = True
                else:
                    delta -= 366
            else:
                if delta <= 365:
                    current = True
                else:
                    delta -= 365
                    
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

        if delta == 0:
            year -= 1
            if year % 400 == 0:
                delta = 366
                m = months.CAESAR_LEAP
            elif year % 100 == 0:
                delta = 365
                m = months.CAESAR_NORMAL
            elif year % 4 == 0:
                delta = 366
                m = months.CAESAR_LEAP
            else:
                delta = 365
                m = months.CAESAR_NORMAL
                
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    else:
        # negative date
        delta = 1721425 - jday

        while delta > 0:
            if year % 400 == 0:
                year += 1
                delta -= 366
            elif year % 100 == 0:
                year += 1
                delta -= 365
            elif year % 4 == 0:
                year += 1
                delta -= 366
            else:
                year += 1
                delta -= 365

        if (year - 1) % 400 == 0:
            # leap year
            m = months.CAESAR_LEAP
        elif (year - 1) % 100 == 0:
            # not a leap year
            m = months.CAESAR_NORMAL
        elif (year - 1) % 4 == 0:
            # leap year
            m = months.CAESAR_LEAP
        else:
            # not leap year
            m = months.CAESAR_NORMAL

        year = 0 - year
        delta = 0 - delta + 1

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = [day, month, year]
    return(date)
