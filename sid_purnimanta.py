#!/usr/bin/python

# Converts between consecutive Julian Days and dates in the traditional Indian lunisolar calendar, using the rules of the Sūrya Siddhānta, and in which months run from full moon to full moon.

from fractions import Fraction
from surya_siddhanta import sankranti, fullmoon, newmoon, antiphase, antiphasetime, dayof_sunrise as dayof, spos, sunrise, t_syn_month as syn_month, t_sid_year as sid_year, t_rasi as rasi, vs
from months import NUM_INDIAN_LUNAR as NUMON, INDIAN_LUNAR_NUM as MONTHNO

epoch = sankranti((vs - rasi), 330) # instant of Mīna Saṁkrānti, 0 VS

def tojd(tithi, month, year):
    '''Given a date in the calendar, compute the corresponding Julian Day'''
    tithi = int(tithi) - 1 # subtract 1 to make subsequent maths easier
    month = str(month)
    year = int(year)

    # number of the month
    if (month[:5] == "Adhik"):
        # leap month
        adhik = True
        month = month[6:]
    else:
        # normal month
        adhik = False
    cigra = NUMON[month] # number of the star sign corresponding to the month, where Meṣa is 0
    angle = ((cigra - 1) % 12) * 30 # zodiacal angle where the aforementioned star sign starts

    # compute the rasi
    mina = epoch + (year * sid_year) # Mīna Saṁkrānti of the current year
    r = sankranti((mina + (cigra * rasi)), angle)

    # compute the start of the month
    amavasya = newmoon(r) # new moon
    while (dayof(newmoon(amavasya)) < dayof(sankranti(r, angle))):
        amavasya += syn_month
    while (dayof(newmoon(amavasya - syn_month)) >= dayof(sankranti(r, angle))):
        amavasya -= syn_month
    if ((adhik == False) and (dayof(newmoon(amavasya + syn_month)) < dayof(sankranti((r + rasi), ((angle + 30) % 360))))):
        # we're in the leap month, but shouldn't be
        amavasya += syn_month
    purnima = amavasya - Fraction(syn_month, 2) # full moon preceding the corresponding new moon

    # account for the tithi and bring it home
    jday = dayof(antiphasetime((purnima + (tithi * Fraction(syn_month, 30))), (tithi * 12)))
    return jday

def fromjd(jday):
    '''Convert a Julian Day into a date in the calendar'''
    jday = Fraction(jday)

    # compute the full moon
    purnima = fullmoon(jday) # full moon on or preceding jday
    while (dayof(fullmoon(purnima)) > jday):
        purnima -= syn_month
    while (dayof(fullmoon(purnima + syn_month)) <= jday):
        purnima += syn_month
    amavasya = purnima + Fraction(syn_month, 2) # next new moon

    # compute the year
    year = (amavasya - epoch) // sid_year
    mina = epoch + (year * sid_year) # estimated instant of Mīna Saṁkrānti
    while (dayof(sankranti(mina, 330)) > dayof(newmoon(amavasya))):
        mina -= sid_year
    while (dayof(sankranti((mina + sid_year), 330)) <= dayof(newmoon(amavasya))):
        mina += sid_year

    # compute the star sign
    cigra = round((amavasya - mina) / rasi)
    angle = ((30 * cigra) - 30) % 360
    r = mina + (cigra * rasi) # time the sun enters the current star sign
    while (dayof(sankranti(r, angle)) > dayof(newmoon(amavasya))):
        cigra = (cigra - 1) % 12
        angle = (angle - 30) % 360
        r -= rasi
    while (dayof(sankranti((r + rasi), ((angle + 30) % 360))) <= dayof(newmoon(amavasya))):
        cigra = (cigra + 1) % 12
        angle = (angle + 30) % 360
        r += rasi
    month = MONTHNO[cigra]

    # check for leap months
    if (dayof(newmoon(amavasya + syn_month)) <= dayof(sankranti((r + rasi), ((angle + 30) % 360)))):
        # we're in the leap month
        month = "Adhik " + month

    # compute the tithi
    tithi = int(antiphase(sunrise(jday)) // 12) + 1

    # bring it home
    return (tithi, month, year)
