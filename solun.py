#!/usr/bin/python3

# algorithms to determine the exact ecliptic longitude of the sun and the moon

from fractions import Fraction
from decimal import Decimal
from math import floor, ceil, cos, acos, pi, sin, asin, tan, atan
import sunmoon
import numpy as np
import gregorian
from tdiff import DIFF
import stars
from surya_siddhanta import uj_lon, uj_lat

tropical_year = 365 + Fraction(5,24) + Fraction(48,1440) + Fraction(45,86400)
syn_month = 29 + Fraction(12,24) + Fraction(44,1440) + Fraction(28,864000)
lunar_month = syn_month # just here for compatibility, will be removed eventually
sid_month = 27 + Fraction(7,24) + Fraction(43,1440) + Fraction(12,86400)
solar_term = tropical_year / 12 # time between major solar terms
sid_year = 365 + Fraction(6, 24) + Fraction(9, 1440) + Fraction(954, 8640000)
rasi = sid_year / 12 # time for the sun to transit one zodiac sign
year12 = 12 * lunar_month
year13 = 13 * lunar_month
r2d = 180 / pi # convert radians to degrees
d2r = pi / 180 # convert degrees to radians
eqm = 0.6749121716696571 # Difference between the celestial longitudes of the sun and counterspica when the sun hit an ecliptic angle of 23°15' in 1955. This is used in computing the instant of Meṣa Saṁkrānti

julian_epoch = 1721424 - 366 # 1st January of the year 0
gregorian_epoch = 1721426 - 366 # 1st January of the year 0
gregorian_cycle = (400 * 365) + 97 # 400 years in the Gregorian calendar
solar4 = (4 * 365) + 1 # 3 years of 365 days and one leap year of 366 days
solar5 = (5 * 365) + 1 # 4 years of 365 days and one leap year of 366 days

ky = 588466 # Consecutive Julian Day on which the Kali Yuga begins.
se = ky + (3179 * sid_year) # Beginning of the Śaka Era
vs = ky + (3044 * sid_year) # Beginning of the Vikram Samvat

def dsin(angle):
    '''sine of an angle in degrees'''
    angle = float(angle)
    ans = sin(angle * d2r)
    return ans

def dcos(angle):
    '''cosine of an angle in degrees'''
    angle = float(angle)
    ans = cos(angle * d2r)
    return ans

def dtan(angle):
    angle = float(angle)
    ans = tan(angle * d2r)
    return ans

def udt(jday):
    '''Get the difference between Universal Time and Dynamical Time for a given Julian Day'''
    jday = floor(jday)

    gdate = gregorian.fromjd(jday)
    year = gdate[2]
    #print(year)

    if year in DIFF.keys():
        deltat = DIFF[year]
    elif year in range(1621,2000):
        deltat = Decimal('0.5') * (DIFF[year - 1] + DIFF[year + 1])
    else:
        # approximate value
        t = Decimal(year - 2000) / 100
        if year < 948:
            deltat = 2177 + (497 * t) + (t * t * Decimal('77.1'))
        #elif (year <= 1600) or (year > 2000):
        else:
            deltat = 102 + (102 * t) + (t * t * Decimal('25.3'))
            if year <= 2100:
                deltat = deltat + (Decimal('0.37') * (year - 2100))

    return deltat

def spos(day):
    '''Ecliptic longitude of the sun'''
    day = floor(day) - 0.5
    return sunmoon.pub.pub_solar_longitude(day)

def mpos(day):
    '''Ecliptic longitude of the moon'''
    day = floor(day) - 0.5
    return sunmoon.pub.pub_lunar_longitude(day)

def trans(day, angle, frtz):
    '''Time the sun hits a particular ecliptic longitude'''
    day = floor(day) - 0.5
    angle = float(angle)
    frtz = Fraction(frtz) # timezone
    
    minutes = int(sunmoon.pub.pub_solar_time(day, angle))
    time = ceil(day) + Fraction(minutes, 1440) + frtz
    return time

