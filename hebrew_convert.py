#!/usr/bin/python

#
# Convert a date in the Hebrew calendar to a Julian Day.
#

import months
from fractions import *

import hebrew_calculations
import julian_day_conversions

def convert(day, month, year):
    day = int(day)
    month = month.title()
    year = int(year)
    days = 0

    leap_years_am = (3,6,8,11,14,17,19,0)
    leap_years_bc = (1,3,6,9,12,14,17)
    leap_years_zo = (0,2,5,8,11,13,16)

    monlen = 29 + Fraction(12,24) + Fraction(793,25920)
    yearlen12 = 12 * monlen
    yearlen13 = 13 * monlen
    cycle19 = 235 * monlen

    molad_tohu = Fraction(5,24) + Fraction(204,25920)

    yeartype = {353:months.HEBREW_MONTHS_DEFICIENT_NORMAL,
                354:months.HEBREW_MONTHS_REGULAR_NORMAL,
                355:months.HEBREW_MONTHS_ABUNDANT_NORMAL,
                383:months.HEBREW_MONTHS_DEFICIENT_LEAP,
                384:months.HEBREW_MONTHS_REGULAR_LEAP,
                385:months.HEBREW_MONTHS_ABUNDANT_LEAP}

    if year > 0:
        # positive dates
        for y in range(1, year):
            if (y % 19) in leap_years_am:
                days += yearlen13
            else:
                days += yearlen12

        days = days + 347997 + molad_tohu

        # if my calculations are correct, the integer part of days is the day of the molad of Tishri,
        # and the fractional part is the time of day the molad occurs

        nums = hebrew_calculations.calc(int(days))
        rosh = nums[0]
        mrosh = rosh
        molad = nums[1]
        r1 = False

        kday = rosh + 390
        next_nums = hebrew_calculations.calc(kday)
        next_rosh = next_nums[0]
        next_mrosh = next_rosh
        next_molad = next_nums[1]
        next_year = next_nums[2]
        next_r1 = False

        # Rule 1: If the molad of Tishri is after noon, postpone Rosh Hashana
        if molad > Fraction(3,4): # noon comes 3/4 through a standard Hebrew day
            days += 1
            rosh += 1
            r1 = True

        if next_molad > Fraction(3,4): # noon comes 3/4 through a standard Hebrew day
            next_rosh += 1
            next_r1 = True

        # Rule 2: If the molad of Tishri falls on a "Tuesday" after 9 hours 204 chalakim
        # and it's NOT a leap year, and rule 1 has not been triggered, postpone Rosh Hashana

        if r1 == False:
            if (year % 19) not in leap_years_am:
                if (mrosh % 7) == 0: # "Tuesday"
                    if molad >= Fraction(9,24) + Fraction(204,25920): # 9 hours 204 chalakim
                        days += 1
                        rosh += 1

        if next_r1 == False:
            if (next_year % 19) not in leap_years_am:
                if (next_mrosh % 7) == 0: # "Tuesday"
                    if next_molad >= Fraction(9,24) + Fraction(204,25920): # 9 hours 204 chalakim
                        next_rosh += 1

        # Rule 3: If the molad of Tishri falls on a "Monday" after 15 hours 589 chalakim
        # and it's the year AFTER a leap year, and rule 1 has not been triggered postpone Rosh Hashana

        if r1 == False:
            if ((year - 1) % 19) in leap_years_am:
                if (mrosh % 7) == 6: # "Monday"
                    if molad >= Fraction(15,24) + Fraction(589,25920): # 15 hours 589 chalakim
                        days += 1
                        rosh += 1

        if next_r1 == False:
            if (year % 19) in leap_years_am:
                if (next_mrosh % 7) == 6: # "Monday"
                    if next_molad >= Fraction(15,24) + Fraction(589,25920): # 15 hours 589 chalakim
                        next_rosh += 1

        # Rule 4: If Rosh Hashanah would fall on a "Sunday", "Wednesday", or "Friday", it is postponed

        if (rosh % 7) in (1,3,5): # "Wednesday", "Friday", "Sunday"
            rosh += 1
            days += 1

        if (next_rosh % 7) in (1,3,5): # "Wednesday", "Friday", "Sunday"
            next_rosh += 1

        m = yeartype[next_rosh - rosh]

        for i in m.keys():
            if i == month:
                days += day
                break
            else:
                days += m[i]
        days -= 1 # fix a fencepost error

    else:
        # negative dates
        position = 347997 + molad_tohu
  #      print(position, int(position), position % 1)

        # we're going to be working with negative numbers
        for y in range(0,abs(year)):
            if (y % 19) in leap_years_zo:
                position -= yearlen13
 #               print(position, int(position), position % 1)
            else:
                position -= yearlen12
