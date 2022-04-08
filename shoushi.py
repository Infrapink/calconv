#!/usr/bin/python3

# Convert between the Shoushi calendar and Julian Days.

from math import floor, ceil
from decimal import Decimal

solar_year = Decimal('365.2425') # tropical year
yue = Decimal('29.530593') # synodic month
zhuan = Decimal('27.275546') # anomalistic month

#zhongqi = sui / 12 # major solar term
nian12 = 12 * yue
nian13 = 13 * yue

century = 100 * solar_year # 100 tropical years

epoch = 2188870
solar_epoch = Decimal('2188925.06') + 1
lunar_epoch = 2188904 # this will have a different decimal component depending on whether the year is before or after 1294 AD.
anom_epoch = Decimal('2188912.06') # this will have a different decimal component depending on whether this year is before or after 1294 AD.

MONTHS = ("Dōngyuè", "Bīngyuè", "Zōuyuè", "Xìngyuè", "Táoyuè", "Méiyuè", "Liúyuè", "Héyuè", "Lányuè", "Guìyuè", "Júyuè", "Lùyuè")

# now somw constants for use in calculating the true moon
bee = Decimal('88.909225')
cee = Decimal('93.712025')
dee = Decimal('1.0962')
kay = Decimal('0.082')

def eff(z):
    z = Decimal(z)

    a = (31 * z) + 24600
    b = 5133200 - (a * z)
    c = (b * z) / (10 ** 8)
    return c

def gee(z):
    z = Decimal(z)

    a = (27 * z) + 22100
    b = 4870600 - (a * z)
    c = (b * z) / (10 ** 8)
    return c

def haych(z):
    year = Decimal(z)

    a = (325 * z) + 28100
    b = 11110000 - (a * z)
    c = (b * z) / (10 ** 8)
    return c

def delta(z):
    z = Decimal(z)

    a = Decimal('0.11081575')
    b = z * Decimal('0.0005815')
    c = z * (z - 1 ) * Decimal('0.00000975')
    d = a - b - c
    return d

def tsun(z, epact, sui):
    z = Decimal(z)
    epact = Decimal(epact)
    sui = Decimal(sui)

    ans = ((z * yue) - epact) % sui
    return ans

def tmoon(z, epact, sui, year):
    z = Decimal(z)
    epact = Decimal(epact)
    sui = Decimal(sui)
    year = int(year)

    a = z * yue

    if year < 0:
        t = (abs(year) + Decimal('13.1904') - epact + a) % zhuan
    elif year <= 14:
        t = (((year - 1) * sui) + Decimal('13.1904') - epact + a) % zhuan
    else:
        t = (((year - 1) * sui) + Decimal('13.0205') - epact + a) % zhuan

    return t

def deltasun(z, epact, sui, year):
    z = Decimal(z)
    epact = Decimal(epact)
    sui = Decimal(sui)
    year = int(year)

    t = tsun(z, epact, sui)
    u = 0

    if t < bee:
        u = eff(t)
    elif t < (sui / 2):
        u = gee((sui / 2) - t)
    elif t < (sui / 2) + cee:
        u = 0 - gee(t - (sui / 2))
    else:
        u = 0 - eff(sui - t)

    return u

def deltamoon(z, epact, sui, year):
    z = Decimal(z)
    epact = Decimal(epact)
    sui = Decimal(sui)
    year = int(year)

    t = tmoon(z, epact, sui, year)
    u = 0

    if t < (zhuan / 4):
        u = 0 - haych(t / kay)
    elif t < (zhuan / 2):
        u = 0 - haych(((zhuan / 2) - t) / kay)
    elif t < Decimal('0.75') * zhuan:
        u = haych(t - ((zhuan / 2) / kay))
    else:
        u = haych((zhuan - 2) / kay)

    return u

