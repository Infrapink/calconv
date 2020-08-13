#!/usr/bin/python

#
# Convert between the pre-Islamic Arab calendar and Julian Day
#

from fractions import *

monlen = 29 + Fraction(12,24) + Fraction(44,1440) + Fraction(28,864000) # mean synodic month, according to Wolfram Alpha
year12 = 12 * monlen
year13 = 13 * monlen
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

    jday = epoch
    current = False
    m = 0
    ytype = 0 # this is used to calculate which type of leap year it might be.

    if year > 0:
        # positive dates

        for y in range(1, year):
            if y % 19 in leap_years:
                jday += year13
                ytype += 1
            else:
                jday += year12

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
           # print("Leap year")
            #print(ytype % 12)

        while current == False:
            if month == months[m]:
                jday += day - 1 # subtract 1 to account for a fencepost error
                current = True
            else:
                jday += monlen
            m += 1


    else:
        # negative dates

        for y in range(-1, (year - 1), -1):
            if abs(y) % 19 in leap_years:
                jday -= year13
                ytype -= 1
                if ytype == 0:
                    ytype -= 1
            else:
                jday -= year12

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

        while current == False:
            if month == months[m]:
                jday += day# + 1 # add 1 to account for a fencepost error
                current = True
            else:
                jday += monlen
            m += 1

    #if jday < 0:
     #   jday -= 1

    return int(jday)

def fromjd(jday):
    jday = int(jday)

    day = 0
    month = ""
    year = 0

    nyd = epoch
    curryear = False
    currmonth = False
    m = 0
    ytype = 0

    if jday >= int(epoch):
        # positive dates

        while curryear == False:
            year += 1
            if year % 19 in leap_years:
                next_nyd = nyd + year13
                ytype += 1
            else:
                next_nyd = nyd + year12
            if jday < int(next_nyd):
                curryear = True
            else:
                nyd = next_nyd

        newmoon = nyd
        nextmoon = nyd + monlen

        if year % 19 not in leap_years:
            months = months0
        else:
            months = CALTYPE[ytype % 12]

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
                year -= 1
                next_nyd = nyd
                if abs(year) % 19 in leap_years:
                    nyd -= year13
                    ytype -= 1
                else:
                    nyd -= year12

        newmoon = nyd
        nextmoon = nyd + monlen

        if abs(year) % 19 not in leap_years:
            months = months0
        else:
            months = CALTYPE[abs(ytype) % 12]

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
