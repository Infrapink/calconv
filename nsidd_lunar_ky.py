#!/usr/bin/python3

# Convert between Julian Days and dates in a naïve version of the lunisolar calendar described in the Sūrya Siddhānta.

from hindu_functions import ky as solar_epoch, sid_year, syn_month, sunrise, ntime, rasi, creation, tithi, uj_lon as lon, uj_lat as lat, n_newmoon as newmoon
from math import floor, ceil
from fractions import Fraction
from months import NUM_HINDU as NUMON, HINDU_NUM as MONTHNO

def suncheck(jday):
    '''Returns the current day if jday is before sunrise, or the previous day if jday is after sunrise.'''
    jday = Fraction(jday)

    dawn = sunrise(jday, lat)

    if ((jday % 1) < (dawn % 1)):
        ans = floor(jday)
    else:
        ans = ceil(jday)

    return ans

def fromjd(jday):
    '''Convert a Julian Day into a date in the naïve version of the lunisolar calendar described in the Sūrya Siddhānta.'''
    jday = Fraction(jday)

    year = (jday - solar_epoch) // sid_year

    mesha = solar_epoch + (year * sid_year) # aproximate time the sun enters Meṣa/Aries
    mina = mesha - rasi # time the sun enters Mīna/Pisces

    while (suncheck(ntime(mina, 330)) > jday):
        mina -= sid_year
        year -= 1
    while (suncheck(ntime((mina + sid_year), 330)) <= jday):
        mina += sid_year
        year += 1

    # new moon of Chaitra
    luns = (mesha - creation) // syn_month
    firstmoon = creation + (luns * syn_month)
    while (suncheck(newmoon(firstmoon)) < suncheck(ntime(mina, 330))):
        firstmoon += syn_month
    while (suncheck(newmoon(firstmoon - syn_month)) >= suncheck(ntime(mina, 330))):
        firstmoon -= syn_month

    # make sure the first new moon doesn't come after jday
    if (suncheck(newmoon(firstmoon)) > jday):
        year -= 1
        mina -= sid_year
        firstmoon -= (12 * syn_month)
        while (suncheck(newmoon(firstmoon - syn_month)) >= suncheck(ntime(mina, 330))):
            firstmoon -= syn_month

    # OK, now we have the first new moon of the year. Time to work out which month it is.
    chigra = (jday - mina) // rasi # number of the sign we're in
    sankranti = mina + (chigra * rasi) # time the sun enters the sign in question
    solar_angle = ((chigra * 30) - 30) % 360
    amavasya = firstmoon # new moon
    while (suncheck(newmoon(amavasya)) < suncheck(ntime(sankranti, solar_angle))):
        amavasya += syn_month
    if (suncheck(newmoon(amavasya)) > jday):
        chigra -= 1
        sankranti -= rasi
        solar_angle = (solar_angle - 30) % 360
        amavasya -= syn_month

    month = NUMON[(chigra - 1) % 12]
    if (suncheck(newmoon(amavasya + syn_month)) < suncheck(ntime((sankranti + rasi), solar_angle))):
        # leap month
        month = "Adhik " + month

    day = (jday - amavasya) // tithi
    while (suncheck(amavasya + (day * tithi)) < jday):
        day += 1
    while (suncheck(amavasya + (day * tithi)) > jday):
        day -= 1

    day += 1 # days are 1-indexed
    return (day, month, year)

def tojd(day, month, year):
    '''Convert a date in the naïve Siddhāntic lunisolar calendar to a Julian Day.'''
    day = int(day)
    month = str(month)
    year = int(year)

    # check for leap months
    if month[:5] == "Adhik":
        adhik = True
        month = month[6:]
    else:
        adhik = False

    mina = solar_epoch + (year * sid_year) - rasi # time the sun enters Mīna/Pisces
    chigra = (MONTHNO[month] + 1) % 12 # number of the sign we're in.
    solar_angle = 30 * MONTHNO[month]
    sankranti = mina + (chigra * rasi)
    luns = (sankranti - creation) // syn_month
    jday = creation + (luns * syn_month) # first new moon of the year, from which we will calculate the Julian Day.
    while (suncheck(newmoon(jday)) < suncheck(ntime(sankranti, solar_angle))):
        jday += syn_month
    while (suncheck(newmoon(jday - syn_month)) >= suncheck(ntime(sankranti, solar_angle))):
        jday -= syn_month

    if ((adhik == False) and (suncheck(newmoon(jday + syn_month)) < suncheck(ntime((sankranti + rasi), (solar_angle + 30))))):
        jday += syn_month

    jday = jday + (tithi * (day - 1)) # subtract 1 from day because days are 1-indexed
    jday = suncheck(jday)

    return jday
