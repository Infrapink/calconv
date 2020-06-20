#!/usr/bin/python

##
## This converts a Lunar Hijri date to a Julian Day.
##

import months

def convert(day, month, year):
    day = int(day)
    month = month
    year = int(year)
    alpha = 1948438
    days = 0
    cycle30 = (30 * 354) + 11
    leap_years_ah = (2,5,7,10,13,16,18,21,24,26,29)
    leap_years_bh = (1,4,6,9,12,15,17,20,23,25,28)

    if year > 0:
        for y in range(1,year):
            if (y % 30) in leap_years_ah:
                days += 355
            else:
                days += 354
        if year in leap_years_ah:
            # leap year
            m = months.LUNAR_HIJRI_MONTHS_LEAP
        else:
            # not a leap year
            m = months.LUNAR_HIJRI_MONTHS_NORMAL

        for i in m.keys():
            if i == month:
                days += day
                break
            else:
                days += m[i]
    else:
        year = 0 - year # modulo operator doesn't play nicely with negative numbers
        for y in range(0,year):
            if (y % 30) in leap_years_bh:
                days -= 355
            else:
                days -= 354
        if year in leap_years_bh:
            # leap year
            #days -= 356
            m = months.LUNAR_HIJRI_MONTHS_LEAP
        else:
            # not a leap year
            #days -= 355
            m = months.LUNAR_HIJRI_MONTHS_NORMAL
        for i in m.keys():
            if i == month:
                days += day
                break
            else:
                days += m[i]
    jday = days + alpha
    return jday

