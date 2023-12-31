#!/usr/bin/python3

# A programme to convert between Julian Days and dates in the modern Bengali calendar

from fractions import Fraction
from math import floor, ceil
from solun import indian_spos as spos, sankranti, sid_year, rasi

epoch = sankranti(1937753, 0) - sid_year

MONTHS = ("Baiśākha", "Jyeṣṭha", "Āṣāḍha", "Śrābaṇa", "Bhādraba", "Āświna", "Kārttika", "Mārgaśira", "Pauṣa", "Māgha", "Phālguna", "Caitra")

NUMON = {"Baiśākha": 0,
         "Jyeṣṭha": 1,
         "Āṣāḍha": 2,
         "Śrābaṇa": 3,
         "Bhādraba": 4,
         "Āświna": 5,
         "Kārttika": 6,
         "Mārgaśira": 7,
         "Pauṣa": 8,
         "Māgha": 9,
         "Phālguna": 10,
         "Caitra": 11}

def fromjd(jday):
    '''Given a Julian Day, compute a date in the modern Bengali'''
    jday = Fraction(jday)

    # get the year
    year = (jday - epoch) // sid_year
    pana = epoch + (year * sid_year)
    while (floor(sankranti((pana + sid_year), 0)) <= jday):
        year += 1
        pana += sid_year
    while (floor(sankranti(pana, 0)) > jday):
        year -= 1
        pana -= sid_year

    # get the month
    cigra = int(spos(jday) // 30) # star sign we're in
    angle = cigra * 30 # zodiacal angle of the sun at saṁkrānti
    while (floor(sankranti((pana + ((cigra + 1) * rasi)), (angle + 30))) <= jday):
        cigra += 1
        angle += 30
    while (floor(sankranti((pana + (cigra * rasi)), angle)) > jday):
        cigra -= 1
        angle -= 30
    month = MONTHS[cigra]

    # get the day
    day = jday - floor(sankranti(jday, angle)) + 1

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a date in the modern Indian sidereal calendar to a Julian Day'''
    day = int(day)
    month = str(month)
    year = int(year)

    # get the number of the month
    cigra = NUMON[month]
    angle = cigra * 30 # zodiacal angle of the onset of the star sign corresponding to the given month

    jday = epoch + (year * sid_year)
    jday = sankranti((jday + (cigra * rasi)), angle)
    jday = floor(jday) + day - 1

    return jday
