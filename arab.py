#!/usr/bin/python

#
# Convert between the pre-Islamic Arab calendar and Julian Day
#

from fractions import *
from math import ceil

monlen = 29 + Fraction(12,24) + Fraction(44,1440) + Fraction(28,864000) # mean synodic month, according to Wolfram Alpha
year12 = 12 * monlen
year13 = 13 * monlen
cycle19 = (12 * year12) + (year13 * 7)
epoch = 1948319 + Fraction(65281, 108000) # Take the Muslim epoch and add 10 years, then subtract 4 leap and 6
                                          # regular years. This all results in Dhu al-Hijjah coinciding in the Arab
                                          # and Islamic calendrs for 1 AH
                                          # If you instead wish for Muharram 10 to coincide, add monlen to epoch

months0 = ("Muharram", "Safar", "Rabi' al-awwal", "Rabi' al-Thani", "Jumada al-awwal", "Jumada al-Thani", "Rajab", "Sha'ban", "Ramadan", "Shawwal", "Dhu al-Qidah", "Dhu al-Hijjah")
months1 = ("Muharram", "Safar", "Rabi' al-awwal", "Rabi' al-Thani", "Jumada al-awwal", "Jumada al-Thani", "Rajab", "Sha'ban", "Ramadan", "Shawwal", "Dhu al-Qidah", "Dhu al-Hijjah", "Nasiʾ")
months2 = ("Muharram", "Nasiʾ", "Safar", "Rabi' al-awwal", "Rabi' al-Thani", "Jumada al-awwal", "Jumada al-Thani", "Rajab", "Sha'ban", "Ramadan", "Shawwal", "Dhu al-Qidah", "Dhu al-Hijjah")
months3 = ("Muharram", "Safar", "Nasiʾ", "Rabi' al-awwal", "Rabi' al-Thani", "Jumada al-awwal", "Jumada al-Thani", "Rajab", "Sha'ban", "Ramadan", "Shawwal", "Dhu al-Qidah", "Dhu al-Hijjah")
months4 = ("Muharram", "Safar", "Rabi' al-awwal", "Nasiʾ", "Rabi' al-Thani", "Jumada al-awwal", "Jumada al-Thani", "Rajab", "Sha'ban", "Ramadan", "Shawwal", "Dhu al-Qidah", "Dhu al-Hijjah")
months5 = ("Muharram", "Safar", "Rabi' al-awwal", "Rabi' al-Thani", "Nasiʾ", "Jumada al-awwal", "Jumada al-Thani", "Rajab", "Sha'ban", "Ramadan", "Shawwal", "Dhu al-Qidah", "Dhu al-Hijjah")
months6 = ("Muharram", "Safar", "Rabi' al-awwal", "Rabi' al-Thani", "Jumada al-awwal", "Nasiʾ", "Jumada al-Thani", "Rajab", "Sha'ban", "Ramadan", "Shawwal", "Dhu al-Qidah", "Dhu al-Hijjah")
months7 = ("Muharram", "Safar", "Rabi' al-awwal", "Rabi' al-Thani", "Jumada al-awwal", "Jumada al-Thani", "Nasiʾ", "Rajab", "Sha'ban", "Ramadan", "Shawwal", "Dhu al-Qidah", "Dhu al-Hijjah")
months8 = ("Muharram", "Safar", "Rabi' al-awwal", "Rabi' al-Thani", "Jumada al-awwal", "Jumada al-Thani", "Rajab", "Nasiʾ", "Sha'ban", "Ramadan", "Shawwal", "Dhu al-Qidah", "Dhu al-Hijjah")
months9 = ("Muharram", "Safar", "Rabi' al-awwal", "Rabi' al-Thani", "Jumada al-awwal", "Jumada al-Thani", "Rajab", "Sha'ban", "Nasiʾ", "Ramadan", "Shawwal", "Dhu al-Qidah", "Dhu al-Hijjah")
months10 = ("Muharram", "Safar", "Rabi' al-awwal", "Rabi' al-Thani", "Jumada al-awwal", "Jumada al-Thani", "Rajab", "Sha'ban", "Ramadan", "Nasiʾ", "Shawwal", "Dhu al-Qidah", "Dhu al-Hijjah")
months11 = ("Muharram", "Safar", "Rabi' al-awwal", "Rabi' al-Thani", "Jumada al-awwal", "Jumada al-Thani", "Rajab", "Sha'ban", "Ramadan", "Shawwal", "Nasiʾ", "Dhu al-Qidah", "Dhu al-Hijjah")
months12 = ("Muharram", "Safar", "Rabi' al-awwal", "Rabi' al-Thani", "Jumada al-awwal", "Jumada al-Thani", "Rajab",
"Sha'ban", "Ramadan", "Shawwal", "Dhu al-Qidah", "Nasiʾ", "Dhu al-Hijjah")