def newmoon2(day, tz):
    '''Julian Day and time of the new moon, in local time'''
    # this function is deprecated. Use newmoon(), further down, instead
    day = floor(day) - 0.5
    tz = Fraction(tz) # timezone

    minutes = int(sunmoon.pub.pub_lunar_time(day))
    time = ceil(day) + Fraction(minutes, 1440) + tz
    return time

def first_visible_crescent(jday, tz):
    '''Approximate Julian Day and time of the first visible crescent, in local time'''
    jday = Fraction(jday)
    tz = Fraction(tz)

    ans = newmoon2(jday, tz) + 1
    return ans

def conj(day, frtz):
    '''This function is deprecated. Use newmoon() instead'''
    day = floor(day) - 0.5
    frtz = Fraction(frtz)
    ans = newmoon(day, frtz)
    return ans

def phase2(jday, tz):
    '''Angle between the sun and the moon at a given time'''
    # this function is deprecated. Use phase(), further down
    # 0° → new moon
    # 180° → full moon
    jday = Fraction(jday) # the instant we are interested in
    tz = Fraction(tz) # time zone we are considering
    ans = (mpos(jday) - spos(jday)) % 360
    return ans

def antiphase(jday, tz):
    '''Angle between the sun and the moon, with the full moon taken as 0'''
    # 0° → full moon
    # 180° → new moon
    jday = Fraction(jday) # the instant we are interested in
    tz = Fraction(tz) # timezone under consideration
    ans = (phase(jday, tz) + 180) % 360
    return ans

def fullmoon(jday, tz):
    '''Zero in on the time of full moon'''
    jday = Fraction(jday) # instant we're interested in
    tz = Fraction(tz) # timezone

    ans = jday
    p = 0
    while (p < 4):
        f = Fraction(1, (60 ** p))
        while (phase((ans + f), tz) <= 180):
            ans += f
        while (phase((ans - f), tz) >= 180):
            ans -= f
        p += 1
    return ans

def phasetime(jday, angle, tz):
    '''Time the angle between the sun and the moon hits a specified value'''

    jday = Fraction(jday) # Julian Day we are starting with
    angle = Fraction(angle) # desired angle between the sun and the moon
    tz = Fraction(tz)

    p = 0
    '''
    while (p < 4):
        #print(float(jday))
        f = Fraction(1, (60 ** p))
        if (angle <= 90):
            while (phase((jday + f), tz) >= 270):
                jday += f
        elif (angle >= 270):
            while (phase((jday - f), tz) <= 90):
                jday -= f
        while (phase((jday + f), tz) <= angle):
            jday += f
        while (phase((jday - f), tz) >= angle):
            jday -= f
        p += 1
    '''
    delta = (phase(jday, tz) - angle) % 360
    if (delta <= 180):
        jday -= (syn_month * (delta / 360))
    else:
        jday += (syn_month * ((360 - delta) / 360))

    while (p < 4):
        f = 1 / (60 ** p)
        while ((phase((jday - f), tz) - angle) % 360 <= 90):
            jday -= f
        while ((phase((jday + f), tz) - angle) % 360 >= 270):
            jday += f
        p += 1
                     
        
    return jday

def antiphasetime(jday, angle, tz):
    '''Time the angle between the sun and the moon hits a given value, where opposition is taken as 0°'''
    jday = Fraction(jday) # Julian Day we are starting with
    angle = Fraction(angle) # desired angle
    tz = Fraction(tz) # timezone

    while ((antiphase(jday, tz) <= 90) and (angle >= 270)):
        jday -= 1
    while ((antiphase(jday, tz) >= 270) and (angle <= 90)):
        jday += 1

    p = 0
    while (p < 4):
        f = Fraction(1, (60 ** p))
        while (antiphase((jday + f), tz) <= angle):
            jday += f
        while (antiphase((jday - f), tz) >= angle):
            jday -= f
        p += 1
    return jday

def truesun(day, angle, timezone):
    day = Fraction(day)
    angle = int(angle)
    timezone = Fraction(timezone)
    return(floor(trans(day, angle, timezone)))

