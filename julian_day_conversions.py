#!/usr/bin/python

#
# Convert a Julian Day to a date in various calendars
#

from fractions import *
from math import *

import months
import leap_years_birashk
import leap_years_assyrian
#import leap_years_rev_hebrew

import hebrew_calculations
#import rev_hebrew_calculations

cycle4 = (4 * 365) + 1
cycle100 = (100 * 365) + 24
cycle400 = (400 * 365) + 97
cycle900 = (900 * 365) + 218
cycle4000 = (4000 * 365) + 969
cycle128j = (128 * 365) + 31

cycle30 = (30 * 354) + 11

cycle5 = (365 * 5) + 1
cycle33 = (7 * cycle4) + cycle5
cycle29 = (6 * cycle4) + cycle5
cycle37 = (8 * cycle4) + cycle5
cycle128 = (3 * cycle33) + cycle29
cycle132 = (2 * cycle33) + cycle29 + cycle37
cycle2820 = (21 * cycle128) + cycle132

cycle19 = (12 * 354) + (7 * 383)

def julian(jday):
    """Convert the Julian Day to a date in the Julian Calendar"""
    jday = int(jday)
    year = 0
    month = ""
    day = 0
    m = None
    d = 0

    if jday > 1721422:
        # positive date
        delta = jday - 1721422
        year_4 = delta // cycle4
        delta %= cycle4
        single_years = delta // 365
        delta %= 365
        year = (4 * year_4) + single_years + 1 # need to add 1 to account for the lack of year 0
        if year % 4 == 0:
            # leap year
            m = months.CAESAR_MONTHS_LEAP
        else:
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL
        if delta == 0:
            delta = 365
            year -= 1
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    else:
        # negative date
        delta = 1721423 - jday
        # This guarantees a nonzero value for delta
        # Because we are counting backwards, it is the first and not the fourth year of the 4-year cycle
        # that has 366 days in it.
        # But we're starting at year 0, which will be corrected later.

        while delta > 0:
            if year % 4 == 0:
                year += 1
                delta -= 366
            else:
                year += 1
                delta -= 365

        # delta is now 0 or negative, and year is the negative of the actual year.
        if (year - 1) % 4 == 0:
            # leap year
            m = months.CAESAR_MONTHS_LEAP
            delta = 0 - delta + 1
        else:
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL
            delta = 0 - delta + 1

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]
        year = 0 - year
        date = (day,month,year)
        return date

    date = (day,month,year)
    return date

def gregorian(jday):
    """Convert a Julian Day to a date in the Gregorian calendar"""
    jday = int(jday)
    year = 0
    month = ""
    day = 0
    m = None
    d = 0
    leap = None

    if jday > 1721424:
        # positive date
        delta = jday - 1721424
        year_400 = delta // cycle400
        delta = delta % cycle400
        year_100 = delta // cycle100
        delta = delta % cycle100
        year_4 = delta // cycle4
        delta = delta % cycle4
        single_years = delta // 365
        delta = delta % 365
        year = (400 * year_400) + (100 * year_100) + (4 * year_4) + single_years +1 # have to add 1 to account for the lack of year 0

        if year % 400 == 0:
            # leap year
            leap = True
        elif year % 100 == 0:
            # not a leap year
            leap = False
        elif year % 4 == 0:
            # leap year
            leap = True
        else:
            # not a leap year
            leap = False

        if leap == True:
            m = months.CAESAR_MONTHS_LEAP
        else:
            m = months.CAESAR_MONTHS_NORMAL
        if delta == 0:
            delta = 365
            year -= 1
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    else:
        # negative date
        delta = 1721425 - jday

        while delta > 0:
            if year % 400 == 0:
                year += 1
                delta -= 366
            elif year % 100 == 0:
                year += 1
                delta -= 365
            elif year % 4 == 0:
                year += 1
                delta -= 366
            else:
                year+= 1
                delta -= 365

        if (year - 1) % 400 == 0:
            # leap year
            m = months.CAESAR_MONTHS_LEAP
        elif (year - 1) % 100 == 0:
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL
        elif (year - 1) % 4 == 0:
            # leap year
            m = months.CAESAR_MONTHS_LEAP
        else:
            # not leap year
            m = months.CAESAR_MONTHS_NORMAL

        year = 0 - year
        delta = 0 - delta + 1

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = [day, month, year]
    return(date)

def coptic(jday):
    """Convert a Julian Day to a date in the Coptic Calendar"""
    jday = int(jday)
    day = 0
    month = ""
    year = 0
    d = 0
    m = None

    if jday > 1825028:
        # positive date
        delta = jday - 1825028
        year_4 = delta // cycle4
        delta = delta % cycle4
        single_years = delta // 365
        delta = delta % 365
        year = (4 * year_4) + single_years + 1 # add 1 year to account for the lack of year 0
        if year % 4 == 0:
            # leap year
            m = months.COPTIC_MONTHS_LEAP
        else:
            # not a leap year
            m = months.COPTIC_MONTHS_NORMAL
        if delta == 0:
            delta = 365
            year -= 1
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    else:
        # negative date
        delta = 1825029 - jday

        while delta > 0:
            if year % 4 == 0:
                year += 1
                delta -= 366
            else:
                year += 1
                delta -= 365

        if (year - 1) % 4 == 0:
            # leap year
            m = months.COPTIC_MONTHS_LEAP
        else:
            # not a leap year
            m = months.COPTIC_MONTHS_NORMAL

        year = 0 - year
        delta = 0 - delta + 1

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]
                
    date = [day, month, year]
    return(date)

