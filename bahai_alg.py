#!/usr/bin/python3

# Convert between the old Bahá'í calendar and Julian Day.

from months import BAHAI_NORMAL, BAHAI_LEAP

cycle4 = (4 * 365) + 1
cycle100 = (100 * 365) + 24
cycle400 = (400 * 365) + 97

epoch = 2394281 # 21 March 1843

def yearlen(year):
    '''Check the length of a given year'''
    year = int(year)
    if year % 400 == 156:
        ans = 366
    elif year % 100 == 56:
        ans = 365
    elif year % 4 == 0:
        ans = 366
    else:
        ans = 365

    return(ans)

def fromjd(jday):
    '''Convert a Julian Day into a date in the Bahá'í calendar'''
    jday = int(jday)

    day = 0
    month = ""
    year = 0

    cycles = (jday - epoch) // cycle400
    year = (400 * cycles)
    nawruz = epoch + (cycles * cycle400)
    while nawruz > jday:
        year -= 400
        nawruz -= cycle400
    while (nawruz + cycle400) <= jday:
        year += 400
        nawruz += cycle400

    while (nawruz + cycle100) <= jday:
        if (((year % 400) <= 156) and (((year + 100) % 400) > 156)):
            nawruz += (25 * cycle4)
        else:
            nawruz += cycle100
        year += 100

    while (nawruz + cycle4) <= jday:
        if (((year % 400) <= 156) and (((year + 4) % 400) > 156)):
            nawruz += cycle4
        elif (((year % 100) <= 56) and (((year + 4) % 100) > 56)):
            nawruz += (4 * 365)
        else:
            nawruz += cycle4
        year += 4

    while (nawruz + yearlen(year)) <= jday:
        nawruz += yearlen(year)
        year += 1

    if yearlen(year) == 366:
        MONTHS = BAHAI_LEAP
    else:
        MONTHS = BAHAI_NORMAL

    monstar = nawruz

    for m in MONTHS.keys():
        if monstar + MONTHS[m] > jday:
            break
        else:
            monstar += MONTHS[m]

    month = m
    day = jday - monstar + 1

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a date in the Bahá'í calendar to a Julian Day'''
    day = int(day)
    month = str(month)
    year = int(year)

    jday = 0

    y = year // 400
    jday = epoch + (y * cycle400)

    while (y + 100) <= year:
        if(((y % 400) <= 156) and (((y + 100) % 400) > 156)):
            jday += (25 * cycle4)
        else:
            jday += cycle100
        y += 100

    while (y + 4) <= year:
        if (((y % 400) <= 156) and (((y + 4) % 400) > 156)):
            jday += cycle4
        elif (((y % 100) <= 56) and (((y + 4) % 100) > 56)):
            jday += (4 * 365)
        else:
            jday += cycle4
        y += 4

    while y < year:
        jday += yearlen(y)
        y += 1

    if yearlen(year) == 366:
        MONTHS = BAHAI_LEAP
    else:
        MONTHS = BAHAI_NORMAL

    for m in MONTHS.keys():
        if m == month:
            jday += day - 1
            break
        else:
            jday += MONTHS[m]

    return jday
        