def truemoon(day, timezone):
    day = Fraction(day)
    timezone = Fraction(timezone)
    return(floor(conj(day, timezone)))

def angsep(ra1, dec1, ra2, dec2):
    '''Determine the angular separation between two bodies, given their right ascensions and declinations'''
    # this function assumes input angles are in degrees
    # the answer is given in the zodiacal, not ecliptical, coordinate system
    ra1 = Decimal(ra1) # right ascension of 1st body
    dec1 = Decimal(dec1) # declination of 1st body
    ra2 = Decimal(ra2) # right ascension of 2nd body
    dec2 = Decimal(dec2) # declination of 2nd body

    cra = cos(d2r * (ra2 - ra1))
    cdec = cos(d2r * (dec2 - dec1))
    sigma = r2d * acos(cra + cdes - 1)
    return sigma

def sunrise(jday, lon, lat):
    '''Time of sunrise on a given day for a given longitude and latitude, in UTC'''
    jday = float(jday) - 0.5 # Julian Day in question
    deltat = udt(ceil(jday))
    #print(deltat)
    lon = float(lon) # observer's longitude
    lat = float(lat) # observer's latitude
    ra2000 = 281.29 # https://astronomy.stackexchange.com/questions/35779/ra-and-dec-of-the-sun-at-j2000
    dec2000 = 0 - 23 - (2/60) - (8.2/3600) # https://astronomy.stackexchange.com/questions/35779/ra-and-dec-of-the-sun-at-j2000

    r = sunmoon.pub.pub_solar_riset(jday, lon, lat)
    return(float(r[0]))

def sunset(jday, lon, lat):
    '''Time of sunset on a given day for a given longitude and latitude, in UTC'''
    deltat = udt(int(jday))
    jday = int(jday) - 0.5 # Julian Day in question
    lon = float(lon) # observer's longitude
    lat = float(lat) # observer's latitude
    ra2000 = 281.29 # https://astronomy.stackexchange.com/questions/35779/ra-and-dec-of-the-sun-at-j2000
    dec2000 = 0	- 23 - (2/60) -	(8.2/3600) # https://astronomy.stackexchange.com/questions/35779/ra-and-dec-of-the-sun-at-j2000
    
    s = sunmoon.pub.pub_solar_riset(jday, lon, lat)
    return(s[1])

def local_sunrise(jday, lon, lat, tz):
    '''Time of sunrise at a given location, in local time rather than UTC.'''
    # This function gives the time of sunrise as (cJD + time), rather than just JD
    jday = Fraction(jday) # consecutive Julian Day in question
    #print(float(jday))    
    lon = float(lon) # observer's longitude
    lat = float(lat) # observer's latitude
    tz = Fraction(tz) # local timezone
    ans = floor(jday) + sunrise(jday, lon, lat) - tz
    return ans

def local_sunset(jday, lon, lat, tz):
    '''Time of sunset at a given location, in local time rather than UTC'''
    # This function gives the time of sunset as (cJD + time), rather than just JD
    jday = Fraction(jday) # consecutive Julian Day in question
    lon = float(lon) # observer's longitude
    lat = float(lat) # observer's latitude
    tz = Fraction(tz) # local timezone
    ans = floor(jday) + sunset(jday, lon, lat) - tz
    return ans

def starrise(jday, lon, lat, ra2000, dec2000, distance, rv, deltara, deltadec):
    '''Time of a star rising for a given longitude and latitude'''
    deltat = udt(int(jday))
    jday = int(jday) - 0.5
    lon = float(lon)
    lat = float(lat)
    ra2000 = float(ra2000)
    dec2000 = float(dec2000)
    distance = float(distance)
    rv = float(rv)
    deltara = float(deltara)
    deltadec = float(deltadec)

    s = sunmoon.pub.pub_stellar_riset(jday, lon, lat, deltat, ra2000, dec2000, distance, rv, deltara, deltadec)
    return(s[0])

