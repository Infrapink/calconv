#!/usr/bin/python

#
# Convert between Hebrew calendar and Julian Day.
#

import months
from fractions import *

from fractions import *

def calc(jday):

# This does various calculations involved in the Hebrew calendar.
# Splitting it off like this is necessary because the algorithm
# always turns up the correct moment for the molad of Tishri
# in the year being examined, but for some reason consistently
# gives the wrong molad of Tishri for the next year if the
# current year is a leap year.

    leap_years_am = (3,6,8,11,14,17,19,0)
    leap_years_bc = (1,3,6,9,12,14,17)
    leap_years_zo = (0,2,5,8,11,13,16)
    
    monlen = 29 + Fraction(12,24) + Fraction(793, (24 * 1080)) # formal mean synodic month length
    yearlen12 = 12 * monlen # length of a 12-month year
    yearlen13 = 13 * monlen # length of a 13-month year
    cycle19 = 235 * monlen
    molad_tohu = Fraction(5,24) + Fraction(204,(24 * 1080))
    
    day = 0
    month = ""
    year = 0

    if jday > 347996:
        # positive dates
        delta = jday - 347996
        cycles = 0

        # First, let's see how many 19-yaer cycles have passed
        while delta > cycle19:
            cycles += 1
            delta -= cycle19

        # Now let's get the number of whole years that have passed
        for y in range(0,19):
            y += 1
            if y in leap_years_am:
                if delta <= yearlen13:
                    single_years = y
                    break
                else:
                    delta -= yearlen13
            else:
                if delta <= yearlen12:
                    single_years = y
                    break
                else:
                    delta -= yearlen12

        # delta now gives us the exact position in the current year.
        rosh = int(jday - delta + molad_tohu) + 1 # add 1 to avoid a fencepost error

        # Work out the molad of Tishri
        days = 235 * monlen * cycles
        for z in range(1, single_years):
            if z in leap_years_am:
                days += yearlen13
            else:
                days += yearlen12
        molad = (days % 1) + molad_tohu
        if molad >= 1:
            molad -= 1

        year = (19 * cycles) + y

        # Is it a leap year?
        if year in leap_years_am:
            leap = True
        else:
            leap = False

        # So to recap:
        # delta is the current position within the year
        # rosh  is the Julian Day on which the molad of Tishri falls
        # molad is the moment of the molad of Tishri
        # year  is the current year number
        # leap  tells us whether or not it's a leap year

    else:
        # negative dates
        delta = 347997 - jday
        cycles = 0
        flag = False

        # Unlike the other algorithms, this one is going to work with negative numbers a lot.

        # calculate the year
        while flag == False:
            year += 1
            if (year % 19) in leap_years_bc:
                if delta < yearlen13:
                    flag = True
                else:
                    delta -= yearlen13
            else:
                if delta < yearlen12:
                    flag = True
                else:
                    delta -= yearlen12

        # year now gives us the current year

        # calculate the molad of Tishri and the date on which it falls
        position = 347997 + molad_tohu
        for y in range(0, year):
            if (y % 19) in leap_years_zo:
                position -= yearlen13
            else:
                position -= yearlen12

        if position >= 0:
            rosh = int(position)
            molad = position % 1
        else:
            rosh = int(position) - 1
           # molad = int(position) - position
            #molad = (0 - position) % 1
            molad = position % 1

    results = (rosh,molad,year)
    return results

def tojd(day, month, year):
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

    yeartype = {353:months.HEBREW_DEFICIENT_NORMAL,
                354:months.HEBREW_REGULAR_NORMAL,
                355:months.HEBREW_ABUNDANT_NORMAL,
                383:months.HEBREW_DEFICIENT_LEAP,
                384:months.HEBREW_REGULAR_LEAP,
                385:months.HEBREW_ABUNDANT_LEAP}

    if year > 0:
        # positive dates
        if month == "Veadar":
            if (year % 19) not in leap_years_am:
                month = "Adar"
                
        for y in range(1,year):
            if (y % 19) in leap_years_am:
                days += yearlen13
            else:
                days += yearlen12

        days = days + 347997 + molad_tohu

        # if my calculations are correct, the integer part of days is the day of the molad of Tishri,
        # and the fractional part is the time of day the molad occurs

        nums = calc(int(days))
        rosh = nums[0]
        mrosh = rosh
        molad = nums[1]
        r1 = False

        kday = rosh + 390
        next_nums = calc(kday)
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
        if month == "Veadar":
            if (abs(year) % 19) not in leap_years_bc:
                month = "Adar"
        position = 347997 + molad_tohu

        for y in range(0,abs(year)):
            if (y % 19) in leap_years_zo:
                position -= yearlen13
            else:
                position -= yearlen12

        # so far so good
        # now, the integer part of position should give us the day of the molad of Tishri, and
        # the fractional part should gives us the point in the day when it occurs.

        r1 = False
        if position > 0:
            rosh = int(position)
            molad = abs(position) % 1
        else:
            rosh = int(position) - 1
            molad = int(position) - position
        mrosh = rosh


        # now do it for next year
        if (abs(year) % 19) in leap_years_bc:
            next_position = position + yearlen13
        else:
            next_position = position + yearlen12

        next_r1 = False
        if next_position > 0:
            next_rosh = int(next_position)
            next_molad = abs(next_position) % 1
        else:
            next_rosh = int(next_position) - 1
            next_molad = int(next_position) - next_position
        next_mrosh = next_rosh            
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
        
        # This right here is some sneaky buggery to fix a fencepost error that appears to actually depend on the phase of the moon
        testdate = fromjd(int(days))
        if days >= 0:
            if testdate[0] != day:
                days += 1
        else:
            if testdate[0] != day:
                days -= 1

 #       correction = testdate[0] - days
  #      days += correction


    days = int(days)
    return days

def fromjd(jday):
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

    yeartype = {353:months.HEBREW_DEFICIENT_NORMAL,
                354:months.HEBREW_REGULAR_NORMAL,
                355:months.HEBREW_ABUNDANT_NORMAL,
                383:months.HEBREW_DEFICIENT_LEAP,
                384:months.HEBREW_REGULAR_LEAP,
                385:months.HEBREW_ABUNDANT_LEAP}

    if jday > 347996:
        # positive dates
        numbers = calc(jday)
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

        prev_numbers = calc(iday)
        prev_rosh = prev_numbers[0]
        prev_mrosh = prev_rosh
        prev_molad = prev_numbers[1]
        prev_year = year - 1
        
        next_numbers = calc(kday)
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
        numbers = calc(jday)
        rosh = numbers[0]  # Julian Day on which the molad of Tishri falls
        mrosh = rosh
        molad = numbers[1] # moment of the molad of Tishri
        year = numbers[2]  # number of the current year
        r1 = False

        # looking good so far. now do it for next year
        kday = rosh + 390 # next year
        next_numbers = calc(kday)
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

