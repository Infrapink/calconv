#!/usr/bin/python3

# A programme to convert between Julian Days and dates in traditional Jalgaon calendar

from math import floor, ceil
from fractions import Fraction
from solun import sankranti, conj, indian_sunrise as sunrise, conj as newmoon, phase, sid_year, lunar_month as syn_month, rasi, phasetime, dayof_hindi as dayof
from surya_siddhanta import se
from months import INDIAN_LUNAR_NUM as NUMON, NUM_INDIAN_LUNAR as MONTHNO

epoch = sankranti((se - (2 * rasi)), 300) # Kumbha Saṁkrānti of 0 SE.
tz = Fraction(11,48) # Indian timezone; UTC+5:30

def fromjd(jday):
    '''Given a Julian Day, compute the date in the Indian lunisolar calendar'''
    jday = Fraction(jday)

    # start with the new moon
    crescent = newmoon(jday, tz)
    while (dayof(newmoon(crescent, tz)) > dayof(jday)):
        crescent -= syn_month
    while (dayof(newmoon((crescent + syn_month), tz)) <= dayof(jday)):
        crescent += syn_month

    # now we can sort out the year
    year = (crescent - epoch) // sid_year
    kumbha = epoch + (year * sid_year) # Kumbha Saṁkrānti
    while (dayof(sankranti(kumbha, 300)) > dayof(newmoon(crescent, tz))):
        year -= 1
        kumbha -= sid_year
    while (dayof(sankranti((kumbha + sid_year), 300)) <= dayof(newmoon(crescent, tz))):
        year += 1
        kumbha += sid_year

    # now to figure out the month
    cigra = (crescent - kumbha) // rasi # number of the star sign the new moon falls in
    angle = ((cigra * 30) - 60) % 360  # zodiacal angle of the cusp of the star sign we're in; note that in this particular calendar, we start at 300°
    s = kumbha + (rasi * cigra) # approximate time of the saṁkrānti immediately preceding the current lunar cycle
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

    # and now the tithi
    tithi = int(1 + (phase(jday, tz) // 12))

    return (tithi, month, year)

def tojd(tithi, month, year):
    '''Given a tithi, a month, and a day, compute the corresponding Julian Day'''
    tithi = int(tithi) - 1
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
    angle = ((m * 30) - 60) % 360 # zodiacal angle of the beginning of the star sign we're interested in
    crescent = newmoon(jday, tz)
    while (dayof(newmoon(crescent, tz)) < dayof(sankranti(jday, angle))):
        crescent += syn_month
    while (dayof(newmoon((crescent - syn_month), tz)) >= dayof(sankranti(jday, angle))):
        crescent -= syn_month
    if ((adhik == False) and (dayof(newmoon((crescent + syn_month), tz)) <= dayof(sankranti((jday + rasi), ((angle + 30) % 360))))):
        # we're in the leap month, but shouldn't be
        crescent += syn_month

    jday = dayof(phasetime((crescent + (tithi * Fraction(syn_month, 30))), (12 * tithi), tz))

    return jday
    