def ethiopian(jday):
    """Convert a Julian Day to a date in the Ethiopian calendar"""
    jday = int(jday)
    year = 0
    month = ""
    day = 0
    m = None
    d = 0

    if jday > 1724221:
        # positive date
        delta = jday - 1724221
        year_4 = delta // cycle4
        delta = delta % cycle4
        single_years = delta // 365
        delta = delta % 365
        year = (4 * year_4) + single_years + 1 # while there is a year 0, Ethiopians still reckon Jesus was born in the year 1
        if year % 4 == 0:
            # leap year
            m = months.ETHIOPIAN_MONTHS_LEAP
        else:
            # not a leap year
            m = months.ETHIOPIAN_MONTHS_NORMAL
        if delta == 0:
            delta = 365
            year -= 1
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    else:
        # negative date
        delta = 1724222 - jday

        while delta > 0:
            if year % 4 == 0:
                year += 1
                delta -= 366
            else:
                year += 1
                delta -= 365

        if (year %4) == 0:
            # leap year
            m = months.ETHIOPIAN_MONTHS_LEAP
        else:
            # not a leap year
            m = months.ETHIOPIAN_MONTHS_NORMAL

        year = 0 - year
        delta = 0 - delta + 1

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = [day, month, year]
    return(date)

def egyptian(jday):
    """Convert a Julian Day to a date in the Egyptian calendar."""
    jday = int(jday)
    m = months.EGYPTIAN_MONTHS
    year = 0
    month = ""
    day = 0

    if jday > 160331:
        # positive year
        delta = jday - 160331
        year = (delta // 365) + 1 # if delta is positive, year > 1 even if less than one full year has passed since day 0
        delta %= 365
        if delta == 0:
            delta = 365
            year -= 1
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]
    else:
        # negative year
        delta = 160332 - jday

        while delta > 0:
            year -= 1
            delta -= 365

        delta = 0 - delta + 1
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = [day, month, year]
    return date

def armenian(jday):
    """Convert a Julian Day to a date in the Armenian calendar"""
    jday = int(jday)
    day = 0
    month = ""
    year = 0
    m = months.ARMENIAN_MONTHS

    if jday > 1922866:
        # positive year
        delta = jday - 1922866
        year = (delta // 365) + 1 # add 1 to account for the lack of year 0
        delta %= 365
        if delta == 0:
            delta = 365
            year -= 1
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]
    else:
        # negative year
        delta = 1922867 - jday
        while delta > 0:
            year -= 1
            delta -= 365

        delta = 0 - delta + 1
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]
                
    date = [day, month, year]
    return date

def lunar_hijri(jday):
    """Convert a Julian Day to a date in the Lunar Hijri calendar."""
    jday = int(jday)
    day = 0
    month = ""
    year = 0
    single_year = 0
    leap_years_ah = (2, 5, 7, 10, 13, 16, 18, 21, 24, 26, 29)
    leap_years_bh = (2, 5, 7, 10, 13, 15, 18, 21, 24, 26, 29)
    leap_years_zero = (1, 4, 6, 9, 12, 14, 17, 20, 23, 25, 28)

    if jday > 1948438:
        # positive year
        delta = jday - 1948438
        cycles = delta // cycle30
        delta = delta % cycle30
        m = None
        for y in range(1, 31):
            if y in leap_years_ah:
                if delta <= 355:
                    # leap year
                    m = months.ARAB_MONTHS_LEAP
                    single_year = y
                    break
                else:
                    delta -= 355
            else:
                if delta <= 354:
                    # not a leap year
                    m = months.ARAB_MONTHS_NORMAL
                    single_year = y
                    break
                else:
                    delta -= 354
        year = (cycles * 30) + single_year
        if delta == 0:
            delta = 354
            year -= 1
            
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]
    else:
        # negative year
        delta = 1948439 - jday
        while delta > 0:
            if (year % 30) in leap_years_zero:
                year += 1
                delta -= 355
            else:
                year += 1
                delta -= 354
            
        if (year % 30) in leap_years_bh:
            # leap year
            m = months.ARAB_MONTHS_LEAP
        else:
            m = months.ARAB_MONTHS_NORMAL
                
        year = 0 - year
        delta = 0 - delta + 1
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = (day, month, year)
    return date
                    


