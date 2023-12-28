#!/usr/bin/python

# Convert between the Assamese calendar and Julian Day

from fractions import Fraction
from solun import indian_sunrise as sunrise, sankranti, dayof_hindi as dayof, sid_year

epoch = sankranti(1937753, 0)

MONTHS = {"Böhag": 31,
          "Zeth": 31,
          "Ahar": 32,
          "Xaün": 31,
          "Bhado": 31,
          "Ahin": 31,
          "Kati": 30,
          "Aghün": 29,
          "Puh": 29,
          "Magh": 30,
          "Fagun": 30,
          "Söt": 30} # Söt has 31 months in leap years, but the rest of the algorithm accounts for that

def fromjd(jday):
    '''Convert a Julian Day to a date in the Assamese calendar'''
    jday = Fraction(jday)

    # compute the year
    year = (jday - epoch) // sid_year
    bihu = epoch + (year * sid_year)
    while (dayof(sankranti((bihu + sid_year), 0)) <= jday):
        year += 1
        bihu += sid_year
    while (dayof(sankranti(bihu, 0)) > jday):
        year -= 1
        bihu -= sid_year

    bihu = dayof(sankranti(bihu, 0))

    # compute the month and day
    if (jday - bihu >= 335):
        month = "Söt"
        day = jday - bihu - 335 + 1
    else:
        z = bihu
        for m in MONTHS.keys():
            if (z + MONTHS[m] <= jday):
                z += MONTHS[m]
            else:
                month = m
                break
        day = jday - z + 1

    return(day, month, year)

def tojd(day, month, year):
    '''Convert a date in the Assamese calendar to Julian Day'''
    day = int(day)
    month = str(month)
    year = int(year)

    bihu = dayof(sankranti((epoch + (year * sid_year)), 0))

    if (month == "Söt"):
        jday = bihu + 335 + day - 1
    else:
        z = bihu
        for m in MONTHS.keys():
            if (m == month):
                break
            else:
                z += MONTHS[m]
        jday = z + day - 1

    return jday
