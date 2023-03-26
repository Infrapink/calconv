#!/usr/bin/python

# Various functions used in modern Hindu calendars.

from decimal import Decimal
from fractions import Fraction
from math import floor, ceil, sqrt
from numpy import sign

sid_year = Fraction(1577917828, 4320000) # sidereal year; Surya Siddhanta 1:29-40
sid_month = Fraction(1577917828, 57753336) # sidereal month; Surya Siddhanta 1:29-40
syn_month = Fraction(1577917828, 53433336) # synodic month; Surya Siddhanta 1:29-40
rasi = Fraction(sid_year, 12) # mean time for the sun to cross a constellation

ky = 588466 # beginning of the Kali Yuga in Julian Days
se = ky + (3179 * sid_year) # Beginning of the Shaka Era
#vs = ky + (3694 * sid_year) # Beginning of the Vikram Samvat
vs = ky + (3046 * sid_year)

creation = ky - (1955880000 * sid_year) # Surya Siddhanta 1:13-23
anom_year = Fraction(1577917828, (4320000 - 387)) # anomalistic year
anom_month = Fraction(1577917828, (57753336 - 488199)) # anomalistic month
#anom_month = Fraction(1577917828, 428203)

trop_year = Fraction(1577917828, 4320180) # Surya Siddhanta 3:9 and Bugess' commentary on same. This is not directly part of any traditional Indian calendar system, which assume libration rather than precession of the equinoxes. Still, it might be useful elsewhere.

uj_lon = 75 + Fraction(46, 60) + Fraction(6, 3600) # longitude of Ujjain, in DEGREES
uj_lat = 23 + Fraction(9, 60) # latitude of Ujjain, in DEGREES

# This is the dictionary of jyas by segment, derived from Surya Siddhanta 2:15-22 and tabulated by Burgess.
# Each segment is 1/24 of a right angle; thus, for each value n in table, we get the jya of an arc of n segments, or n/24 or a right angle.
#
# A jya is a measurement of a line based on an arc of a circle.
# Select an arc of a given circle. Draw a radius from the centre to one point of the arc, then draw a line from the other point of the arc perpendicular to that radius.
# The length of the perpendicular line, from the point on the circle to where it intersects the radius, is the jya of that arc.
#
# If you draw this out, you will see that the jya of an arc divided by the radius is equal to the sine of the angle subtended by that arc.
# In other words, if the angle θ subtends an arc AB, then jya(AB) == r*sin(θ)
#
# This dictionary assumes a circle of radius 3438 units. As such, the sine of an arc can be obtained by taking its jya and dividing it by 3438.

JYA_SEG = {0: 0,    # 0º == 0 radians
           1: 225,
           2: 449,
           3: 671,
           4: 890,
           5: 1105,
           6: 1315,
           7: 1520,
           8: 1719,
           9: 1910,
           10: 2098,
           11: 2267,
           12: 2431, # 45º == π/4 radians
           13: 2585,
           14: 2728,
           15: 2859,
           16: 2978,
           17: 3084,
           18: 3177,
           19: 3256,
           20: 3321,
           21: 3372,
           22: 3409,
           23: 3431,
           24: 3438} # 90º == π/2 radians

# This next dictionary gives the jya for an arc which subtends an angle of k arcminutes. That's MINUTES, not degrees or radians! Don't forget to convert when necessary!

JYA_MIN = {0: 0,       # 0º == 0 radians
           225: 225,
           450: 449,
           675: 671,
           900: 890,
           1125: 1105,
           1350: 1315,
           1575: 1520,
           1800: 1719,
           2025: 1910,
           2250: 2098,
           2475: 2267,
           2700: 2431, # 45º == π/4 radians
           2925: 2585,
           3150: 2728,
           3375: 2850,
           3600: 2978,
           3825: 3084,
           4050: 3177,
           4275: 3256,
           4500: 3321,
           4725: 3372,
           4950: 3409,
           5175: 3431,
           5400: 3438} # 90º == π/2 radians

