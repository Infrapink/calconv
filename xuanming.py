#!/usr/bin/python3

# Convert between the Xuanming calendard and Julian day
# This is based on Astronomy and Calendars: The Other Chinese Mathematics 104 BC - AD 1644; Jean-Claude Martzloff, Springer, 2009 (French), 2016 (English)

from fractions import Fraction
from decimal import Decimal
from math import floor
from solun import trans, conj

# Global variables

sui = 365 + Fraction(2055, 8400) # tropical year
yue = 29 + Fraction(4457, 8400) # synodic month
zhuan = 27 + Fraction(4658,8400) + Fraction(9,840000) # anomalistic month
jieqi = 15 + Fraction(1835, 8400) + Fraction(5, (8400 * 8)) # solar term

solar_epoch = 2021278 + Fraction(213,280) # southern solstice of 821 AD
lunar_epoch = 2021259 + Fraction(409,600) # new moon immediately preceding solar_epoch
anom_epoch = 2021242 + Fraction(667349, 840000) # where the anomalistic months are measured from

MONTHS = ("Dōngyuè", "Bīngyuè", "Zōuyuè", "Xìngyuè", "Táoyuè", "Méiyuè", "Liúyuè", "Héyuè", "Lányuè", "Guìyuè", "Júyuè", "Lùyuè")

STADJ = (-Fraction(6000,8400), -Fraction(5000,8400), -Fraction(4000,8400), -Fraction(3000,8400), -Fraction(1800,8400), -Fraction(600,8400), Fraction(600,8400), Fraction(1800,8400), Fraction(3000,8400), Fraction(4000,8400), Fraction(5000,8400), Fraction(6000,8400), Fraction(6000,8400), Fraction(5000,8400), Fraction(4000,8400), Fraction(3000,8400), Fraction(1800,8400), Fraction(600,8400), Fraction(-600,8400), Fraction(-1800,8400), Fraction(-3000,8400), Fraction(-4000,8400), Fraction(-5000,8400), Fraction(-6000,8400)) # adjustments to the solar terms. Martzloff divides the numerators by 100 and neglects to mention it, leaving the reader to figure out what he's done by careful reading and manually checking his calculations.

BETA = (0, 449, 823, 1122, 1346, 1481, 1526, 1481, 1346, 1122, 823, 449, 0, -449, -823, -1122, -1346, -1481, -1526, -1481, -1346, -1122, -823, -449) # used in calculating the solar correction, from Martzloff (2009) after Uchida (1975)
#BETA = (Decimal('33.4511'), Decimal('28.0315'), Decimal('22.6998'), Decimal('17.8923'), Decimal('11.7966'), Decimal('5.7986'), Decimal('-0.2433'), Decimal('-6.1254'), Decimal('-12.2048'), Decimal('-16.9060'), Decimal('-21.5362'), Decimal('-26.0498'), Decimal('-30.3119'), Decimal('-25.8126'), Decimal('-21.2454'), Decimal('-17.0296'), Decimal('-11.4744'), Decimal('-5.6429'), Decimal('0.1432'), Decimal('6.1488'), Decimal('12.6336'), Decimal('17.8043'), Decimal('23.0590'), Decimal('28.4618')) # used in calculating the solar correction, from Martzloff (2009) after Uchida (1975). The Xuanming li lists these values as fractions, but their denominators are not 8400; for this reason, Uchida converts them into decimals to make the maths easier, and Martzloff states that some analagous method of approximation was used by Tang-dynasty scholars. Unfortunately, I do not have access to the Xuanming li or Uchida's book, and in any case, they are both written in languages I do not speak.
#GAMMA = (Decimal('−0.3695'), Decimal('−0.3606'), Decimal('−0.3519'), Decimal('−0.4068'), Decimal('−0.3998'), Decimal('−0.3998'), Decimal('−0.3779'), Decimal('−0.3634'), Decimal('−0.2987'), Decimal('−0.2919'), Decimal('−0.2854'), Decimal('−0.2854'), Decimal('0.2854'), Decimal('0.2919'), Decimal('0.2987'), Decimal('0.3634'), Decimal('0.3779'), Decimal('0.3779'), Decimal('0.3998'), Decimal('0.4068'), Decimal('0.3519'), Decimal('0.3606'), Decimal('0.3695'), Decimal('0.3695')) # used in calculating the solar correction, from Martzloff (2009) after Uchida (1975). The Xuanming li lists these values as fractions, but their denominators are not 8400; for this reason, Uchida converts them into decimals to make the maths easier, and Martzloff states that some analagous method of approximation was used by Tang-dynasty scholars. Unfortunately, I do not have access to the Xuanming li or Uchida's book, and in any case, they are both written in languages I do not speak.

