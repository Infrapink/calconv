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

nian12 = 12 * yue
nian13 = 13 * yue

solar_epoch = 2021278 + Fraction(213,280) # southern solstice of 821 AD
lunar_epoch = 2021259 + Fraction(409,600) # new moon immediately preceding solar_epoch
anom_epoch = 2021242 + Fraction(667349, 840000) # where the anomalistic months are measured from

MONTHS = ("Dōngyuè", "Bīngyuè", "Zōuyuè", "Xìngyuè", "Táoyuè", "Méiyuè", "Liúyuè", "Héyuè", "Lányuè", "Guìyuè", "Júyuè", "Lùyuè")

STADJ = (-Fraction(6000,8400), -Fraction(5000,8400), -Fraction(4000,8400), -Fraction(3000,8400), -Fraction(1800,8400), -Fraction(600,8400), Fraction(600,8400), Fraction(1800,8400), Fraction(3000,8400), Fraction(4000,8400), Fraction(5000,8400), Fraction(6000,8400), Fraction(6000,8400), Fraction(5000,8400), Fraction(4000,8400), Fraction(3000,8400), Fraction(1800,8400), Fraction(600,8400), Fraction(-600,8400), Fraction(-1800,8400), Fraction(-3000,8400), Fraction(-4000,8400), Fraction(-5000,8400), Fraction(-6000,8400)) # adjustments to the solar terms. Martzloff divides the numerators by 100 and neglects to mention it, leaving the reader to figure out what he's done by careful reading and manually checking his calculations.

SIGMA = (0, 449, 823, 1122, 1346, 1481, 1526, 1481, 1346, 1122, 823, 449, 0, -449, -823, -1122, -1346, -1481, -1526, -1481, -1346, -1122, -823, -449) # used in calculating the solar correction, from Martzloff (2009) after Uchida (1975)

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
            q = (q - 1) % 24
            j = j - jieqi - STADJ[q % 24]
    elif newmoon > j:
        while (j + jieqi + STADJ[(q + 1) % 24]) < newmoon:
            j = j + jieqi + STADJ[(q + 1) % 24]
            q = (q + 1) % 24

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

    while (j + jieqi + STADJ[(q + 1) % 24]) < n:
        j = j + jieqi + STADJ[(q + 1) % 24]
        q = (q + 1) % 24

    while j > n:
        q = (q - 1) % 24
        j = j - jieqi - STADJ[q % 24]

    delta = (SIGMA[(q - 0) % 24] - SIGMA[(q - 1) % 24],
             SIGMA[(q + 1) % 24] - SIGMA[(q + 0) % 24],
             SIGMA [(q + 2) % 24] - SIGMA[(q + 1) % 24])

    eta = (j - jieqi - STADJ[(q - 1) % 24],
           j,
           j + jieqi + STADJ[(q + 1) % 24],
           j + (2 * jieqi) + STADJ[(q + 2) % 24] + STADJ[(q + 3) % 24])

    zeta = (eta[1] - eta[0],
            eta[2] - eta[1],
            eta[3] - eta[2])
    
    a = SIGMA[q % 24]

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

    return Fraction((t + s), 8400) # Martzloff does not specify that his results need to be divided by 8400

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
        y = (ruli % 1).numerator * Fraction(840000, (ruli % 1).denominator) # numerator of the fractional part of ruli when the denominator is 8400
        y //= 100 # isolate the part that is /8400, dropping the part that is /840000
        if phase == 0: # first part of the anomalistic month
            if y < 7465: # Martzloff gives this value as both 7465 and 7565 on p. 288. 7465 gives an answer slightly closer to the result of his calculations, and it's in the table rather than the body of the text.
                delta = 3172 + (53 * Fraction(y, 7465))
            else:
                delta = 3172 + ((-7) * Fraction(y, 935))
        else: # second part of the anomalistic month
            if y < 6529:
                delta = (-3142) + ((-53) * Fraction(y, 6529))
            else:
                delta = (-3142) * (7 * Fraction(y, 1871))
    else:
        if phase == 0: # first part of the anomalistic month
            delta = ALPHA_1[floor(ruli)] + (LAMBDA_1[floor(ruli)] * (ruli % 1))
        else: # second part of the anomalistic month
            delta = ALPHA_2[floor(ruli)] + (LAMBDA_2[floor(ruli)] * (ruli % 1))

    return Fraction(delta, 8400)

