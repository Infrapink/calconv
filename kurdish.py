#!/usr/bin/python

#
# Convert between the Kurdish Calendar and Julian Day
#

import months

cycle4 = (4 * 365) + 1
cycle5 = (365 * 5) + 1
cycle33 = (7 * cycle4) + cycle5

def tojd(day, month, year):
    day = int(day)
    month = month
    year = int(year)
    days = 0

    leap_years_an = (2,6,10,14,18,23,27,31)
    leap_years_bn = (3,7,11,16,20,24,28,32)
    leap_years_zo = (2,6,10,15,19,23,27,31)

    cycle4 = (4 * 365) + 1
    cycle5 = (5 * 365) + 1
    cycle33 = (7 * cycle4) + cycle5

    if year > 0:
        # positive years
        alpha = 1497974
        for y in range(1,year):
            if (y % 33) in leap_years_an:
                days += 366
            else:
                days += 365

        if (year % 33) in leap_years_an:
            # leap year
            m = months.KURDISH_LEAP
        else:
            # not a leap eyar
            m = months.KURDISH_NORMAL

        for i in m.keys():
            if i == month:
                days += day
                break
            else:
                days += m[i]

    else:
        # negative years
        alpha = 1497975
        year = abs(year) # modulo operator doesn't play nicely with negative numbers
        if (year % 33) in leap_years_an:
            # leap year
            m = months.KURDISH_LEAP
        else:
            # nto a leap year
            m = months.KURDISH_NORMAL

        for i in m.keys():
            if i == month:
                days += day - 1
                break
            else:
                days += m[i]

        for y in range(0,year):
            if (y % 33) in leap_years_zo:
                days -= 366
            else:
                days -= 365

    jday = days + alpha
    return jday

def fromjd(jday):
    """Convert a Julian Day into a date in the Kurdish calendar."""
    jday = int(jday)
    day = 0
    month = 0
    year = 0

    leap_years_an = (2,6,10,14,18,23,27,31)
    leap_years_bn = (3,7,11,16,20,24,28,32)
    leap_years_zo = (2,6,10,15,19,23,27,31)

    if jday > 1497974:
        # positive date
        delta = jday - 1497974
        cycles = delta // cycle33
        delta %= cycle33
        for y in range(1,34):
            if y in leap_years_an:
                if delta <= 366:
                    # leap year
                    single_years = y
                    m = months.KURDISH_LEAP
                    break
                else:
                    delta -= 366
            else:
                if delta <= 365:
                    # not a leap year
                    single_years = y
                    m = months.KURDISH_NORMAL
                    break
                else:
                    delta -= 365

        year = (33 * cycles) + single_years
        if delta == 0:
            year -= 1
            if (year % 19) in leap_years_an:
                delta = 366
                m = months.KURDISH_LEAP
            else:
                delta = 365
                m = months.KURDISH_NORMAL
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    else:
        # negative dates
        delta = 1497975 - jday
        while delta > 0:
            if (abs(year) % 33) in leap_years_zo:
                year -= 1
                delta -= 366
            else:
                year -= 1
                delta -= 365

        if (abs(year) % 19) in leap_years_bn:
            # leap year
            m = months.KURDISH_LEAP
        else:
            # not a leap year
            m = months.KURDISH_NORMAL

        delta = abs(delta) + 1
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = (day,month,year)
    return date

