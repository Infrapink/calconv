#!/usr/bin/python3

# A programme to convert between Julian Days and dates in the Tamil calendar (Śaka era)

from fractions import Fraction
from math import floor, ceil
from solun import indian_spos as spos, sankranti, indian_sunrise as sunrise, indian_sunset as sunset, sid_year, rasi, dayof_tamil as dayof
from surya_siddhanta import ky

epoch = ky + (3179 * sid_year) - Fraction(11,48) # ensure epoch is given in IST

MONTHS = ("Chittirai", "Vaikāsi", "Āni", "Ādi", "Āvani", "Purattāsi", "Aippasi", "Kartikai", "Mārgazhi", "Thai", "Māsi", "Panguni")
NUMON = {"Chittirai": 0,
         "Vaikāsi": 1,
         "Āni": 2,
         "Ādi": 3,
         "Āvani": 4,
         "Purattāsi": 5,
         "Aippasi": 6,
         "Kartikai": 7,
         "Mārgazhi": 8,
         "Thai": 9,
         "Māsi": 10,
         "Panguni": 11}

def fromjd(jday):
    '''Given a Julian Day, compute a date in the Tamil calendar'''
    jday = Fraction(jday)

    # get the year
    year = (jday - epoch) // sid_year
    chittirai = epoch + (year * sid_year)
    while (dayof(sankranti((chittirai + sid_year), 0)) <= jday):
        year += 1
        chittirai += sid_year
    while (dayof(sankranti(chittirai, 0)) > jday):
        year -= 1
        chittirai -= sid_year

    # get the month
    cigra = int(spos(jday)) // 30 # star sign we're in
    angle = cigra * 30 # zodiacal angle of the sun at saṁkrānti
    while (dayof(sankranti((chittirai + ((cigra + 1) * rasi)), (angle + 30))) <= jday):
        cigra += 1
        angle += 30
    while (dayof(sankranti((chittirai + (cigra * rasi)), angle)) > jday):
        cigra -= 1
        angle -= 30
    month = MONTHS[cigra]

    # get the day
    day = jday - dayof(sankranti(jday, angle)) + 1

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a date in the Tamil calendar to a Julian Day'''
    day = int(day)
    month = str(month)
    year = int(year)

    # get the number of the month
    cigra = NUMON[month]
    angle = cigra * 30 # zodiacal angle of the onset of the star sign corresponding to the given month

    jday = epoch + (year * sid_year)
    jday = sankranti((jday + (cigra * rasi)), angle)
    jday = dayof(jday) + day - 1

    return jday