YOGS = ("Vishkumbha", "Preeti", "Ayushman", "Saubhagya", "Shobhana", "Atiganda", "Sukarma", "Dhriti", "Shoola", "Ganda", "Vriddhi", "Dhruva", "Vyaghata", "Harshana", "Vajra", "Siddhi", "Vyatipata", "Variyana", "Parigha", "Shiva", "Siddha", "Sadhya", "Shubha", "Shukla", "Brahma", "Indra", "Vaidhriti")

ASCHIGRA = {0: Fraction(1670, 1800),
            1: Fraction(1795, 1800),
            2: Fraction(1935, 1800),
            3: Fraction(1935, 1800),
            4: Fraction(1795, 1800),
            5: Fraction(1670, 1800)}
           
def marc(jday, orbital_period):
    '''Returns the fraction of the zodiac a celestial object has traced, from its last conjunction with Revati, based on Surya Siddhanta 1:53'''
    jday = Fraction(jday)
    orbital_period = Fraction(orbital_period) # time for the body to traverse the zodiac; this will usually be sid_year or sid_month

    frac = Fraction((jday - creation), orbital_period)
    ans = frac % 1
    while (ans < 0):
        ans += 1
    return ans

def mpos(jday, orbital_period):
    '''Mean zodiacal longitude of a celestial body, based on Surya Siddhanta 1:53'''
    jday = Fraction(jday) # Julian Day
    orbital_period = Fraction(orbital_period) # time for the body to traverse the zodiac; this will ususally be sid_year or sid_month

    ans = marc(jday, orbital_period) * 360 # angle in DEGREES
    return ans

def meansun(jday):
    '''zodiacal longitude of the sun as of jday, in DEGREES'''
    jday = Fraction(jday)

    ans = mpos(jday, sid_year)
    return ans

def meanmoon(jday):
    '''zodiacal longitude of the moon as of jday, in DEGREES'''
    jday = Fraction(jday)

    ans = mpos(jday, sid_month)
    return ans

def meanphase(jday):
    '''mean phase of the moon as of jday'''
    # phase of the moon is given in degrees.
    ## 0º == 360º: new moon/dark moon/0th quarter/4th quarter
    ## 180º: full moon/second quarter
    
    jday = Fraction(jday)

    sun = meansun(jday)
    moon = meanmoon(jday)

    phase = moon - sun
    while phase < 0:
        phase += 360
    phase %= 360
    return phase

def jya(angle):
    '''obtain the jya of any angle, as per Surya Siddhanta 2:31-33'''
    angle = Fraction(angle) % 21600 # angle must be in MINUTES! Not degrees! Not radians! MINUTES!
    
    if angle > 16200: # 270º == 3π/2 radians
        angle = 21600 - angle
    elif angle > 10800: # 180º == π radians
        angle = angle - 10800
    elif angle > 5400: # 90º == π/2 radians
        angle = 10800 - angle
    else:
        angle = angle

    alpha = floor(Fraction(angle, 225))
    omega = ceil(Fraction(angle, 225))
    frac = Fraction(angle, 225) % 1

    #inter = Fraction((frac * (JYA_SEG[omega] - JYA_SEG[alpha])), 225)
    inter = frac * (JYA_SEG[omega] - JYA_SEG[alpha])
    ans = JYA_SEG[alpha] + inter
    return ans

def kotijya(angle):
    '''obtain the kotijya of any angle, as per Surya Siddhanta 2:31-33'''
    angle = Fraction(angle) % 21600 # angle must be in MINUTES! Not degrees! Not radians! MINUTES!

    ans = jya(5400 - angle)
    return ans

def utkramajya(angle):
    '''obtain the utkrama-jya of any angle, as per Surya Siddhanta 2:321-33'''
    angle = Fraction(angle)
    ans = 3438 - kotijya(angle)
    return ans

