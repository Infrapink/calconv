#!/usr/bin/python

#
# Convert between Jewish Hebrew calendar and Julian Day
#

import months
from fractions import *

leap_years_am = (3,6,8,11,14,17,19,0)
leap_years_bc = (1,3,6,9,12,14,17)
leap_years_zo = (0,2,5,8,11,13,16)
    
monlen = 29 + Fraction(12,24) + Fraction(793, (24 * 1080)) # formal mean synodic month length
yearlen12 = 12 * monlen # length of a 12-month year
yearlen13 = 13 * monlen # length of a 13-month year
cycle19 = 235 * monlen
molad_tohu = 347997 + Fraction(5,24) + Fraction(204,25920)

YEARTYPE = {353: months.HEBREW_DEFICIENT_NORMAL,
            354: months.HEBREW_REGULAR_NORMAL,
            355: months.HEBREW_ABUNDANT_NORMAL,
            383: months.HEBREW_DEFICIENT_LEAP,
            384: months.HEBREW_REGULAR_LEAP,
            385: months.HEBREW_ABUNDANT_LEAP}

def tojd(day, month, year):
    day = int(day)
    month = month
    year = int(year)
    
    days = molad_tohu

    if year >= 1:
        # positive years

        if month == "Veadar":
            if year % 19 not in leap_years_am:
                month = "Adar"
                
        for y in range(1, year):
            if y % 19 in leap_years_am:
                days += yearlen13
            else:
                days += yearlen12

        # the value of days is now the moment of the molad of Tishri for the year in question
        
        if year % 19 in leap_years_am:
            next_year = days + yearlen13
        else:
            next_year = days + yearlen12

        rosh = int(days)
        molad = days % 1
        r1 = False

        next_rosh = int(next_year)
        next_molad = next_year % 1
        next_r1 = False

        next_year = year + 1
        prev_year = year - 1

        # Rule 1: If the molad of Tishri falls after noon, postpone Rosh Hashanah

        if molad > Fraction(3,4): # noon is 3/4 of the way through a standard Hebrew day
            days += 1
            rosh += 1
            r1 = True

        if next_molad > Fraction(3,4):
            next_rosh += 1
            next_r1 = True

        # Rule 2: If the molad of Tishri falls on a "Tuesday" after 9 hours 204 chalakim
        # and it's NOT a leap year, and rule 1 has not been triggered, postpone Rosh Hashanah

        if r1 == False:
            if (year % 19) not in leap_years_am:
                if rosh % 7 == 0: # "Tuesday"
                    if molad > Fraction(9,24) + Fraction(204,25920): # 9 hours 204 chalakim
                        days += 1
                        rosh += 1

        if next_r1 == False:
            if (next_year % 19) not in leap_years_am:
                if next_rosh % 7 == 0: # "Tuesday"
                    if next_molad > Fraction(9,24) + Fraction(204,25920): # 9 hours 204 chalakim
                        next_rosh += 1

        # Rule 3: If the molad of Tishri falls after 15 hours 589 chalakim on a "Monday"
        # in the year AFTER a leap yer, and rule 1 has not been triggered, postpone Rosh Hashanah

        if r1 == False:
            if (prev_year % 19) in leap_years_am:
                if rosh % 7 == 6: # "Monday"
                    if molad > Fraction(15,24) + Fraction(589,25920): # 15 hours 589 chalakim
                        days += 1
                        rosh += 1

        if next_r1 == False:
            if (year % 19) in leap_years_am:
                if next_rosh % 7 == 6: # "Monday"
                    if next_molad > Fraction(15,24) + Fraction(589,25920): # 15 hours 589 chalakim
                        next_rosh += 1

        # Rule 4: If Rosh Hashanah would fall on a "Wednesday", "Friday", or "Sunday", it is postponed
        if (rosh % 7) in (1,3,5): # "Wednesday", "Friday", "Sunday"
            rosh += 1
            days +=1

        if (next_rosh  % 7) in (1,3,5): # "Wednesday", "Friday", "Sunday"
            next_rosh += 1

        m = YEARTYPE[next_rosh - rosh]

        for i in m.keys():
            if i == month:
                days += day - 1
                break
            else:
                days += m[i]
        days = int(days)

    else:
        # negative dates
        hashanah = molad_tohu
        
        for y in range(-1, (year - 1), -1):
            if abs(y) % 19 in leap_years_bc:
                hashanah -= yearlen13
            else:
                hashanah -= yearlen12

        if abs(year) % 19 in leap_years_bc:
            next_hashanah = hashanah + yearlen13
        else:
            next_hashanah = hashanah + yearlen12

        next_year = year + 1
        prev_year = year - 1

        if hashanah < 0:
            rosh = int(hashanah) - 1
        else:
            rosh = int(hashanah)
        molad = hashanah % 1
        r1 = False

        if next_hashanah < 0:
            next_rosh = int(next_hashanah) - 1
        else:
            next_rosh = int(next_hashanah)
        next_molad = next_hashanah % 1
        next_r1 = False

        # Rule 1: If the molad of Tishri falls after noon, postpone Rosh Hashanah

        if molad > Fraction(3,4): # noon comes 3/4 of the way through a standard Hebrew day
            rosh += 1
            r1 = True

        if next_molad > Fraction(3,4): # noon falls 3/4 of the way through a standard Hebrew day
            next_rosh += 1
            next_r1 = True

        # Rule 2: If the molad of Tishri falls on a "Tuesday" after 9 hours chalakim and it's NOT a leap year,
        if r1 == False:
            if abs(year) % 19 not in leap_years_bc:
                if rosh % 7 == 0: # "Tuesday"
                    if molad >= Fraction(9,24) + Fraction(204,25920): # 9 hours 204 chalakim
                        rosh += 1

        if next_r1 == False:
            if abs(next_year) % 19 not in leap_years_bc:
                if next_rosh % 7 == 0: # "Tuesday"
                    if next_molad >= Fraction(9,24) + Fraction(204,25920): # 9 hours 204 chalakim
                        next_rosh += 1

        # Rule 3: If the molad of Tishri falls on a "Monday" in the year AFTER a leap year
        # after 15 hours 589 chalakim, postpone Rosh Hashanah

        if r1 == False:
            if abs(prev_year) % 19 in leap_years_bc:
                if rosh % 7 == 6: # "Monday" (this apparently works regardless of whether rosh is (+) or (-)
                    if molad >= Fraction(15,24) + Fraction(589,25920): # 15 hours 589 chalakim
                        rosh += 1

        if next_r1 == False:
            if abs(year) % 19 in leap_years_bc:
                if next_rosh % 7 == 6: # "Monday"
                    if next_molad >= Fraction(15,24) + Fraction(589,25920): # 15 hours 589 chalakim
                        next_rosh += 1

        # Rule 4: If Rosh Hashanah would fall on a "Sunday", "Wednesday", or "Friday", it is posponed

        if rosh % 7 in (1,3,5): # "Wednesday", "Friday", "Sunday"
            rosh += 1

        if next_rosh % 7 in (1,3,5): # "Wednesday", "Friday", "Sunday"
            next_rosh += 1

        days = rosh
        m = YEARTYPE[next_rosh - rosh]

        for i in m.keys():
            if i == month:
                days += day - 1
                break
            else:
                days += m[i]
        days = int(days)

    return(days)

