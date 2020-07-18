#!/usr/bin/python

#
# Convert between the Solar Hijri Calendar and Julian Day
#

import months

cycle4 = (4 * 365) + 1
cycle5 = (365 * 5) + 1
cycle33 = (7 * cycle4) + cycle5

def tojd(day, month, year):
    day = int(day)
    month = month.title()
    year = int(year)
    days = 0

    leap_years_ah = (5,9,13,17,21,25,29,33,0)
    leap_years_zero = (0,4,8,12,16,20,24,28)
    leap_years_bh = (1,5,9,13,17,21,25,29)

    cycle4 = (4 * 365) + 1
    cycle5 = (365 * 5) + 1
    cycle33 = (7 * cycle4) + cycle5

    if year > 0:
        # positive years
        alpha = 1948319
        for y in range(1,year):
            if (y % 33) in leap_years_ah:
                days += 366
            else:
                days += 365

        if (year % 33) in leap_years_ah:
            # leap year
            m = months.SOLAR_HIJRI_LEAP
        else:
            m = months.SOLAR_HIJRI_NORMAL

        for i in m.keys():
            if i == month:
                days += day
                break
            else:
                days += m[i]

    else:
        # negative years
        alpha = 1948320
        year = 0 - year # modulo operator doesn't play nicely with negative numbers
        if (year % 33) in leap_years_bh:
            # leap year
            m = months.SOLAR_HIJRI_LEAP
        else:
            # not a leap year
            m = months.SOLAR_HIJRI_NORMAL

        for i in m.keys():
            if i == month:
                days += day - 1
                break
            else:
                days += m[i]
        for y in range(0,year):
            if y % 33 in leap_years_zero:
                days -= 366
            else:
                days -= 365

    jday = alpha + days
    return jday

def fromjd(jday):
    """Convert a Julian Day to a date in the Solar Hijri calendar."""
    jday = int(jday)
    day = 0
    month = ""
    year = 0

    leap_years_ah = (5,9,13,17,21,25,29,33)
    leap_years_zero = (0,4,8,12,16,20,24,28)
    leap_years_bh = (1,5,9,13,17,21,25,29)

    if jday > 1948319:
        # positive date
        delta = jday - 1948319
        cycles = delta // cycle33
        delta %= cycle33
        for y in range(1,34):
            if y in leap_years_ah:
                if delta <= 366:
                    # leap year
                    single_years = y
                    m = months.SOLAR_HIJRI_LEAP
                    break
                else:
                    delta -= 366
            else:
                if delta <= 365:
                    # not a leap year
                    single_years = y
                    m = months.SOLAR_HIJRI_NORMAL
                    break
                else:
                    delta -= 365
        year = (33 * cycles) + single_years
        if delta == 0:
            delta = 365
            year -= 1
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]
    else:
        # negative date
        delta = 1948320 - jday

        while delta > 0:
            if (year % 33) in leap_years_zero:
                year += 1
                delta -= 366
            else:
                year += 1
                delta -= 365

        if year in leap_years_bh:
            # leap year
            m = months.SOLAR_HIJRI_LEAP
        else:
            # not a leap year
            m = months.SOLAR_HIJRI_NORMAL

        year = 0 - year
        delta = 0 - delta + 1
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]
    date = (day,month,year)
    return date