def solar_hijri(jday):
    """Convert a Julian Day to a date in the Solar Hijri calendar."""
    jday = int(jday)
    day = 0
    month = ""
    year = 0

    leap_years_ah = (5,9,13,17,21,25,29,33)
    leap_years_zero = (0,4,8,12,16,20,24,28)
    leap_years_bh = (1,5,9,13,17,21,25,29)

    if jday > 1948319:
        # positive date
        delta = jday - 1948319
        cycles = delta // cycle33
        delta %= cycle33
        for y in range(1,34):
            if y in leap_years_ah:
                if delta <= 366:
                    # leap year
                    single_years = y
                    m = months.SOLAR_HIJRI_MONTHS_LEAP
                    break
                else:
                    delta -= 366
            else:
                if delta <= 365:
                    # not a leap year
                    single_years = y
                    m = months.SOLAR_HIJRI_MONTHS_NORMAL
                    break
                else:
                    delta -= 365
        year = (33 * cycles) + single_years
        if delta == 0:
            delta = 365
            year -= 1
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]
    else:
        # negative date
        delta = 1948320 - jday

        while delta > 0:
            if (year % 33) in leap_years_zero:
                year += 1
                delta -= 366
            else:
                year += 1
                delta -= 365

        if year in leap_years_bh:
            # leap year
            m = months.SOLAR_HIJRI_MONTHS_LEAP
        else:
            # not a leap year
            m = months.SOLAR_HIJRI_MONTHS_NORMAL

        year = 0 - year
        delta = 0 - delta + 1
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]
    date = (day,month,year)
    return date

def birashk(jday):
    jday = int(jday)
    day = 0
    month = ""
    year = 0
    delta = jday - 1948319 # days that have passed, starting on 1/1/1

    # I tried to be smart anc calculate by cycles and subcycles, but Python apparently gets confused when you go too many levels deep in if..else statements, so screw it I'm just going to use one big 2820-year cycle.

    if delta > 0:
        great_cycles = delta // cycle2820
        delta %= cycle2820

        for y in range(1,2821):
            if y in leap_years_birashk.ah:
                if delta <= 366:
                    # leap year
                    single_year = y
                    m = months.SOLAR_HIJRI_MONTHS_LEAP
                    break
                else:
                    delta -= 366
            else:
                if delta <= 365:
                    # not a leap year
                    single_year = y
                    m = months.SOLAR_HIJRI_MONTHS_NORMAL
                    break
                else:
                    delta -= 365

        year = (great_cycles * 2820) + single_year
        if delta == 0:
            delta = 365
            year -= 1
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    else:
        delta = 0 - delta # module operator doesn't place nicely with negative numbers
        great_cycles = delta // cycle2820
        delta %= cycle2820

        for y in range(0,2820):
            if y in leap_years_birashk.bh:
                if delta <= 366:
                    # leap year
                    single_year = y
                    m = months.SOLAR_HIJRI_MONTHS_LEAP
                    delta = 366 - delta
                    if delta == 0:
                        delta = 1
                    break
                else:
                    delta -= 366
            else:
                if delta <= 365:
                    # not a leap year
                    single_year = y
                    m = months.SOLAR_HIJRI_MONTHS_NORMAL
                    delta = 366 - delta
                    break
                else:
                    delta -= 365

        year = (great_cycles * 2820) + single_year
        year = 0 - year - 1

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = [day,month,year]
    return date

def assyrian(jday):
    """Convert a Julian Day to a date in the Assyrian calendar."""
    jday = int(jday)
    day = 0
    month = ""
    year = 0
    leap = None

    if jday > -13388:
        # positive year
        delta = jday - -13388
        cycles = delta // cycle400
        delta %= cycle400


        for y in range(1,401):
            if y in leap_years_assyrian.PD:
                if delta <= 366:
                    m = months.ASSYRIAN_MONTHS_LEAP
                    single_year = y
                    break
                else:
                    delta -= 366
            else:
                if delta <= 365:
                    m = months.ASSYRIAN_MONTHS_NORMAL
                    single_year = y
                    break
                else:
                    delta -= 365

        year = (400 * cycles) + single_year
        if delta == 0:
            year -= 1
            if year in leap_years_assyrian.PD:
                m = months.ASSYRIAN_MONTHS_LEAP
                delta = 366
            else:
                m = months.ASSYRIAN_MONTHS_NORMAL
                delta = 365
                
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]
    else:
        # negative date
        delta = -13387 - jday

        while delta > 0:
            if (year % 400) in leap_years_assyrian.ZO:
                year += 1
                delta -= 366
            else:
                year += 1
                delta -= 365

        if (year % 400) in leap_years_assyrian.AD:
            m = months.ASSYRIAN_MONTHS_LEAP
        else:
            m = months.ASSYRIAN_MONTHS_NORMAL

        year = 0 - year
        delta = 0 - delta

        if delta == 0:
            year -= 1
            if (year % 400) in leap_years_assyrian.AD:
                m = months.ASSYRIAN_MONTHS_LEAP
                delta = 366
            else:
                m = months.ASSYRIAN_MONTHS_NORMAL
                delta = 365

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = (day,month,year)
    return date
        


