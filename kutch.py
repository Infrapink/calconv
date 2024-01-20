#!/usr/bin/python3

# A programme to convert between Julian Days and dates in the local calendar of Kutch

from math import floor, ceil
from fractions import Fraction
from solun import sankranti, conj, indian_sunrise as sunrise, conj as newmoon, phase, sid_year, lunar_month as syn_month, rasi, phasetime, dayof_hindi as dayof
from surya_siddhanta import vs
from months import INDIAN_LUNAR_NUM as NUMON, NUM_INDIAN_LUNAR as MONTHNO

epoch = sankranti((vs + (2 * rasi)), 60) # Mithuna Saṁkrānti of 0 VS
tz = Fraction(11,48) # Indian timezone; UTC+5:30

def fromjd(jday):
    '''Given a Julian Day, compute the date in the Kutch calendar'''
    jday = Fraction(jday)

    # start with the new moon
    crescent = newmoon(jday, tz)
    while (dayof(newmoon(crescent, tz)) > dayof(jday)):
        crescent -= syn_month
    while (dayof(newmoon((crescent + syn_month), tz)) <= dayof(jday)):
        crescent += syn_month

    # now we can sort out the year
    year = (crescent - epoch) // sid_year
    mithuna = epoch + (year * sid_year) # Mithuna Saṁkrānti
    while (dayof(sankranti(mithuna, 60)) > dayof(newmoon(crescent, tz))):
        year -= 1
        mithuna -= sid_year
    while (dayof(sankranti((mithuna + sid_year), 60)) <= dayof(newmoon(crescent, tz))):
        year += 1
        mithuna += sid_year

    # now to figure out the month
    cigra = (crescent - mithuna) // rasi # number of the star sign the new moon falls in
    angle = ((cigra * 30) + 60) % 360  # zodiacal angle of the cusp of the star sign we're in; note that in this particular calendar, we start at 60°
    s = mithuna + (rasi * cigra) # approximate time of the saṁkrānti immediately preceding the current lunar cycle
    while (dayof(sankranti(s, angle)) > dayof(newmoon(crescent, tz))):
        s -= rasi
        cigra =(cigra - 1) % 12
        angle = (angle - 30) % 360
    while (dayof(sankranti((s + rasi), ((angle + 30) % 360))) <= dayof(newmoon(crescent, tz))):
        s += rasi
        cigra = (cigra + 1) % 12
        angle = (angle + 30) % 360
    month = NUMON[(cigra + 3) % 12]
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

    m = (MONTHNO[month] - 3) % 12 # number of the star sign that the month begins in

    jday = epoch + (year * sid_year) + (m * rasi) # approximate saṁkrānti of the month specified
    angle = ((m * 30) + 60) % 360 # zodiacal angle of the beginning of the star sign we're interested in
    crescent = newmoon(jday, tz)
    while (dayof(newmoon(crescent, tz)) < dayof(sankranti(jday, angle))):
        crescent += syn_month
    while (dayof(newmoon((crescent - syn_month), tz)) >= dayof(sankranti(jday, angle))):
        crescent -= syn_month
    if ((adhik == False) and (dayof(newmoon((crescent + syn_month), tz)) <= dayof(sankranti((jday + rasi), ((angle + 30) % 360))))):
        # we're in the leap month, but shouldn't be
        crescent += syn_month

    if (tithi == 0):
        # for some reason, it gets stuck in an infinite loop if it's the first tithi of the month
        jday = dayof(newmoon(crescent, tz))
    else:
        jday = dayof(phasetime((crescent + (tithi * Fraction(syn_month, 30))), (12 * tithi), tz))

    return jday
    
