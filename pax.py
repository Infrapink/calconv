#!/usr/bin/python

#
# Convert between the Pax calendar and Julian day
#

import months

def tojd(day, month, year):
    day = int(day)
    month = month
    year = int(year)
    lear = abs(year) % 100 # use to check leap years
    days = 0

    leap_digits_ad = (0,6,12,18,24,30,36,42,48,54,60,66,72,78,84,90,96,99)
    leap_digits_bc = (0,94,88,82,76,70,64,58,52,46,40,34,28,22,16,10,4,1)

    if year >= 0:
        # positive dates
        alpha = 1721060

        for y in range(0, year):
            if y % 400 == 0:
                days += 364
            elif y % 100 in leap_digits_ad:
                days += 371
            else:
                days += 364

        if year % 400 == 0:
            # not a leap year
            m = months.PAX_NORMAL
        elif year % 100 in leap_digits_ad:
            # leap year
            m = months.PAX_LEAP
        else:
            # not a leap year
            m = months.PAX_NORMAL
        for i in m.keys():
            if i == month:
                days += day
                break
            else:
                days += m[i]

    else:
        # negative dates
        alpha = 1721061
        year = 0 - year

        for y in range(1, year + 1):
            if y % 400 == 0:
                days -= 364
            elif y % 100 in leap_digits_bc:
                days -= 371
            else:
                days -= 364

        if year % 400 == 0:
            # not a leap year
            m = months.PAX_NORMAL
        elif year % 100 in leap_digits_bc:
            # leap year
            m = months.PAX_LEAP
        else:
            # not a leap year
            m = months.PAX_NORMAL

        for i in m.keys():
            if i == month:
                days += day - 1
                break
            else:
                days += m[i]

    jday = days + alpha
    return jday

def fromjd(jday):
    """Convert a Julian day to a date in the Pax calendar."""
    jday = int(jday)
    year = 0
    month = ""
    day = 0
    current = False

    leap_digits_ad = (0,6,12,18,24,30,36,42,48,54,60,66,72,78,84,90,96,99)
    leap_digits_bc = (0,94,88,82,76,70,64,58,52,46,40,34,28,22,16,10,4,1)
    
    if jday > 1721060:
        delta = jday - 1721060
        # positive dates
        while current == False:
            if year % 400 == 0:
                if delta <= 364:
                    current = True
                    break
                else:
                    delta -= 364
            elif year % 100 in leap_digits_ad:
                if delta <= 371:
                    current = True
                    break
                else:
                    delta -= 371
            else:
                if delta <= 364:
                    current = True
                    break
                else:
                    delta -= 364
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

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    else:
        # negative dates
        delta = 1721061 - jday
        while delta > 0:
            year -= 1
            if abs(year) % 400 == 0:
                delta -= 364
            elif abs(year) % 100 in leap_digits_bc:
                delta -= 371
            else:
                delta -= 364

        if abs(year) % 400 == 0:
            # not a leap year
            m = months.PAX_NORMAL
        elif abs(year) % 100 in leap_digits_bc:
            # leap year
            m = months.PAX_LEAP
        else:
            # not a leap yer
            m = months.PAX_NORMAL

        delta = 0 - delta + 1

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = (day, month, year)
    return date