def babylonian(jday):
    """Convert a Julian Day to a date in the Babylonian calendar."""
    jday = int(jday)
    day = 0
    month = ""
    year = 0
    leap_years_pd = (3,6,8,11,14,17,19,0)
    leap_years_ad = (1,3,6,9,12,14,17)
    leap_years_zo = (0,2,5,8,11,13,16)

    # Years 17 PD, 3 AD, and 2 ZO are the ones where Veululu and not Veadar is the leap month

    if jday > -210488: #-210264:
        # positive year
        delta = jday - -210488 #-210264
        cycles = delta // cycle19
        delta %= cycle19

        for y in range (1,20):
            if y == 17:
                if delta <= 383:
                    m = months.BABYLONIAN_MONTHS_LEAP_17
                    single_year = y
                    break
                else:
                    delta -= 383
            elif y in leap_years_pd:
                if delta <= 383:
                    # leap year
                    m = months.BABYLONIAN_MONTHS_LEAP
                    single_year = y
                    break
                else:
                    delta -= 383
            else:
                if delta <= 354:
                    # not a leap year
                    m = months.BABYLONIAN_MONTHS_NORMAL
                    single_year = y
                    break
                else:
                    delta -= 354

        year = (19 * cycles) + single_year
        if delta == 0:
            year -= 1
            if (year % 19) == 17:
                delta = 383
                m = months.BABYLONIAN_MONTHS_LEAP_17
            elif (year % 19) in leap_years_pd:
                m = months.BABYLONIAN_MONTHS_LEAP
                delta = 383
            else:
                m = months.BABYLONIAN_MONTHS_NORMAL
                delta = 353

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]
                

    else:
        #delta = -210263 - jday
        delta = -210487 - jday
        while delta > 0:
            if (year % 19) in leap_years_zo:
                year += 1
                delta -= 383
            else:
                year += 1
                delta -= 354

        if (year % 19) in leap_years_ad:
            # leap year
            m = months.BABYLONIAN_MONTHS_LEAP
        else:
            # not a leap year
            m = months.BABYLONIAN_MONTHS_NORMAL

        year = 0 - year
        delta = 0 - delta
        if delta == 0:
            year -= 1
            if (year % 19) == 2:
                m = months.BABYLONIAN_MONTHS_LEAP_17
                delta = 383
            elif (year % 19) in leap_years_ad:
                m = months.BABYLONIAN_MONTHS_LEAP
                delta = 383
            else:
                m = months.BABYLONIAN_MONTHS_NORMAL
                delta = 354
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = (day,month,year)
    return date

