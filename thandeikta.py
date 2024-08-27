#!/usr/bin/python3

# A programme to convert between the Myanmar lunisolar calendar (Thandeikta system) and Julian Days                 

# Sources                                                                                                           
## The Burmese and Arakanese Calendars, AMB Iwin, Hanthawaddy Printing Works, 1909                                  
## Calendrical Systems of Mainland Sout-East Asia, JC Eade, E.J. Brill, 1995                                  
## Traditional Calendar of Myanmar (Burma), GK Chatterjee, Indian Journal of the History of Science, 33(2)1998 

from math import floor, ceil
from fractions import Fraction
from months import MYANMAR_NORMAL as NORMAL, MYANMAR_LEAP as LEAP, MYANMAR_LONG as LONG

# astronomical constants
sid_year = Fraction(56395952, 154400)
rasi = Fraction(sid_year, 12)
syn_month = rasi * Fraction(911, 939) # Irwin, 3:65

solar_epoch = 2355953 # Meṣa Saṃkrānti of 1100 ME; see Irwin, 4:55
lunar_epoch = solar_epoch - Fraction(17742,800) + Fraction(142,800) # midnight following the last new moon of 1099 ME; see Irwin, 4:55
#lunar_epoch = 2355921 # midnight following the last new moon of 1099 ME; see Irwin, 4:55

MONTH_LENGTHS = {354: NORMAL,
                 384: LEAP,
                 385: LONG}
def lny(year):
    '''Compute the Julian Day on which Lunar New Year falls, among other things'''
    year = int(year)

    days_expired = Fraction((year * 292207), 800) + Fraction(year, (193 * 800)) + Fraction(17742, 800) # Irwin, 4:55
    haragon = ceil(days_expired) # Irwin, 4:57
    kaya = ceil(Fraction((11 * haragon), 692) - Fraction(year, (25 * 692)) + Fraction(176,692)) # total tithis less total days; Irwin, 4:59
    #awaman = (Fraction((11 * haragon), 692) - Fraction(year, (25 * 692)) + Fraction(176,692)) % 1 # Irwin, 4:59
    total_tithis = haragon + kaya # Irwin, 4:59
    #luns = total_tithis // 30 # Irwin, 4:59
    yet_lun = total_tithis % 30

    ata_yet = ceil(solar_epoch + (year * sid_year))
    darkmoon = ata_yet - (syn_month * Fraction(yet_lun, 30))
    newmoon = ceil(darkmoon)

    return (ata_yet, yet_lun, newmoon)

    return(ata_yet, yet_lun, newmoon)

def fmw2(year):
    '''Compute some numbers relating to the 15th tithi of Wahso 2'''
    year = int(year)

    rasis_past = (12 * year) + 4 # Irwin, 4:65
    adimath = floor( Fraction((28 * rasis_past), 911) + Fraction(year, (475 * 911)) + Fraction(690, 911) ) # Irwin, 4:65
    adimath_theta = ( Fraction((28 * rasis_past), 911) + Fraction(year, (475 * 911)) + Fraction(690, 911) ) % 1 # Irwin, 4:65
    luns = rasis_past + adimath
    fullmoon_tithis = (30 * luns) + 14 # Irwin, 4:67
    kaya = floor( Fraction((11 * fullmoon_tithis), 703) + Fraction(year, (25 * 703)) + Fraction(176,703) ) # Irwin, 4:67
    awaman = ( Fraction((11 * fullmoon_tithis), 703) + Fraction(year, (25 * 703)) + Fraction(176,703) ) % 1 # Irwin, 4:67
    haragon = fullmoon_tithis - kaya # Irwin, 4:67
    kyammat_pon = Fraction( ((800 * haragon) - Fraction(year, 193) - 17742), 292207) % 1 # Irwin, 4:68
    thokdadein = floor(kyammat_pon / 800) # Irwin, 4:68
    ata_kyammat = Fraction(kyammat_pon, 800) % 1 # Irwin, 4:68

    return (thokdadein, ata_kyammat, awaman)

def yeartype(year):
    '''Is this a normal, leap, or long leap year?'''
    year = int(year)

    figures = lny(year)
    ata_yet = figures[0]
    yet_lun = figures[1]
    newmoon = figures[2]

    if( (yet_lun <= 26) and (yet_lun > lny(year - 1)[1]) ):
        # normal year, as per Irwin 4:85
        year_length = 354
    else:
        # leap year. but is there an extra day?    
        figures = fmw2(year)
        thokdadein = figures[0]
        ata_kyammat = figures[1]
        awaman = figures[2]
        
        solar_longitude = Fraction( ((1000 * ((800 * thokdadein) + ata_kyammat)) - (6 * thokdadein)), (13528 * 60)) # solar longitude expressed in degrees; see Irwin, 4:90
        lunar_difference = 12 * ((yet_lun + Fraction(awaman, 692) + (thokdadein * Fraction(703,692))) % 30) # distance between the sun and the moon, in degrees; see Irwin, 4:91
        dawaman = (Fraction((11 * thokdadein), 692) + Fraction(awaman, 692)) % 1 # Irwin, 4:93
        daily_difference = Fraction( (180 * dawaman), (173 * 60)) # Irwin, 4:93
        lunar_longitude = (solar_longitude + lunar_difference + daily_difference - Fraction(52,60)) % 360 # lunar longitude in degress; see Irwin, 4:94
        if( lunar_longitude < 266 + Fraction(40, 60) ):
            # long year
            year_length = 385
        else:
            year_length = 384

    return(year_length, newmoon, ata_yet)
        
        
def tojd(day, month, year):
    '''Given a date in the Thandeikta calendar, compute the corresponding Julian Day'''
    day = int(day) - 1 # subtract 1 because computers count from 0
    month = str(month)
    year = str(year)

    if( year[len(year) - 1:] == '*' ):
        # user has specified the time before solar new year
        if( month == "Tagu" ):
            year = int(year[:len(year)]) + 1
        else:
            year = int(year[:len(year)])
    else:
        year = int(year)
    year -= 1100 # subtract 1100 from the calendar year to get years since the epoch

    figures = yeartype(year)
    jday = ceil(figures[1])
    MONTHS = MONTH_LENGTHS[figures[0]]

    for m in MONTHS.keys():
        if(m == month):
            break
        else:
            jday += MONTHS[m]

    jday += day

    return jday

def fromjd(jday):
    '''Convert a Julian Day to a date in the Thandeikta calendar'''
    jday = int(jday)

    # compute the year
    year = ((jday - solar_epoch) // sid_year) + 1100
    while(lny(year)[2] > jday):
        year -= 1
    while(lny(year + 1)[2] <= jday):
        year += 1

    figures = yeartype(year)
    MONTHS = MONTH_LENGTHS[figures[0]]
    newmoon = ceil(figures[1])
    ata_yet = ceil(figures[2])
    year += 1100 # add 1100 to years since the epoch to get the calendar year
    if(jday < ata_yet):
        year = str(year - 1) + '*'

    # compute the month
    if(newmoon + 29 > jday):
        month = "Tagu"
    else:
        for m in MONTHS.keys():
            if(newmoon + MONTHS[m] > jday):
                month = m
                break
            else:
                newmoon += MONTHS[m]

    # compute the day
    day = jday - newmoon + 1 # add 1 because humans don't count from 0

    return (day, month, year)
