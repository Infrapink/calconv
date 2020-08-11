#!/usr/bin/python

#
# Convert between Lunar Hijri dates and Julian Days
#

from fractions import *

monlen = 29 + Fraction(12,24) + Fraction(793, 25920) # using Hebrew measurements, which should be accurate enough
yearlen = 12 * monlen
#epoch = Fraction(8417249647, 4320)
epoch = 1948437 + Fraction(1987,4320)# - yearlen# New Moon of 1 Muharram 1 AH, Arab Time by Saudi Arabian meridian

months = ("Muharram", "Safar", "Rabi' al-awwal", "Rabi' al-Thani", "Jumada al-awwal", "Jumada al-Thani", "Rajab", "Sha'ban", "Ramadan", "Shawwal", "Dhu al-Qidah", "Dhu al-Hijjah")

def tojd(day, month, year):
    day = int(day)
    month = month
    year = int(year)
    jday = epoch
    current = False
    m = 0

    if year > 0:
        # positive dates

        for y in range(1, year):
            jday += yearlen

        while current == False:
            if month == months[m]:
                jday += day - 1
                current = True
            else:
                jday += monlen
            m += 1

    else:
        # negative dates

        for y in range(-1, (year - 1), -1):
            jday -= yearlen

        while current == False:
            if month == months[m]:
                jday += day + 1 # add 1 to account for a fencepost error
                current = True
            else:
                jday += monlen
            m += 1

    if jday < 0:
        jday -= 1
        
    return int(jday)

def fromjd(jday):
    jday = int(jday)
    day = 0
    month = ""
    year = 0
    nyd = epoch
    next_nyd = nyd + yearlen
    curryear = False
    currmonth = False
    m = 0

    if jday >= int(epoch):
        # positive dates

        while curryear == False:
            year += 1
            if jday < int(next_nyd):
                curryear = True
            else:
                nyd += yearlen
                next_nyd += yearlen

        newmoon = nyd
        nextmoon = nyd + monlen

        while currmonth == False:
            if jday < int(nextmoon):
                day = jday - int(newmoon) + 1
                month = months[m]
                currmonth = True
            else:
                newmoon += monlen
                nextmoon += monlen
            m += 1

    else:
        # negative dates

        while curryear == False:

            if jday > int(nyd):
                curryear = True
            else:
                nyd -= yearlen
                next_nyd -= yearlen
                year -= 1
            
        newmoon = nyd
        nextmoon = newmoon + monlen
        
        while currmonth == False:
            if newmoon >= 0:
                mu = int(nextmoon)
            else:
                mu = int(nextmoon) - 1
            if jday < mu:
                day = jday - int(newmoon)
                month = months[m]
                currmonth = True
            else:
                newmoon += monlen
                nextmoon += monlen
            m += 1

    return (day, month, year)
