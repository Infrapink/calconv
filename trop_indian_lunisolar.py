#!/usr/bin/python3

# A programme to convert between Julian Days and the tropical Indian lunisolar calendar

from fractions import Fraction
from solun import tropical_sankranti as sankranti, saurya, dayof_hindi as dayof, tropical_year as trop_year, solar_term as rasi, lunar_month as syn_month, newmoon, phase, indian_sunrise as sunrise, phasetime
from surya_siddhanta import se
from months import INDIAN_LUNAR_NUM as NUMON, NUM_INDIAN_LUNAR as MONTHNO

tz = Fraction(11,48) # India is 5hr 30min ahead of UTC
epoch = sankranti((se - rasi), 330, tz)

def fromjd(jday):
    '''Convert a Julian Day into a date in the tropical Indian lunisolar calendar'''
    jday = Fraction(jday)

    # compute the start of the month
    crescent = newmoon(jday, tz)
    while (dayof(newmoon(crescent, tz)) > jday):
        crescent -= syn_month
    while (dayof(newmoon(crescent + syn_month, tz)) <= jday):
        crescent += syn_month

    # compute which month it is
    cigra = saurya(jday, tz) // 30
    angle = cigra * 30
    transition = sankranti(jday, angle, tz)
    while (dayof(sankranti(transition, angle, tz)) > jday):
        transition -= rasi
        angle = (angle - 30) % 360
        cigra = (cigra - 1) % 12
    while (dayof(sankranti((transition + rasi), ((angle + 30) % 360), tz)) <= jday):
        transition += rasi
        angle = (angle + 30) % 360
        cigra = (cigra + 1) % 360
    month = NUMON[(cigra + 1) % 12]

    # account for leap months
    if (dayof(newmoon(crescent + syn_month, tz)) < dayof(sankranti((transition + rasi), ((angle + 30) % 360), tz))):
        # it's the adhik month
        month = "Adhik " + month

    # compute the year
    year = round((transition - epoch) / trop_year)
    mina = epoch + (year * trop_year)
    while (dayof(sankranti((mina + trop_year), 330, tz)) <= jday):
        year += 1
        mina += trop_year
    while (dayof(sankranti(mina, 330, tz)) > jday):
        year -= 1
        mina -= trop_year

    # compute the tithi
    tithi = 1 + int(phase(sunrise(jday), tz) // 12)
    return (tithi, month, year)

def tojd(tithi, month, year):
    '''Convert a date in the tropical Indian lunisolar calendar to a Julian Day'''
    tithi = int(tithi) - 1 # subtract 1 to make subsequent maths easier
    month = str(month)
    year = int(year)

    # check if the leap month was entered
    if (month[:5] == "Adhik"):
        # leap month specified
        adhik = True
        month = month[6:]
    else:
        # normal month specified
        adhik = False

    # account for the year
    jday = epoch + (year * trop_year)

    # find the right part of the ecliptic
    cigra = MONTHNO[month]
    angle = 30 * ((cigra - 1) % 360)
    transition = sankranti((jday + (cigra * rasi)), angle, tz)

    # find the new moon
    crescent = newmoon(transition, tz)
    while (dayof(newmoon(crescent, tz)) > dayof(sankranti(transition, angle, tz))):
        crescent -= syn_month
    while (dayof(newmoon(crescent + syn_month, tz)) <= dayof(sankranti(transition, angle, tz))):
        crescent += syn_month

    # account for the leap month
    if ((adhik == False) and (dayof(newmoon(crescent + syn_month, tz)) < dayof(sankranti((transition + rasi), ((angle + 30) % 360), tz)))):
        crescent += syn_month

    # crescent is the instant of the new moon. now we just need to find the day which starts with the sunrise when the relevant tithi is active
    jday = crescent + Fraction(tithi, syn_month)
    jday = phasetime(jday, (tithi * 12), tz)
    jday = dayof(jday)

    return jday
