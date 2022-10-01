#!/usr/bin/python

# Various functions used in modern Hindu calendars.

from decimal import Decimal
from fractions import Fraction
from math import sin, floor, ceil
from numpy import sign

from solun import imod

ky = 588466 # Beginning of the Kali Yuga in Julian Days; note that the epoch actually happens at sunrise, but I haven't figured out how to calculate that just yet
sid_year = 365 + Fraction(279547, 1080000) # sidereal year
sid_month = 27 + Fraction(4644439, 14438334) # sidereal month
syn_month = 29 + Fraction(7087771, 13358334) # synodic month

creation = ky - (1955880000 * sid_year)
anom_year = Fraction(1577917828000, (4320000000 - 387)) # anomalistic year
anom_month = Fraction(1577917828, (57753336 - 488199)) # anomalistic month

uj_lon = 75 + Fraction(46, 60) + Fraction(6, 3600) # longitude of Ujjain, in DEGREES
uj_lat = 23 + Fraction(9, 60) # latitude of Ujjain, in DEGREES

# Hindu sines, based on Dershowitz and Rheingolds, chapter 20, for use in modern Hindu calendars

TABLE = {0: (0, 0, 0),
         1: (225, 225, Decimal('224.86')),
         2: (450, 449, Decimal('448.75')),
         3: (675, 671, Decimal('670.72')),
         4: (900, 890, Decimal('889.82')),
         5: (1125, 1105, Decimal('1105.11')),
         6: (1350, 1315, Decimal('1315.67')),
         7: (1575, 1520, Decimal('1520.59')),
         8: (1800, 1719, Decimal('1719.00')),
         9: (2025, 1910, Decimal('1910.05')),
         10: (2250, 2093, Decimal('2092.92')),
         11: (2475, 2267, Decimal('2266.83')),
         12: (2700, 2431, Decimal('2431.03')),
         13: (2925, 2585, Decimal('2584.83')),
         14: (3150, 2728, Decimal('2727.55')),
         15: (3375, 2859, Decimal('2858.59')),
         16: (3600, 2978, Decimal('2977.40')),
         17: (3825, 3084, Decimal('3083.45')),
         18: (4050, 3177, Decimal('3176.30')),
         19: (4275, 3256, Decimal('3255.55')),
         20: (4500, 3321, Decimal('3320.85')),
         21: (4725, 3372, Decimal('3371.94')),
         22: (4950, 3409, Decimal('3408.59')),
         23: (5175, 3431, Decimal('3430.64')),
         24: (5400, 3438, Decimal('3438.00'))}

# This is a table of jyas of arcs of n segments, in a circle of radius 3438 units.
# A right angle contains 24 segments.
# The jya is the length of a line drawn from the point where a radius intersects the arc,
# and that line is perpendicular to the radius that intersects the point at the other end of the arc.
# (This makes way more sense visually).
# If an angle S subtends an arc of length s, then jya(s) == r*sin(S)

JYA_SEG = {0: 0,
           1: 225,
           2: 449,
           3: 671,
           4: 890,
           5: 1105,
           6: 1315,
           7: 1520,
           8: 1719,
           9: 1910,
           10: 2093,
           11: 2267,
           12: 2431,
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
           24: 3438}

# This table gives the jyas of an arc subtended by a specific angle for a circle of radius 3438 units
# Angles are measured in ARCMINUTES.

JYA_MIN = {0: 0,
           225: 225,
           450: 449,
           675: 671,
           900: 890,
           1125: 1105,
           1350: 1315,
           1575: 1520,
           1800: 1719,
           2025: 1910,
           2250: 2093,
           2475: 2267,
           2700: 2431,
           2925: 2585,
           3150: 2728,
           3375: 2859,
           3600: 2978,
           3825: 3084,
           4050: 3177,
           4275: 3256,
           4500: 3321,
           4725: 3372,
           4950: 3409,
           5175: 3431,
           5400: 3438}


RISING_SIGNS = {0: Fraction(1670, 1800),
                1: Fraction(1795, 1800),
                2: Fraction(1935, 1800),
                3: Fraction(1935, 1800),
                4: Fraction(1795, 1800),
                5: Fraction(1970, 1800)}

def jya_seg(entry):
    '''jya of an arc of entry segments'''
    entry = int(entry) % 96
    
    if entry > 72:
        entry = 96 - entry
    elif entry > 48:
        entry = entry - 48
    elif entry > 24:
        entry = 48 - entry

    while entry < 0:
        entry += 96

    ans = JYA_SEG[entry]
    return ans

def jya_min(angle):
    '''jya of an arc subtended by angle.'''
    # Not that angle is measured in ARCMINUTES
    angle = int(angle) % 21600

    if angle > 16200: # 270º
        angle = 21600 - angle
    elif angle > 10800: # 180º
        angle = angle - 1800
    elif angle > 5400: # 90º
        angle = 10800 - angle

    ans = JYA_MIN[angle]
    return ans