def fromjd(jday):
    """Convert a Julian day to a date in the Jewish calendar."""
    jday = int(jday)
    day = 0
    month = ""
    year = 0

    hashanah = molad_tohu

    if jday >= int(molad_tohu):
        # positive dates

        current = False

        while current == False:
            year += 1
            if year % 19 in leap_years_am:
                y = yearlen13
            else:
                y = yearlen12
                
            if jday - hashanah < y:
                current = True
            else:
                hashanah += y

        # now we have the current year, and hashanah gives the molad of Tishri
        if year % 19 in leap_years_am:
            next_hashanah = hashanah + yearlen13
        else:
            next_hashanah = hashanah + yearlen12

        next_year = year + 1
        prev_year = year - 1

        rosh = int(hashanah)
        molad = hashanah % 1
        r1 = False

        next_rosh = int(next_hashanah)
        next_molad = next_hashanah % 1
        next_r1 = False

        # Rule 1: If the molad of Tishri falls after noon, postpone Rosh Hashanah
        if molad > Fraction(3,4): # noon comes 3/4 of the way through a standard Hebrew day
            rosh += 1
            r1 = True

        if next_molad > Fraction(3,4): # noon comes 3/4 of the way through a standard Hebrew day
            next_rosh += 1
            next_r1 = True

        # Rule 2: if the molad of Tishri falls on a "Tuesday" in a NON-leap year
        # after 9 hours 204 chalakim, postpone Rosh Hashanah

        if r1 == False:
            if year % 19 not in leap_years_am:
                if rosh % 7 == 0: # "Tuesday"
                    if molad >= Fraction(9,24) + Fraction(204,25920): # 9 hours 204 chalakim
                        rosh += 1

        if next_r1 == False:
            if next_year % 19 not in leap_years_am:
                if next_rosh % 7 == 0: # "Tuesday"
                    if next_molad >= Fraction(9,24) + Fraction(204,25920): # 9 hours 204 chalakim
                        next_rosh += 1

        # Rule 3: If the molad of Tishri falls on a "Monday" in the year AFTER a leap year
        # after 15 hours 589 chalakim, postpone Rosh Hashanah

        if r1 == False:
            if prev_year % 19 in leap_years_am:
                if rosh % 7 == 6: # "Monday"
                    if molad >= Fraction(15,24) + Fraction(589,25920): # 15 hours 589 chalakim
                        rosh += 1

        if next_r1 == False:
            if year % 19 in leap_years_am:
                if next_rosh % 7 == 6: # "Monday"
                    if next_molad >= Fraction(15,24) + Fraction(589,25920): # 15 hours 589 chalakim
                        next_rosh += 1

        # Rule 4: If Rosh Hashanah would fall on a "Sunday", "Wednesday", or "Friday", it is postponed

        if rosh % 7 in (1,3,5): # "Wednesday", "Friday", "Sunday"
            rosh += 1

        if next_rosh % 7 in (1,3,5): # "Wednesday", "Friday", "Sunday"
            next_rosh += 1

        delta = jday - rosh + 1
        m = YEARTYPE[next_rosh - rosh]
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
        while hashanah > jday:
            year -= 1
            if abs(year) % 19 in leap_years_bc:
                hashanah -= yearlen13
            else:
                hashanah -= yearlen12

        # This gives us the exact year, and hashanah gives the exact moment of the molad of Tishri for year
        next_year = year + 1
        prev_year = year - 1
        if abs(year) % 19 in leap_years_bc:
            next_hashanah = hashanah + yearlen13
        else:
            next_hashanah = hashanah + yearlen12

        if hashanah < 0:
            rosh = int(hashanah) - 1
        else:
            rosh = int(hashanah)
        molad = hashanah % 1
        r1 = False

        if next_hashanah < 0:
            next_rosh = int(next_hashanah) - 1
        else:
            next_rosh = int(next_hashanah)
        next_molad = next_hashanah % 1
        next_r1 = False

        # Rule 1: If the molad of Tishri falls after noon, postpone Rosh Hashanah
        if molad > Fraction(3,4): # noon falls 3/4 of the way through a standard Hebrew day
            rosh += 1
            r1 = True

        if next_molad > Fraction(3,4): # noon falls 3/4 of the way through a standard Hebrew day
            next_rosh += 1
            next_r1 = True

        # Rule 2: If the molad of Tishri falls on a "Tuesday" afer 9 hours 204 chalakim and it's NOT a leap year,

        if r1 == False:
            if abs(year) % 19 not in leap_years_bc:
                if rosh % 7 == 0: # "Tuesday"
                    if molad >= Fraction(9,24) + Fraction(204,25920): # 9 hours 204 chalakim
                        rosh += 1

        if next_r1 == False:
            if abs(next_year) % 19 not in leap_years_bc:
                if next_rosh % 7 == 0: # "Tuesday"
                    if next_molad >= Fraction(9,24) + Fraction(204,25920): # 9 hours 204 chalakim
                        next_rosh += 1

        # Rule 3: If the molad of Tishri falls on a "Monday" after 15 hours 589 chalakim in the year
        #         AFTER a leap year, postpone Rosh Hashanah

        if r1 == False:
            if abs(prev_year) % 19 in leap_years_bc:
                if rosh % 7 == 6: # "Monday"
                    if molad >= Fraction(15,24) + Fraction(589,25920): # 15 hours 589 chalakim
                        rosh += 1

        if next_r1 == False:
            if abs(year) % 19 in leap_years_bc:
                if next_rosh % 7 == 6: # "Monday"
                    if next_molad >= Fraction(15,24) + Fraction(589,25920): # 15 hours 589 chalakim
                        next_rosh += 1

        # Rule 4: Postpone Rosh Hashanah if it would fall on a "Sunday", "Wednesday", or "Friday"
        if rosh % 7 in (1,3,5): # "Wednesday", "Friday", "Sunday"
            rosh += 1

        if next_rosh % 7 in (1,3,5): # "Wednesday", "Friday", "Sunday"
            next_rosh += 1

        m = YEARTYPE[next_rosh - rosh]
        delta = jday - rosh + 1

        if jday == next_rosh:
            day = 1
            month = "Tishrei"
            year += 1
        elif delta <= 0:
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

    return (day,month,year)
