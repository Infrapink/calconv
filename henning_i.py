#!/usr/bin/python

# Convert between Henning's tropical Tibetan calendar and Julian Days, with Indian leap month rule

from math import floor, ceil
from fractions import Fraction
from months import NUM_TIBETAN as MONTHS, TIBETAN_NUM as MONTHNO
from solun import tropical_year as trop_year, lunar_month as syn_month, newmoon, trans, solar_term as st, phase, phasetime

tz = Fraction(6,24) # Xinjiang time; Tibet officially uses Beijing time, but Xinjiang time gives more correct results
solar_epoch = 2096243 -st # approximate time the sun hit 330° of the ecliptic just before the start of the era year

def dayof(jday):
    '''Determine whether an astronomical event is associated with today or tomorrow.'''
    jday = Fraction(jday)
    
    if (jday % 1 < Fraction(5,24)):
        ans = floor(jday)
    else:
        ans = ceil(jday)

    return ans

def moonof(jday):
    '''Compute the new moon associated with an astronomical event'''
    jday = Fraction(jday)

    crescent = newmoon(jday, tz)
    while( dayof(newmoon(crescent, tz)) > dayof(jday)):
        crescent -= syn_month
    while( dayof(newmoon((crescent + syn_month), tz)) <= dayof(jday)):
        crescent += syn_month

    return crescent

def fromjd(jday):
    '''Convert a Julian Day into a date in the Indian-style tropical Tibetan calendar'''
    jday = Fraction(jday)

    # begin with the month
    c = moonof(jday) # new moon that commences the month we're in

    # now account for the year
    year = (c - solar_epoch) // trop_year
    mesha = trans( (solar_epoch + (year * trop_year)), 330, tz)
    while( dayof(trans(mesha, 330, tz)) > c):
        mesha -= trop_year
        year -= 1
    while( dayof(trans((mesha + trop_year), 330, tz)) <= c):
        mesha += trop_year
        year += 1
    next_mesha = mesha + trop_year
    d = moonof(trans(next_mesha, 330, tz))
    if( round( (newmoon(d, tz) - newmoon(c, tz)) / syn_month) == 12):
        # normal year
        month = MONTHS[round( (newmoon(c) - newmoon(moonof(trans(mesha, 330, tz)))) / syn_month) - 1]
    else:
        # leap year
        m = 0 # number of the month
        z = 0 # ecliptic longitude of the next solar term, starting with the northward equinox
        l = False # have we passed the leap month?
        zhongqi = mesha + st # next zhongqi the lunation has to straddle to count, starting with the northward equinox
        crescent = newmoon((moonof(mesha) + syn_month), tz) # time of the new moon, starting with losar

        while(moonof(crescent + syn_month) <= jday):
            if(l):
                # we are passed the leap month
                m += 1
            elif( moonof(crescent + syn_month) < dayof(trans(zhongqi, z, tz))):
                # this is the leap month
                l = True
            else:
                m += 1
                z += 30
                zhongqi += st
            crescent += syn_month

        if( (not l) and ( moonof(crescent + syn_month) < dayof(trans(zhongqi, z, tz)))):
            # it's the leap month
            month = "Leap " + MONTHS[m + 1]
        else:
            month = MONTHS[m]

    # finally, compute the tithi
    tithi = int(phase( (jday + Fraction(5,24)), tz) // 12) + 1 # add 1 because humans don't count from 0
    return(tithi, month, year)

def tojd(tithi, month, year):
    '''Convert a date in Henning's reformed calendar to Julian Days.'''
    tithi = int(tithi) - 1 # subtract 1 because computers count from 0
    month = str(month)
    year = int(year)

    if(month[:4] == "Leap"):
        month = month[5:]
        leap = True
    else:
        leap = False

    mesha = solar_epoch + (year * trop_year)
    next_mesha = mesha + trop_year

    jday = newmoon((moonof(mesha) + syn_month), tz) # losar
    next_losar = newmoon((moonof(next_mesha) + syn_month), tz) # next losar

    if( round( (next_losar - jday) / syn_month) == 12):
        # normal year
        jday = jday + (MONTHNO[month] * syn_month)
    else:
        # leap year
        m = 0 # number of the current month
        z = 0 # ecliptic longitude of the next zhongqi, starting with the northward equinox
        l = False # have we passed the leap month?
        zhongqi = mesha + st # time of the next zhongqi, starting with the northward equinox
        
        while( MONTHS[m] != month ):
            if(l):
                # we are past the leap month
                m += 1
            elif( moonof(jday + syn_month) < dayof(trans(zhongqi, z, tz))):
                # this is the leap month
                l = True
            else:
                m += 1
                z += 30
                zhongqi += st
            jday += syn_month
        if( (not leap) and (not l) and ( moonof(jday + syn_month) < dayof(trans(zhongqi, z, tz)) ) ):
            # the user specified the regular month as opposed to the corresponding leap month
            jday += syn_month

    # finally, account for the tithis
    jday = dayof(phasetime( (jday + (syn_month * Fraction(tithi, 30))), (tithi * 12), tz))
    return jday
