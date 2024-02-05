#!/usr/bin/python3

# Convert between the Nepali lunisolar calendar and Julian Days

from fractions import Fraction
from solun import newmoon, local_sunrise, get_solar_zpos, eqm, sid_year, lunar_month as syn_month, rasi
from stars import SPICA
from months import NUM_NEPALI as MONTHS, NEPALI_NUM as MONTHNO
from math import floor, ceil

tz = Fraction(5,24) + Fraction(45,1440) # Nepal's timezone is 5hr 45min ahead of UTC
lon = 52 + Fraction(32,100) # longitude of Kathmandu
lat = 27 + Fraction(71,100) # latitude of Kathmandu
epoch = 2042401

def sunrise(jday):
    '''Compute the local time of sunrise in Kathmandu'''
    jday = Fraction(jday)
    ans = local_sunrise(jday, lon, lat, tz)
    return ans

def dayof(jday):
    '''Determine the day associated with a given astronomical event'''
    jday = Fraction(jday)

    # the day of jday is the day beginning with the first sunrise at or following jday
    if (jday <= sunrise(jday)):
        ans = floor(jday)
    else:
        ans = ceil(jday)
    return ans

def sankranti(jday, angle):
    '''Zero in on the time the sun hits a given zodiacal angle'''
    jday = Fraction(jday)
    angle = (Fraction(angle) + 180) % 360 # Nepali calendar is anchored to Kāttik/Tulā rather than Meṣa

    ans = get_solar_zpos((jday - tz), SPICA, True, ((angle + eqm) % 360))
    return ans

def amanta(jday):
    '''Compute the time of the new moon closest to jday'''
    jday = Fraction(jday)
    
    ans = newmoon(jday, tz)
    return ans

def fromjd(jday):
    '''Convert a Julian Day into a date in the Nepali lunisolar calendar'''
    jday = Fraction(jday)

    # compute the new moon
    crescent = amanta(jday)
    while( dayof(crescent) > jday):
        crescent -= syn_month
    while( dayof(crescent + syn_month) <= jday):
        crescent += syn_month

    # compute the year
    year = (crescent - epoch) // sid_year
    mhapuja = sankranti( (epoch + (year * sid_year)), 0) # estimated time of Kāttik Saṁkrānti
    while( dayof( sankranti(mhapuja, 0)) > dayof(amanta(crescent)) ):
        year -= 1
        mhapuja -= sid_year
    while( dayof( sankranti( (mhapuja + sid_year), 0)) <= dayof(amanta(crescent)) ):
        year += 1
        mhapuja += sid_year

    # compute the month
    cigra = round( (crescent - mhapuja) // rasi)
    angle = cigra * 30
    r = sankranti( (mhapuja + (cigra * rasi)), angle) # time the rasi begins in which the new moon falls
    while( dayof( sankranti(r, angle)) > dayof(amanta(crescent))):
        r -= rasi
        angle -= 30
        cigra -= 1
    while( dayof( sankranti( (r + rasi), ((angle + 30 % 360) ))) <= dayof(amanta(crescent))):
        r += rasi
        angle += 30
        cigra += 1
    if( dayof(amanta(crescent + syn_month)) <= dayof( sankranti( (r + rasi), ((angle + 30) % 360) ) )):
        # leap month
        month = "Analā"
    else:
        # normal month
        month = MONTHS[cigra]

    # compute the day
    day = jday - dayof(amanta(crescent)) + 1

    # bring it home
    return (day, month, year)

def tojd(day, month, year):
    '''Convert a Julian Day to a date in the Nepali lunisolar calendar'''
    day = int(day)
    month = str(month)
    year = int(year)

    # account for the year
    mhapuja = sankranti( (epoch + (year * sid_year)), 0)
    
    # account for the month
    if (month == "Analā"):
        # leap month specified
        next_mhapuja = sankranti( (mhapuja + sid_year), 0)
        kattik_moon = amanta(mhapuja)
        next_moon = amanta(next_mhapuja)
        while( dayof(amanta(kattik_moon)) < dayof(sankranti(mhapuja, 0)) ):
            kattik_moon += syn_month
        while( dayof(amanta(kattik_moon - syn_month)) >= dayof(sankranti(mhapuja, 0)) ):
            kattik_moon -= syn_month
        while( dayof(amanta(next_moon)) < dayof(sankranti(next_mhapuja, 0)) ):
            next_moon += syn_month
        while( dayof(amanta(next_moon - syn_month)) >= dayof(sankranti(mhapuja, 0)) ):
            next_moon -= syn_month
        if( round( (next_moon - kattik_moon) / 12) == 12):
            # normal year
            month = "Kāttik"
        else:
            # leap year
            crescent = kattik_moon
            r = mhapuja
            angle = 0

            while( dayof(amanta(crescent + syn_month)) >= dayof( sankranti( (r + rasi), ((angle + 30) % 360)) ) ):
                crescent += syn_month
                r += rasi
                angle += 30

            jday = crescent

    if (month in MONTHS):
        angle = MONTHNO[month] * 30
        r = sankranti( (mhapuja + (rasi * MONTHNO[month]) ), angle )
        crescent = amanta(r)
        while( dayof(amanta(crescent)) < dayof(sankranti(r, angle)) ):
            crescent += syn_month
        while( dayof(amanta(crescent - syn_month)) >= dayof(sankranti(r, angle)) ):
            crescent -= syn_month

    # bring it home
    jday = dayof(amanta(crescent)) + day - 1
    return jday
