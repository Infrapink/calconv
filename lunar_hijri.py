#!/usr/bin/python

#
# Convert between Lunar Hijri dates and Julian Days
#

from fractions import *
from math import ceil

monlen = 29 + Fraction(12,24) + Fraction(44,1440) + Fraction(28,864000) # mean synodic month, according to Wolfram Alpha
yearlen = 12 * monlen
epoch = 1948437 + Fraction(5233,7200) # Based on taking the New Moon of Muharram 1442 and subtracting (1441 * yearlen)

months = ("Muharram", "Safar", "Rabi' al-awwal", "Rabi' al-Thani", "Jumada al-awwal", "Jumada al-Thani", "Rajab", "Sha'ban", "Ramadan", "Shawwal", "Dhu al-Qidah", "Dhu al-Hijjah")

def tojd(day, month, year):
    day = int(day)
    month = month
    year = int(year)
    current = False

    if year > 0:
        # positive dates
        newmoon = epoch + (yearlen * (year - 1)) # 1 Muharram
    else:
        # negative dates
        newmoon = epoch + (year * yearlen) # 1 Muharram
        
    jday = newmoon
    for m in range(0,12):
        if month == months[m]:
            jday += day - 1
            break
        else:
            jday += monlen

    return ceil(jday)

def fromjd(jday):
    jday = int(jday)
    day = 0
    month = ""
    year = 0
    current = False
    m = 0

    if jday >= int(epoch):
        # positive dates
        y = (jday - epoch) // yearlen
        year = y + 1
        newmoon = epoch + (y * yearlen)

    else:
        # negative dates
        year = (jday - epoch) // yearlen
        newmoon = epoch + (year * yearlen)

    nextmoon = newmoon + monlen

    while current == False:
        if jday < ceil(nextmoon):
            day = jday - ceil(newmoon) + 1
            month = months[m]
            current = True
        else:
            newmoon += monlen
            nextmoon += monlen
        m += 1

    return (day, month, year)

