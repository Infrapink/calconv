#!/usr/bin/python3

# Convert between Julian Days and a lunisolar calendar combining the Balinese Metonic system with the Javanese cycles of months

from months import JAVANESE as MONTHS

epoch = 2317574
windu = 2835 # 96 months
kurup = (15 * windu) - 1 # 1440 months
sk = (9 * windu) - 1 # 864 months
lunar_cycle = (4 * kurup) + sk # 6624 months
MONTH_LENGTHS = {354: (29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30), # normal years
                 355: (29, 30, 29, 30, 29, 30, 29, 30, 30, 30, 29, 30)} # leap years
lunar_leaps = (0, 3, 6)
solar_leaps = (2, 5, 7, 10, 13, 16, 18)
leap_months = {2:  1,
               4:  5,
               7:  3,
               10: 1,
               13: 0,
               15: 4}

def months_in_year(year):
    '''Return the number of months in a specified year'''
    if (int(year) % 19 in solar_leaps):
        ans = 13
    else:
        ans = 12
    return ans

def m12(m):
    '''Return number of days in a 12-month period'''
    m = int(m) # total months since epoch
    m = m // 12 # cycles of 12 months since the epoch; a Muslim liturgical year
    if (m % 552 in (120, 192, 312, 432, 0)):
        # would be leap but it's normal
        ans = 354
    elif (m % 8 in lunar_leaps):
        # leap cycles
        ans = 355
    else:
        # normal cycle
        ans = 354
    return ans

def days_in_month(m):
    '''Return the number of days in the mth month since the epoch'''
    m = int(m)
    return MONTH_LENGTHS[m12(m)][m % 12]

def fromjd(jday):
    '''Convert a Julian Day to a date in the Jabvali calendar'''
    jday = int(jday)

    # account for the months
    # start with the long cycle
    cycles = (jday - epoch) // lunar_cycle
    months_past = cycles * 6624
    newmoon = epoch + (cycles * lunar_cycle)
    while (newmoon + lunar_cycle <= jday):
        newmoon += lunar_cycle
        months_past += 6624
    while (newmoon > jday):
        newmoon -= lunar_cycle
        months_past -= 6624

    # next, the kurups
    if (newmoon + kurup <= jday):
        newmoon += kurup
        months_past += 1440

        if (newmoon + sk <= jday):
            newmoon += sk
            months_past += 864

        while (newmoon + kurup <= jday):
            newmoon += kurup
            months_past += 1440

    # we are now at the start of a kurup
    # now to account for the windus
    while (newmoon + windu <= jday):
        newmoon += windu
        months_past += 96
    while (newmoon + m12(months_past) <= jday):
        newmoon += m12(months_past)
        months_past += 12
    while (newmoon + days_in_month(months_past) <= jday):
        newmoon += days_in_month(months_past)
        months_past += 1
    

    # newmoon is now the first of the month in which jday falls
    # months_past is the months between newmoon and the epoch

    # let's get the year
    # first, account for the cycles of 19 years == 235 months

    year = (months_past // 235) * 19
    months_to_nyd = (months_past // 235) * 235 # total months from the epoch to new year's day
    while (months_to_nyd + months_in_year(year) <= months_past):
        months_to_nyd += months_in_year(year)
        year += 1
    year += 1555 # add 1555 to get calendar year

    # now account for the actual months
    m = months_past - months_to_nyd # number of the month containing jday
    if (not((year % 19) in solar_leaps)):
        # normal year
        month = MONTHS[m]
    else:
        # leap year
        if (m > leap_months[year % 19]):
            month = MONTHS[m - 1]
        elif (m == leap_months[year % 19]):
            month = "Leap " + MONTHS[m]
        else:
            month = MONTHS[m]

    # get the day
    day = jday - newmoon + 1 # add 1 because humans don't count from 0

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a date in the Jabvali calendar to a Julian Day'''
    day = int(day) - 1 # subtract 1 because computers count from 0
    month = str(month)
    year = int(year) - 1555 # subtract 1555 to get years since the epoch

    # how many months have passed since the epoch?
    months_passed = 235 * (year // 19)
    y = 19 * (year // 19)
    while (y < year):
        months_passed += months_in_year(y)
        y += 1

    m = 0
    if (month[:4] == "Leap"):
        leap = True
        month = month[4:]
    else:
        leap = False
        
    if (not((year % 19) in solar_leaps)):
        # normal year
        while (MONTHS[m] != month):
            months_passed += 1
            m += 1
    else:
        # leap year
        l = False # have we passed the leap month?
        while (MONTHS[m] != month):
            months_passed += 1
            if (m != leap_months[year % 19]):
                m += 1
            else:
                l = True
        if ( (not l) and (m == leap_months[year % 19]) ):
            # we're in the leap month but need to be in the normal month
            months_passed += 1

    # months_passed is now equal to the number of months that have passed since the epoch.
    # how many days is that?
    # first, account for the long cycles
    cycles = months_passed // 6624
    months_to_j = 6624 * cycles
    jday = epoch + (cycles * lunar_cycle)

    # account for the kurups
    if (months_passed - months_to_j >= 1440):
        months_to_j += 1440
        jday += kurup

        if (months_passed - months_to_j >= 864):
            months_to_j += 864
            jday += sk

        while (months_passed - months_to_j >= 1440):
            months_to_j += 1440
            jday += kurup

    # account for the windus
    while (months_passed - months_to_j >= 96):
        months_to_j += 96
        jday += windu

    # account for the 12-month cycles
    while (months_passed - months_to_j >= 12):
        jday += m12(months_to_j)
        months_to_j += 12

    # account for the remaining individual months
    while (months_to_j < months_passed):
        jday += days_in_month(months_to_j)
        months_to_j += 1

    jday += day
    return jday