CALTYPE = {1: months1,
           2: months2,
           3: months3,
           4: months4,
           5: months5,
           6: months6,
           7: months7,
           8: months8,
           9: months9,
           10: months10,
           11: months11,
           0: months12}

#leap_years_ah = (2,5,7,10,13,15,18)
#leap_years_bh = (2,5,7,10,13,15,18)
leap_years = (2,5,7,10,13,15,18) # as it turns out, the remainder pattern of leap years is the same whether the year be positive or negative

def tojd(day, month, year):
    day = int(day)
    month = month
    year = int(year)
    current = False

    if year > 0:
        # positive dates
        y = 1
        cycles = (year - y) // 19
        y += (19 * cycles)
        res = epoch + (cycles * cycle19)
        ytype = 7 * cycles # use this to work out where Nasi' falls

        while y < year:
            if y % 19 in leap_years:
                res += year13
                ytype += 1
            else:
                res += year12
            y += 1

        #print(y, ":", year)

        # now we need to figure out what type of year it is
        if (year % 19) not in leap_years:
            months = months0
            # This next bit accounts for someone entering Nasiʾ incorrectly
            if month == "Nasiʾ":
                notmo = CALTYPE[ytype % 12]
                for n in range(0,13):
                    if notmo[n] == "Nasiʾ":
                        month = notmo[n - 1]
            #print("Not a leap year")
        else:
            months = CALTYPE[ytype % 12] # There are 12 types of leap year, so take the remainder to figure out which one

    else:
        # negative dates
        y = 0
        cycles = (y - year) // 19
        y -= (19 * cycles)
        res = epoch - (cycle19 * cycles)
        ytype = (-7) * cycles

        while y > year:
            y -= 1
            if abs(y) % 19 in leap_years:
                res -= year13
                ytype -= 1
                # if ytype == 0:
                    #ytype -= 1
            else:
                res -= year12

        if abs(year) % 19 not in leap_years:
            months = months0
            # Check if Nasiʾ was entered in error
            if month == "Nasiʾ":
                notmo = CALTYPE[abs(ytype) % 12]
                for n in range(0,13):
                    if notmo[n] == "Nasiʾ":
                        month = notmo[n - 1]
                
        else:
            months = CALTYPE[abs(ytype) % 12]

    jday = res
    m = 0
    while current == False:
        if month == months[m]:
            jday = ceil(jday) +  day - 1 # add 1 to account for a fencepost error
            current = True
        else:
            jday += monlen
        m += 1

    return jday

def fromjd(jday):
    jday = int(jday)

    day = 0
    month = ""
    year = 0

    curryear = False
    currmonth = False
    m = 0
    ytype = 0

    if jday >= int(epoch):
        # positive dates
        year = 1
        cycles = (jday - epoch) // cycle19
        year += (19 * cycles)
        res = epoch + (cycle19 * cycles)

        while curryear == False:
            if year % 19 in leap_years:
                next_res = res + year13
                ytype += 1
            else:
                next_res = res + year12
            if jday < ceil(next_res):
                curryear = True
            else:
                res = next_res

    else:
        # negative dates
        cycles = (epoch - jday) // cycle19
        year -= (19 * cycles)
        res = epoch - (cycle19 * cycles)
        ytype -= (7 * cycles)

        while jday < ceil(res):
            year -= 1
            if abs(year) % 19 in leap_years:
                res -= year13
                ytype -= 1
            else:
                res -= year12

    newmoon = res
    nextmoon = res + monlen

    if abs(year) % 19 not in leap_years:
        months = months0
    else:
        months = CALTYPE[abs(ytype) % 12]

    while currmonth == False:
            if jday < ceil(nextmoon):
                day = jday - ceil(newmoon) + 1
                month = months[m]
                currmonth = True
            else:
                newmoon += monlen
                nextmoon += monlen
            m += 1    

    return (day, month, year)