def starrise2(jday, lon, lat, star):
    '''Time of a star rising for a given longitude and latitude.'''
    deltat = udt(int(jday))
    jday = int(jday) - 0.5
    lon = float(lon)
    lat = float(lat)

    s = sunmoon.pub.pub_stellar_riset(jday, lon, lat, deltat, star.ra, star.dec, star.distance, star.rv, star.dra, star.ddec)
    return(s[0])

def local_starrise(jday, lon, lat, star, tz):
    '''Time of a star rising at a given longitude and latitude, in local time'''
    jday = Fraction(jday)
    lon = float(lon)
    lat = float(lat)
    tz = Fraction(tz)

    ans = floor(jday) + starrise2(jday, lon, lat, star) - tz
    return ans

def starpos(jday, star):
    '''Determine the right ascension and declination of a given star as of jday. See Meeus, chapter 23'''
    jday = Fraction(jday) - Fraction(12,24) # convert from midnight-to-midnight to noon-to-noon denotation

    # first, the effect of proper motion
    radec = sunmoon.pub.pub_propmot(jday, star.ra, star.dec, star.distance, star.rv, star.dra, star.ddec)
    ra = radec[0]
    dec = radec[1]

    # next, apply the effect of nutation
    nut = sunmoon.pub.pub_nutation(jday)
    epsilon = nut[0]
    delta_psi = nut[1]
    delta_epsilon = nut[2]
    delta_ra1 = ((dcos(epsilon) + (dsin(epsilon) * dsin(ra) * dtan(dec))) * delta_psi) - ((dcos(ra) * dtan(dec)) * delta_epsilon)
    delta_dec1 = (dsin(epsilon) * dcos(ra) * delta_psi) + (dsin(ra) * delta_epsilon)

    # next, the effect of aberration
    T = (jday - 2451545 + Fraction(12,24)) / 36525 # Julian Centuries since J2000.0
    ecc = 0.016708634 - (0.000042037 * T) - (0.0000001267 * T * T) # eccentricity of Earth's orbit
    per = 102.93735 + (1.71946 * T) + (0.00046 * T * T) # longitude of perihelion, in DEGREES
    kappa = 20.49552 / 3600 # constant of aberration, in DEGREES

    solar_radec = sunmoon.pub.pub_solar_radec(jday)
    solar_ra = solar_radec[0]
    solar_dec = solar_radec[1]

    delta_ra2a = (0 - kappa) * (((dcos(ra) * dcos(solar_ra) * dcos(epsilon)) + (dsin(ra) * dsin(epsilon))) / dcos(dec))
    delta_ra2b = (ecc * kappa) * (((dcos(ra) * dcos(per) * dcos(epsilon)) + (dsin(ra) * dsin(per))) / dcos(dec))
    delta_ra2 = delta_ra2a + delta_ra2b

    delta_dec2a = (dcos(solar_ra) * dcos(epsilon) * ((dtan(epsilon) * dcos(dec)) - (dsin(ra) * dsin(dec)))) + (dcos(ra) * dsin(dec) * dsin(solar_ra))
    delta_dec2b = ((((dtan(epsilon) * dtan(dec)) - (dsin(ra) + dsin(dec)))) * dcos(per) * dcos(epsilon)) + (dcos(ra) * dsin(dec) * dsin(per))
    delta_dec2 = ((0 - kappa) * delta_dec2a) + (ecc * kappa * delta_dec2b)

    delta_ra = (delta_ra1 + delta_ra2) / 3600 # divide by 3600 to convert from seconds to degrees
    delta_dec = (delta_dec1 + delta_dec2) / 3600 # divide by 3600 to convert from seconds to degrees

    ra += delta_ra
    dec += delta_dec
    
    return(ra, dec)

def counterstar(jday, star):
    '''Calculate the point exactly opposite a given star, in the celestial coördinate system'''
    jday = Fraction(jday)
    coords = starpos(jday, star)
    counter_ra = (coords[0] + 180) % 360
    counter_dec = 0 - coords[1]
    return(counter_ra, counter_dec)