def hebrew(jday):
    """Convert a Julian Day to a day in the Hebrew calendar."""
    leap_years_am = (3,6,8,11,14,17,19,0)
    leap_years_bc = (1,3,6,9,12,14,17)
    leap_years_zo = (0,2,5,8,11,13,16)
    monlen = 29 + Fraction(12,24) + Fraction(793, (24 * 1080))
    yearlen12 = 12 * monlen
    yearlen13 = 13 * monlen
    cycle19 = 235 * monlen
    molad_tohu = Fraction(5,24) + Fraction(204,(24 * 1080))

    jday = int(jday)
    day = 0
    month = ""
    year = 0

    yeartype = {353:months.HEBREW_MONTHS_DEFICIENT_NORMAL,
                354:months.HEBREW_MONTHS_REGULAR_NORMAL,
                355:months.HEBREW_MONTHS_ABUNDANT_NORMAL,
                383:months.HEBREW_MONTHS_DEFICIENT_LEAP,
                384:months.HEBREW_MONTHS_REGULAR_LEAP,
                385:months.HEBREW_MONTHS_ABUNDANT_LEAP}

    if jday > 347996:
        # positive dates
        numbers = hebrew_calculations.calc(jday)
        rosh = numbers[0]  # Julian Day of the molad of Tishri
        mrosh = rosh
        molad = numbers[1] # moment of the molad of Tishri
        year = numbers[2]  # number of the current year
        if (year % 19) in leap_years_am: # Is it a leap year?
            leap = True
        else:
            leap = False

        # Now we have to do the same for last year and next year
        iday = rosh - 50 # last year
        kday = rosh + 390 # next year

        prev_numbers = hebrew_calculations.calc(iday)
        prev_rosh = prev_numbers[0]
        prev_mrosh = prev_rosh
        prev_molad = prev_numbers[1]
        prev_year = year - 1
        
        next_numbers = hebrew_calculations.calc(kday)
        next_rosh = next_numbers[0]
        next_mrosh = next_rosh
        next_molad = next_numbers[1]
        next_year = year + 1

        r1 = False # check if R1 has applied. If R1 == False, do not apply rules 3 or 4.
        prev_r1 = False
        next_r1 = False

        # Rule 1: If the molad of Tishri for year n falls after noon, subtract 1 day from Kislev in year n
        # and add 1 day to Marcheshvan in year (n - 1)

        if molad > Fraction(3,4):
            rosh += 1
            r1 = True

        if next_molad > Fraction(3,4):
            next_rosh += 1
            next_r1 = True

        # Rule 2: If the molad of Tishri in year n falls on a "Tuesday", after 9 hours 204 chalakim, and year n
        # is NOT a leap year, postpone Rosh Hashana. To accomplish this, subtract 1 day from Kislev in year n
        # and add 1 day to Marcheshvan in year (n - 1)

        if r1 == False:
            if (year % 19) not in leap_years_am:
                if (mrosh % 7) == 0: # "Tuesday"
                    if molad >= Fraction(9,24) + Fraction(204,(24 * 1080)): # 9 hours 204 chalakim
                        rosh += 1

        if next_r1 == False:
            if (next_year % 19) not in leap_years_am:
                if (next_mrosh % 7) == 0: # "Tuesday"
                    if next_molad >= Fraction(9,24) + Fraction(204,(24 * 1080)): # 9 hours 204 chalakim
                        next_rosh += 1

        # Rule 3: If year n comes AFTER a leap year, and the molad of Tishri falls on a "Monday" on or after
        # 15 hours 589 chalakim, Rosh Hashana is postponed. This is accomplished by subtracting 1 day from
        # Kislev in year n and adding 1 day to Marcheshvan in year (n - 1)

        if r1 == False:
            if (prev_year % 19) in leap_years_am:
                if (mrosh % 7) == 6: # "Monday"
                    if molad >= Fraction(15,24) + Fraction(589,(24 * 1080)): # 15 hours 589 chalakim
                        rosh += 1

        if next_r1 == False:
            if (year % 19) in leap_years_am:
                if (next_mrosh % 7) == 6: # "Monday"
                    if next_molad >= Fraction(15,24) + Fraction(589,(24 * 1080)): # 15 hours 589 chalakim
                        next_rosh += 1

        # Rule 4: If Rosh Hashanah in year n falls on a "Sunday", "Wednesday", or "Friday", it is postponed.
        # To accomplish this, subtract 1 day from Kislev in year n and add 1 day to Marcheshvan in year (n - 1)

        if (rosh % 7) in (1,3,5): # "Wednesday", "Friday", "Sunday"
            rosh += 1

        if (next_rosh % 7) in (1,3,5):
            next_rosh += 1

        delta = jday - rosh + 1

        m = yeartype[next_rosh - rosh]
        if delta <= 0:
            year -= 1
            month = "Elul"
            day = 29 + delta
        else:
            for i in m.keys():
                if delta <= m[i]:
                    month = i
                    day = delta
                    break
                else:
                    delta -= m[i]

    else:
        # negative dates
        numbers = hebrew_calculations.calc(jday)
        rosh = numbers[0]  # Julian Day on which the molad of Tishri falls
        mrosh = rosh
        molad = numbers[1] # moment of the molad of Tishri
        year = numbers[2]  # number of the current year
        r1 = False



        # looking good so far. now do it for next year
        kday = rosh + 390 # next year
        next_numbers = hebrew_calculations.calc(kday)
        next_rosh = next_numbers[0]
        next_mrosh = next_rosh
        next_molad = next_numbers[1]
        next_year = year - 1 # year is positive, so next_year is 1 less
        if next_year == 0:
            next_year = 1
        next_r1 = False



        # Rule 1: If the molad of Tishri falls after noon, postpone Rosh Hashanah
        if abs(molad) > Fraction(3,4): # noon falls 3/4 of the way through a standard Hebrew day
            rosh += 1
            r1 = True

        if abs(next_molad) > Fraction(3,4): # noon falls 3/4 of the way through a standard Hebrew day
            next_rosh += 1
            next_r1 = True


        # Rule 2: If the molad of Tishri falls on a "Tuesday" after 9 hours 204 chalakim
        # and it's NOT a leap year, postpone Rosh Hashanah. This rule is only invoked if rule 1 has not been.
        if r1 == False:
            if (abs(year) % 19) not in leap_years_bc:
                if (mrosh % 7) == 0: # "Tuesday". This applies to both positive and negative Julian Days
                    if molad >= Fraction(9,24) + Fraction(204,25920): # 9 hours 204 chalakim
                        rosh += 1

        if next_r1 == False:
            if (abs(next_year) % 19) not in leap_years_bc:
                if (next_mrosh % 7) == 0: # "Tuesday"
                    if next_molad >= Fraction(9,24) + Fraction(204,25920): # 9 hours 204 chalakim
                        next_rosh += 1


        # Rule 3: If it's the year AFTER a leap year, and the molad of Tishri falls on a "Monday" on or after
        # 15 hours 589 chalakim, postpone Rosh Hashanah. Again, this rule is only invoked if rule 1 has not been.

        if r1 == False:
            if ((year + 1) % 19) in leap_years_bc: # year is still positive, so add 1 to get the previous year
                if mrosh > 0: # mrosh might be negative, so we need to account for that.
                    if (mrosh % 7) == 6: # "Monday"
                        if molad >= Fraction(15,24) + Fraction(589,25920): # 15 hours 589 chalakim
                            rosh += 1
                else:
                    if (abs(mrosh) % 7) == 1: # "Monday"
                        if abs(molad) >= Fraction(15,24) + Fraction(589,25920): # 15 hours 589 chalakim
                            rosh += 1

        if next_r1 == False:
            if (year % 19) in leap_years_bc:
                if next_mrosh > 0: # next_mrosh might be negative, so we need to account for that
                    if (next_mrosh % 7) == 6: # "Monday"
                        if next_molad >= Fraction(15,24) + Fraction(589,25920): # 15 hours 589 chalakim
                            next_rosh += 1
                else:
                    if (abs(next_mrosh) % 7) == 6: # "Monday"
                        if abs(next_molad) >= Fraction(15,24) + Fraction(589,25920): # 15 hours 589 chalakim
                            next_rosh += 1


        # Rule 4: If Rosh Hashanah would fall on a "Sunday", "Wednesday", or "Friday", it is postponed

        if rosh > 0:
            if (rosh % 7) in (1,3,5): # "Wednesday", "Friday", "Sunday"
                rosh += 1
        else:
            if (abs(rosh) % 7) in (2,4,6): # "Sunday", "Friday", "Wednesday"
                rosh += 1

        if next_rosh > 0:
            if (next_rosh % 7) in (1,3,5): # "Wednesday", "Friday", "Sunday"
                next_rosh += 1
        else:
            if (abs(next_rosh) % 7) in (2,4,6): # "Sunday", "Friday", "Wednesday"
                next_rosh += 1

        delta = jday - rosh + 1
        year = 0 - year
        m = yeartype[next_rosh - rosh]

        if delta <= 0:
            year -= 1
            month = "Elul"
            day = 29 + delta
        elif jday == next_rosh:
            day = 1
            month = "Tishrei"
            year += 1
        else:
            for i in m.keys():
                if delta <= m[i]:
                    month = i
                    day = delta
                    break
                else:
                    delta -= m[i]

    date = (day,month,year)
    return date

