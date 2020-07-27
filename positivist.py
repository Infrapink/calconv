#!/usr/bin/python

#
# Convert between the Positivist Calendar and Julian Day
#

import months

cycle4 = (4 * 365) + 1
cycle100 = (100 * 365) + 24
cycle400 = (400 * 365) + 97

def tojd(day, month, year):

    day = int(day)
    month = month
    year = int(year)
    days = 0

    if year >= 0:
        alpha = 2374478
        for y in range(0, year):
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
            m = months.POSITIVIST_LEAP
        elif year % 100 == 0:
            # not a leap year
            m = months.POSITIVIST_NORMAL
        elif year % 4 == 0:
            # leap year
            m = months.POSITIVIST_LEAP
        else:
            # not a leap year
            m = months.POSITIVIST_NORMAL

        for i in m.keys():
            if i == month:
                days += day
                break
            else:
                days += m[i]
    else:
        alpha = 2374479
        year = 0 - year

        for y in range(1, year + 1):
            if y % 400 == 0:
                days -= 366
            elif y % 100 == 0:
                days -= 365
            elif y % 4 == 0:
                days -= 366
            else:
                days -= 365        

        if year % 400 == 0:
            # leap year
            m = months.POSITIVIST_LEAP
        elif year % 100 == 0:
            # not a leap year
            m = months.POSITIVIST_NORMAL
        elif year % 4 == 0:
            # leap year
            m = months.POSITIVIST_LEAP
        else:
            # not a leap year
            m = months.POSITIVIST_NORMAL

        for i in m.keys():
            if i == month:
                days += day - 1
                break
            else:
                days += m[i]

    jday = alpha + days
    return jday

def fromjd(jday):
    """Convert a Julian Day to a date in the Positivist calendar"""
    jday = int(jday)
    year = 0
    month = ""
    day = 0

    if jday > 2374478:
        # positive date
        delta = jday - 2374478
        current = False

        while current == False:
            if year % 400 == 0:
                if delta <= 366:
                    current = True
                    break
                else:
                    delta -= 366
            elif year % 100 == 0:
                if delta <= 365:
                    current = True
                    break
                else:
                    delta -= 365
            elif year % 4 == 0:
                if delta <= 366:
                    current = True
                    break
                else:
                    delta -= 366
            else:
                if delta <= 365:
                    current = True
                    break
                else:
                    delta -= 365
            year += 1

        if year % 400 == 0:
            # leap year
            m = months.POSITIVIST_LEAP
        elif year % 100 == 0:
            # not a leap year
            m = months.POSITIVIST_NORMAL
        elif year % 4 == 0:
            # leap year
            m = months.POSITIVIST_LEAP
        else:
            # not a leap year
            m = months.POSITIVIST_NORMAL

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    else:
        # non-positive date
        delta = 2374479 - jday
        current = False
        year += 1

        while delta > 0:
            if year % 400 == 0:
                if delta <= 366:
                    m = months.POSITIVIST_LEAP
                    delta = 367 - delta
                    break
                else:
                    delta -= 366
            elif year % 100 == 0:
                if delta <= 365:
                    m = months.POSITIVIST_NORMAL
                    delta = 366 - delta
                    break
                else:
                    delta -= 365
            elif year % 4 == 0:
                if delta <= 366:
                    m = months.POSITIVIST_LEAP
                    delta = 367 - delta
                    break
                else:
                    delta -= 366
            else:
                if delta <= 365:
                    m = months.POSITIVIST_NORMAL
                    delta = 366 - delta
                    break
                else:
                    delta -= 365
            year += 1

        year = 0 - year

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = (day, month, year)
    return(date)
