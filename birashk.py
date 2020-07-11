#!/usr/bin/python

import months
import leap_years_birashk

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
            m = months.SOLAR_HIJRI_LEAP
        else:
            # not a leap year
            m = months.SOLAR_HIJRI_NORMAL

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
            m = months.SOLAR_HIJRI_LEAP
            days -= 367 # subtract 367 rather than 366 to avoid a fencepost error
        else:
            # not a leap year
            m = months.SOLAR_HIJRI_NORMAL
            days -= 366 # subtract 366 rathger than 365 to avoid a fencepost error

        for i in m.keys():
            if i == month:
                days += day
                break
            else:
                days += m[i]

    jday = days + alpha
    return jday

def fromjd(jday):
    jday = int(jday)
    day = 0
    month = ""
    year = 0
    delta = jday - 1948319 # days that have passed, starting on 1/1/1

    # I tried to be smart anc calculate by cycles and subcycles, but Python apparently gets confused when you go too many levels deep in if..else statements, so screw it I'm just going to use one big 2820-year cycle.

    if delta > 0:
        great_cycles = delta // cycle2820
        delta %= cycle2820

        for y in range(1,2821):
            if y in leap_years_birashk.ah:
                if delta <= 366:
                    # leap year
                    single_year = y
                    m = months.SOLAR_HIJRI_LEAP
                    break
                else:
                    delta -= 366
            else:
                if delta <= 365:
                    # not a leap year
                    single_year = y
                    m = months.SOLAR_HIJRI_NORMAL
                    break
                else:
                    delta -= 365

        year = (great_cycles * 2820) + single_year
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
        delta = 0 - delta # module operator doesn't place nicely with negative numbers
        great_cycles = delta // cycle2820
        delta %= cycle2820

        for y in range(0,2820):
            if y in leap_years_birashk.bh:
                if delta <= 366:
                    # leap year
                    single_year = y
                    m = months.SOLAR_HIJRI_LEAP
                    delta = 366 - delta
                    if delta == 0:
                        delta = 1
                    break
                else:
                    delta -= 366
            else:
                if delta <= 365:
                    # not a leap year
                    single_year = y
                    m = months.SOLAR_HIJRI_NORMAL
                    delta = 366 - delta
                    break
                else:
                    delta -= 365

        year = (great_cycles * 2820) + single_year
        year = 0 - year - 1

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = [day,month,year]
    return date