def samaritan(jday):
    """Convert a Julian Day to a date in the Samaritan calendar."""
    leap_years_ai = (3,6,8,11,14,17,19,0)
    leap_years_bi = (1,3,6,9,12,14,17)
    leap_years_zo = (0,2,5,8,11,13,16)
    monlen = 29 + Fraction(12,24) + Fraction(793, (24 * 1080))
    yearlen12 = 12 * monlen
    yearlen13 = 13 * monlen
    cycle19 = 235 * monlen
    #molad0 = Fraction(2,24) + Fraction(655,25920)
    #molad0 = Fraction(17,24) + Fraction(859,25920)
    molad0 = Fraction(11,24) + Fraction(451,25920)

    jday = int(jday)
    day = 0
    month = ""
    year = 0

    if jday > 1122908:
        # positive dates
        delta = jday - 1122908

        # First count 19-year cycles
        while delta > cycle19:
            year += 19
            delta -= cycle19

        # whole years
        for y in range(0, 19):
            y += 1
            if y in leap_years_ai:
                if delta <= yearlen13:
                    year += y
                    break
                else:
                    delta -= yearlen13
            else:
                if delta <= yearlen12:
                    year += y
                    break
                else:
                    delta -= yearlen12

        # delta now gives the exact position in the current year.
        delta = int(delta)
        if delta == 0:
            year -= 1
            if (year % 19) in leap_years_ai:
                delta = 384
            else:
                delta = 354
                
        if (year % 19) in leap_years_ai:
            m = months.SAMARITAN_MONTHS_LEAP
        else:
            m = months.SAMARITAN_MONTHS_NORMAL

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    else:
        # negative years
        delta = 1122909 - jday
        flag = False

        while flag == False:
            year -= 1
            if (abs(year) % 19) in leap_years_bi:
                if delta <= yearlen13:
                    flag = True
                else:
                    delta -= yearlen13
            else:
                if delta <= yearlen12:
                    flag = True
                else:
                    delta -= yearlen12

        # year now gives us the current year year and delta the exact position within that year.
        delta = int(delta)
        if delta == 0:
            year -= 1
#            if (abs(year) % 19) in leap_years_bi:
 #               delta = 384
  #          else:
   #             delta = 354
                
        if (abs(year) % 19) in leap_years_bi:
            m = months.SAMARITAN_MONTHS_LEAP
            delta = 384 - delta
        else:
            m = months.SAMARITAN_MONTHS_NORMAL
            delta = 354 - delta

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = (day,month,year)
    return date

def kurdish(jday):
    """Convert a Julian Day into a date in the Kurdish calendar."""
    jday = int(jday)
    day = 0
    month = 0
    year = 0

    leap_years_an = (2,6,10,14,18,23,27,31)
    leap_years_bn = (3,7,11,16,20,24,28,32)
    leap_years_zo = (2,6,10,15,19,23,27,31)

    if jday > 1497975:
        # positive date
        delta = jday - 1497975
        cycles = delta // cycle33
        delta %= cycle33
        for y in range(1,34):
            if y in leap_years_an:
                if delta <= 366:
                    # leap year
                    single_years = y
                    m = months.KURDISH_MONTHS_LEAP
                    break
                else:
                    delta -= 366
            else:
                if delta <= 365:
                    # not a leap year
                    single_years = y
                    m = months.KURDISH_MONTHS_NORMAL
                    break
                else:
                    delta -= 365

        year = (33 * cycles) + single_years
        if delta == 0:
            year -= 1
            if (year % 19) in leap_years_an:
                delta = 366
                m = months.KURDISH_MONTHS_LEAP
            else:
                delta = 365
                m = months.KURDISH_MONTHS_NORMAL
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    else:
        # negative dates
        delta = 1497976 - jday
        while delta > 0:
            if (abs(year) % 33) in leap_years_zo:
                year -= 1
                delta -= 366
            else:
                year -= 1
                delta -= 365

        if (abs(year) % 19) in leap_years_bn:
            # leap year
            m = months.KURDISH_MONTHS_LEAP
        else:
            # not a leap year
            m = months.KURDISH_MONTHS_NORMAL

        delta = abs(delta) + 1
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = (day,month,year)
    return date

def amazigh(jday):
    """Convert a Julian day to a date in the Amazigh calendar."""
    jday = int(jday)
    year = 0
    month = ""
    day = 0

    if jday > 1374434:
        # positive dates
        delta = jday - 1374434
        current = False
        while current == False:
            year += 1
            if (year + 2) % 4 == 0:
                if delta <= 366:
                    current = True
                else:
                    delta -= 366
            else:
                if delta <= 365:
                    current = True
                else:
                    delta -= 365

        if (year + 2) % 4 == 0:
            # leap year
            m = months.AMAZIGH_MONTHS_LEAP
        else:
            # not a leap year
            m = months.AMAZIGH_MONTHS_NORMAL
            
