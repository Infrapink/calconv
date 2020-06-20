#!/usr/bin/python

import months
import leap_years_birashk

def convert(day,month,year):
    day = int(day)
    month = month.title()
    year = int(year)
    days = 0
    alpha = 1948319

    cycle4 = (4 * 365) + 1
    cycle5 = (5 * 365) + 1
    cycle29 = (6 * cycle4) + cycle5
    cycle33 = (7 * cycle4) + cycle5
    cycle37 = (8 * cycle4) + cycle5

    if year > 0:
        for y in range(1,year):
            if (y % 2820) in leap_years_birashk.ah:
                days += 366
            else:
                days += 365

        if (year % 2820) in leap_years_birashk.ah:
            # leap year
            m = months.SOLAR_HIJRI_MONTHS_LEAP
        else:
            # not a leap year
            m = months.SOLAR_HIJRI_MONTHS_NORMAL

        for i in m.keys():
            if i == month:
                days += day
                break
            else:
                days += m[i]

    else:
        year = 0 - year - 1 # modulo operator doesn't play nicely with negative numebrs
        for y in range (0, year):
            if (y % 2820) in leap_years_birashk.bh:
                days -= 366
            else:
                days -= 365

        if year in leap_years_birashk.bh:
            # leap year
            m = months.SOLAR_HIJRI_MONTHS_LEAP
            days -= 367 # subtract 367 rather than 366 to avoid a fencepost error
        else:
            # not a leap year
            m = months.SOLAR_HIJRI_MONTHS_NORMAL
            days -= 366 # subtract 366 rathger than 365 to avoid a fencepost error

        for i in m.keys():
            if i == month:
                days += day
                break
            else:
                days += m[i]

    jday = days + alpha
    return jday
