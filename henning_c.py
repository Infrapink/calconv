#!/usr/bin/python

# Convert between Henning's tropical Tibetan calendar and Julian Days, with Chinese leap month rule

from math import floor, ceil
from fractions import Fraction
from months import NUM_TIBETAN as MONTHS, TIBETAN_NUM as MONTHNO
from solun import tropical_year as trop_year, lunar_month as syn_month, newmoon, trans, solar_term as st, phase, phasetime

tz = Fraction(6,24) # Xinjiang time; Tibet officially uses Beijing time, but Xinjiang time gives more correct results
solar_epoch = 2096243 # approximate time of the northward equinox in the era year

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

    # compute for the year
    year = (jday - solar_epoch) // trop_year
    equinox = trans( (solar_epoch + (year * trop_year)), 0, tz)
    while( moonof(trans((equinox + trop_year), 0, tz)) <= jday):
        year += 1
        equinox += trop_year
    while( moonof(trans(equinox, 0, tz)) > jday):
        year -= 1
        equinox -= trop_year

    # compute the month
    crescent = newmoon(moonof(trans(equinox, 0, tz)), tz)    
    if( round( (newmoon(moonof(trans((equinox + trop_year), 0, tz)), tz) - newmoon(crescent, tz)) / syn_month) == 12):
        # normal year
        month = MONTHS[round( (moonof(jday) - crescent) / syn_month)]
    else:
        # leap year
        m = 0 # number of the month
        z = 0 # ecliptic longitude of the next solar term, starting with the northward equinox
        l = False # have we passed the leap month?
        zhongqi = equinox # next zhongqi the lunation has to straddle to count, starting with the northward equinox

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

        month = MONTHS[m]
        if( (not l) and ( moonof(crescent + syn_month) < dayof(trans(zhongqi, z, tz)))):
            # it's the leap month
            month = "Leap " + month

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

    equinox = solar_epoch + (year * trop_year)
    jday = newmoon(moonof(equinox), tz) # losar

    if( round( (moonof(trans((equinox + syn_month), 0, tz)) - jday) / syn_month) == 12):
        # normal year
        jday = jday + (MONTHNO[month] * syn_month)
    else:
        # leap year
        m = 0 # number of the current month
        z = 0 # ecliptic longitude of the next zhongqi, starting with the northward equinox
        l = False # have we passed the leap month?
        zhongqi = equinox # time of the next zhongqi, starting with the northward equinox
        
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
        if( (leap) and (not l) and ( moonof(jday + (2 * syn_month)) < dayof(trans((zhongqi + st), (z + 30), tz)) ) ):
            # the user specified the leap month as opposed to the corresponding regular month
            jday += syn_month

    # finally, account for the tithis
    jday = dayof(phasetime( (jday + (syn_month * Fraction(tithi, 30))), (tithi * 12), tz))
    return jday