#        if delta == 0:
 #           delta = 365
  #          year -= 1

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    else:
        # negative dates
        delta = 1374435 - jday
        while delta > 0:
            if (year - 2) % 4 == 0:
                year -= 1
                delta -= 366
            else:
                year -= 1
                delta -= 365

        delta = abs(delta) + 1

        if (abs(year) - 2) % 4 == 0:
            # leap yar
            m = months.AMAZIGH_MONTHS_LEAP
        else:
            # not a leap year
            m = months.AMAZIGH_MONTHS_NORMAL

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = (day,month,year)
    return date

def rumi(jday):
    """Convert a Julian day to a date in the Rumi calendar."""
    jday = int(jday)
    year = 0
    month = ""
    day = 0

    if jday > 1948242:
        # positive dates
        delta = jday - 1948242
        current = False
        while current == False:
            year += 1
            if (year + 2) % 4 == 0:
                if delta <= 366:
                    current = True
                else:
                    delta -= 366
            else:
                if delta <= 365:
                    current = True
                else:
                    delta -= 365

        if (year + 2) % 4 == 0:
            # leap year
            m = months.TURKISH_MONTHS_LEAP
        else:
            # not a leap year
            m = months.TURKISH_MONTHS_NORMAL

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    else:
        # negative dates
        delta = 1948243 - jday
        while delta > 0:
            if (abs(year) - 2) % 4 == 0:
                year -= 1
                delta -= 366
            else:
                year -= 1
                delta -= 365

        delta = abs(delta) + 1

        if (abs(year) % 4) == 0:
            # leap year
            m = months.TURKISH_MONTHS_LEAP
        else:
            # not a leap year
            m = months.TURKISH_MONTHS_NORMAL

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = (day,month,year)
    return date

def rev_gregorian(jday):
    """Convert a Julian Day to a date in the Gregorian calendar"""
    jday = int(jday)
    year = 0
    month = ""
    day = 0

    if jday > 1721424:
        # positive date
        delta = jday - 1721424
        year_4000 = delta // cycle4000
        delta %= cycle4000
        year_400 = delta // cycle400
        delta %= cycle400
        year_100 = delta // cycle100
        delta %= cycle100
        year_4 = delta // cycle4
        delta %= cycle4
        single_years = delta // 365
        delta %= 365
        year = (4000 * year_4000) + (400 * year_400) + (100 * year_100) + (4 * year_4) + single_years + 1 # add 1 to account for lack ofyear 0
        if year % 4000 == 0:
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL
        elif year % 400 == 0:
            # leap year
            m = months.CAESAR_MONTHS_LEAP
        elif year % 100 == 0:
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL
        elif year % 4 == 0:
            # leap year
            m = months.CAESAR_MONTHS_LEAP
        else:
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL

        if delta == 0:
            delta = 365
            year -= 1

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    else:
        # negative dates
        delta = 1721425 - jday

        while delta > 0:
            if year % 4000 == 0:
                delta -= 365
            elif year % 400 == 0:
                delta -= 366
            elif year % 100 == 0:
                delta -= 365
            elif year % 4 == 0:
                delta -= 366
            else:
                delta -= 365
            year += 1

        if (year - 1) % 4000 == 0:
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL
        elif (year - 1) % 400 == 0:
            # leap year
            m = months.CAESAR_MONTHS_LEAP
        elif (year - 1) % 100 == 0:
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL
        elif (year - 1) % 4 == 0:
            # leap year
            m = months.CAESAR_MONTHS_LEAP
        else:
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL

        year = 0 - year
        delta = 0 - delta + 1

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = (day,month,year)
    return date

def parker(jday):
    """Convert a Julian day to a date in the Parker calendar."""
    jday = int(jday)
    year = 0
    month = ""
    day = 0

    if jday > 1721424:
        # positive date
        delta = jday - 1721424
        current = False

        while current == False:
            year += 1
            if (year % 10000) in (2800, 5600, 8400):
                if delta <= 365:
                    current = True
                else:
                    delta -= 365
            elif year % 400 == 0:
                if delta <= 366:
                    current = True
                else:
                    delta -= 366
            elif year % 100 == 0:
                if delta <= 365:
                    current = True
                else:
                    delta -= 365
            elif year % 4 == 0:
                if delta <= 366:
                    current = True
                else:
                    delta -= 366
            else:
                if delta <= 365:
                    current = True
                else:
                    delta -= 365

        if (year % 10000) in (2800,5600,8400):
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL
        elif year % 400 == 0:
            # leap year
            m = months.CAESAR_MONTHS_LEAP
        elif year % 100 == 0:
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL
        elif year % 4 == 0:
            # leap year
            m = months.CAESAR_MONTHS_LEAP
        else:
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    else:
        # negative dates
        delta = 1721425 - jday

        while delta > 0:
            if (year % 10000) in (2800, 5600, 8400):
                delta -= 365
            elif year % 400 == 0:
                delta -= 366
            elif year % 100 == 0:
                delta -= 365
            elif year % 4 == 0:
                delta -= 366
            else:
                delta -= 365
            year += 1

        if (year - 1) % 10000 in (2800,5600,8400):
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL
        elif (year - 1) % 400 == 0:
            # leap year
            m = months.CAESAR_MONTHS_LEAP
        elif (year - 1) % 100 == 0:
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL
        elif (year - 1) % 4 == 0:
            # leap year
            m = months.CAESAR_MONTHS_LEAP
        else:
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL

        year = 0 - year
        delta = 0 - delta + 1

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = (day, month, year)
    return date

