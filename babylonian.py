#!/usr/bin/python

# # Convert a date in the Babylonian Calendar to a Julian Day
#

import months

cycle19 = (12 * 354) + (7 * 383)

def tojd(day, month, year):
    day = int(day)
    month = month
    year = int(year)
    days = 0

    leap_years_pd = (3,6,8,11,14,17,19,0)
    leap_years_ad = (1,3,6,9,12,14,17)
    leap_years_zo = (0,2,5,8,11,13,16)

    if year > 0:
        # positive year
        alpha = -210488

        if month == "Ulūlu Arku":
            if (year % 19) != 17:
                month = "Ulūlu"

        if month == "Addaru Arku":
            if (year % 19) not in (3,6,8,11,14,19,0):
                month = "Addaru"
                
        for y in range(1,year):
            if (y % 19) in leap_years_pd:
                days += 383
            else:
                days += 354

        if (year % 19) == 17:
            m = months.BABYLONIAN_LEAP_17
        elif (year % 19) in leap_years_pd:
            m = months.BABYLONIAN_LEAP
        else:
            m = months.BABYLONIAN_NORMAL

        for i in m.keys():
            if i == month:
                days += day
                break
            else:
                days += m[i]

    else:
        # negative years
        alpha = -210487
        year = 0 - year

        if month == "Ulūlu Arku":
            if (year % 19) != 3:
                month = "Ulūlu"

        if month == "Addaru Arku":
            if (year % 19) not in (1,6,9,12,14,17):
                month = "Addaru"
                
        if (year % 19) == 3:
            m = months.BABYLONIAN_LEAP_17
        elif (year % 19) in leap_years_ad:
            m = months.BABYLONIAN_LEAP
        else:
            m = months.BABYLONIAN_NORMAL

        for i in m.keys():
            if i == month:
                days += day
                break
            else:
                days += m[i]

        for y in range(0,year):
            if (y % 19) in leap_years_zo:
                days -= 383
            else:
                days -= 354

    jday = alpha + days
    return jday

def fromjd(jday):
    """Convert a Julian Day to a date in the Babylonian calendar."""
    jday = int(jday)
    day = 0
    month = ""
    year = 0
    leap_years_pd = (3,6,8,11,14,17,19,0)
    leap_years_ad = (1,3,6,9,12,14,17)
    leap_years_zo = (0,2,5,8,11,13,16)

    # Years 17 PD, 3 AD, and 2 ZO are the ones where Veululu and not Veadar is the leap month

    if jday > -210488: #-210264:
        # positive year
        delta = jday - -210488 #-210264
        cycles = delta // cycle19
        delta %= cycle19

        for y in range (1,20):
            if y == 17:
                if delta <= 383:
                    m = months.BABYLONIAN_LEAP_17
                    single_year = y
                    break
                else:
                    delta -= 383
            elif y in leap_years_pd:
                if delta <= 383:
                    # leap year
                    m = months.BABYLONIAN_LEAP
                    single_year = y
                    break
                else:
                    delta -= 383
            else:
                if delta <= 354:
                    # not a leap year
                    m = months.BABYLONIAN_NORMAL
                    single_year = y
                    break
                else:
                    delta -= 354

        year = (19 * cycles) + single_year
        if delta == 0:
            year -= 1
            if (year % 19) == 17:
                delta = 383
                m = months.BABYLONIAN_LEAP_17
            elif (year % 19) in leap_years_pd:
                m = months.BABYLONIAN_LEAP
                delta = 383
            else:
                m = months.BABYLONIAN_NORMAL
                delta = 353

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]
                

    else:
        #delta = -210263 - jday
        delta = -210487 - jday
        while delta > 0:
            if (year % 19) in leap_years_zo:
                year += 1
                delta -= 383
            else:
                year += 1
                delta -= 354

        if (year % 19) in leap_years_ad:
            # leap year
            m = months.BABYLONIAN_LEAP
        else:
            # not a leap year
            m = months.BABYLONIAN_NORMAL

        year = 0 - year
        delta = 0 - delta
        if delta == 0:
            year -= 1
            if (year % 19) == 2:
                m = months.BABYLONIAN_LEAP_17
                delta = 383
            elif (year % 19) in leap_years_ad:
                m = months.BABYLONIAN_LEAP
                delta = 383
            else:
                m = months.BABYLONIAN_NORMAL
                delta = 354
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = (day,month,year)
    return date
