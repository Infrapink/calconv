#!/usr/bin/python3

# Just going to record some vedic values here

from fractions import Fraction
from math import floor, ceil
from numpy import sign

# Lengths of time
# Derived from Sūrya Siddhānta chapter 1

ts = Fraction(1577917828, 1582237820) # topical days in a sidereal day
st = Fraction(1, ts) # sidereal days in a tropical day

t_sid_year = Fraction(1577917828, 4320000) # tropical days in a sidereal year
s_sid_year = Fraction(1582237820, 4320000) # sidereal days in a sidereal year

t_tithi = Fraction(1577917828, 1603000080) # tropical days in a mean tithi
s_tithi = Fraction(1582237820, 1603000080) # sidereal days in a mean tithi

t_ap_rev = Fraction(1577917828, 488203) # tropical days in one revolution of the moon's apogee
s_ap_rev = Fraction(1582237820, 488203) # sidereal days in one revolution of the moon's apogee

t_node_rev = Fraction(1577917828, 232238) # tropical days in one revolution of the moon's ascending node
s_node_rev = Fraction(1582237820, 232238) # sidereal days in one revolution of the moon's ascending node

t_rasi = Fraction(1577917828, 51840000) # tropical days in one solar month
s_rasi = Fraction(1582237820, 51840000) # sidereal days in one solar month

t_rev_aphelion = Fraction(1577917828000, 387) # tropical days in one revolution of Earth's aphelion
s_rev_aphelion = Fraction(1582237820000, 387) # sidereal days in one revolution of Earth's aphelion

t_anom_year = Fraction(1577917828000, (4320000000 - 387)) # tropical days in an anomalistic year
s_anom_year = Fraction(1582237820000, (4320000000 - 387)) # sidereal days in an anomalistic year

t_sid_month = Fraction(1577917828, 57753336) # tropical days in a sidereal month
s_sid_month = Fraction(1582237820, 57753336) # sidereal days in a sidereal month

#t_syn_month = Fraction(1577917828, 51840000) # tropical days in a synodic month
#s_syn_month = Fraction(1582237820, 51840000) # sidereal sayd in a synodic month
t_syn_month = Fraction(1577917828, 53433336) # tropical days in a synodic month
s_syn_month = Fraction(1582237820, 53433336) # sidereal days in a synodic month

t_anom_month = Fraction(1577917828, (57753336 - 488203)) # tropical days in an anomalistic month
s_anom_month = Fraction(1582237820, (57753336 - 488203)) # sidereal days in an anomalistic month

t_drac_month = Fraction(1577917828, (57753336 - 232238)) # tropical days in a draconic month
s_drac_month = Fraction(1582237820, (57753336 - 232238)) # sidereal days in a draconic month

t_prec_cycle = Fraction(1577917828, 600) # tropical days in a cycle of the precession of the equinoxes
s_prec_cycle = Fraction(1582237820, 600) # sidereal days in a cycle of the precession of the equinoxes

t_prec_q = Fraction(t_prec_cycle, 4) # tropical days in 1/4 of the precessional cycle. The time it takes for the distance between Revati and the northward equinox to change by 27°
s_prec_q = Fraction(s_prec_cycle, 4) # sidereal days in 1/4 of the precessional cycle. The time it takes for the distance between Revati and the northward equinox to change by 27°

# Epochs
ky = 588466 # Consecutive Julian Day on which the Kali Yuga begins.
se = ky + (3179 * t_sid_year) # Beginning of the Shaka Era
vs = ky + (3044 * t_sid_year) # Beginning of the Vikram Samvat
ty = ky - (t_sid_year * 5 * 432000) # Moment the Treta Yuga begins, when everything is in conjunction except for the moon's nodes; Sūrya Siddhānta 1:57
# As of the start of the Treta Yuga, the moon's node of apsis was at 0° Makara (Capricorn), or 270°
# The moon's node of declination was at 0° Tula (Libra), or 180°