def solar_cel_coords(jday):
    '''Get the right ascension and declination of the sun'''
    radec = sunmoon.pub.pub_solar_radec(float(jday - 0.5)) # subtract 0.5 to convert from local Julian Day to true Julian Day
    # yes this step is necessary due to how numpy arrays and tuples express themselves differently as strings
    # explanation from someone who knows what they're talking about: https://techhub.social/@diazona/113653958945875533
    # if you think it is unnecessary, try taking out the next non-comment line
    # and replacing the return statement with "return radec"
    # then pass the value 2460576 to this function
    # radec will have the value (179.9776911256796, 0.00967182122046539)
    # but the function will return (1.79977691e+02, 9.67182122e-03)
    ans = (radec[0], radec[1])
    return ans

def solar_ra(jday, tz):
    '''Return the right ascension of the sun'''
    return solar_cel_coords(float(jday - tz))[0]

def solar_dec(jday):
    '''Return the declination of the sun, if you want that for some reason'''
    return solar_cel_coords(float(jday - tz))[1]

def solar_zpos(jday, star, opp):
    '''Compute the sun's zodiacal position'''
    jday = Fraction(jday) # time under consideration
    opp = bool(opp) # False means the zodiac starts at a given star, True means it starts opposite that star
    
    solar_radec = solar_cel_coords(jday)
    solar_ra = solar_radec[0]
    if (opp == False):
        # zodiac starts at the star
        zero = starpos(jday, star)
    else:
        # zodiac starts opposite the star
        zero = counterstar(jday, star)
        
    stellar_ra = zero[0]
    sep = solar_ra - stellar_ra # angular separation of the sun from the star
    while (sep < 0):
        sep += 360

    return sep

def get_solar_zpos(jday, star, opp, angle):
    '''Zero in on the time the sun hits a given zodiacal angle'''
    jday = Fraction(jday)
    opp = bool(opp) # False means the zodiac starts at a given star, True means it starts opposite that star
    angle = float(angle)

    p = 0

    while (p < 4):
        if (solar_zpos(jday, star, angle) == angle):
            p = 4
        else:
            f = Fraction(1, (60 ** p))
            while ((solar_zpos(jday, star, opp) <= 90) and (angle >= 270)):
                jday -= f
            while ((solar_zpos(jday, star, opp) >= 270) and (angle <= 90)):
                jday += f
            while (solar_zpos(jday, star, opp) + f <= angle):
                jday += Fraction(1, (60 ** p))
            while (solar_zpos(jday, star, opp) - f >= angle):
                jday -= f
            p += 1

    return jday

def indian_spos(jday):
    '''Compute the zodiacal position of the sun for modern Indian calendars'''
    jday = Fraction(jday) - Fraction(11,48) # convert IST to UTC
    ans = (solar_zpos(jday, stars.SPICA, True) - eqm) % 360
    return ans

def sankranti(jday, angle):
    '''Zero in on the time the sun hits a given zodiacal longitude as used in modern Indian calendars'''
    jday = Fraction(jday)
    angle = float(angle)

    ans = get_solar_zpos(jday, stars.SPICA, True, ((angle + eqm) % 360)) # time in UTC
    ans += Fraction(11,48) # convert from UTC to IST
    return ans

def indian_sunrise(jday):
    '''Compute the time of sunrise for a given day in Ujjain'''
    jday = Fraction(jday)

    ans = local_sunrise(jday, uj_lon, uj_lat, Fraction(11,48))
    return ans

def indian_sunset(jday):
    '''Compute the time of sunset for a given day in Ujjain'''
    jday = Fraction(jday)

    ans = local_sunset(jday, uj_lon, uj_lat, Fraction(11,48))
    return ans

def tropical_sankranti(jday, angle, tz):
    '''Compute the time the sun hits a given ecliptic longitude, where 0° is defined as 23°15' past the northward equinox'''
    jday = Fraction(jday)
    angle = (Fraction(angle) + (23 + Fraction(15,60))) % 360 # convert from given angle to equinox-anchored angle
    ans = trans(jday, angle, tz)
    return ans

def saurya(jday, tz):
    '''Compute the ecliptic longitude of the sun at a given time, where 0° is defined as 23°15' past the northward equinox'''
    jday = Fraction(jday)
    ans = spos(jday - tz)
    return ans

