#!/usr/bin/python3

# A programme to convert between the Myanmar lunisolar calendar (Makaranta system) and Julian Days

# Sources
## The Burmese and Arakanese Calendars, AMB Iwin, Hanthawaddy Printing Works, 1909
## Calendrical Systems of Mainland Sout-East Asia, JC Eade, E.J. Brill, 1995
## Traditional Calendar of Myanmar (Burma), GK Chatterjee, Indian Journal of the History of Science, 33(2)1998

from math import floor, ceil
from fractions import Fraction
from months import MYANMAR_NORMAL as NORMAL, ARAKAN_LEAP as LEAP, ARAKAN_LONG as LONG

# astronomical constants
sid_year = Fraction(292207, 800)
rasi = Fraction(sid_year, 12)
syn_month = rasi * Fraction(912, 940) # Irwin, 4:66
t2d = Fraction(syn_month, 30) # convert tithis to days
d2t = Fraction(30, syn_month) # convert days to tithis

leap_years = (2, 5, 7, 10, 13, 15, 18)
# this dictionary is used for working out if a leap year has a leap day in Nayon. See Irwin, 4:71
watat_add = {2:   4,
             5:   5,
             7:   6,
             10:  7,
             13:  8,
             15:  9,
             18: 10}
solar_epoch = 1954168 # Midnight prior to Meṣa Saṁkrānti of 0 ME; see Eade, Appendix II; and Irwin, 4:56
lunar_epoch = solar_epoch - Fraction(373,800) # midnight following the last new moon of 0 ME; see Irwin, 4:56

