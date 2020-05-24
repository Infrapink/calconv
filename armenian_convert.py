#!/usr/bin/python

import months

def convert(day, month, year):
    alpha = 1922866
    day = int(day)
    month = month.title()
    year = int(year)
    days = 0
    jday = 0
    m = months.ARMENIAN_MONTHS

    if year > 0:
        days = (year - 1) * 365 # have to subtract 1 to account for the lack of year 0
        for i in m.keys():
            if i == month:
                days += day
                break
            else:
                days += m[i]
        else:
            year = 1 - year
            days = year * 365
            for i in m.keys():
                if i == month:
                    days -= day
                    break
                else:
                    days -= m[i]

    jday = days + alpha
    return jday
