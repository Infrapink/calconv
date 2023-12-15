#!/usr/bin/python3

# A programme to convert between Julian Days and dates in the alternative Malayam calendar, using modern techniques and observations

# When reading these comments:
## Malayam days start at sunset
## Roman days start at midnight
## Ordinal numbers go 0th, 1st, 2nd, etc

from fractions import Fraction
from solun import sid_year, rasi, dayof_tamil as dayof, sankranti
from surya_siddhanta import ky

MONTHS = ("Kanni", "Thulam", "Vrischikam", "Dhanu", "Makaram", "Kumbham", "Meenam", "Medam", "Edavam", "Midhunam", "Karkitaka", "Chingam")
NUMON = {"Kanni": 0,
         "Thulam": 1,
         "Vrischikam": 2,
         "Dhanu": 3,
         "Makaram": 4,
         "Kumbham": 5,
         "Meenam": 6,
         "Medam": 7,
         "Edavam": 8,
         "Midhunam": 9,
         "Karkitaka": 10,
         "Chingam": 11}

epoch = ky + (3926 * sid_year) + (5 * rasi) # add 5 rasi because Kumbham is the 5th sign of the zodiac after Meṣa (here called Medam)

def fromjd(jday):
    '''Convert a Julian Day into a date in the observational Malayam calendar'''
    jday = Fraction(jday) # Julian Day we are interested in

    # compute the year
    year = (jday - epoch) // sid_year
    kumbham = epoch + (year * sid_year) # 1st-order estimate of the time of Kumbham Saṃkrānti
    while (dayof(sankranti((kumbham + sid_year), 150)) <= jday):
        kumbham += sid_year
    while (dayof(sankranti(kumbham, 150)) > jday):
        kumbham -= sid_year

    # compute the month
    cigra = (jday - kumbham) // rasi # number of star signs the sun has traversed since Kumbham Saṃkrānti
    angle = 30 * ((cigra + 5) % 12) # zodiacal angle of the cusp of the rasi that the sun is in. add 5 and mod 12 to account for the fact that Kumbham is the 4th rasi
    while (dayof(sankranti((kumbham + (cigra * rasi)), angle)) > jday):
        # current saṃkrānti is later than jday
        cigra -= 1
        angle = (angle - 30) % 360
    while (dayof(sankranti((kumbham + ((cigra + 1) * rasi)), ((angle + 30) % 360))) <= jday):
        # There is at least one saṃkrānti between the current one and jday
        cigra += 1
        angle = (angle + 30) % 360
    month = MONTHS[cigra]

    # compute the day
    day = jday - dayof(sankranti((kumbham + (cigra * rasi)), angle)) + 1

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a date in the observational Malayam calendar into a Julian Day'''
    day = int(day)
    month = str(month)
    year = int(year)

    cigra = NUMON[month] # number of the rasi we're currently in
    angle = 30 * ((cigra + 5) % 12) # zodiacal angle of the cusp of the specified star sign

    jday = day + dayof(sankranti((epoch + (year * sid_year)) + (cigra * rasi), angle)) - 1
    return jday