def ayj(vert):
    '''Given the jya of an arc, find the length of that arc, in MINUTES, as per Surya Siddhanta 2:33'''
    vert = Fraction(vert)

    alpha = vert // 225
    while (JYA_SEG[alpha + 1] <= vert):
        alpha += 1
    while (JYA_SEG[alpha] > vert):
        alpha -= 1

    if JYA_SEG[alpha] == vert:
        ans = 225 * alpha
    else:
        omega = alpha + 1
        frac = Fraction((vert - JYA_SEG[alpha]), (JYA_SEG[omega] - JYA_SEG[alpha]))
        ans = 225 * (alpha + frac)

    return ans

def tpos(jday, sid, anom, ext):
    '''True position of a celestial body, based on Surya Siddhanta chapter 2'''
    jday = Fraction(jday) # Julian Day
    sid = Fraction(sid) # Sidereal revolution; time it takes the body to traverse the zodiac
    anom = Fraction(anom) # Anomalistic revolution; time it takes the body to move from apogee to apogee.
    ext = Fraction(ext) # Maximum "diameter" of the epicycle, measured in MINUTES of the deferent.

    mean = mpos(jday, sid) # mean position; location of the centre of the epicycle upon the deferent
    frac = Fraction(((jday - creation) % anom), anom) # fraction of the anomalistic revolution the body has undergone
    anom_angle = frac * 360 # anomalistic longitude, in DEGREES
    #print(float(anom_angle))

    # now to calculate the amount the epicycle shrinks. See Surya Siddhanta 2:34
    # this gives an answer in MINUTES
    if anom_angle <= 90:
        shrinkage = 20 * Fraction(anom_angle, 90)
    elif anom_angle <= 180:
        shrinkage = 20 * Fraction((180 - anom_angle), 90)
    elif anom_angle <= 270:
        shrinkage = 20 * Fraction((anom_angle - 180), 90)
    else:
        shrinkage = 20 * Fraction((360 - anom_angle), 90)

    sphuta = ext - shrinkage # true "diameter" of the epicycle, measured in MINUTES of deferent
    offset = ayj(Fraction(sphuta, 21600) * jya(60 * anom_angle)) # difference between the mean and true positions of the body
    #offset_angle = Fraction(jya(60 * anom_angle), 3438) # multiple anom_angle by 60 to convert it into MINUTES
    #offset = offset_angle * sphuta * Fraction(1,2) # since sphuta is the diameter of the epicycle, we need to divide it by 2 because what we want is the radius
    offset = Fraction(offset, 60) # divide by 60 to convert from minutes to degrees
    #print(float(offset))
    #print(float(offset))
    if ((anom_angle >= 270) or (anom_angle < 90)):
        ans = mean + offset
    else:
        ans = mean - offset

    while (ans < 0):
        ans += 360

    ans = ans % 360

    return ans

def naive_sun(jday):
    '''Calculate the true position of the sun, based on a naïve reading of Surya Siddhanta chapter 2, which assumes an anomalistic year independent of the sidereal.'''

    jday = Fraction(jday)
    ext = 14 * 60 # maximum circumference of the epicycle, in MINUTES. Surya Siddhanta 2:34
    arc = Fraction((jday - creation), anom_year) % 1 # how far along the anomalistic year is the sun?

    ans = tpos(jday, sid_year, anom_year, ext)
    return ans

