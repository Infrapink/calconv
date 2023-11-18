#!/usr/bin/python

# Convert between the tradition Indian solar calendar and Julian Day, dating from the start of the Kali Yuga, using methods described in the Sūrya Siddhānta

# When reading the comments, Indian days run from sunrise to sunrise, and Roman days run from midnight to midnight.

from fractions import Fraction
from math import floor, ceil
from surya_siddhanta import ky as epoch, sunrise, sunset, sankranti, t_sid_year as sid_year, t_rasi as rasi
from months import INDIAN_SOLAR_NUM as MONTHNO, NUM_INDIAN_SOLAR as NUMON

def dayof(jday):
    # In traditional Indian reckoning, the days begins at sunrise.
    # Also, zodiacal months are determined by the sign in which the sun is present at sunrise
    # Hence, if an astronomical event (which for the purpose of this file will always be a Saṁkrānti)
    # happens after midnight but before sunrise,
    # the Roman day beginning with that midnight marks the start of the month.
    # Otherwise, the month starts on the day of the sunrise following the next midnight.
    jday = Fraction(jday)
    #print(float(sunrise(jday)))

    if (sunrise(jday) <= jday):
        # event happens before sunrise, hence the period it indicates is the current Roman day
        ans = floor(jday)
    else:
        # event happens after sunrise, hence the period it indicates is the next Roman day.
        ans = ceil(jday)

    return ans

def fromjd(jday):
    '''Convert a Julian Day into a date in the traditional Indian solar calendar, dating from the start of the Kali Yuga'''
    jday = Fraction(jday) # Julian Day we are interested in

    # compute the year
    year = (jday - epoch) // sid_year
    mesha = epoch + (year * sid_year) # estimated time of Meṣa Saṁkrānti
    while (dayof(sankranti((mesha + sid_year), 0)) <= jday):
        mesha += sid_year
        year += 1
        #print(float(sunrise(mesha)))
    while (dayof(sankranti(mesha, 0)) > jday):
        mesha -= sid_year
        year -= 1
        #print(float(sunrise(mesha)))

    #print(float((jday - mesha) / sid_year))

    # compute the month
    cigra = (jday - sankranti(mesha, 0)) // rasi # number of the zodiacal month, starting from 0
    angle = cigra * 30 # solar zodiacal longitude, in degrees
    while (dayof(sankranti(mesha + ((cigra + 1) * rasi), (angle + 30))) <= jday):
        #print(cigra)
        cigra += 1
        angle += 30
    while (dayof(sankranti(mesha, angle)) > jday):
        cigra -= 1
        angle -= 30
    month = MONTHNO[cigra]

    # compute the day
    day = jday - dayof(sankranti((mesha + (rasi * cigra)), angle)) + 1

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a date in the traditional Indian solar calendar (Kali Yuga epoch) into a Julian Day'''
    day = int(day)
    month = str(month)
    year = int(year)

    cigra = NUMON[month] # number of the month, starting from 0
    angle = 30 * cigra # zodiacal angle at which the month begins

    jday = dayof(sankranti((epoch + (year * sid_year) + (cigra * rasi)), angle)) + day - 1
    return jday