def dayof_hindi(jday):
    '''Compute the day associated with an astronomical event, where days begin at sunrise'''
    # The first day of a solar month is the day beginning with the first sunrise after the sun enters the star sign in question.
    # The first day of a synodic month is normally the day beginning with the first sunrise after the instant of the new moon.
    # In some calendars, the first day of a synodic month is the day beginning with the first sunrise after the full moon
    jday = Fraction(jday)

    ans = round(jday)
    while (indian_sunrise(ans) < jday):
        ans += 1
    while (indian_sunrise(ans - 1) >= jday):
        ans -= 1

    return ans

def dayof_kerala(jday):
    '''Compute the Julian Day associated with an astronomical event, as per the Malayali (Kerala) rule'''
    # First, calculate the aparahna; this is the moment ⅗ between sunrise and sunset
    # If the instant in question falls after aparahna, it is associated with the following day
    # Otherwise, it is associated with the current day
    # Source: http://packolkata.gov.in/INDIAN_CALADAR_PAC.pdf
    jday = Fraction(jday)

    aparahna = indian_sunrise(jday) + ((indian_sunset(jday) - indian_sunrise(jday)) * Fraction(3,5))
    if (jday > aparahna):
        ans = ceil(jday)
    else:
        ans = floor(jday)

    return ans

def dayof_tamil(jday):
    '''Compute the day associated with an astronomical event, as per the Tamil rule'''
    # In the Tamil calendar, days begin at sunrise.
    # However, an astronomical even belongs to the tropical day in which it falls unless it falls after sunset, in which case it is assigned to the following day.
    # So, for example, if the sun enters Tulā at noon, then that day is the first day is the first day of Aipassi even though it is after sunrise.
    jday = Fraction(jday)

    if (jday >= indian_sunset(jday)):
        ans = ceil(jday)
    else:
        ans = floor(jday)

    return ans

def dayof_arab(jday, lon, lat, tz):
    '''Compute the day associated with an astronomical event, as per the Arab rule'''
    # The Arab rule is that days begin at sunset
    jday = Fraction(jday) # instant of the event in question
    lon = Fraction(lon) # local longitude
    lat = Fraction(lat) # local latitude
    tz = Fraction(tz) # timezone

    if (jday <= local_sunrise(jday, lon, lat, tz)):
        ans = floor(jday)
    else:
        ans = ceil(jday)

    return ans

def dayof_kazakh(jday, lon, lat, tz):
    '''Compute the day associated with an astronomical event, as per the Kazakh rule'''
    # Days begin at sunset
    # but if an event happens while it can't be seen, it is still associated with the day beginning last sunset
    jday = Fraction(jday) # instant of the event in question
    lon = Fraction(lon) # local geographic longitude
    lat = Fraction(lat) # local geographic latitude
    tz = Fraction(tz) # local timezone

    if (jday >= local_sunset(jday, lon, lat, tz)):
        ans = ceil(jday)
    else:
        ans = floor(jday)

    return ans

def heliacal_rising(jday, lon, lat, star, tz):
    '''Compute the nearest day of the heliacal rising of a given star at a given place.'''
    jday = Fraction(jday) # the time we start with
    lon = Fraction(lon) # geographical longitude; East of Greenwich is positive, West is negative
    lat = Fraction(lat) # geographical latitude
    tz = Fraction(tz) # local timezone
    # star is an object of Star class as defined in stars.py
    
    # first, roughly zero in on the day when the sun and the star are in alignment
    #jday = jday + (((solar_cel_coords(jday)[0] - starpos(jday, star)[0]) / 360) * sid_year)
    #if (((solar_cel_coords(jday)[0] - starpos(jday, star)[0]) % 360) > ((starpos(jday, star)[0] - solar_cel_coords(jday)[0]) % 360)):
    s = (solar_cel_coords(jday)[0] - starpos(jday, star)[0]) % 360
    #t = solar_cel_coords(jday)[0] - starpos(jday, star)[0]
    #print(starpos(jday, star)[0])
    if ( s >= 180 ):
        # sun is behind star, so step forward
        #print("Sweet")
        jday = jday + (sid_year * (s / 360))
    else:
        # sun is opposite or ahead of star, so step backward
        #print("Dude")
        jday = jday - (sid_year * (s / 360))

    # we're at the point where the sun and the star are approximately in conjunction
    # now, zero in on a more exact time
    # assume that the heliacal rising is the day when the star rises about 30 minutes before the sun
    ans = round(jday) # we are, ultimately, looking for an integer consecutive Julian Day.

    while (local_sunrise(ans, lon, lat, tz) - local_starrise(ans, lon, lat, star, tz) < Fraction(30, 1440)):
        ans += 1
    while (local_sunrise(ans, lon, lat, tz) - local_starrise(ans, lon, lat, star, tz) > Fraction(30, 1440)):
        ans -= 1

    return ans

