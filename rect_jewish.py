#!/usr/bin/python3

# Convert between Julian Days and Irv Bromborg's rectified Jewish calendar

from math import floor
from fractions import Fraction
from months import HEBREW as MONTHS, JEWISH_LENGTHS as MONTH_LENGTHS

# Dr. Bromborg's web page gives two different values for the molad tohu and the synodic month (which he refers to as the molad interval). The commented-out values here are those which he computed were correct at the epoch.
# However, I believe his algorithms use the traditional values of the synodic month and molad tohu, and subsequently apply and adjustment to get the computed true instant of the molad of Tishrei.
#syn_month = 29 + Fraction(48353482985, 91128068928) # synodic month as of the molad tohu. this gets gradually shorter as one moves into the future, and longer into the past
#molad_tohu = 347998 - Fraction(5,24) + Fraction(204,25920) - Fraction(14, 1440)

syn_month = 29 + Fraction(12,24) + Fraction(793, (24 * 1080)) # traditional mean synodic month length
cycle353 = 4366 * syn_month # 4366 months in 353 years. this value will also shorten after molad tohu and increase before it
molad_tohu = 347998 + Fraction(5,24) + Fraction(204,25920)

def leap(year):
    '''Returns the number of months in a year'''
    if ( ((130 * int(year)) + 269) % 353 < 130):
        # leap year
        ans = 13
    else:
        ans = 12

    return ans

def molad_adjustment(months_elapsed):
    '''Compute how much to adjust the molad of a given synodic month'''
    ans = (((int(months_elapsed) - 50834) ** 2) * Fraction(1, 6328338120)) + Fraction(26, 1440)
    return ans
    

def rosh_molad(year):
    '''Compute the molad of Tishrei for a given year'''
    year = int(year)

    cycles = (year - 1) // 353
    y = (cycles * 353) + 1
    months_elapsed = 4366 * cycles
    while (y < year):
        months_elapsed += leap(y)
        y += 1

    molad = molad_tohu + (syn_month * months_elapsed) - molad_adjustment(months_elapsed) # instant of true new moon

    return molad

def rosh_hashanah(year):
    '''Compute the Julian Day of Rosh Hashanah for a given year, and the length of the year'''
    year = int(year)

    # Adding ¼ accounts for dechiyot 1
    rosh = rosh_molad(year) + Fraction(1,4)
    next_rosh = rosh_molad(year + 1) + Fraction(1,4)
    prev_rosh = rosh_molad(year - 1) + Fraction(1,4)

    # Now apply the other dechiyot

    # Rule 4: If rosh of this year falls on a Monday, and prev_rosh fell on a Wednesday in a leap year, postpone Rosh Hashanah by 1 day
    if ( (floor(rosh) % 7 == 0) and (floor(prev_rosh) % 7 == 2) and (leap(year - 1) == 13) ):
        rosh += 1
    if ( (floor(next_rosh) % 7 == 0) and (floor(rosh) % 7 == 2) and (leap(year) == 13) ):
        next_rosh += 1

    # Rule 3: In a normal year, if rosh falls on a Tuesday and next_rosh will be on a Sunday, postpone Rosh Hashanah by 1 day
    if ( (leap(year) == 12) and (floor(rosh) % 7 == 1) and (floor(next_rosh) % 7 == 6) ):
        rosh += 1
    if ( (leap(year + 1) == 12) and (floor(next_rosh) % 7 == 1) and floor(rosh_molad(year + 2) + Fraction(1,4)) % 7 == 6):
        next_rosh += 1

    # Rule 2: Rosh Hashanah can't fall on a Wednesday, Friday, or Sunday
    if (floor(rosh) % 7 in (2, 4, 6)):
        rosh += 1
    if (floor(next_rosh) % 7 in (2, 4, 6)):
        next_rosh += 1

    length = floor(next_rosh) - floor(rosh)

    return (floor(rosh), length)

def tojd(day, month, year):
    '''Convert a date in the rectified Jewish calendar to a Julian Day'''
    day = int(day) - 1 # subtract 1 because humans don't count from 0
    month = str(month)
    year = int(year)

    # account for the year
    rosh = rosh_hashanah(year)
    jday = rosh[0]

    # account for the month
    m = 0
    if ((month == "Veadar") and (rosh[1] < 383)):
        month = "Adar"
    while (MONTHS[m] != month):
        jday += MONTH_LENGTHS[rosh[1]][m]
        m += 1

    # account for the day
    jday += day

    return jday

def fromjd(jday):
    '''Convert a Julian Day into a date in the rectified Jewish calendar'''
    jday = int(jday)

    # compute the year
    cycles = (jday - molad_tohu) // cycle353
    year = (cycles * 353) + 1
    while (rosh_hashanah(year + 353)[0] <= jday):
        year += 353
    while (rosh_hashanah(year + 1)[0] <= jday):
        year += 1
    while (rosh_hashanah(year)[0] > jday):
        year -= 1

    rosh_tishrei = rosh_hashanah(year)
    rosh = rosh_tishrei[0]

    # compute the month
    m = 0
    while (rosh + MONTH_LENGTHS[rosh_tishrei[1]][m] <= jday):
        rosh += MONTH_LENGTHS[rosh_tishrei[1]][m]
        m += 1
    month = MONTHS[m]

    # compute the day
    day = jday - rosh + 1 # add 1 because computers count from 0

    return (day, month, year)
