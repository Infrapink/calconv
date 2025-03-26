#!/usr/bin/python3

# Convert between Julian Days and the Callipic calendar

from fractions import Fraction
from months import ATHENIAN as MONTHS, NUM_ATHENIAN as MONTHNO

solar_year = 365 + Fraction(1,4)
epoch = 1601069
year_lengths = {0:  354,
                1:  355,
                2:  384,
                3:  354,
                4:  384,
                5:  354,
                6:  355,
                7:  384,
                8:  354,
                9:  355,
                10: 384,
                11: 354,
                12: 384,
                13: 354,
                14: 355,
                15: 384,
                16: 354,
                17: 354,
                18: 384}

daysin = {354: (30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29),
          355: (30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 30),
          384: (30, 29, 30, 29, 30, 29, 30, 30, 29, 30, 29, 30, 29)}

def yl(year):
    '''Compute the number of days in a year'''
    year = int(year)
    if (year > 0):
        year -= 1
    if (year % 76 == 74):
        ans = 354
    else:
        ans = year_lengths[year % 19]
    return ans

def nyd(year):
    '''Compute the Julian Day on which a given year begins'''
    year = int(year)
    if (year > 0):
        year -= 1 # ancient Greeks did not recognise the number 0
    
    y = 76 * (year // 76)
    noumenia = epoch + (27759 * (year // 76))
    while (y > year):
        y -= 76
        noumenia -= 27759
    while (y + 76 <= year):
        y += 76
        noumenia += 27759
    while (y + 19 <= year):
        y += 19
        noumenia += 6940
    while (y < year):
        if (y < 0):
            noumenia += yl(y)
            y += 1
        else:
            y += 1
            noumenia += yl(y)

    return noumenia

def fromjd(jday):
    '''Convert a Julian Day into a Callipic date'''
    jday = int(jday)

    # compute the year
    year = int((jday - epoch) // solar_year)
    if (year >= 0):
        year += 1
    while (nyd(year) > jday):
        year -= 1
    while (nyd(year + 1) <= jday):
        year += 1
    noumenia = nyd(year)

    # compute the month
    if ((yl(year) == 384) and ((jday - noumenia) in range(177,207))):
        # leap month
        noumenia += 177
        month = "Poseideon 2"
    else:
        if ((yl(year) != 384) or (jday - noumenia < 177)):
            # normal year or before the leap month
            m = 0
        else:
            # after the leap month
            m = 6
            noumenia += 207
        while (noumenia + daysin[yl(year)][m] <= jday):
            noumenia += daysin[yl(year)][m]
            m += 1
        month = MONTHS[m]

    # compute the day
    day = jday - noumenia + 1 # add 1 because humans don't count from 0

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a Callipic date to a Julian Day'''
    day = int(day) - 1 # subtract 1 because computers count from 0
    month = str(month)
    year = int(year)

    # account for the year
    jday = nyd(year)

    # account for the month
    if ((year_lengths[year % 19] != 384) and (month == "Poseideon 2")):
        month = "Poseideon"
    if (month == "Poseideon 2"):
        jday += 177
    else:
        if ((year_lengths[year % 19] == 384) and (MONTHNO[month] > 5)):
            # after the leap month
            m = 6
            jday += 207
        else:
            m = 0
        while (MONTHS[m] != month):
            jday += daysin[year_lengths[year % 19]][m]
            m += 1

    # account for the day
    jday += day

    return jday
