#!/usr/bin/python3

# A programme to convert between Julian Days and dates in the Mughal Faṣlī lunisolar calendar

from math import floor, ceil
from fractions import Fraction
from solun import sankranti, conj, indian_sunrise as sunrise, conj as newmoon, phase, sid_year, lunar_month as syn_month, rasi, phasetime, dayof_tamil as dayof, vs
from months import INDIAN_LUNAR_NUM as NUMON, NUM_INDIAN_LUNAR as MONTHNO

epoch = sankranti((vs - rasi + (649 * sid_year)), 330) # Mīna Saṁkrānti of the year 0
tz = Fraction(11,48) # Indian timezone; UTC+5:30

def fromjd(jday):
    '''Given a Julian Day, compute the date in the Mughal Faṣlī lunisolar calendar'''
    jday = Fraction(jday)

    # start with the new moon
    crescent = newmoon(jday, tz)
    while (dayof(newmoon(crescent, tz)) > dayof(jday)):
        crescent -= syn_month
    while (dayof(newmoon((crescent + syn_month), tz)) <= dayof(jday)):
        crescent += syn_month

    # now we can sort out the year
    year = (crescent - epoch) // sid_year
    mina = epoch + (year * sid_year) # Mīna Saṁkrānti
    while (dayof(sankranti(mina, 330)) > dayof(newmoon(crescent, tz))):
        year -= 1
        mina -= sid_year
    while (dayof(sankranti((mina + sid_year), 330)) <= dayof(newmoon(crescent, tz))):
        year += 1
        mina += sid_year

    # now to figure out the month
    cigra = (crescent - mina) // rasi # number of the star sign the new moon falls in
    angle = ((cigra * 30) - 30) % 360  # zodiacal angle of the cusp of the star sign we're in; note that in the case of lunisolar calendars, we start at 330°
    s = mina + (rasi * cigra) # approximate time of the saṁkrānti immediatelly preceding the current lunar cycle
    while (dayof(sankranti(s, angle)) > dayof(newmoon(crescent, tz))):
        s -= rasi
        cigra = (cigra - 1) % 12
        angle = (angle - 30) % 360
    while (dayof(sankranti((s + rasi), ((angle + 30) % 360))) <= dayof(newmoon(crescent, tz))):
        s += rasi
        cigra = (cigra + 1) % 12
        angle = (angle + 30) % 360
    month = NUMON[cigra]
    if (dayof(newmoon((crescent + syn_month), tz)) <= dayof(sankranti((s + rasi), ((angle + 30) % 360)))):
        # we're in the leap month
        month = "Adhik " + month

    day = jday - dayof(newmoon(crescent, tz)) + 1
    
    return (day, month, year)

def tojd(day, month, year):
    '''Given a year, a month, and a day, compute the corresponding Julian Day'''
    day = int(day) - 1
    month = str(month)
    year = int(year)

    # leap month check
    if (month[:5] == "Adhik"):
        # leap month specificed
        adhik = True
        month = month[6:]
    else:
        adhik = False

    m = MONTHNO[month] # number of the star sign that the month begins in

    jday = epoch + (year * sid_year) + (m * rasi) # approximate saṁkrānti of the month specified
    angle = ((m * 30) - 30) % 360 # zodiacal angle of the beginning of the star sign we're interested in
    crescent = newmoon(jday, tz)
    while (dayof(newmoon(crescent, tz)) < dayof(sankranti(jday, angle))):
        crescent += syn_month
    while (dayof(newmoon((crescent - syn_month), tz)) >= dayof(sankranti(jday, angle))):
        crescent -= syn_month
    if ((adhik == False) and (dayof(newmoon((crescent + syn_month), tz)) <= dayof(sankranti((jday + rasi), ((angle + 30) % 360))))):
        # we're in the leap month, but shouldn't be
        crescent += syn_month

    jday = dayof(newmoon(crescent, tz)) + day

    return jday
    