def lny(year):
    '''Compute the Julian Day of the 1st of Tagu preceding Meṣa Saṁkrānti for the year specified'''
    year = int(year)
    
    ratha = (year * sid_year) + Fraction(373, 800) # the extra fraction is the time from midnight to Meṣa Saṁkrānti
    ata_yet = solar_epoch + ratha # Meṣa Saṁkrānti for this year
    haragon = ceil(ratha) # Irwin, 4:57
    kaya = Fraction( (11 * haragon), 692) + Fraction(650, 692) # total tithis minus total days; Irwin, 4:59
    total_tithis = haragon + kaya # tithis since new moon preceding solar epoch; Irwin, 4:60
    luns = total_tithis // 30 # total months since the new moon preceding the epoch; Irwin, 4:60
    yet_lun = Fraction(total_tithis, 30) % 1 # time from preceding new moon to Meṣa Saṁkrānti, in fractions of a mean synodic month
    adimath = floor(luns * Fraction(7, 235)) # total leap months that have passed as of Meṣa Saṁkrānti; Irwin, 4:61
    adimath_theta = (luns * Fraction(7, 235)) % 1 # Irwin, 4:62
    awaman = yet_lun * 692
    epact = yet_lun * syn_month
    
    rasis = luns - adimath # Irwin, 4:61
    # if rasis % 12 == 0, Meṣa Saṁkrānti falls in Tagu
    # if rasis % 12 == 1, Meṣa Saṁkrānti falls in Kason
    newmoon = ceil(ata_yet - epact)

    if( rasis % 12 == 1):
        # solar new year falls in kason, which means we need to subtract 29 days to get the first of tagu
        newmoon -= 29

    # check if it's a leap year
    if(year % 19 not in leap_years):
        # normal year
       MONTHS = NORMAL
       next_moon = newmoon + 354 # 1 Tagu preceding next Meṣa Saṁkrānti
    else:
        # leap year
        # is it normal or long?
        tcp = (year // 19) * 7050 # total tithis of completed 19-year cycles; Irwin, 4:71
        full_moon_tithis = tcp + (30 * (year % 19) + watat_add[year % 19] + 14) # tithis from the start of the cycle to the full moon of Wahso 2; see Irwin, 4:71
        labyi_kaya = floor(Fraction( (11 * full_moon_tithis), 703) + Fraction(650,703) ) # Irwin, 4:72
        labyi_awaman = (Fraction( (11 * full_moon_tithis), 703) + Fraction(650,703) ) % 1 # Irwin, 4:72

        # Irwin defines the rule as follows:
        ## if labyi_awaman is less than in the previous leap year, Nayon gets a leap day
        ## this is because, by modulo arithmetic, the fractions have added up to a full day
        # I will define it as labyi_awaman being less than the amount it increases by between each leap year
        # labyi_awaman increases by 517/703 if leap years are two years apart,
        # and by 259/703 if leap years are three years apart (that's how modulo arithmetic works)
        # so if it's been two years since the last leap year and labyi_awaman is < 517/703, it's a long year
        # likewise if it's been three years and labyi_awaman is < 259/703

        if(year % 19 in (7, 15)):
            # two-year gap
            if(labyi_awaman < Fraction(517,703)):
                # long leap year
                next_moon = newmoon + 384 # 1 Tagu preceding next Meṣa Saṁkrānti
            else:
                # short leap year
                next_moon = newmoon + 383 # 1 Tagu preceding next Meṣa Saṁkrānti
        else:
            # three-year gap
            if(labyi_awaman < Fraction(259,703)):
                # long leap year
                next_moon = newmoon + 384 # 1 Tagu preceding next Meṣa Saṁkrānti
            else:
                # short leap year
                next_moon = newmoon + 383 # 1 Tagu preceding next Meṣa Saṁkrānti
    next_ata_yet = ata_yet + sid_year

    return(ata_yet, next_ata_yet, newmoon, next_moon)

def tojd(day, month, year):
    '''Convert a date in the Makaranta calendar to Julian Day'''
    day = int(day) - 1 # subtract 1 because computers count from 0
    month = str(month)
    year = str(year)
    
    if( (month == "Wahso 2") and (year not in leap_years) ):
        month = "Wahso"

    if(year[len(year) - 1:] == '*'):
        # user specified the month at the end of the lunar year, before the year number increments
        if(month not in ("Tagu", "Kason")):
            # can't happen
            end = False
            year = int(year[:len(year) - 1])
        else:
            end = True
            year = int(year[:len(year) - 1]) + 1
    else:
        year = int(year)
        end = False

    figures = lny(year)
    ata_yet = figures[0]
    next_ata_yet = figures[1]
    newmoon = figures[2]
    next_moon = figures[3]

    # which set of months to use
    if(next_moon - newmoon == 354):
        # normal year
        MONTHS = NORMAL
    elif(next_moon - newmoon == 383):
        # short leap year
        MONTHS = LEAP
    else:
        # long leap year
        MONTHS = LONG

    # OK. We now know when 1 Tagu falls.
    # We know how long the year is.
    # We know which set of months to use.
    # Now to account for the fact that the user might have specified a month at the end of the year instead of the beginning
    if(end):
        next_ata_yet = ceil(ata_yet + sid_year)
        if( (month == "Kason") and (next_moon + 29 + day < next_ata_yet) ):
            jday = next_moon + 29 + day
        elif(next_moon + day < next_ata_yet):
            jday = next_moon + day
        else:
            end = False
    if(not end):
         for m in MONTHS.keys():
             if(m == month):
                 break
             else:
                 newmoon += MONTHS[m]
    jday = newmoon + day    
    return jday

def fromjd(jday):
    '''Convert a Julian Day to a date in the Makaranta calendar'''
    jday = int(jday)

    year = (jday - solar_epoch) // sid_year
    while(lny(year)[2] > jday):
        year -= 1
    while(lny(year + 1)[2] <= jday):
        year += 1

    figures = lny(year)
    ata_yet = figures[0]
    next_ata_yet = figures[1]
    newmoon = figures[2]
    next_moon = figures[3]

    # which set of months to use
    if(next_moon - newmoon == 354):
        # normal year
        MONTHS = NORMAL
    elif(next_moon - newmoon == 383):
        # short leap year
        MONTHS = LEAP
    else:
        # long leap year
        MONTHS = LONG

    if(jday < ceil(ata_yet)):
        year = str(year - 1) + '*'

    # compute the month
    for m in MONTHS.keys():
        if(newmoon + MONTHS[m] <= jday):
            newmoon += MONTHS[m]
        else:
            break
    month = m

    day = jday - newmoon + 1 # add 1 because humans don't count from 0
    return (day, month, year)