def sin_seg(entry):
    '''sine of an angle of entry segments, where 1 segment == 3.75º'''
    entry = int(entry)
    ans = Fraction(jya_seg(entry), 3438)
    return ans

def sin_table(entry):
    '''sine of an entry in TABLE'''
    # entry is an integer from 0 to 24. This function gives the entryth sine value in the table.
    entry = int(entry)
    exact = 3438 * sin_seg(entry)
    error = Fraction(215,1000) * sign(exact) * sign(abs(exact) - 1716)
    num = round(exact + error)
    ans = Fraction(num, 3438)
    return ans

def sine(angle):
    '''sine of any number'''
    angle = Fraction(angle) # angle must be in ARCMINUTES! not degrees! not radians! MINUTES!

    entry = Fraction(angle, 225)
    frac = entry % 1

    a = sin_table(ceil(entry)) * frac
    b = sin_table(floor(entry)) * (1 - frac)
    ans = a + b
    return ans

def arcsin(amp):
    '''arcsin of any sine'''
    amp = Fraction(amp)
    if (amp < 0):
        amp = 0 - amp
        neg = True
    else:
        neg = False

    pos = 0
    while sin_table(pos) < abs(amp):
        pos += 1

    if (pos == 0):
        below = sin_table(24)
    else:
        below = sin_table(pos - 1)

    frac = Fraction((abs(amp) - below), (sin_table(pos) - below))
    brac = pos - 1 + frac

    ans = 225 * brac

    if (neg == True):
        ans = 0 - ans

    return ans

def mean_position(time, period):
    '''longitude in DEGREES at a given time since creation, when period is measured in DAYS.'''
    time = Fraction(time)
    period = Fraction(period)

    num = time - creation
    ans = Fraction(num, period) % 1
    ans = ans * 360
    return ans # ans is in DEGREES, so may need to be converted into minutes for use in other functions.

def true_position(time, period, size, anom, change):
    '''adjust the mean longitudinal position by the equation of motion'''
    time = Fraction(time)
    period = Fraction(period)
    size = Fraction(size)
    anom = Fraction(anom)
    change = Fraction(change)

    l = mean_position(time, period)
    offset = sine(60 * mean_position(time, anom)) # multiply by 60 to convert degrees into arcminutes
    contraction = abs(offset) * change * size
    equation = arcsin(offset * (size - contraction)) * Fraction(1,60) # divide by 60 to convert arcminutes to degrees
    ans = l - equation
    if ans < 0:
        ans += 360
    else:
        ans = ans % 360
    return ans # ans is measured in DEGREES, so may need to be converted into minutes for use in other functions

def solar_longitude(time):
    '''zodiacal longitude of the sun'''
    time = Fraction(time)
    ans = true_position(time, sid_year, Fraction(14,360), anom_year, Fraction(1,42))

    return ans

def zodiac(time):
    '''zodiac sign of the sun'''
    ans = floor(Fraction(solar_longitude(time), 30)) # Dershowitz and Rheingold add 1 to this, but I'm just going to count from 0.
    return ans

def lunar_longitude(time):
    time = Fraction(time)
    ans = true_position(time, sid_month, Fraction(32,360), anom_month, Fraction(1,96))
    return ans

def lunar_phase(time):
    time = Fraction(time)

    ans = (lunar_longitude(time) - solar_longitude(time)) % 360
    return ans

def lunar_day_from_moment(time):
    '''determine the tithi by dividing the lunar phase by 12 degrees (1/30 of a synodic month)'''
    time = Fraction(time)
    ans = floor(lunar_phase(time) / 12) + 1
    return ans

def new_moon_before(time):
    time = Fraction(time)
    # actually I don't think I need this one

def tropical_longitude(time):
    time = Fraction(time)

    days = time - creation
    alpha = Fraction(600, 1577917828) * days
    alpha = alpha - Fraction(1, 4)
    alpha = imod(alpha, Fraction(-1, 2), Fraction(1, 2))
    alpha = abs(Fraction(108, 360) - alpha)
    precession = Fraction(27, 360) - alpha

    ans = (solar_longitude(time) - precession) % 360 # this is in DEGREES
    return ans

def daily_motion(time):
    time = Fraction(time)
    
    mmot = Fraction(360, sid_year) # degrees
    anomaly = mean_position(time, anom_year) # degrees
    epicycle = (Fraction(14, 360) - Fraction(1, 1080)) * abs(sine(60 * anomaly)) # multiply the argument to sine by 60 so it will be in ARCMINUTES
    entry = floor(Fraction((anomaly * 60), 225)) # multiplying by 60 so that the numerator will be in ARCMINUTES like the denominator
    table_step = sin_table(entry + 1) - sin_table(entry)
    factor = 0 - (Fraction(3438, 225) * table_step * epicycle)
    ans = mmot * (factor + 1)
    return ans
    