ALPHA_1 = (0, 830, 1556, 2162, 2633, 2970, 3172, 3218, 3136, 2912, 2546, 2037, 1394, 646) # used for the lunar correction
ALPHA_2 = (0, -830, -1556, -2154, -2618, -2947, -3142, -3188, -3106, -2881, -2515, -2014, -1386, -646) # used for the lunar correction
LAMBDA_1 = (830, 726, 606, 471, 337, 202, 0, -82, -224, -366, -509, -643, -748, -646) # used for the lunar correction. The 0 is a placeholder for a value that depends on various factors.
LAMBDA_2 = (-830, -726, -598, -464, -329, -195, 0, 82, 225, 366, 501, 628, 740, 646) # used for the lunar correction. The 0 is a placeholder for a value that depends on various factors.


def getruqi(solstice, newmoon):
    '''Get the ruqi for a given date. This is only to be used for the mean new moon.'''
    j = Fraction(solstice)
    newmoon = Fraction(newmoon)
    q = 0

    if newmoon < j:
        while j > newmoon:
            q -= 1
            j = j - jieqi - STADJ[q % 24]
    elif newmoon > j:
        while (j + jieqi + STADJ[q % 24]) < newmoon:
            j = j + jieqi + STADJ[q % 24]
            q += 1

    return (newmoon - j)

def getruli(newmoon):
    '''Determine the ruli for a given new moon.'''
    newmoon = Fraction(newmoon)
    if newmoon >= anom_epoch:
        peris = (newmoon - anom_epoch) // zhuan
        anom = anom_epoch + (peris * zhuan)
    else:
        peris = (anom_epoch - newmoon) // zhuan
        anom = anom_epoch - (peris * zhuan)

    while (anom + zhuan) <= newmoon:
        anom += zhuan
    while anom > newmoon:
        anom -= zhuan

    if (newmoon - anom) <= Fraction(zhuan, 2):
        r = newmoon - anom
        p = 0
    else:
        r = newmoon - anom - Fraction(zhuan, 2)
        p = 1

    return (r, p)

def sunyi(b, n, c):
    '''A calculation used in solcor(). Variable names from Martzloff, p. 187-8'''
    b = Fraction(b)
    c = Fraction(c)
    n = int(n)

    s = b + (n * c)
    return s

def tiaonu(n, a, b, c):
    '''A calculation used in solcor().'''
    n = int(n)
    a = int(a)
    b = Fraction(b)
    c = Fraction(c)
    #t = 0
    #k = 0

    #while k < n:
        #t += sunyi(b, k, c)
        #k += 1

    t = a + (n * b) + (Fraction(1,2) * n * (n - 1) * c)    

    return t
            