# Other constants
uj_lon = 75 + Fraction(79,100) # longitude of Ujjain; 75.79° E
uj_lat = 23 + Fraction(17,100) # latitude of Ujjain; 23.17° N

JYAS_BY_PARTS = {0: 0, # 0/24 of a right angle, 0 arcminutes
                 1: 225, # 1/24 of a right angle, 225 arcminutes
                 2: 449, # 2/24 of a right angle, 450 arcminutes
                 3: 671, # 3/24 of a right angle, 675 arcminutes
                 4: 890, # 4/24 of a right angle, 900 arcminutes
                 5: 1105, # 5/24 of a right angle, 1125 arcminutes
                 6: 1315, # 6/24 of a right angle, 1350 arcminutes
                 7: 1520, # 7/24 of a right angle, 1575 arcminutes
                 8: 1719, # 8/24 of a right angle, 1800 arcminutes
                 9: 1910, # 9/24 of a right angle, 2025 arcminutes
                 10: 2093, # 10/24 of a right angle, 2250 arcminutes
                 11: 2267, # 11/24 of a right angle, 2475 arcminutes
                 12: 2431, # 12/24 of a right angle, 2700 arcminutes
                 13: 2585, # 13/24 of a right angle, 2925 arcminutes
                 14: 2728, # 14/24 of a right angle, 3150 arcminutes
                 15: 2859, # 15/24 of a right angle, 3375 arcminutes
                 16: 2978, # 16/24 of a right angle, 3600 arcminutes
                 17: 3084, # 17/24 of a right angle, 3825 arcminutes
                 18: 3177, # 18/24 of a right angle, 4050 arcminutes
                 19: 3256, # 19/24 of a right angle, 4275 arcminutes
                 20: 3321, # 20/24 of a right angle, 4500 arcminutes
                 21: 3372, # 21/24 of a right angle, 4725 arcminutes
                 22: 3409, # 22/24 of a right angle, 4950 arcminutes
                 23: 3431, # 23/24 of a right angle, 5175 arcminutes
                 24: 3438} # 24/24 of a right angle, 5400 arcminutes

# Times of rising of the zodiacal constellations, as described in Sūrya Siddhānta 3:42-44
# In other words, these are the lengths of time, in prānas, which each constellation takes to rise.
# For example, Meṣa (Aries) takes 1670 prānas to rise.
TIMES_OF_RISING = {0: 1670, # Meṣa/Aries
                   1: 1795, # Vṛṣabha/Taurus
                   2: 1935, # Mithuna/Gemini
                   3: 1935, # Karkaṭa/Cancer
                   4: 1795, # Siṃha/Leo
                   5: 1670, # Kanyā/Virgo
                   6: 1670, # Tulā/Libra
                   7: 1795, # Vṛścika/Scorpio
                   8: 1935, # Dhanu/Sagittarius
                   9: 1935, # Makara/Capricorn
                   10: 1795, # Kumbha/Aquarius
                   11: 1670} # Mīna/Pisces
                   

def jya_int(angle):
    '''Compute the jya of an angle, given in 24ths of a right angle, described in Sūrya Siddhānta 2:15-27'''
    angle = int(angle) # angle, in 24ths of a right angle
    ans = JYAS_BY_PARTS[angle]
    return ans