def solar_sid_diff(time):
    time = Fraction(time)

    iota = floor(Fraction(tropical_longitude(time), 30))
    risign = RISING_SIGNS[iota % 6]

    ans = daily_motion(time) * risign
    return ans

def asc_diff(time, lon, lat):
    '''ascensional difference'''
    time = Fraction(time)
    lon = Fraction(lon) # longitude
    lat = Fraction(lat) # latitude

    deltasin = Fraction(1397, 3438) * sine(60 * tropical_longitude(time)) # sine's argument is multiplied by 60 to put it into ARCMINUTES
    drad = sine(5400 + arcsin(deltasin)) # 90º = 5400'
    tan = Fraction(sine(60 * lat), sine(5400 + lat)) # arguments to sine must be in ARCMINUTES
    esin = deltasin * tan
    ans = sine(0 - Fraction(esin, drad))
    return ans

def eqtime(time):
    '''Equation of time'''
    time = Fraction(time)

    alpha = Fraction(daily_motion(time), 360) # degrees

    offset = sine(60 * mean_position(time, anom_year)) # multiple the argument to sine by 60 because it has to be in ARCMINUTES
    eqsun = offset * (Fraction(57, 360) + Fraction(18, 21600)) + (Fraction(14, 360) - Fraction(abs(offset), 1080))
    beta = Fraction(eqsun, 360)

    ans = alpha * beta * sid_year
    return ans    

def sunrise(time, lon, lat):
    '''Sunrise for a given location and day'''

    time = Fraction(time)
    lon = Fraction(lon) # longitude
    lat = Fraction(lat) # latitude

    alpha = Fraction((lon - lat), 360)
    beta = eqtime(time)
    gamma = Fraction(1577917828, (1582237828 * 360))
    delta = asc_diff(time, lon, lat)
    eta = Fraction(1,4) * solar_sid_diff(time)

    omega = gamma * (delta + eta)

    ans = time + Fraction(6,24) + alpha - beta + omega
    return ans

def sunset(time, lon, lat):
    '''Sunrise for a given location and day'''

    time = Fraction(time)
    lon = Fraction(lon)	# longitude    
    lat = Fraction(lat)	# latitude
    
    alpha = Fraction((lon - lat), 360)
    beta = eqtime(time)
    gamma = Fraction(1577917828, (1582237828 * 360))
    delta = asc_diff(time, lon, lat)
    eta = Fraction(3,4) * solar_sid_diff(time)
    
    omega = gamma * (delta + eta)
    
    ans = time + Fraction(18,24) + alpha - beta + omega
    return ans

def sundial(time):
    '''Determine the time from the sundial, used in the Malayali calendar'''
    time = Fraction(time)

    d = floor(time)
    q = floor(4 * (time % 1))

    if (q == 0):
        a = sunset(d - 1)
        b = sunrise(d)
        c = 0 - Fraction(6, 24)
    elif (q == 3):
        a = sunset(d)
        b = sunrise(d + 1)
        c = Fraction(18, 24)
    else:
        a = sunrise(d)
        b = sunset(d)
        c = Fraction(6, 24)

    ans = a + (2 * (b - a) * (floor(time) - c))
    return ans

def solar_convergence(time, angle):
    '''Zero in on the instant the sun hits a given zodiacal longitude'''
    time = Fraction(time) # given moment, in JULIAN DAYS. should be close to the transition of a rasi
    angle = Fraction(angle) # zodiacal angle we're looking for, in DEGREES
    ans = time

    p = 0

    while (p < 4):
        if (angle < 30):
            while (solar_longitude(ans) >= 330):
                ans += Fraction(1, (60 ** p))
            while (solar_longitude(ans) > angle) and (solar_longitude(ans) < 90):
                ans -= Fraction(1, (60 ** p))
            while (solar_longitude(ans) < angle):
                ans += Fraction(1, (60 ** p))
        elif (angle > 330):
            while (solar_longitude(ans) <= 30):
                ans -= Fraction(1, (60 ** p))
            while (solar_longitude(ans) > angle):
                ans -= Fraction(1, (60 ** p))
            while (solar_longitude(ans) < angle):
                ans += Fraction(1, (60 ** p))
        else:
            while (solar_longitude(ans) < angle):
                ans += Fraction(1, (60 ** p))
            while (solar_longitude(ans) > angle):
                ans -= Fraction(1, (60 ** p))

        if (solar_longitude(ans) == angle):
            p = 6

        p += 1
        #print("p == ", p)
    return ans