def truesun(jday):
    '''Calculate true position of the sun, as per Surya Siddhanta chapter 2'''
    # OK. So. Look.
    # Surya Siddhanta 1:41 gives a very precise value for the anomalistic year,
    # but Burgess says that traditional Indian astronomers completely ignored this
    # (and to be fair the value is quite a bit off).
    # Taking the value of the anomalistic year to be precisely equal to the sidereal year
    # does appear to yield the correct value of Mesha Sankranti,
    # so that's what I'm going with.
    jday = Fraction(jday)
    ext = 14 * 60 # maximum circumference of the epicycle, in MINUTES! Surya Siddhanta 2:34
    #arc = Fraction((jday - creation), anom_year) % 1 # how far is the sun past the apogee?

    mean = mpos(jday, sid_year)
    arc = (mean - 90) % 360
    if (arc <= 90):
        shrinkage = 20 * Fraction(arc, 90)
    elif (arc <= 180):
        shrinkage = 20 * Fraction((180 - arc), 90)
    elif (arc <= 270):
        shrinkage = 20 * Fraction((arc - 180), 90)
    else:
        shrinkage = 20 * Fraction((360 - arc), 90)

    sphuta = ext - shrinkage # true diameter of the epicycle, given in MINUTES of the deferent.
    offset = ayj(Fraction(sphuta, 21600) * jya(60 * arc)) # difference between the sun's mean and true positions
    offset = Fraction(offset, 60) # divide by 60 to convert from minutes to degrees
    #print(float(offset))
    #if ((arc <= 90) or (arc > 270)):
        #pos = mean + offset
    #else:
        #pos = mean - offset

    if (arc <= 180):
        pos = mean - offset
    else:
        pos = mean + offset

    return pos

def truemoon(jday):
    '''Calculated true position of the moon, as per Surya Siddhanta chapter 2'''
    jday = Fraction(jday)

    arc = Fraction((jday - creation), anom_month) % 1 # how far is the moon past the apogee?
    ext = 32 * 60 # maximum circumference of the epicycle, in MINUTES! Suryda Siddhanta 2:35

    ans = tpos(jday, sid_month, anom_month, ext)
    return ans

def phase(jday):
    '''Calculate the angle, in DEGREES, between the sun and the moon; this gives the phase of the moon.'''
    # 0º == new moon
    # 180º == full moon
    jday = Fraction(jday)

    sun = truesun(jday)
    moon = truemoon(jday)

    angle = moon - sun
    while angle < 0:
        angle += 360
    angle %= 360
    return angle

def rpos(jday, sid, anom, ext):
    '''True position of a celestial body, based on Surya Siddhanta chapter 2, based solely on Fourier functions of anomalistic cycles'''
    jday = Fraction(jday) # Julian Day
    sid = Fraction(sid) # Sidereal revolution; time it takes the body to traverse the zodiac
    anom = Fraction(anom) # Anomalistic revolution; time it takes the body to move from apogee to apogee.
    ext = Fraction(ext) # Maximum "diameter" of the epicycle, measured in MINUTES of the deferent.

    mean = mpos(jday, sid) # mean position; location of the centre of the epicycle upon the deferent
    frac = Fraction(((jday - creation) % anom), anom) # fraction of the anomalistic revolution the body has undergone
    anom_angle = frac * 360 # anomalistic longitude, in DEGREES

    # now to calculate the amount the epicycle shrinks. See Surya Siddhanta 2:34
    # this gives an answer in MINUTES
    if anom_angle <= 90:
        shrinkage = 20 * Fraction(anom_angle, 90)
    elif anom_angle <= 180:
        shrinkage = 20 * Fraction((180 - anom_angle), 90)
    elif anom_angle <= 270:
        shrinkage = 20 * Fraction((anom_angle - 180), 90)
    else:
        shrinkage = 20 * Fraction((360 - anom_angle), 90)

    sphuta = ext - shrinkage # true "diameter" of the epicycle, measured in MINUTES of deferent
    offset = ayj(Fraction(sphuta, 21600) * jya(60 * anom_angle)) # difference between the mean and true positions of the body
    offset = Fraction(offset, 60) # divide by 60 to convert from minutes to degrees
    if (anom_angle) < 180:
        ans = mean - offset
    else:
        ans = mean + offset

    while (ans < 0):
        ans += 360

    ans = ans % 360

    return ans