def goucher(jday):
    """Convert a Julian day to a date in the Goucher-Parker calendar."""
    jday = int(jday)
    year = 0
    month = ""
    day = 0

    if jday > 1721422:
        # positive date
        delta = jday - 1721422
        year_128 = delta // cycle128j
        delta %= cycle128j
        year_4 = delta // cycle4
        delta %= cycle4
        single_years = delta // 365
        delta %= 365
        year = (128 * year_128) + (4 * year_4) + single_years + 1 # need to add 1 to account for the lack of year 0
        if year % 128 == 0:
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL
        elif year % 4 == 0:
            # leap year
            m = months.CAESAR_MONTHS_LEAP
        else:
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    else:
        # negative date
        delta = 1721423 - jday
        while delta > 0:
            if year % 128 == 0:
                delta -= 365
            elif year % 4 == 0:
                delta -= 366
            else:
                delta -= 365
            year += 1

        if (year - 1) % 128 == 0:
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL
        elif (year - 1) % 4 == 0:
            # leap year
            m = months.CAESAR_MONTHS_LEAP
        else:
            # not a leap yer
            m = months.CAESAR_MONTHS_NORMAL

        year = 0 - year
        delta = 0 - delta + 1
        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = (day,month,year)
    return date

def serbian_church(jday):
    """Convert a Julian day to a date in the Serbian church calendar."""
    jday = int(jday)
    day = 0
    month = ""
    year = 0

    if jday> 1721424:
        # positive date
        delta = jday - 1721424
        current = False
        while current == False:
            year += 1
            if (year % 900) in (0, 400):
                if delta <= 366:
                    current = True
                else:
                    delta -= 366
            elif year % 100 == 0:
                if delta <= 365:
                    current = True
                else:
                    delta -= 365
            elif year % 4 == 0:
                if delta <= 366:
                    current = True
                else:
                    delta -= 366
            else:
                if delta <= 365:
                    current = True
                else:
                    delta -= 365

        if (year % 900) in (0,400):
            # leap year
            m = months.CAESAR_MONTHS_LEAP
        elif year % 100 == 0:
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL
        elif year % 4 == 0:
            # leap year
            m = months.CAESAR_MONTHS_LEAP
        else:
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    else:
        # negative dates
        delta = 1721425 - jday

        while delta > 0:
            if (year % 900) in (0, 400):
                delta -= 366
            elif year % 100 == 0:
                delta -= 365
            elif year % 4 == 0:
                delta -= 366
            else:
                delta -= 365
            year += 1

        if ((year - 1) % 900) in (0, 400):
            # leap year
            m = months.CAESAR_MONTHS_LEAP
        elif (year - 1) % 100 == 0:
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL
        elif (year - 1) % 4 == 0:
            # leap year
            m = months.CAESAR_MONTHS_LEAP
        else:
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL

        year = 0 - year
        delta = 0 - delta + 1

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = (day, month, year)
    return date




def rev_julian(jday):
    """Convert a Julian day to a date in the revised Julian calendar."""
    jday = int(jday)
    day = 0
    month = ""
    year = 0

    if jday > 1721424:
        # positive date
        delta = jday - 1721424
        current = False
        while current == False:
            year += 1
            if (year % 900) in (200,600):
                if delta <= 366:
                    current = True
                else:
                    delta -= 366
            elif year % 100 == 0:
                if delta <= 365:
                    current = True
                else:
                    delta -= 365
            elif year % 4 == 0:
                if delta <= 366:
                    current = True
                else:
                    delta -= 366
            else:
                if delta <= 365:
                    current = True
                else:
                    delta -= 365
                    
        if (year % 900) in (200,600):
            # leap year
            m = months.CAESAR_MONTHS_LEAP
        elif year % 100 == 0:
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL
        elif year % 4 == 0:
            # leap year
            m = months.CAESAR_MONTHS_LEAP
        else:
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    else:
        # negative dates
        delta = 1721425 - jday

        while delta > 0:
            if (year % 900) in (200, 600):
                delta -= 366
            elif year % 100 == 0:
                delta -= 365
            elif year % 4 == 0:
                delta -= 366
            else:
                delta -= 365
            year += 1


        if ((year - 1) % 900) in (200,600):
            # leap year
            m = months.CAESAR_MONTHS_LEAP
        elif (year - 1) % 100 == 0:
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL
        elif (year - 1) % 4 == 0:
            # leap year
            m = months.CAESAR_MONTHS_LEAP
        else:
            # not a leap year
            m = months.CAESAR_MONTHS_NORMAL

        year = 0 - year
        delta = 0 - delta + 1

        for i in m.keys():
            if delta <= m[i]:
                month = i
                day = delta
                break
            else:
                delta -= m[i]

    date = (day, month, year)
    return date
