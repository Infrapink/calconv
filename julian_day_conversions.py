#!/usr/bin/python

import months

cycle4 = (4 * 365) + 1
cycle100 = (100 * 365) + 24
cycle400 = (400 * 365) + 97

def julian_day_to_julian(jday):
    """Convert the Julian Day to a date in the Julian Calendar"""
    alpha = int(jday)
    year = 0
    month = ""
    day = 0
    m = None
    d = 0

    # number of days that have passed since day 31/Dec/1 BC
    delta = alpha - 1721422

    if delta > 0:
        year_4 = delta // cycle4
        delta = delta % cycle4
        single_years = delta // 365
        single_years += 1 # need to add 1 to account for the lack of year 0
        delta = delta % 365
        year =  (4 * year_4) + single_years
        if year % 4 == 0:
            # leap year
            m = months.CAESAR_MONTHS_LEAP
        else:
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]
    elif delta <= 0:
        delta = 0 - delta # modulo operator doesn't play nicely with negative numbers
        year_4 = delta // cycle4
        delta = delta % cycle4
        single_years = delta // 365
        delta = delta % 365
        year = (4 * year_4) + single_years # won't correct for lack of year 0 just yet to make leap years easier
        if year % 4 == 0:
            # leap year
            m = months.CAESAR_MONTHS_LEAP
            d = 366
        else:
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL
            d = 365
        year = 0 - year - 1 # have to deduct 1 to account for the lack of year 0
        delta = d - delta
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = [day, month, year]
    return(date)

def julian_day_to_gregorian(jday):
    """Convert a Julian Day to a date in the Gregorian calendar"""
    alpha = int(jday)
    year = 0
    month = ""
    day = 0
    m = None
    d = 0
    leap = None

    # number of days that have passed since 31/Dec/1 BC
    delta = alpha - 1721424 # apparently 01/Jan/1 in the Gregorian calendar is 03/Jan/1 in the Julian calendar
    if delta > 0:
        year_400 = delta // cycle400
        delta = delta % cycle400
        year_100 = delta // cycle100
        delta = delta % cycle100
        year_4 = delta // cycle4
        delta = delta % cycle4
        single_years = delta // 365
        delta = delta % 365
        year = (400 * year_400) + (100 * year_100) + (4 * year_4) + single_years + 1 # need to add 1 to account for the lack of year 0

        if year % 400 == 0:
            # leap year
            leap = True
        elif year % 100 == 0:
            # not a leap year
            leap = False
        elif year % 4 == 0:
            # leap year
            leap = True
        else:
            # not a leap year
            leap = False

        if leap == True:
            m = months.CAESAR_MONTHS_LEAP
        else:
            m = months.CAESAR_MONTHS_NORMAL
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    elif delta <= 0:
        delta = 0 - delta # modulo operator doesn't play nicely with negative numbers
        year_400 = delta // cycle400
        delta = delta % cycle400
        year_100 = delta // cycle100
        delta = delta % cycle100
        year_4 = delta // cycle4
        delta = delta % cycle4
        single_years = delta // 365
        delta = delta % 365
        year = (400 * year_400) + (100 * year_100) + (4 * year_4) + single_years # don't add the corrective year just yet
        if year	% 400 == 0:
            # leap year
            leap = True
        elif year % 100 == 0:
            # not a leap year                                                                                       
            leap = False
        elif year % 4 == 0:
            # leap year                                                                                             
            leap = True
        else:
            # not a leap year                                                                                       
            leap = False

        year = 0 - year - 1 # have to subtract 1 to account for the lack of year 0
        if leap == True:
            m = months.CAESAR_MONTHS_LEAP
            delta = 366 - delta
        else:
            m = months.CAESAR_MONTHS_NORMAL
            delta = 365 - delta

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = [day, month, year]
    return(date)

def julian_day_to_coptic(jday):
    """Convert a Julian Day to a date in the Coptic Calendar"""
    alpha = int(jday)
    delta = alpha - 1825028 # days that have passed since day 0
    day = 0
    month = ""
    year = 0
    d = 0
    m = None

    if delta > 0:
        year_4 = delta // cycle4
        delta = delta % cycle4
        single_years = delta // 365
        delta = delta % 365
        year = (4 * year_4) + single_years + 1 # add 1 year to account for the lack of year 0
        if year % 4 == 0:
            # leap year
            m = months.COPTIC_MONTHS_LEAP
        else:
            # not a leap year
            m = months.COPTIC_MONTHS_NORMAL

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    elif delta <= 0:
        delta = 0 - delta # modulo operator doesn't play nicely with negative numbers
        year_4 = delta // cycle4
        delta = delta % cycle4
        single_years = delta // 365
        delta = delta % 365
        year = (4 * year_4) + single_years # won't correct for the lack of year 0 just yet to make it easier to determine leap years
        if year % 4 == 0:
            # leap year
            m = months.COPTIC_MONTHS_LEAP
            d = 366
        else:
            # not a leap year
            m = months.COPTIC_MONTHS_NORMAL
            d = 365
        year = 0 - year - 1 # deduct 1 to account for the lack of year 0
        delta = d - delta
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = [day, month, year]
    return(date)

def julian_day_to_ethiopian(jday):
    """Convert a Julian Day to a date in the Ethiopian calendar"""
    alpha = int(jday)
    year = 0
    month = ""
    day = 0
    m = None
    d = 0

    # Number of days that have passed since the end of 1 BC
    delta = alpha - 1724221

    if delta > 0:
        year_4 = delta // cycle4
        delta = delta % cycle4
        single_years = delta // 365
        delta = delta % 365
        year = (4 * year_4) + single_years + 1 # while there is a year 0, Ethiopians still reckon Jesus was born in the year 1
        if year % 4 == 0:
            # leap year
            m = months.ETHIOPIAN_MONTHS_LEAP
        else:
            # not a leap year
            m = months.ETHIOPIAN_MONTHS_NORMAL
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    elif delta <= 0:
        delta = 0 - delta # modulo operator doesn't play nicely with negative numbers
        year_4 = delta // cycle4
        delta = delta % cycle4
        single_years = delta // 365
        delta = delta % 365
        year = (4 * year_4) + single_years
        if year % 4 == 0:
            # leap year
            m = months.ETHIOPIAN_MONTHS_LEAP
            d = 366
        else:
            # not a leap year
            m = months.ETHIOPIAN_MONTHS_NORMAL
            d = 365
        year = 0 - year
        delta = d - delta
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = [day, month, year]
    return(date)