def getyog(jday):
    '''Get the yog for a given time, as per Surya Siddhanta 2:64-65'''
    jday = Fraction(jday)

    total = (truesun(jday) + truemoon(jday))
    total = (total * 60) % 21600 # multiply by 60 to convert to minutes
    yog = YOGS[total // 800]
    return yog

def anglen(angle):
    '''Obtain "the part which determines the jya", as Burgess puts it; see Surya Siddhanta 2:29-30 and 3:9-12.'''
    angle = Fraction(angle) # this is in DEGREES
    if angle <= 90:
        ans = angle
    elif angle <= 180:
        ans = 180 - angle
    elif angle <= 270:
        ans = angle - 180
    else:
        ans = 360 - angle

    return ans
    
def libration(jday):
    '''Calculate the libration of the equinoxes as of jday, as per Surya Siddhanta 3:9-12'''
    jday = Fraction(jday)

    arcfrac = Fraction((jday - ky), (7200 * sid_year))
    bhuja = arcfrac * 360 # tropical longitude, in DEGREES. See Burgess p. 116
    while (bhuja < 0):
        bhuja += 360
    
    libr = anglen(bhuja) * Fraction(3,10) # extent of precession, in DEGREES
    if bhuja >= 180:
        libr = 0 - libr

    return libr

def precession(jday):
    '''Calculate the precession of the equinoxes, based on values described in Surya Siddhanta 3:9-12'''
    jday = Fraction(jday)

    arc = (jday - creation) % trop_year
    while arc < 0:
        arc += 360

    frac = Fraction(arc, trop_year)
    ecl = frac * 360 # sun's ecliptic longitude, in DEGREES. Note that this has nothing at all to do with the zodiacal longitude, and the two cannot be interconverted.
    # 0 == 360: northward equinox
    # 90: northern solstice
    # 180: southward equinox
    # 270: southern solstice
    return arc

def mel(jday):
    '''mean ecliptic longitude'''
    jday = Fraction(jday)

    ans = meansun(jday) + libration(jday)
    while ans < 0:
        ans += 360
    ans %= 360
    return ans

def tel(jday):
    '''true ecliptic longitude'''
    jday = Fraction(jday)
    ans = truesun(jday) + libration(jday)
    while ans < 0:
        ans += 360
    ans %= 360
    return ans

def declination(jday):
    '''Compute sun's declination, as per Surya Siddhanta 3:18-19'''
    jday = Fraction(jday)

    ecl = tel(jday) # ecliptic longitude
    if ecl > 270:
        ecl = 360 - ecl
    elif ecl > 180:
        ecl = ecl - 180
    elif ecl > 90:
        ecl = 180 - ecl
    else:
        ecl = ecl
    arg = Fraction(jya(60 * ecl), 3438) * jya(24 * 60) # multiply the argument to jya by 60 to convert to minutes
    dec = ayj(arg) * Fraction(1,60) # divide by 60 to convert minutes to degrees
    return dec

def arhagra(jday, lat):
    '''Compute the sun's measure of amplitude, as per Surya Siddhanta 3:21-23'''
    jday = Fraction(jday)
    lat = Fraction(lat) # latitude of observer

    clat = 90 - lat # co-latitude
    dec = declination(jday) # declination as of jday
    eh = Fraction((3438 * 12), jya(60 * clat)) # equinoctial hypotenuse; Surya Siddhanta 3:
    es = 12 * Fraction(ya(60 * lat), (60 * clat)) # equinoctial shadow; Surya Siddhanta 3:17

    zen = lat - dec # zenith distance
    shadow = 12 * jya(zen) * Fraction(1, kotijya(zen)) # Midday shadow; Surya Siddhanta 3:21-22
    hyp = 12 * 3438 * Fractin(1, kotijya(zen)) # Midday hypotenuse; Surya Siddhanta 3:21-22
    #ampl = jya(60 * dec) * eh * Fraction(1, 12) # solar amplitude; Surya Siddhanta 3:22-23

    ja = 3438 * Fraction(jya(60 * dec), jya(60 * clat)) # jya of solar amplitude; Surya Siddhanta 3:27-28
    ampl = ayj(ja) # solar amplitude in MINUTES
    return(ampl)

def qlon(jday, lat):
    '''Compute the sun's ecliptic longitude within a quadrant of the sky, as per Surya Siddhanta 3:40'''
    jday = Fraction(jday)
    lat = Fraction(lat) # observer's latitude

    dec = declination(jday)
    maxdec = 23 + Fraction(1,2) # maximun declination == 23.5°
    qecl = 3438 * jya(dec) * Fraction(1, jya(maxdec)) # location within a quadrant
    return qecl

# These next functions are to calculate the times of sunrise and sunset.
# I tried to decipher the second half of Surya Siddhanta chapter 3, but in
# the end, I just couldn't figure out what it was on about and gave up.
# My own algorithm just uses jya and kotijya, so hopefully
# it will give the same answers as the traditional algorithms.

def nightside(jday, lat):
    '''Compute the fraction of the latitudinal circle in which it is night.'''
    # this algorithm assumes that Earth's radius is 3438 units.
    jday = Fraction(jday)
    lat = Fraction(lat) # observer's latitude

    dec = declination(jday) # declination
    # since dec and lat are in degrees, they need to be multiplied by 60 to get the correct values for jya and kotijya
    ans = Fraction((jya(60 * lat) * jya(60 * dec)), (kotijya(60 * lat) * kotijya(60 * dec)))
    ans = ans * Fraction(1,2)
    ans = Fraction(1,2) - ans
    ans = ans * Fraction(1,2)
    return ans

def sunrise(jday, lat):
    '''Compute time of sunrise'''
    jday = Fraction(jday)
    lat = Fraction(lat) # observer's latitude

    ecl = tel(jday) # ecliptic longitude
    frac = nightside(jday, lat)

    if (ecl < 180): # between northward and southward equinoxes; in India, this is the bright half of the year
        ans = floor(jday) + frac
    else: # between southward and northward equinoxes; in India, this is the dark half of the year
        ans = floor(jday) + Fraction(1,2) - frac
    return ans

def sunset(jday, lat):
    '''Compute time of sunset'''
    jday = Fraction(jday)
    lat = Fraction(lat)

    ecl = tel(jday)
    frac = nightside(jday, lat)

    if (ecl < 180): # between the northward and souththward equinoxes; in India, this is the bright half of the year
        ans = ceil(jday) - frac
    else:
        ans = ceil(jday) - Fraction(1,2) + frac

    return ans

def ztime(jday, angle):
    '''Zero in on the time the sun hits a specific zodiacal angle, using the standard algorithms.'''
    jday = Fraction(jday) # instant we're starting at
    angle = Fraction(angle) % 360 # angle we're looking for

    while angle < 0:
        angle += 360

    p = 0
    while p < 3:
        if (truesun(jday) == angle):
            p = 3
        else:
            f = Fraction(1, 60 ** p)
            if (angle <= 90):
                while (truesun(jday) >= 270):
                    jday += f
            elif (angle >= 270):
                while (truesun(jday) <= 90):
                    jday -= f
            while ((truesun(jday) > angle) and (truesun(jday - f) < truesun(jday))):
                jday -= f
            while ((truesun(jday) < angle) and (truesun(jday + f) > truesun(jday))):
                jday += f
        p += 1
    return jday        

def ntime(jday, angle):
    '''Zero in on the time the sun hits a specific zodiacal angle, using the naïve algorithms.'''
    jday = Fraction(jday) # instant we're starting at
    angle = Fraction(angle) % 360 # angle we're looking for

    while angle < 0:
        angle += 360

    p = 0
    while p < 3:
        if (naive_sun(jday) == angle):
            p = 3
        else:
            f = Fraction(1, (60 ** p))
            if (angle <= 90):
                while (naive_sun(jday) >= 270):
                    jday += f
            elif (angle >= 270):
                while (naive_sun(jday) <= 90):
                    jday -= f
            while ((naive_sun(jday) > angle) and (naive_sun(jday - f) < naive_sun(jday))):
                jday -= f
            while ((naive_sun(jday) < angle) and (naive_sun(jday + f) > naive_sun(jday))):
                jday += f

        p += 1
    return jday
