#!/usr/bin/python3

# Convert between the Tabot calendar and Julian Days

epoch = 2426283 # 1 Ambassa of year 0
cycle4 = (4 * 365) + 1 # days in 4 years with a leap year
cycle400 = (400 * 365) + 97 # days in 400 years

months = ("Anbassa", "Hymanot", "Immanuel", "Ras", "Ta'Berhan", "Manassa", "Danaffa", "Negest", "Tafari", "Emru", "Sawwara", "Negus and Dejazmatch")
monthno = {"Anbassa":               0,
           "Hymanot":               1,
           "Immanuel":              2,
           "Ras":                   3,
           "Ta'Berhan":             4,
           "Manassa":               5,
           "Danaffa":               6,
           "Negest":                7,
           "Tafari":                8,
           "Emru":                  9,
           "Sawwara":              10,
           "Negus and Dejazmatch": 11}
month_lengths = {365: (30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35), # normal years
                 366: (30, 30, 30, 31, 30, 30, 30, 30, 30, 30, 30, 35)} # leap years

def leap(year):
    '''How many days in a year?'''
    year = int(year)

    if (year % 400 == 69):
        ans = 366
    elif (year % 100 == 69):
        ans = 365
    elif (year % 4 == 1):
        ans = 366
    else:
        ans = 365

    return ans

def nyd(year):
    '''Compute New Year's Day for a given year'''
    year = int(year)

    cycles = year // 400
    y = 400 * cycles
    jday = epoch + (cycles * cycle400)

    if (y + 100 <= year):
        y += 100
        jday += 36525

        while (y + 100 <= year):
            y += 100
            jday += 36524

    while (y + 4 <= year):
        if ( (y % 400 <= 69) and ((y + 4) % 400 > 69)):
            y += 4
            jday += cycle4
        elif ( (y % 100 <= 69) and ((y + 4) % 400 > 69)):
            y += 4
            jday += (4 * 365)
        else:
            y += 4
            jday += cycle4

    while (y < year):
        jday += leap(y)
        y += 1

    return jday

def fromjd(jday):
    '''Convert a Julian Day to a date in the Tabot calendar'''
    jday = int(jday)

    # compute the year
    year = int(round((jday - epoch) // 365.2425))
    n = nyd(year)
    while (n + leap(year) <= jday):
        n += leap(year)
        year += 1
    while (n > jday):
        year -= 1
        n -= leap(year)

    # compute the month and day
    if (jday - n >= leap(year) - 35):
        month = "Negus and Dejazmatch"
        day = n + leap(year) - 34
    elif (leap(year) == 365):
        # normal year
        m = (jday - n) // 30
        month = months[m]
        day = ((jday - n) % 30) + 1
    elif (jday - n == 121):
        # leap day
        month = "Ras"
        day = 31
    elif (jday - n < 121):
        # leap year, before leap day
        m = (jday - n) // 30
        month = months[m]
        day = ((jday - n) % 30) + 1
    else:
        # leap year, after leap day
        n += 121
        m = (jday - n) // 30
        month = months[m + 3]
        day = ((jday - n) % 30) + 1

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a Tabot date to a Julian Day'''
    day = int(day) - 1 # subtract 1 because computers count from 0
    month = str(month)
    year = int(year)

    jday = nyd(year)

    if (leap(year) == 365):
        # normal year
        jday = jday + (30 * monthno[month]) + day
    else:
        if (month in ("Anbassa", "Hymanot", "Immanuel", "Ras")):
            # leap year before or on leap day
            jday = jday + (30 * monthno[month]) + day
        else:
            # leap year after leap day
            jday = jday + (30 * monthno[month]) + day + 1

    return (jday)