def jya_min(angle):
    '''Compute the jya of an angle, given in arcminutes, as described in Sūrya Siddhānta 2:15-33'''
    angle = Fraction(angle) % 21600 # reduce to a number between 0° and 360°
    if (angle in (5400, 16200)):
        ans = 3438
    elif (angle in (0, 10800)):
        ans = 0
    elif (angle % 255 == 0):
        # whole number of parts
        ans = JYAS_BY_PARTS[(angle % 5400) / 255] # divide by 5400 to reduce it to a part of a right angle.
    else:
        # angle is cannot be expressed in the form n/24 of a right angle where n is an integer.
        if (angle <= 5400):
            # 0° - 90°
            angle = angle
        elif (angle <= 10800):
            # 90° - 180 °
            angle = 10800 - angle
        elif (angle <= 16200):
            # 180° - 270°
            angle = angle - 10800
        else:
            # 270° - 360°
            angle = 21600 - angle
        alpha = 225 * (angle // 225)
        omega = angle + 225
        gata = jya_int(alpha / 225) # preceding tabular jya
        gamya = jya_int(omega / 225) # following tabular jya
        rem = angle - alpha
        r = Fraction((rem * (gamya - gata)), 225)
        ans = gata + r

    #if (angle >= 10800):
        #ans = 0 - ans # becomes negative if in the bottom quadrant.
    return ans

def jya(angle):
    '''Compute the jya of an angle, given in degrees, as described in Sūrya Siddhānta 2:15-27'''
    angle = Fraction(angle)
    ans = jya_min(angle * 60)
    return ans

def arcjya_parts(j):
    '''Given a jya, find the corresponding angle in terms of 24ths of a right angle.'''
    j = int(j)
    ans = 0
          
    while (jya_int(ans + 1) <= j):
        ans += 1

    return ans

def arcjya_min(j):
    '''Given a jya, find the corresponding angle in arcminutes as described in Sūrya Siddānta 2:33'''
    j = Fraction(j)

    if (j == 3438):
        ans = 5400
    else:
        gata = jya_int(arcjya_parts(j)) # highest tabular jya not greater than j
        gamya = jya_int(arcjya_parts(j) + 1) # lowest tabular jya greater than j
        frac = Fraction((j - gata), (gamya - gata))
        ans = 225 * (frac + arcjya_parts(j))
    return ans

def arcjya(j):
    '''Given a jya, find the corresponding angle in degrees as described in Sūrya Siddhānta 2:33'''
    j = Fraction(j)
    ans = Fraction(arcjya_min(j), 60)
    return ans

def kotijya_parts(angle):
    '''Given an angle in 24ths of a right angle, compute the kotijya'''
    parts = int(angle)
    ans = jya(24 - angle)
    return ans

def kotijya_min(angle):
    '''Given an angle in arcminutes, compute the kotijya.'''
    angle = Fraction(angle)
    ans = jya_min(5400 - angle)
    return ans

def kotijya(angle):
    '''Given an angle in degrees, compute the kotijya.'''
    angle = Fraction(angle)
    ans = jya(90 - angle)
    return ans

def utkramajya(angle):
    '''Given an angle in degrees, compute the utkramajya.'''
    angle = Fraction(angle)
    ans = 3438 - kotijya(angle)
    return ans

es = 12 * Fraction(jya(uj_lat), kotijya(uj_lat)) # length of the equinoctial shadow at Ujjain in angulas, as described in Sūrya Siddhānta 3:16

def lon2dec(lon):
    '''Given a celestial body's zodiacal longitude, compute its declination, as per Sūrya Siddhānta 2:28-30'''
    # nominally, opposition to Spica corresponds to northward equinox.
    # it hasn't for centuries, but that's what the mathematical methods are based on.
    lon = Fraction(lon) # zodiacal longitude, expressed in degrees.
    jd = jya(lon) * Fraction(1397, 3438)
    dec = arcjya(jd) # declination
    if (lon > 180):
        # nominally means the sun is below the celestial equator
        dec = 0 - dec
    return dec

#2:29-30 has rules for finding the anomaly and commutation

def anomaly(jday, anom):
    jday = Fraction(jday) # instant for which we wish to determine the anomaly
    anom = Fraction(anom) # anomalistic period

    revs = (jday - ty) // anom # anomalistic revolutions that have passed so far
    apogee = ty + (revs * anom)
    angle = 360 * Fraction((jday - apogee), anom) # anomalistic angle
    return angle

def solar_anomaly(jday):
    jday = Fraction(jday)
    ans = anomaly(jday, t_anom_year)
    return ans

def lunar_anomaly(jday):
    jday = Fraction(jday)
    ans = (anomaly(jday, t_anom_month) + 270) % 360 # add 270 to account for the node's position at the start of the Treta Yuga
    return ans


# See 2:29—30 for how to get bhujajya and kotijya
# Basically, if in quadrant 0 or 2 of the circle, you want the jya and kotijya of (angle - theta), where theta is 0° or 180° depending on quadrant.
# If it's in quadrant 1 or 3, you want the jya and kotijya of (theta - angle), where theta is either 180° or 360°

# 2:34 describes the epicycles of the apsides of the sun and the moon.
# At apogee, the sun's apsidal epicycle is 14° and the moon's apsidal epicycle is 32°
# At 90° from apogee, the sun's apsidal epicycle is 13°40' and the moon's apsidal epicycle is 31°40'
# At 180° from apogee (at perigee), the sun's apsidal epicycle is 14° and the moon's apsidal epicycle is 32°
# At 270° from apogee, the sun's apsidal epicycle is 13°40' and the moon's apisdal epicycle is 31°40'.

def bhujajya(angle):
    '''Compute the bhujajya (base jya) of a given angle'''
    angle = Fraction(angle)
    if (angle <= 90):
        bhujajya = jya(angle)
    elif (angle <= 180):
        bhujajya = jya(180 - angle)
    elif (angle <= 270):
        bhujajya = jya(angle - 180)
    else:
        bhujajya = jya(360 - angle)

    return bhujajya    

def solar_epicycle(jday):
    '''Compute the actual size of the sun's apsidal epicycle, as described in Sūrya Siddhānta 2:29—38'''
    jday = Fraction(jday) # the instant we're interested in

    delta = Fraction(20,60) # 20 arcminutes, or 20/60 of a degree
    anom = solar_anomaly(jday)
    bj = bhujajya(anom)
    epsilon = delta * Fraction(bj, 3438) # result is in DEGREES
    sphuta = 14 - epsilon # result is in DEGREES
    return sphuta # degrees of the zodiac which the solar apsidal epicycle spans

def lunar_epicycle(jday):
    '''Compute the actual side of the moon's apsidal epicycle, as described in Sūrya Siddhānta 2:29—38'''
    jday = Fraction(jday) # the instant we're interested in

    anom = lunar_anomaly(jday)
    bj = bhujajya(anom)
    sphuta = 32 - (Fraction(20, 60) * Fraction(bj, 3438)) # result is in DEGEEES
    return sphuta # degrees of the zodiac which the lunar apsidal epicycle spans

# sphuta refers to the correct size of the epicycle at time jday.
# Now we need to find the body's offset from the apsis.

def solar_phala(jday):
    '''Compute the mandaphala of the sun at time jday, as described in Sūrya Siddhānta 2:39'''
    jday = Fraction(jday)

    sphuta = solar_epicycle(jday)
    anom = solar_anomaly(jday)
    bhujaphala = Fraction((bhujajya(anom) * sphuta), 360)
    mandaphala = arcjya(bhujaphala) # screw minutes, I'm giving the answer in DEGREES
    if (anom < 180):
        # true position is lagging mean position; if it's ahead of perigee, the true position is leading the mean position
        mandaphala *= (-1)
    return mandaphala # actual difference between the sun's mean and true positions, in DEGREES

def lunar_phala(jday):
    '''Compute the mandaphala of the moon at time jday, as described in Sūrya Siddhānta 2:39'''
    jday = Fraction(jday)

    sphuta = lunar_epicycle(jday)
    anom = lunar_anomaly(jday)
    bhujaphala = Fraction((bhujajya(anom) * sphuta), 360)
    mandaphala = arcjya(bhujaphala) # screw minutes, I'm giving the answer in DEGREES
    if (anom < 180):
        # true position is lagging mean position
        mandaphala *= (-1) # between 180° and 360° of the anomalistic path, the true position leads the mean position
    return mandaphala # actual difference between the moon's mean and true positions, in DEGREES

def spos(jday):
    '''Compute the true position of the sun, as described in Sūrya Siddhānta chapter 2'''
    jday = Fraction(jday)

    mean = 360 * Fraction(((jday - ty) % t_sid_year), t_sid_year) # mean position of the sun
    tpos = (mean + solar_phala(jday)) % 360 # true position of the sun
    return tpos

def mpos(jday):
    '''Compute the true position of the moon, as described in Sūrya Siddhānta chapter 2'''
    jday = Fraction(jday)

    mean = 360 * Fraction(((jday - ty) % t_sid_month), t_sid_month) # mean zodiacal position of the moon
    tpos = (mean + lunar_phala(jday)) % 360 # true zodiacal position of the moon
    return tpos

def phase(jday):
    '''Compute the angle between the sun and the moon'''
    # 0° → new moon
    # 180° → full moon
    jday = Fraction(jday)
    angle = (mpos(jday) - spos(jday)) % 360 # angle between the sun and the moon
    return angle

def antiphase(jday):
    '''Compute the angle between the sun and the moon, where opposition is taken as 0'''
    # 0° → full moon
    # 180° → new moon
    jday = Fraction(jday)
    ans = (phase(jday) + 180) % 360
    return ans
    
def newmoon(jday):
    '''Compute the time of the closest new moon to time jday'''
    jday = Fraction(jday)

    p = 0
    # zero in on the time of the new moon
    # start with increments of 1/(60^p) and reduce the size of the increments until we get to within 0.4 seconds
    while (p < 4):
        while ((phase(jday) >= 180) and (phase(jday + Fraction(1, (60 ** p)) > phase(jday)))):
            jday += Fraction(1, (60 ** p))
            if (phase(jday) == 0):
                p = 4
                break
        while ((phase(jday) < 180) and (phase(jday - Fraction(1, (60 ** p)) < phase(jday)))):
            jday -= Fraction(1, (60 ** p))
            if (phase(jday) == 0):
                p = 4
                break
        p += 1
    return jday

def fullmoon(jday):
    '''Compute the time of the closes full moon to time jday'''
    jday = Fraction(jday)

    p = 0
    # zero in on the time of the full moon, in increments of 1/(60^p), with p increasing each loop.
    while (p < 4):
        while ((phase(jday) < 180) and (phase(jday + Fraction(1, (60 ** p))) <= 180)):
            jday += Fraction(1, (60 ** p))
        while ((phase(jday) > 180) and (phase(jday - Fraction(1, (60 ** p))) >= 180)):
            jday -= Fraction(1, (60 ** p))
        p += 1
    return jday

def phasetime(jday, angle):
    '''Zero in on the time of a given angle between the sun and the moon'''
    jday = Fraction(jday) # time we start with. find the time closest to jday when the angle between the sun and the moon is equal to angle.
    angle = Fraction(angle) # desired angle between the sun and the moon

    p = 0
    while (p < 4):
        f = Fraction(1, (60 ** p))
        while (phase(jday + f) <= angle):
            jday += f
        while (phase(jday - f) >= angle):
            jday -= f
        p += 1
    return jday

def antiphasetime(jday, angle):
    '''Zero in on the time of a given angle between the sun and the moon, where the full moon is taken as 0'''
    jday = Fraction(jday) # time we start with. find the time closest to jday when the angle between the sun and the moon is equal to angle
    angle = Fraction(angle) # desired angle between the sun and the moon

    while ((antiphase(jday) >= 270) and (angle <= 90)):
        jday += 1
    while ((antiphase(jday) <= 90) and (angle >= 270)):
        jday -= 1

    p = 0
    while (p < 4):
        f = Fraction(1, (60 ** p))
        while (antiphase(jday + f) <= angle):
            jday += f
        while (antiphase(jday - f) >= angle):
            jday -= f
        p += 1
    return jday
    
def sankranti(jday, angle):
    '''Compute the time the sun hits a given zodiacal angle'''
    jday = Fraction(jday) # time given
    angle = Fraction(angle) # zodiacal longitude we're looking for, in DEGREES
    
    while ((spos(jday) <= 90) and (angle >= 270)):
        jday -= 1
    while ((spos(jday) >= 270) and (angle <= 90)):
        jday += 1

    p = 0
    while (p < 4):
        f = Fraction(1, (60 ** p))
        while (((spos(jday + f) <= angle)) and (spos(jday + f) > spos(jday))):
            jday += f
        while (((spos(jday - f) >= angle)) and (spos(jday - f) < spos(jday))):
            jday -= f
        if (spos(jday) == angle):
            break
        p += 1

    return jday # this is the time the sun's zodiacal longitude is equal to angle, ± 0.4 seconds

def prec(jday):
    '''Compute the precession of the equinoxes, as described in Sūrya Siddhānta 3:9–12'''
    # The language in the Sūrya Siddhanta is complicated and confusing,
    # which Burgess attributes to the precession being added well after the rest of the next,
    # and later interpolated to change it from a true revolution to a libration.
    # John Bentley, in Hindu Astronomy (1825), describes the equinox
    # as moving according to an epicycle with a diameter of 108° of the zodiac.
    # Burgess makes a good case that Bentley is mistaken (p. 120).
    # Dershowitz & Rheingold use Bentley's formulation,
    # but their algorithms are full of bizarre errors and nonsensical procedures,
    # and as such I feel confident in ignoring them entirely.
    
    jday = Fraction(jday) # instant that we want to determine the precession for.
    frac = (jday - ky) * Fraction(600, 1577917828) # Sūrya Siddhānta 3:9
    angle = arcjya(frac) * Fraction(3,10)

    # angle is the differenve between Revati and the northward equinox.
    # but which direction is it?

    osc = Fraction(((jday - ky) % t_prec_cycle), t_prec_cycle) # how far into the precession cycle are we?
    if (osc >= Fraction(1,2)):
        # Revati is ahead of the equinox.
        # as such, in the zodiacal reference frame,
        # the sun's longitude is lower
        angle = angle * (-1)
    else:
        angle = angle

    return angle

def troplon(jday):
    '''Compute the sun's actual (tropical) longitude, as described in Sūrya Siddhānta 3:9–12'''
    jday = Fraction(jday)

    ans = (spos(jday) + prec(jday)) % 360
    return ans

def tropdec(jday):
    '''Compute the sun's declination, accounting for the precession of the equinoxes'''
    jday = Fraction(jday)
    ans = lon2dec(troplon(hday))
    return ans

#def daylength(jday):
    #'''Compute the "day and night" of the sun, as described in Sūrya Siddhānta 2:59'''
    # for the sun, this is the time between two successive transits of a given meridian
    #jday = Fraction(jday)

    #daily_motion = ??? #figure this out
    #cigra = troplon(jday) // 30 # number of the zodiac sign that the sun is in
    #ans = 21600 + Fraction((daily_motion * TIMES_OF_RISING[cigra]), 1800)
    # there are 21600 prānas in a mean sidereal day
    # the sun is never in retrograde, and as such the answer will always be greater than a mean sidereal day
    
    #return ans # sidereal transit time of the sun, in PRÃNAS

def asc_p(jday):
    '''Compute the ascensional difference of the sun, in PRÃNAS, as described in Sūrya Siddhānta 2:61-63'''
    jday = Fraction(jday)

    dec = lon2dec(troplon(jday)) # declination of the sun
    cara = Fraction((es * jya(abs(dec))), 12) * Fraction(3438, (3438 - utkramajya(abs(dec)))) # kshitijya times some other suff; see Sūrya Siddhānta 2:60—61
    ans = arcjya_min(cara) * sign(dec) # ascensional difference, measured in prānas; see  Sūrya Siddhānta 2:60-61

    return ans

def asc(jday):
    '''Compute the ascensional difference of the sun, expressed as a fraction of a tropical day.'''
    jday = Fraction(jday)

    # there are 21600 prānas in a sidereal day.
    # to convert these into tropical days, it must be multiplied by ts
    ans = Fraction(asc_p(jday), 21600) * ts
    return ans

def halfday(jday):
    '''Compute the length of the half-day, as described in Sūrya Siddhānta 2:61-63'''
    jday = Fraction(jday)

    ans = Fraction(6,24) + asc(jday) # time from sunrise to noon, which is equal to the time from noon to sunset
    return ans

def halfnight(jday):
    '''Compute the length of the half-night, as described in Sūrya Siddhānta 2:61-63'''
    jday = Fraction(jday)

    ans = Fraction(6,24) - asc(jday) # time from sunset to midnight, which is equal to the time from midnight to sunrise
    return ans

def sunrise(jday):
    '''Compute the time of the sunrise between the midnights prior and subsequent to jday, expressed as a fraction of a tropical day'''
    jday = Fraction(jday)

    dawn = floor(jday) + halfday(jday)
    return dawn

def sunset(jday):
    '''Compute the time of sunset between the midnights prior and subsequent to jday, expressed as a fraction of a tropical day'''
    jday = Fraction(jday)

    if (jday % 1 == 0):
        # the algorithm gets confused if we feed it a mignight
        # because floor(jday) == ceil(jday) and so it
        # gives yesterday's sunset
        dusk = jday + 1 - halfnight(jday)
    else:
        dusk = ceil(jday) - halfnight(jday)
    return dusk

# 2:64—66 explains how to find the yogas, nakshatras, and tithis

def dayof_sunrise(jday):
    '''Compute the Julian Day associated with an astronomical event, where the civil day begins at sunrise'''
    # The first day of a solar month is the day that the sun rises while already in the associated star sign
    # The first day of a normal synodic month is the day beginning with the first sunrise following the instant of the new moon
    # In some calendrs, the first day of the synodic month is the day beginning with the first sunrise following the instant of the full moon
    jday = Fraction(jday)
    ans = round(jday)

    while (sunrise(ans) < jday):
        ans += 1
    while (sunrise(ans - 1) >= jday):
        ans -= 1

    return ans

def dayof_sunset(jday):
    '''Compute the Julian Day associated with an astronomical event, where the civil day begins at sunset'''
    # The first day of the solar month is the day whose midnight follows the first sunset when the sun is in the associated star sign
    # Tne first day of a normal synodic month is the day whose midnight comes after the first sunset following the instant of the new moon
    # In some calendars, the first day of the synodic month is the day whose midnight follows the first sunset following the instant of the full moon
    jday = Fraction(jday)
    ans = round(jday)

    while (sunset(ans) < jday):
        ans += 1
    while (sunset(ans - 1) >= jday):
        ans -= 1

    return (ans + 1) # have to add 1 because the algorithms model the tropical day as running from midnight to midnight

def dayof_malayali(jday):
    '''Compute the Julian Day associated with a given astronomical event, as per the Malayali (Keralan) rule'''
    # Here's how it works in Kerala.
    # Compute the instant ⅗ between sunrise and sunset; this is termed the aparahna
    # If the instant happens after the aparahna, the corresponding day is tomorrow
    # Otherwise, it's today
    # Source: http://packolkata.gov.in/INDIAN_CALADAR_PAC.pdf
    jday = Fraction(jday) # instant we are interested in

    aparahna = sunrise(jday) + ((sunset(jday) - sunrise(jday)) * Fraction(3,5))
    if (jday > aparahna):
        ans = ceil(jday)
    else:
        ans = floor(jday)

    return ans

def dayof_tamil(jday):
    '''Compute the Julian Day associated with an astronomical event, as per the Tamil rule'''
    # If the even happens between sunset and sunrise, it belongs to the following day
    # If it happens while the sun is up, it belongs to the current day
    # Source: http://packolkata.gov.in/INDIAN_CALADAR_PAC.pdf
    jday = Fraction(jday) # instant we're interested in

    if (jday > sunset(jday)):
        ans = ceil(jday)
    else:
        ans = floor(jday)

    return ans
