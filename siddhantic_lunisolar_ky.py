#!/usr/bin/python

# A programme to convert between Julian Days and dates in the traditional Indian lunisolar calendar (Kali Yuga era), according to methods described in the Sūrya Siddhānta

# Indian days start at sunrise
# Roman days start at midnight
# Since this is a lunisolar calendar, days are numbered according to the tithi which is active at sunrise
# As such, some days numbers may be skipped

from math import floor, ceil
from fractions import Fraction
from surya_siddhanta import sankranti, newmoon, ky as epoch, t_sid_year as sid_year, t_rasi as rasi, t_syn_month as syn_month, spos, mpos, sunrise, phasetime, phase
from months import INDIAN_LUNAR_NUM as MONTHNO, NUM_INDIAN_LUNAR as NUMON

def dayof(jday):
    '''Determine the Roman day of an astronomical event'''
    # A month is considered to start on the day of the first sunrise after a new moon.

    jday = Fraction(jday) # the time we are interested in

    if (sunrise(jday) <= jday):
        # sunrise comes before the event, so it starts tomorrow
        ans = ceil(jday)
    else:
        # event is before sunrise, so it starts on that Roman day
        ans = floor(jday)

    return ans

def moonday(crescent):
    '''Compute the Roman day that a lunar month begins'''
    crescent = Fraction(crescent) # a new moon
    ans = dayof(newmoon(crescent))
    return ans

def sunday(conjunction, angle):
    '''Compute the Roman day that a solar month begins'''
    conjunction = Fraction(conjunction) # the time that the sun is in conjunction with the cusp of a star sign
    angle = Fraction(angle) # zodiacal longitude of the cusp of the star sign
    ans = dayof(sankranti(conjunction, angle))
    return ans

def fromjd(jday):
    '''Given a Julian Day, compute a date in the traditional Indian lunisolar calendar'''
    jday = Fraction(jday)

    # determine the new moon
    luns = (jday - epoch) // syn_month
    crescent = newmoon(epoch + (luns * syn_month))
    while (moonday(crescent) > jday):
        crescent -= syn_month
    while (moonday(crescent + syn_month) <= jday):
        crescent += syn_month

    # determine the year
    year = (jday - epoch) // sid_year
    mina = epoch + (year * sid_year) - rasi # approximate time of Mīna Saṁkrānti
    while (sunday((mina + sid_year), 330) <= moonday(crescent)):
        year += 1
        mina += sid_year
    while (sunday(mina, 330) > moonday(crescent)):
        year -= 1
        mina -= sid_year

    # determine the month
    cigra = (crescent - mina) // rasi # star sign the new moon is in
    angle = (330 + (cigra * 30)) % 360 # zodiacal longitude of the cusp of the rasi

    while (sunday((mina + ((cigra + 1) * rasi)), ((angle + 30) % 360)) <= moonday(crescent)):
        cigra += 1
        angle += 30
    while (sunday((mina + (cigra * rasi)), angle) > moonday(crescent)):
        cigra -= 1
        angle -= 30
    month = MONTHNO[cigra] # name of the month

    # check if it's a leap month
    if (moonday(crescent + syn_month) <= sunday((mina + ((cigra + 1) * rasi)), ((angle + 30) % 360))):
        month = "Adhik " + month

    # get the tithi
    # a tithi is the time it takes the moon to gain 12° on the sun
    # the number of a day's tithi is that tithi which is active at sunrise
    #day = (((mpos(sunrise(jday)) - spos(sunrise(jday))) % 360) // 12) + 1
    tithi = (phase(sunrise(jday)) // 12) + 1

    return(tithi, month, year)

def tojd(tithi, month, year):
    '''Given a date in the traditional Indian lunisolar calendar (Kali Yuga era), compute the corresponding Julian Day.'''
    tithi = int(tithi) - 1 # this is a tithi rather than a tropical day. subtract 1 because computers count from 0
    month = str(month)
    year = int(year)

    # count the years
    jday = epoch + (year * sid_year) - rasi # approximate time of Mīna Saṁkrānti

    # account for the month
    if (month[:5] == "Adhik"):
        # leap month specified
        month = month[6:]
        adhik = True
    else:
        # normal month specified
        adhik = False

    cigra = NUMON[month] # number of the month
    angle = (330 + (cigra * 30)) % 360 # zodiacal angle of the cusp of the star sign corresponding to the month
    jday = jday + (cigra * rasi) # approximate time of the saṁkrānti preceding the new moon

    crescent = newmoon(jday)
    while (moonday(crescent) < sunday(jday, angle)):
        crescent += syn_month
    while (moonday(crescent - syn_month) >= sunday(jday, angle)):
        crescent -= syn_month
    if ((adhik == False) and (moonday(crescent + syn_month) < sunday((jday + rasi), ((angle + 30) % 360)))):
        # there is a leap month and we need to be in the non-leap month
        crescent += syn_month

    # count the tithis
    #jday = dayof(phasetime((crescent + (day * tithi)), (day * 12)))
    lunar_angle = tithi * 12
    t = crescent + (tithi * Fraction(syn_month, 30))
    m = phasetime(t, lunar_angle)
    jday = m
    while (sunrise(jday) < m):
        jday += 1
    while (sunrise(jday - 1) >= m):
        jday -= 1
    jday = floor(jday)

    return jday