def truemoon(newmoon, msm, solstice):
    newmoon = Fraction(newmoon) # the mean new moon in question
    msm = Fraction(msm) # the mean solstice moon
    solstice = Fraction(solstice) # obvious

    solar = solcor(solstice, newmoon)
    lunar = luncor(newmoon, msm)

    darkmoon = newmoon + solar + lunar
    return darkmoon

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
    else:
        # negative dates
        year = 0 - ((solar_epoch - jday) // sui)
        solstice = 0 - (sui * year)
        while floor(solstice) > jday:
            year -= 1
            solstice -= sui

        luns = (lunar_epoch - solstice) // yue
        msm = lunar_epoch - (luns * yue)

    while floor(truemoon(msm, msm + yue, solstice)) <= floor(solstice):
        msm += yue
    while floor(truemoon(msm, msm, solstice)) > floor(solstice):
        msm -= yue

    next_solstice = solstice + sui
    prev_solstice = solstice - sui

    if floor(truemoon(msm + nian13, msm + nian13, next_solstice)) <= floor(next_solstice):
        next_msm = msm + nian13
    else:
        next_msm = msm + nian12

    if floor(truemoon(msm - nian12, msm - nian12, prev_solstice)) > floor(prev_solstice):
        prev_msm = msm - nian13
    else:
        prev_msm = msm - nian12

    # OK, so now we have the solstices and their corresponding new moons for the current, as well as next and previous, years.
    # Is there a leap year?

    if msm - prev_msm == nian12:
        prev_leap = False
        leap = False
        xin = prev_msm + (14 * yue)
    elif floor(truemoon(prev_msm + (2 * yue), prev_msm, prev_solstice)) <= floor(prev_solstice + (2 * jieqi) + STADJ[0] + STADJ[1]):
        prev_leap = True
        leap = False
        xin = prev_msm + (15 * yue)
    elif floor(truemoon(prev_msm + (3 * yue), prev_msm, prev_solstice)) <= floor(prev_solstice + (4 * jieqi) + STADJ[0] + STADJ[1] + STADJ[2] + STADJ[3]):
        prev_leap = True
        leap = False
        xin = prev_msm + (15 * yue)
    else:
        prev_leap = False
        leap = True
        xin = prev_msm + (14 * yue)

    if next_msm - msm == nian12:
        next_leap = False
        next_xin = msm + (14 * yue)
    elif floor(truemoon(msm + (2 * yue), msm, solstice)) <= floor(solstice + (2 * jieqi) + STADJ[0] + STADJ[1]):
        leap = True
        next_xin = msm + (15 * yue)
    elif floor(truemoon(msm + (3 * yue), msm, solstice)) <= floor(solstice + (4 * jieqi) + STADJ[0] + STADJ[1] + STADJ[2] + STADJ[3]):
        leap = True
        next_xin = msm + (15 * yue)
    else:
        next_leap = True
        next_xin = msm + (14 * yue)

    if floor(truemoon(xin, msm, solstice)) > jday:
        year -= 1
        if year == 0:
            year = (-1)
        solstice = prev_solstice
        msm = prev_msm
        leap = prev_leap

        if floor(truemoon(msm - nian12, msm, solstice)) > floor(prev_solstice):
            prev_msm = msm - nian13
        else:
            prev_msm = msm - nian12

        if msm - prev_msm == nian12:
            xin = prev_msm + (14 * yue)
        elif floor(truemoon(prev_msm + (2 * yue), prev_msm, prev_solstice)) <= floor(prev_solstice + (2 * jieqi) + STADJ[0] + STADJ[1]):
            xin = prev_msm + (15 * yue)
        elif floor(truemoon(prev_msm + (3 * yue), prev_msm, prev_solstice)) <= floor(prev_solstice + (4 * jieqi) + STADJ[0] + STADJ[1] + STADJ[2] + STADJ[3]):
            xin = prev_msm + (15 * yue)
        else:
            leap = True
            xin = prev_msm + (14 * yue)
    newmoon = xin
    m = 0

    if leap == False:
        # normal year
        while floor(truemoon(newmoon + yue, msm, solstice)) <= jday:
            m += 1
            newmoon += yue
        month = MONTHS[m]
        day = 1 + jday - floor(truemoon(newmoon, msm, solstice))
    else:
        leapt = False # have we passed the leap month?
        run = False # are we in the leap month?
        zhongqi = solstice
        q = 0 # count of which solar term we're in, where the southern solstice is number 0
        
        while floor(zhongqi) < floor(truemoon(xin, msm, solstice)):
            zhongqi = zhongqi + (2 * jieqi) + STADJ[q % 24] + STADJ[(q + 1) % 24]
            q += 2

        while floor(truemoon(newmoon + yue, msm, solstice)) <= jday:
            newmoon += yue
            run = False

            if floor(truemoon(newmoon, msm, solstice)) < floor(zhongqi):
                if leapt == True:
                    m += 1
                else:
                    run = True
                leapt = True
            else:
                m += 1
                zhongqi = zhongqi + (2 * jieqi) + STADJ[q % 24] + STADJ[(q + 1) % 24]
                q += 2

        if run == True:
            month = "Rùn" + MONTHS[m]
        else:
            month = MONTHS[m]

        day = 1 + jday - floor(truemoon(newmoon, msm, solstice))

    return (day, month, year)

def tojd(day, month, year):
    day = int(day)
    month = str(month)
    year = int(year)

    jday = 0

    if year == 0:
        year = (-1)

    if year >= 1:
        solstice = solar_epoch + ((year - 1) * sui)
        luns = (solstice - lunar_epoch) // yue
        msm = lunar_epoch + (luns * yue)
    else:
        solstice = solar_epoch + (year * sui)
        luns = (lunar_epoch - solstice) // yue
        msm = lunar_epoch - (luns * yue)

    while floor(truemoon(msm, msm, solstice)) > floor(solstice):
        msm -= yue
    while floor(truemoon(msm + yue, msm, solstice)) <= floor(solstice):
        msm += yue

    next_solstice = solstice + sui
    prev_solstice = solstice - sui

    if floor(truemoon(msm + nian13, msm, solstice)) <= floor(next_solstice):
        next_msm = msm + nian13
    else:
        next_msm = msm + nian12
    if floor(truemoon(msm - nian12, msm, solstice)) > floor(prev_solstice):
        prev_msm = msm - nian13
    else:
        prev_msm = msm - nian12

    # is there a leap year?
    if msm - prev_msm == nian12:
        prev_leap = False
        leap = False
        xin = prev_msm + (14 * yue)
    elif floor(truemoon(prev_msm + (2 * yue), prev_msm, prev_solstice)) < floor(prev_solstice + (2 * jieqi) + STADJ[0] + STADJ[1]):
        prev_leap = True
        leap = False
        xin = prev_msm + (15 * yue)
    elif floor(truemoon(prev_msm + (3 * yue), prev_msm, prev_solstice)) < floor(prev_solstice + (4 * jieqi) + STADJ[0] + STADJ[1] + STADJ[2] + STADJ[3]):
        prev_leap = True
        leap = False
        xin = prev_msm + (15 * yue)
    else:
        prev_leap = False
        leap = True
        xin = prev_msm + (14 * yue)

    if next_msm - msm == nian12:
        next_leap = False
        next_xin = msm + (14 * yue)
    elif floor(truemoon(msm + (2 * yue), msm, solstice)) < floor(solstice + (2 * jieqi) + STADJ[0] + STADJ[1]):
        leap = True
        next_leap = False
        next_xin = msm + (15 * yue)
    elif floor(truemoon(msm + (3 * yue), msm, solstice)) < floor(solstice + (4 * jieqi) + STADJ[0] + STADJ[1] + STADJ[2] + STADJ[3]):
        leap = True
        next_leap = False
        next_xin = msm + (15 * yue)
    else:
        next_leap = True
        next_xin = msm + (14 * yue)

    jday = xin
    m = 0 # month tracker

    if leap == False:
        # normal year
        if month[0:3] == "Rùn":
            month = month[:4] # cut of the "Rùn" part

        while MONTHS[m] != month:
            m += 1
            jday += yue

        jday = floor(truemoon(jday, msm, solstice)) + day - 1

    else:
        # leap year
        if month[0:3] == "Rùn":
            run = True # assume the user meant the actual leap month
        else:
            run = False

        zhongqi = solstice # major solar term
        q = 0 # keep track of which solar term we're in, where the southern solstice is 0

        while floor(zhongqi) < floor(truemoon(jday, msm, solstice)):
            zhongqi = zhongqi + (2 * jieqi) + STADJ[q % 24] + STADJ[(q + 1) % 24]
            q += 2

        while month != MONTHS[m]:
            if (run == True) and (floor(truemoon(jday + yue, msm, solstice)) < floor(zhongqi)):
                break

            m += 1
            jday += yue
            if floor(zhongqi) < floor(truemoon(jday, msm, solstice)):
                zhongqi = zhongqi + (2 * jieqi) + STADJ[q % 24] + STADJ[(q + 1) % 24]
                q += 2

        jday = floor(truemoon(jday, msm, solstice)) + day - 1

    return(jday)
