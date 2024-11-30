#!/usr/bin/python3

# A programme to convert between Julian Days and the calendar described in the Vedāṅga Jyotiṣa

from fractions import Fraction
from math import floor, ceil
from solun import heliacal_rising, ky, newmoon, sid_year, lunar_month as syn_month, local_sunrise
from stars import SHRAVISHTHA as s
from months import INDIAN_LUNAR_NUM as NUMON, NUM_INDIAN_LUNAR as MONTHNO

lat = 27 + Fraction(19, 60) + Fraction(20, 3600) # latitude of Mohenjo Daro
lon = 68 + Fraction(8, 60) + Fraction(20, 3600) # longitude of Mohenjo Daro
tz = Fraction(lon, 360) # local timezone, or rather the absolute offset from UTC, in fractions of a day

epoch = heliacal_rising(ky, lon, lat, s, tz)

def hr(jday):
    '''heliacal_rising() but always for SHRAVISHTHA at local coördinates; this makes the code much cleaner'''
    jday = Fraction(jday)
    ans = heliacal_rising(jday, lon, lat, s, tz)
    return ans

def dayof(jday):
    '''Day that should be associated with a given astronomical event, which in this case will be the new moon'''
    jday = Fraction(jday)
    if (jday <= local_sunrise(jday, lon, lat, tz)):
        # sun rises after the new moon
        ans = floor(jday)
    else:
        # sun rises before the new moon
        ans = ceil(jday)
    return ans

def tojd(day, month, year):
    '''Convert a day in the ancient Indian calendar to a Julian Day'''
    day = int(day)
    month = str(month)
    year = int(year)

    # compute the start of the solar year
    kumbha = epoch + (year * sid_year) # approximate time the sun in in conjunction with Śraviṡṭḥa

    # compute the first new moon of the year
    solstice_moon = newmoon(kumbha, tz)
    while (dayof(newmoon(solstice_moon, tz)) < hr(kumbha)):
        solstice_moon += syn_month
    while (dayof(newmoon((solstice_moon - syn_month), tz)) >= hr(kumbha)):
        solstice_moon -= syn_month

    # solstice_moon is the first visible crescent following the heliacal rising of Śraviṡṭḥa

    # now compute the month
    if (dayof(newmoon((solstice_moon + (12 * syn_month)), tz)) >= hr(kumbha + sid_year)):
        # normal year
        if (month == "Adhikmasa"):
            # invalid option
            m = 0 # just go with the first month of the year
        else:
            m = (MONTHNO[month] + 1) % 12
    elif (year % 5 < 2):
        # leap year; leap month goes at the end
        if (month == "Adhikmasa"):
            m = 12
        else:
            m = (MONTHNO[month] + 1) % 12
    else:
        # leap year; leap month goes in the middle
        if (month == "Adhikmasa"):
            m = 6
        elif (month in ("Phālguna", "Chaitra", "Vaisākha", "Jyēshtha", "Āshādha", "Shrāvana")):
            m = (MONTHNO[month] + 1) % 12
        else:
            m = (MONTHNO[month] + 2) % 12
    crescent = solstice_moon + (m * syn_month) # new moon of the specified month

    # bring it home
    jday = dayof(newmoon(crescent, tz)) + day - 1
    
    return jday

def fromjd(jday):
    '''Convert a Julian Day into a date in the calendar described in the Vedāṅga Jyotiṣā'''
    jday = Fraction(jday)

    # compute the year
    year = (jday - epoch) // sid_year
    kumbha = epoch + (year * sid_year)
    while (hr(kumbha + sid_year) <= jday):
        year += 1
        kumbha += sid_year
    while (hr(kumbha) > jday):
        year -= 1
        kumbha -= sid_year

    # first new moon of the year
    solstice_moon = newmoon(kumbha, tz)
    while (dayof(newmoon(solstice_moon, tz)) < hr(kumbha)):
        solstice_moon += syn_month
    while (dayof(newmoon((solstice_moon - syn_month), tz)) >= hr(kumbha)):
        solstice_moon -= syn_month

    # kumbha corresponds to the time the sun is in conjunction with Śraviṡṭḥa
    # solstice_moon is the following new moon

    # make sure we haven't overshot
    if (dayof(newmoon(solstice_moon, tz)) > jday):
        year -= 1
        kumbha -= sid_year
        solstice_moon -= (12 * syn_month)
        while (dayof(newmoon((solstice_moon - syn_month), tz)) >= hr(kumbha)):
            solstice_moon -= syn_month

    # now find the new moon preceding jday
    crescent = newmoon(jday, tz)
    while (dayof(newmoon(crescent, tz)) > jday):
        crescent -= syn_month
    while (dayof(newmoon((crescent + syn_month), tz)) <= jday):
        crescent += syn_month
    m = round((crescent - solstice_moon) / syn_month) # number of the month, starting from 0

    # now to account for leap years
    if (dayof(newmoon((solstice_moon + (12 * syn_month)), tz)) >= hr(kumbha + sid_year)):
        # normal year
        month = NUMON[(m - 1) % 12]
    elif (year % 5 < 2):
        # leap year; leap month goes at the end
        if (m == 12):
            month = "Adhikmasa"
        else:
            month = NUMON[(m - 1) % 12]
    else:
        # leap year; leap month goes in the middle
        if (m == 6):
            month = "Adhikmasa"
        elif (m < 6):
            month = NUMON[(m - 1) % 12]
        else:
            month = NUMON[(m - 2) % 12]

    day = jday - dayof(newmoon(crescent, tz)) + 1

    return (day, month, year)
                          