def solcor(solstice, newmoon):
    '''Solar correction, applied to a mean new moon. Used in determining the true new moon. See Martzloff chs. 5 and 10'''
    j = Fraction(solstice)
    n = Fraction(newmoon)
    q = 0

    ruqi = getruqi(j, n)

    while (j + jieqi + STADJ[q % 24]) <= n:
        j = j + jieqi + STADJ[q % 24]
        q += 1

    while j > n:
        q -= 1
        j = j - jieqi - STADJ[q % 24]

    delta = (BETA[(q - 0) % 24] - BETA[(q - 1) % 24],
             BETA[q + 1] - BETA[q + 0],
             BETA [q + 2] - BETA[q + 1])

    eta = (j - jieqi - STADJ[(q - 1) % 24],
           j,
           j + jieqi + STADJ[q % 24],
           j + (2 * jieqi) + STADJ[q % 24] + STADJ[(q + 1) % 24])

    zeta = (eta[1] - eta[0],
            eta[2] - eta[1],
            eta[3] - eta[2])
    
    a = BETA[q % 24]

    b = Fraction(delta[1], zeta[1])
    c = 0
    if (q % 24) in (5, 11, 17, 23): # Martzloff indexes from 1, but Python is 0-indexed.
        b = b + (Fraction(zeta[0], (zeta[0] + zeta[1])) * (Fraction(delta[0], zeta[0]) - Fraction(delta[1], zeta[1])))
        b = b - (Fraction(1, zeta[0] + zeta[1]) * (Fraction(delta[0], zeta[0]) - Fraction(delta[1], zeta[1])))

        c = Fraction(0 - 2, zeta[0] + zeta[1]) + (Fraction(delta[0], zeta[0]) - Fraction(delta[1], zeta[1]))
    else:
        b = b + (Fraction(zeta[1], (zeta[1] + zeta[2])) * (Fraction(delta[1], zeta[1]) - Fraction(delta[2], zeta[2])))
        b = b - (Fraction(1, zeta[1] + zeta[2]) * (Fraction(delta[1], zeta[1]) - Fraction(delta[2], zeta[2])))

        c = Fraction(0 - 2, zeta[1] + zeta[2]) + (Fraction(delta[1], zeta[1]) - Fraction(delta[2], zeta[2]))

    t = tiaonu(floor(ruqi), a, b, c)
    s = sunyi(b, (ruqi % 1), c)

    return(t + s) # this might possibly need to be divided by 8400

def luncor(newmoon, msm):
    '''Lunar correction'''
    msm = Fraction(msm) # mean solstice moon
    newmoon = Fraction(newmoon) # the moon in question
    delta = 0

    lunation = (newmoon - msm) // yue
    r = getruli(newmoon)
    ruli = r[0]
    phase = r[1]

    if floor(ruli) == 6: # 7 in Martzloff, but his book is 1-indexed while Python is 0-indexed
        y = (ruli % 1).numerator * (8400 / (ruli % 1).denominator) # numerator of the fractional part of ruli when the denominator is 8400
        if y < 3172:
            delta = 3172 + (53 * 
    else:
        if phase == 0:
            delta = ALPHA_1[floor(ruli)] + (LAMBDA_1[floor(ruli)] * (ruli % 1))
        else:
            delta = ALPHA_2[floor(ruli)] + (LAMBDA_2[floor(ruli)] * (ruli % 1))

    return Fraction(delta, 8400)

def fromjd(jday):
    '''Convert a Julian Day into a Xuanming li date'''
    jday = int(jday)

    day = 0
    month = ""
    year = 0

    if jday > int(solar_epoch):
        # positive dates... probably
        orbits = (jday - solar_epoch) // sui
        solstice = solar_epoch + (sui * orbits)
        year = orbits + 1
        while floor(solstice + sui) <= jday:
            year += 1
            solstice += sui

        luns = (solstice - lunar_epoch) // yue
        msm = lunar_epoch + (luns * yue) # mean solstice moon

        peris = (msm - anom_epoch) // zhuan # how many anomalistic months have passed?
        anom = anom_epoch + (zhuan * peris)
        
    else:
        # negative dates
        year = (solar+epoch - jday) // sui
        solstice = 0 - (sui * year)
        while floor(solstice) > jday:
            year -= 1
            solstice -= sui

        luns = (lunar_epoch - solstice) // yue
        msm = lunar_epoch - (luns * yue)

        peris = (anom_epoch - msm) // zhuan
        anom = anom_epoch - (zhuan * peris)

    while floor(msm + yue) <= floor(solstice):
        msm += yue
    while floor(msm) > floor(solstice):
        msm -= yue
    while anom > msm:
        anom -= zhuan
    while anom + zhuan <= msm:
        anom += zhuan
    sruqi = getruqi(solstice, msm) # ruqi of the mean new moon preceding the southern solstice
        