#                print(position, int(position), position % 1)

        # so far so good
        # now, the integer part of position should give us the day of the molad of Tishri, and
        # the fractional part should gives us the point in the day when it occurs.

        r1 = False
        rosh = int(position)
        mrosh = rosh
        molad = abs(position) % 1

        # now do it for next year
        if (abs(year) % 19) in leap_years_bc:
            next_position = position + yearlen13
        else:
            next_position = position + yearlen12

        next_r1 = False
        next_rosh = int(next_position)
        next_mrosh = next_rosh
        next_molad = abs(next_position) % 1
        next_year = year + 1
        if next_year == 0:
            next_year = 1

        if molad > Fraction(3,4): # noon is 3/4 through a standard Hebrew day
            rosh += 1
            days += 1
            r1 = True

        if next_molad > Fraction(3,4): # noon is 3/4 through a standard Hebrew day
            next_rosh += 1
            next_r1 = True

        # Rule 2: If the molad of Tishri falls on a "Tuesday" after 9 hours 204 chalakim and it's
        # NOT a leap year, postpone Rosh Hashana

        if r1 == False:
            if (abs(year) % 19) not in leap_years_bc:
                if (mrosh % 7) == 0: # "Tuesday"
                    if molad >= Fraction(9,24) + Fraction(204,25920): # 9 hours 204 chalakim
                        rosh += 1
                        position += 1

        if next_r1 == False:
            if next_year < 0: # if next_year > 0, there is no need to do anything because this rule does not apply
                if (abs(next_year) % 19) not in leap_years_bc:
                    if (next_mrosh % 7) == 0: # "Tuesday"
                        if next_molad >= Fraction(9,24) + Fraction(204,25920): # 9 hours 204 chalakim
                            next_rosh += 1

        # Rule 3: If the molad of Tishri falls on a "Monday" after 15 hours 589 chalakim
        # in the year AFTER a leap year, postpone Rosh Hashana

        if r1 == False:
            if (abs(year - 1) % 19) in leap_years_bc:
                if mrosh > 0:
                    if (mrosh % 7) == 6: # "Monday"
                        if molad >= Fraction(15,24) + Fraction(589,25920): # 15 hours 589 chalakim
                            rosh += 1
                            position += 1
                else:
                    if (abs(mrosh) % 7) == 1: # "Monday"
                        if molad >= Fraction(15,24) + Fraction(589,25920): # 15 hours 589 chalakim
                            rosh += 1
                            position += 1


        if next_r1 == False:
            if (abs(year) % 19) in leap_years_bc:
                if next_mrosh > 0:
                    if (next_mrosh % 7) == 6: # "Monday"
                        if next_molad >= Fraction(15,24) + Fraction(589,25920): # 15 hours 589 chalakim
                            next_rosh += 1
                else:
                    if (abs(next_mrosh) % 7) == 1: # "Monday"
                        if next_molad >= Fraction(15,24) + Fraction(589,25920): # 15 hours 589 chalakim
                            next_rosh += 1

        # Rule 4: If Rosh Hashana would falls on a "Sunday", "Wednesday", or "Friday", it is postponed

        if rosh > 0:
            if (rosh % 7) in (1,3,5): # "Wednesday", "Friday", "Sunday"
                rosh += 1
                position += 1
        else:
            if (abs(rosh) % 7) in (6,4,2): # "Wednesday", "Friday", "Sunday"
                rosh += 1
                position += 1

        if next_rosh > 0:
            if (next_rosh % 7) in (1,3,5): # "Wednesday", "Friday", "Sunday"
                next_rosh += 1
        else:
            if (abs(next_rosh) % 7) in (6,4,2): # "Wednesday", "Friday", "Sunday"
                next_rosh += 1

        m = yeartype[next_rosh - rosh]
        days = int(position)
        
        for i in m.keys():
            if i == month:
                days += day
                break
            else:
                days += m[i]

        days = int(days) - 1 # fix the fencepost error
        
        # This right here is some sneaky buggery to fix an obscure fencepost error that I can't figure out.
        testdate = julian_day_conversions.hebrew(int(days))                                                 
        if testdate[0] != day:
            days += 1


    days = int(days)
    return days