def nu(z, epact, sui, year):
    z = Decimal(z)
    epact = Decimal(epact)
    sui = Decimal(sui)
    year = int(year)

    t = tmoon(z, epact, sui, year)
    u = 0

    if t < (81 * kay):
        u = dee + delta(t / kay)
    elif t < (86 * kay):
        u = dee
    elif t < (249 * kay):
        u = dee - delta(abs((zhuan / 2) - t) / kay)
    elif t < (254 * kay):
        u = dee
    else:
        u = dee + delta(abs((zhuan / 2) - t) / kay)

    return u

def lunadj(z, epact, sui, year):
    z = Decimal(z)
    epact = Decimal(epact)
    sui = Decimal(sui)
    year = int(year)

    a = deltasun(z, epact, sui, year)
    b = deltamoon(z, epact, sui, year)
    c = nu(z, epact, sui, year)

    ans = kay * ((a + b) / c)
    #print(ans)
    return ans

def fromjd(jday):
    '''Convert a Julian Day into a date in the Shoushi calendar'''

    jday = int(jday)

    day = 0
    month = ""
    year = 0

    sui = solar_year

    if (jday - solar_epoch) <= (13 * sui):
        ladd = Decimal('0.1850')
        #anom_epoch -= Decimal('0.1904')
    else:
        ladd = Decimal('0.205')
        #anom_epoch -= Decimal('0.0205')

    if jday >= floor(solar_epoch):
        # positive years... probably
        centuries = (jday - solar_epoch) // century
        year = (100 * centuries) + 1
        solstice = solar_epoch + (centuries * century) - (centuries * Decimal('0.0001'))
        sui -= (centuries * Decimal('0.0001'))
        orbits = (jday - solstice) // sui
        year += orbits
        solstice += (orbits * sui)
        if (year // 100) > centuries:
            sui -= Decimal('0.0001')
            solstice -= Decimal('0.0001')
        while floor(solstice + sui) <= jday:
            solstice += sui
            year += 1
            if year % 100 == 0:
                sui -= Decimal('0.0001')

        luns = (solstice - (lunar_epoch + ladd)) // yue
        solstice_moon = (lunar_epoch + ladd) + (luns * yue)
    else:
        # negative dates
        centuries = (solar_epoch - jday) //century
        year = 0 - centuries
        solstice = solar_epoch - (centuries * century) - (centuries * Decimal('0.0001'))
        sui += ((1 + centuries) * Decimal('0.0001'))
        orbits = (solstice - jday) // sui
        year -= orbits
        solstice -= (orbits * sui)
        if (abs(year) // 100) > centuries:
            sui += Decimal('0.0001')
            solstice -= Decimal('0.0001')
        while floor(solstice) > jday:
            solstice -= sui
            year -= 1
            if year % 100 == 0:
                solstice -= sui
                year -= 1
                if year % 100 == 0:
                    sui += Decimal('0.0001')

        luns = (lunar_epoch + ladd - jday) // yue
        solstice_moon = lunar_epoch + ladd - (luns * yue)

    while floor(solstice_moon) > floor(solstice):
        solstice_moon -= yue

    epact = solstice - solstice_moon
    zhongqi = sui / 12 # major solar term
    n = 1 # number of the month we're in
    truemoon = lambda newmoon, z: newmoon + lunadj(z, epact, sui, year) # save myself some typing
    
    while floor(truemoon(solstice_moon + yue, n)) <= floor(solstice):
        solstice_moon += yue
    while floor(truemoon(solstice_moon, n)) > floor(solstice):
        solstice_moon -= yue

    epact = solstice - solstice_moon

    prev_solstice = solstice - sui
    next_solstice = solstice + sui

    if floor(truemoon(solstice_moon - nian12, 1)) > floor(prev_solstice):
        prev_moon = solstice_moon - nian13
    else:
        prev_moon = solstice_moon - nian12
        
    if floor(truemoon(solstice_moon + nian13, 1)) <= floor(next_solstice):
        next_moon = solstice_moon + nian13
    else:
        next_moon = solstice_moon + nian12

    leap = None
    prev_leap = None
    next_leap = None
    
    # check for leap years
    if solstice_moon - prev_moon == nian12:
        prev_leap = False
        xin = prev_moon + (14 * yue)
    elif floor(truemoon(prev_moon + (2 * yue), 3)) <= floor(prev_solstice + zhongqi):
        prev_leap = True
        xin = prev_moon + (15 * yue)
    elif floor(truemoon(prev_moon + (3 * yue), 4)) <= floor(prev_solstice + (2 * zhongqi)):
        prev_leap = True
        xin = prev_moon + (15 * yue)
    else:
        prev_leap = False
        leap = True
        xin = prev_moon + (14 * yue)

    if next_moon - solstice_moon == nian12:
        next_xin = solstice_moon + (14 * yue)
    elif floor(truemoon(solstice_moon + (2 * yue), 3)) <= floor(solstice + zhongqi):
        leap = True
        next_xin = solstice_moon + (15 * yue)
    elif floor(truemoon(solstice_moon + (3 * yue), 4)) <= floor(solstice + (2 * zhongqi)):
        leap = True
        next_xin = solstice_moon + (15 * yue)
    else:
        leap = False
        next_xin = solstice_moon + (14 * yue)

    n = int((xin - solstice_moon) / yue)

    if floor(truemoon(xin, n)) > jday:
        year -= 1
        if year == 0:
            year = (-1)
            
        next_xin = xin
        next_solstice = solstice
        next_moon = solstice_moon

        solstice = prev_solstice
        solstice_moon = prev_moon
        leap = prev_leap

        prev_solstice = solstice - sui
        if floor(truemoon(solstice_moon - nian12, 1)) > floor(prev_solstice):
            prev_moon = solstice_moon - nian13
        else:
            prev_moon = solstice_moon - nian12

        if solstice_moon - prev_moon == nian12:
            xin = prev_moon + (14 * yue)
            leap = False
        elif floor(truemoon(prev_moon + (2 * yue), 3)) <= floor(prev_solstice + zhongqi):
            xin = prev_moon + (15 * yue)
        elif floor(truemoon(prev_moon + (3 * yue), 4)) <= floor(prev_solstice + (2 * zhongqi)):
            xin = prev_moon + (15 * zhongqi)
        else:
            xin = prev_moon + (14 * zhongqi)
            leap = True
            

    newmoon = xin
    m = 0
    n = (xin - solstice_moon) / yue

    if leap == False:
        # regular year
        m = int((jday - xin) // yue)
        n += m
        newmoon += (m * yue)
        while floor(truemoon(newmoon + yue, n + 1)) <= jday:
            m += 1
            n += 1
            newmoon += yue
            if newmoon == next_moon:
                n = 1

        month = MONTHS[m]
        day = jday - floor(truemoon(newmoon, n)) + 1
    else:
        # leap year
        leapt = False # have we passed the leap month?
        z = solstice # major solar term
        while floor(z + zhongqi) <= floor(truemoon(xin, n)):
            z += zhongqi

        while floor(truemoon(newmoon + yue, n + 1)) <= jday:
            if (floor(truemoon(newmoon + yue, n + 1)) <= floor(z)) and (leapt == False):
                # leap month
                leapt = True
                newmoon += yue
                n += 1
            else:
                # normal month
                newmoon += yue
                n += 1
                m += 1
                z += zhongqi
            if newmoon == next_moon:
                n = 1

        day = jday - floor(truemoon(newmoon, n)) + 1

        if (leapt == False) and floor(truemoon(newmoon + yue, n + 1)):
            # we've landed in the leap month
            month = "Rùn " + MONTHS[m - 1]
        else:
            # it's a normal month
            month = MONTHS[m]

    return(day, month, year)

def tojd(day, month, year):
    '''Convert a date in the Shoushi calendar into a Julian Day'''
    day = int(day)
    month = str(month)
    year = int(year)

    jday = 0

    sui = solar_year

    if year == 0:
        year = (-1)

    if year <= 13:
        ladd = Decimal('0.1850')
    else:
        ladd = Decimal('0.205')

    if year > 0:
        # positice years
        solstice = solar_epoch + ((year - 1) * sui) - (Decimal('0.0001') * (year // 100))
        sui -= (Decimal('0.0001') * (year // 100))
        luns = (solstice - lunar_epoch) // yue
        solstice_moon = lunar_epoch + (luns * yue)
    else:
        # negative years
        solstice = solar_epoch + (year * sui) - (Decimal('0.0001') * ceil(abs(year) / 100))
        sui += ceil(abs(year) / 100)
        luns = (lunar_epoch - solstice) // yue
        solstice_moon = lunar_epoch - ((luns + 1) * yue)

    while floor(solstice_moon) > floor(solstice):
        solstice_moon -= yue

    zhongqi = sui / 12 # major solar term
    epact = solstice - solstice_moon
    n = 1

    # save myself some typing
    truemoon = lambda newmoon, z: newmoon + lunadj(z, epact, sui, year)
    
    while floor(truemoon(solstice_moon, n)) > floor(solstice):
        solstice_moon -= yue
    while floor(truemoon(solstice_moon + yue, n + 1)) <= floor(solstice):
        solstice_moon += yue

    prev_solstice = solstice - sui
    next_solstice = solstice + sui

    if floor(truemoon(solstice_moon - nian12, 1)) > floor(prev_solstice):
        prev_moon = solstice_moon - nian13
    else:
        prev_moon = solstice_moon - nian12

    if floor(truemoon(solstice_moon + nian13, 1)) <= floor(next_solstice):
        next_moon = solstice_moon + nian13
    else:
        next_moon = solstice_moon + nian12

    # check for leap years
    leap = False
    if solstice_moon - prev_moon == nian12:
        prev_leap = False
        leap = False
        xin = prev_moon + (14 * yue)
    elif floor(truemoon(prev_moon + (2 * yue), 3)) <= floor(prev_solstice + zhongqi):
        prev_leap = True
        leap = False
        xin = preV_moon + (15 * yue)
    elif floor(truemoon(prev_moon + (3 * yue), 4)) <= floor(prev_solstice + (2 * zhongqi)):
        prev_leap = True
        leap = False
        xin = prev_moon + (15 * yue)
    else:
        prev_leap = False
        leap = True
        xin = prev_moon + (14 * yue)
    
    if next_moon - solstice_moon == nian12:
        next_leap = False
    elif floor(truemoon(solstice_moon + (2 * yue), 3)) <= floor(solstice + zhongqi):
        leap = True
    elif floor(truemoon(solstice_moon + (3 * yue), 4)) <= floor(solstice + (2 * zhongqi)):
        leap = True
    else:
        next_leap = True

    jday = xin
    n = (xin - solstice_moon) / yue
    m = 0

    if leap == False:
        # normal year
        if month[0:3] == "Rùn":
            month = month[4:] # cut off the "Rùn " part.

        while MONTHS[m] != month:
            m += 1
            n += 1
            jday += yue
            if jday == next_moon:
                n = 1

        jday = floor(truemoon(jday, n)) + day - 1
    else:
        # leap year
        if month[0:3] == "Rùn":
            run = True # assume that if the user enters the leap month, they want the actual leap month
        else:
            run = False

        leapt = False # have we passed the leap month?
        z = solstice
        while floor(z) < floor(jday):
            z += zhongqi

        while MONTHS[m] != month:
            if (run == True) and (floor(truemoon(jday + yue, n + 1)) <= floor(z)):
                break # because we're in the leap month
            elif (floor(truemoon(jday + yue, n + 1)) <= floor(z)) and (leapt == False):
                n += 1
                jday += yue
                leapt = True
            else:
                jday += yue
                m += 1
                n += 1
                z += zhongqi
            if jday == next_moon:
                n = 1

        jday = floor(truemoon(jday, n)) + day - 1

    return(jday)
