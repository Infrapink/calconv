#!/usr/bin/python

# # Convert a date in the Babylonian Calendar to a Julian Day
#

import months

def convert(day, month, year):
    day = int(day)
    month = month
    year = int(year)
    days = 0

    leap_years_pd = (3,6,8,11,14,17,19,0)
    leap_years_ad = (1,3,6,9,12,14,17)
    leap_years_zo = (0,2,5,8,11,13,16)

    if year > 0:
        # positive year
        alpha = -210264

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
            m = months.BABYLONIAN_MONTHS_LEAP_17
        elif (year % 19) in leap_years_pd:
            m = months.BABYLONIAN_MONTHS_LEAP
        else:
            m = months.BABYLONIAN_MONTHS_NORMAL

        for i in m.keys():
            if i == month:
                days += day
                break
            else:
                days += m[i]

    else:
        # negative years
        alpha = -210263
        year = 0 - year

        if month == "Ulūlu Arku":
            if (year % 19) != 3:
                month = "Ulūlu"

        if month == "Addaru Arku":
            if (year % 19) not in (1,6,9,12,14,17):
                month = "Addaru"
                
        if (year % 19) == 3:
            m = months.BABYLONIAN_MONTHS_LEAP_17
        elif (year % 19) in leap_years_ad:
            m = months.BABYLONIAN_MONTHS_LEAP
        else:
            m = months.BABYLONIAN_MONTHS_NORMAL

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
