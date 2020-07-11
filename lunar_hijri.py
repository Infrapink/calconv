#!/usr/bin/python

##
## This converts a Lunar Hijri date to a Julian Day.
##

import months

cycle30 = (30 * 354) + 11

def tojd(day, month, year):
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
            m = months.ARAB_LEAP
        else:
            # not a leap year
            m = months.ARAB_NORMAL

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
            m = months.ARAB_LEAP
        else:
            # not a leap year
            #days -= 355
            m = months.ARAB_NORMAL
        for i in m.keys():
            if i == month:
                days += day
                break
            else:
                days += m[i]
    jday = days + alpha
    return jday

def fromjd(jday):
    """Convert a Julian Day to a date in the Lunar Hijri calendar."""
    jday = int(jday)
    day = 0
    month = ""
    year = 0
    single_year = 0
    leap_years_ah = (2, 5, 7, 10, 13, 16, 18, 21, 24, 26, 29)
    leap_years_bh = (2, 5, 7, 10, 13, 15, 18, 21, 24, 26, 29)
    leap_years_zero = (1, 4, 6, 9, 12, 14, 17, 20, 23, 25, 28)

    if jday > 1948438:
        # positive year
        delta = jday - 1948438
        cycles = delta // cycle30
        delta = delta % cycle30
        m = None
        for y in range(1, 31):
            if y in leap_years_ah:
                if delta <= 355:
                    # leap year
                    m = months.ARAB_LEAP
                    single_year = y
                    break
                else:
                    delta -= 355
            else:
                if delta <= 354:
                    # not a leap year
                    m = months.ARAB_NORMAL
                    single_year = y
                    break
                else:
                    delta -= 354
        year = (cycles * 30) + single_year
        if delta == 0:
            delta = 354
            year -= 1
            
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]
    else:
        # negative year
        delta = 1948439 - jday
        while delta > 0:
            if (year % 30) in leap_years_zero:
                year += 1
                delta -= 355
            else:
                year += 1
                delta -= 354
            
        if (year % 30) in leap_years_bh:
            # leap year
            m = months.ARAB_LEAP
        else:
            m = months.ARAB_NORMAL
                
        year = 0 - year
        delta = 0 - delta + 1
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = (day, month, year)
    return date
