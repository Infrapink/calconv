#!/usr/bin/python

#
# Convert between Julian days and Ahmad Birashk's calendar
#

import months
import leap_years_birashk

epoch = 1948320

cycle4 = (4 * 365) + 1
cycle5 = (365 * 5) + 1
cycle33 = (7 * cycle4) + cycle5
cycle29 = (6 * cycle4) + cycle5
cycle37 = (8 * cycle4) + cycle5
cycle128 = (3 * cycle33) + cycle29
cycle132 = (2 * cycle33) + cycle29 + cycle37
cycle2820 = (21 * cycle128) + cycle132

def tojd(day,month,year):
    day = int(day)
    month = month.title()
    year = int(year)
    jday = epoch

    if year > 0:
        y = 1
        while y < year:
            if year - y > 2820:
                y += 2820
                jday += cycle2820
            elif y % 2820 in leap_years_birashk.ah:
                y += 1
                jday += 366
            else:
                y += 1
                jday += 365

        if (year % 2820) in leap_years_birashk.ah:
            # leap year
            m = months.IRANIAN_LEAP
        else:
            # not a leap year
            m = months.IRANIAN_NORMAL

    else:
        y = 0
        while y > year:
            if y - year > 2820:
                y -= 2820
                jday -= cycle2820
            else:
                y -= 1
                if abs(y) % 2820 in leap_years_birashk.bh:
                    jday -= 366
                else:
                    jday -= 365

        if abs(year) % 2820 in leap_years_birashk.bh:
            # leap year
            m = months.IRANIAN_LEAP
        else:
            # not a leap year
            m = months.IRANIAN_NORMAL

    for i in m.keys():
        if i == month:
            jday += day - 1
            break
        else:
            jday += m[i]

    return jday

def fromjd(jday):
    jday = int(jday)
    day = 0
    month = ""
    year = 0
    nowruz = epoch

    if jday >= epoch:
        # positive dates
        year = 1
        curryear = False
        while curryear == False:
            if jday - nowruz > cycle2820:
                year += 2820
                nowruz += cycle2820
            elif year % 2820 in leap_years_birashk.ah:
                if jday - nowruz <= 366:
                    curryear = True
                else:
                    year += 1
                    nowruz += 366
            else:
                if jday - nowruz <= 365:
                    curryear = True
                else:
                    year += 1
                    nowruz += 365

        if year % 2820 in leap_years_birashk.ah:
            m = months.IRANIAN_LEAP
        else:
            m = months.IRANIAN_NORMAL

    else:
        # negative dates
        while nowruz > jday:
            if nowruz - jday > cycle2820:
                nowruz -= cycle2820
                year -= 2820
            else:
                year -= 1
                if abs(year) % 2820 in leap_years_birashk.bh:
                    nowruz -= 366
                else:
                    nowruz -= 365

        if abs(year) % 2820 in leap_years_birashk.bh:
            m = months.IRANIAN_LEAP
        else:
            m = months.IRANIAN_NORMAL

    delta = jday - nowruz
    for i in m.keys():
        if delta < m[i]:
            month = i
            day = delta + 1
            break
        else:
            delta -= m[i]

    return (day, month, year)