def acronycal_rising(jday, lon, lat, star, tz):
    '''Compute the nearest day of the acronycal rising of a given star at a given place, assuming the day begins at sunset.'''
    jday = Fraction(jday) # the time we start with
    lon = Fraction(lon) # geographical longitude; east of Greenwich is postive, west is negative
    lat = Fraction(lat) # geographical latitude
    tz = Fraction(tz)
    # star is an object of Star class as defined in stars.py

    # first, roughly zero in on the day when the sun and the star are in opposition
    theta = (solar_cel_coords(jday)[0] - starpos(jday, star)[0]) % 360
    if (theta < 180):
        jday += (180 - theta)
    else:
        jday -= (theta - 180)

    # we're at the point where the sun and the star are approximately in opposition
    # now, zero in on a more exacttime
    # assume the the achronycal rising is the day beginning with the sunset about 30 minutes after starrise
    ans = local_sunset(jday, lon, lat, tz)

    while (local_starrise(ans, lon, lat, star, tz) - local_sunset(ans, lon, lat, tz) < Fraction(30, 1440)):
    #while (starrise2(ans, lon, lat, star) - sunset(ans, lon, lat) < Fraction(30, 1440)):
        ans -= 1
    while (local_starrise((ans - 1), lon, lat, star, tz) - local_sunset((ans - 1), lon, lat, tz) >= Fraction(30, 1440)):
    #while (starrise2((ans - 1), lon, lat, star) - sunset((ans - 1), lon, lat) >= Fraction(30, 1440)):
        ans += 1

    return ceil(ans)

def lunar_cel_coords(jday):
    '''Compute the right ascension and declination of the moon as of jday'''
    jday = Fraction(jday) - 0.5 # subtract 0.5 because true Julian Days start at noon

    radec = sunmoon.pub.lunar_celestial_coords(jday)
    ans = (radec[0], radec[1])
    return ans

def lunar_ra(jday, tz):
    '''Return the right ascension of the moon as of jday'''
    jday = Fraction(jday) # local Julian Day
    tz = Fraction(tz) # local timezone
    return float(lunar_cel_coords(jday - tz)[0])

def lunar_dec(jday, tz):
    '''Return the declination of the moon as of jday, if you want that for some reason'''
    jday = Fraction(jday) # local Julian Day
    tz = Fraction(tz) # local timezone
    return float(lunar_cel_coords(jday - tz)[1])

def lunar_solar_angle(jday, tz):
    '''Compute the angle between the sun and the moon'''
    # 0° → new moon
    # 180° → full moon
    jday = Fraction(jday) # local time we are interested in
    tz = Fraction(tz) # local timezone
    return ( float((lunar_ra(jday, tz) - solar_ra(jday, tz)) % 360))

def phase(jday, tz):
    # this is just for compatibility at this point
    return lunar_solar_angle(jday, tz)

