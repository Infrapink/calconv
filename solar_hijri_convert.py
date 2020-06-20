#!/usr/bin/python

#
# Convert a date in the Solar Hijri Calendar to Julian Day

import months

def convert(day, month, year):
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
            m = months.SOLAR_HIJRI_MONTHS_LEAP
        else:
            m = months.SOLAR_HIJRI_MONTHS_NORMAL

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
            m = months.SOLAR_HIJRI_MONTHS_LEAP
        else:
            # not a leap year
            m = months.SOLAR_HIJRI_MONTHS_NORMAL

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
