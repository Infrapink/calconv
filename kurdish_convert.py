#!/usr/bin/python

#
# Convert a date in the Kurdish Calendar to Julian Day

import months

def convert(day, month, year):
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
        alpha = 1497975
        for y in range(1,year):
            if (y % 33) in leap_years_an:
                days += 366
            else:
                days += 365

        if (year % 33) in leap_years_an:
            # leap year
            m = months.KURDISH_MONTHS_LEAP
        else:
            # not a leap eyar
            m = months.KURDISH_MONTHS_NORMAL

        for i in m.keys():
            if i == month:
                days += day
                break
            else:
                days += m[i]

    else:
        # negative years
        alpha = 1497976
        year = abs(year) # modulo operator doesn't play nicely with negative numbers
        if (year % 33) in leap_years_an:
            # leap year
            m = months.KURDISH_MONTHS_LEAP
        else:
            # nto a leap year
            m = months.KURDISH_MONTHS_NORMAL

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
