#!/usr/bin/python

# Convert between Julian Days and the Metonic Athenian calendar with fixed month lengths, assuming the solar year is approximately 365¼ days long

from months import ATHENIAN as MONTHS, NUM_ATHENIAN as MONTHNO
from fractions import Fraction

solar_year = 365 + Fraction(5,19)
epoch = 1563449
year_lengths = {0:  354,
                1:  384,
                2:  355,
                3:  354,
                4:  384,
                5:  354,
                6:  355,
                7:  384,
                8:  354,
                9:  384,
                10: 354,
                11: 354,
                12: 384,
                13: 354,
                14: 355,
                15: 384,
                16: 354,
                17: 384,
                18: 355}

daysin = {354: (30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29),
          355: (30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 30),
          384: (30, 29, 30, 29, 30, 29, 30, 30, 29, 30, 29, 30, 29)}


def nyd(year):
    '''Compute the Julian Day on which a given year begins'''
    year = int(year)
    if (year > 0):
        # ancient Greeks did not accept the number 0
        year -= 1

    y = 19 * (year // 19)
    noumenia = epoch + (6940 * (year // 19))
    while (y < year):
        noumenia += year_lengths[year % 19]
        y += 1

    return noumenia

def fromjd(jday):
    '''Convert a Julian Day to a date in the Metonic calendar with fixed month lengths'''
    jday = int(jday)

    # compute the year
    year = (jday - epoch) // solar_year
    if (year >= 0):
        year += 1 # ancient Greeks did not recognise the number 0
    noumenia = nyd(year) # New Year's Day, for now
    while (noumenia > jday):
        year -= 1
        noumenia -= year_lengths[year % 19]
    while (noumenia + year_lengths[year % 19] <= jday):
        noumenia += year_lengths[year % 19]
        year += 1

    # compute the month
    m = 0
    if ((jday - noumenia == 354) and (year_lengths[year % 19] == 355)):
        # final day of a 355-day year
        month = "Skirophorion"
        noumenia += 325
    elif ((year_lengths[year % 19] != 384) or (jday - noumenia < 177)):
        # normal year, or it's before the leap month
        while (noumenia + 59 <= jday):
            noumenia += 59
            m += 2
        while (noumenia + daysin[year_lengths[year % 19]][m] <= jday):
            noumenia += daysin[year_lengths[year % 19]][m]
            m += 1
        month = MONTHS[m]
    elif (jday - noumenia < 207):
        # leap month
        noumenia += 177
        month = "Poseideon 2"
    else:
        # after the leap month
        noumenia += 207
        m = 6
        while (noumenia + 59 <= jday):
            noumenia += 59
            m += 2
        while (noumenia + daysin[year_lengths[year % 19]][m] <= jday):
            noumenia += daysin[year_lengths[year % 19]][m]
            m += 1
        month = MONTHS[m]

    # compute the day
    day = jday - noumenia + 1 # add 1 because humans don't count from 0

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a date in the Metonic calendar to a Julian Day.'''
    day = int(day) - 1 # subtract 1 because humans don't count from 0
    month = str(month)
    year = int(year)

    # account for the year
    jday = nyd(year)

    # account for the month
    m = 0
    if (year_lengths[year % 19] != 384):
        if (month == "Poseideon 2"):
            month = "Poseideon"
        M = MONTHNO[month]
    elif (month == "Poseideon 2"):
        M = 6
    elif (MONTHNO[month] < 6):
        M = MONTHNO[month]
    else:
        M = MONTHNO[month] + 1

    while (m < M):
        jday += daysin[year_lengths[year % 19]][m]
        m += 1

    # account for the day
    jday += day

    return jday
                
            