def newmoon(jday, tz):
    '''Compute the time of the new moon closest to jday'''
    jday = Fraction(jday) # local time we are starting with
    tz = Fraction(tz) # local timezone

    angle = lunar_solar_angle(jday, tz)

    # first, get the sun and the moon into approximate conjunction
    if (angle <= 180):
        jday -= (syn_month * (angle / 360))
    else:
        jday += (syn_month * ((360 - angle) / 360))

    p = 0
    while (p < 5):
        f = 1 / (60 ** p)
        while (lunar_solar_angle((jday + f), tz) > 270):
            jday += f
        while (lunar_solar_angle((jday - f), tz) < 90):
            jday -= f
        p += 1
    return float(jday)

def lunar_stellar_angle(jday, star):
    '''Compute the difference between the right ascensions of the moon and a given star as of jday, UTC'''
    jday = Fraction(jday)

    lunar_radec = lunar_cel_coords(jday)
    stellar_radec = starpos(jday, star)
    ans = (lunar_radec[0] - stellar_radec[0]) % 360
    return ans
    
def lunar_stellar_conjunction(jday, star):
    '''Compute when the moon is in conjunction with a given star, UTC'''
    jday = Fraction(jday) # Julian Day to star looking from

    # get the time when the moon and the star are approximately in conjunction
    if (lunar_stellar_angle(jday, star) <= 180):
        jday -= (sid_month * (lunar_stellar_angle(jday, star) / 360))
    else:
        jday += (sid_month * ((360 - lunar_stellar_angle(jday, star)) / 360))

    # get them into the same quadrant
    while (lunar_stellar_angle(jday, star) >= 270):
        jday += 1

    # zero in on the exact time
    p = 0
    while (p < 5):
        f = Fraction(1, (60 ** p))
        while ( lunar_stellar_angle(jday, star) > lunar_stellar_angle((jday - f), star) ):
            jday -= f
        while ( lunar_stellar_angle(jday, star) > lunar_stellar_angle((jday + f), star) ):
            jday += f
        p += 1

    return jday

def local_lunar_stellar_conjunction(jday, star, tz):
    '''Compute when the moon is in conjunction with a given star, in local time'''
    jday = Fraction(jday) # Julian Day in question
    tz = Fraction(tz) # timezone

    ans = lunar_stellar_conjunction(jday, star) + tz
    return ans

def julian_year_length(year):
    '''Returns the number of days in a year in the Julian calendar, assuming there is a year 0'''

    if (int(year) % 4 == 0):
        ans = 366
    else:
        ans = 365

    return ans

def julian_nyd(year, z):
    '''Returns the Julian Day corresponding to 1st January in a given year in the Julian calendar'''
    year = int(year) # the year in question
    z = bool(z) # is there a year 0?

    if (year < 0):
        year += int(not(z))

    cycles = year // 4
    y = 4 * cycles
    ans = julian_epoch + (cycles * solar4)
    while (y < year):
        ans += julian_year_length(y)
        y += 1

    return ans

def gregorian_year_length(year):
    '''Returns the number of days in a Gregorian year'''
    year = int(year)

    if (year % 400 == 0):
        ans = 366
    elif (year % 100 == 0):
        ans = 365
    elif (year % 4 == 0):
        ans = 366
    else:
        ans = 365

    return ans

def gregorian_nyd(year, z):
    '''Compute New Year's Day for a given year in the Gregorian calendar'''
    year = int(year) # the year in question
    z = bool(z) # is there a year 0?
    if (year < 1):
        year += int(not(z))

    cycles = year // 400
    y = 400 * cycles
    nyd = gregorian_epoch + (cycles * gregorian_cycle) # new year's day

    if (y + 100 <= year):
        y += 100
        nyd += 36525
        while (y + 100 <= year):
            y += 100
            nyd += 36524
        if (y + 4 <= year):
            y += 4
            nyd += (4 * 365)

    quads = (year - y) // 4
    y += (4 * quads)
    nyd += (solar4 * quads)
    while (y < year):
        nyd += gregorian_year_length(y)
        y += 1

    return nyd

def lunar_visibility(jday, tz):
    '''Return the fraction of the near side of the moon which is illuminated at a given time'''
    jday = float(jday) - 0.5 - float(tz) # True Julian Day in question
    ans = sunmoon.pub.pub_lunar_visibility(jday)
    return ans
