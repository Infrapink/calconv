#!/usr/bin/python3

# A programme to convert between the Myanmar lunisolar calendar (Thandeikta system) and Julian Days                 

# Sources                                                                                                           
## The Burmese and Arakanese Calendars, AMB Iwin, Hanthawaddy Printing Works, 1909                                  
## Calendrical Systems of Mainland Sout-East Asia, JC Eade, E.J. Brill, 1995                                  
## Traditional Calendar of Myanmar (Burma), GK Chatterjee, Indian Journal of the History of Science, 33(2)1998

# Literally half the functions here are redundant. I have left them in, commented out, just in case they might be useful in a future update.

from math import floor, ceil
from fractions import Fraction
from months import MYANMAR as MONTHS, MYANMAR_MONTH_LENGTHS as MONTH_LENGTHS

# astronomical constants
sid_year = Fraction(56395952, 154400)
epoch = 2355960 # Midnight PRECEDING Meṣa Saṃkrānti of 1100 ME; see Irwin, 4:55

def days_expired(year):
    '''Returns days expired as of solar new year'''
    # Irwin, 4:55
    # when calling this function, subtract 1100 from the actual year for the maths to work
    year = int(year) # ratha

    ans = Fraction(((292207 * year) + Fraction(year, 193) + 17742), 800)
    return ans

def solar_haragon(year):
    '''Returns the haragon as of solar new year'''
    # Irwin, 4:57
    # when calling this function, subtract 1100 from the actual year for the maths to work
    return ceil(days_expired(int(year)))

#def solar_kaya(year):
    #'''Returns the difference between total tithis and total days as of solar new year'''
    # Irwin, 4:59
    # when calling this function, subtract 1100 from the actual year for the maths to work

    #ans = floor(Fraction(((11 * solar_haragon(int(year))) - Fraction(year, 25) + 176), 692)) # TITHIS1
    #return ans

#def solar_awaman(year):
    #'''Returns the awaman as of solar new year'''
    # Irwin, 4:59
    # when calling this function, subtract 1100 from the actual year for the maths to work

    #ans = Fraction(((11 * solar_haragon(int(year))) - Fraction(year, 25) + 176), 692) % 1 # fraction of a TITHI
    #return ans

#def solar_tithis_expired(year):
    #'''Returns the total tithis between the epoch and solar new year'''
    # Irwin, 4:59—60
    # when calling this function, subtract 1100 from the actual year for the maths to work

    #ans = solar_haragon(year) + solar_kaya(year)
    #return ans

#def sandra_matha(year):
    #'''Returns number of full months past between the epoch and solar new year'''
    # Irwin, 4:60
    # when calling this function, subtract 1100 from the actual year for the maths to work

    #return (solar_tithis_expired(int(year)) // 30)

#def epact(year):
    #'''Return the epact as of solar new year, in TITHIS'''
    # Irwin, 4:60
    # when calling this function, subtract 1100 from the actual year for the maths to work
    #year = int(year)

    #ans = (solar_tithis_expired(year) % 30) + solar_awaman(year)
    #return ans # this is in TITHIS, not days

def adimath(year, m):
    '''Return the total leap months past for a given month in a given year'''
    # Irwin, 4:65
    # when calling this function, subtract 1100 from the year for the maths to work
    year = int(year)
    m = int(m) # number of the month. Tagu is 0

    solar_months = (12 * year) + m
    ans = floor(Fraction(((28 * solar_months) + Fraction(year, 475) + 690), 911))
    return ans

#def adimath_theta(year, m):
    #'''Returns the epact of the leap month for a given month in a given year'''
    # Irwin, 4:65
    # when calling this function, subtract 1100 from the year for the maths to work
    #year = int(year)
    #m = int(m) # number of the month. Tagu is 0

    #solar_months = (12 * year) + m
    #ans = Fraction(((28 * solar_months) + Fraction(year, 475) + 690), 911) % 1
    #return ans

def lunar_kaya(year, m):
    '''Returns the tithis less days since the epoch as of midnight on the 0th day of the month'''
    # Irwin, 4:67
    # when calling this function, subtract 1100 from the year for the maths to work
    year = int(year) # Ratha
    m = int(m) # number of the month. Tagu is 0

    lunar_months = (12 * year) + adimath(year, m)
    tithis = 30 * lunar_months

    ans = floor(Fraction(((11 * tithis) - Fraction(year, 25) + 176), 703))
    return ans

#def lunar_awaman(year, m):
    #'''Returns the awaman as of midnight on the 0th day of the month'''
    # Irwin, 4:67
    # when calling this function, subtract 1100 from the year for the maths to work
    #year = int(year) # Ratha
    #m = int(m) # number of the month. Tagu is 0

    #lunar_months = (12 * year) + m + adimath(year, m)
    #tithis = 30 * lunar_months

    #ans = Fraction(((11 * tithis) - Fraction(year, 25) + 176), 703) % 1
    #return ans

def lunar_haragon(year, m):
    '''Returns days since the epoch as of midnight on the 0th day of the month'''
    # Irwin, 4:67
    # when calling this functions, subtract 100 from the year for the maths to work
    year = int(year) # Ratha
    m = int(m) # number of the month. Tagu is 0

    lunar_months = (12 * year) + m + adimath(year, m)
    tithis = 30 * lunar_months

    ans = tithis - lunar_kaya(year, m)
    return ans

#def kyammat_pon(year, m):
    #'''Return the time since Meṣa Saṁkranti, in KYAMMATS'''
    # Irwin, 4:68
    # when calling this function, subtract 1100 from the year for the maths to work
    #year = int(year) # Ratha
    #m = int(m) # number of the month. Tagu is 0

    # ratha is the year number as of the 0th day of the month
    # note that the year number increments on solar new year,
    # which is always some ways into Tagu, and sometimes a few days into Kason
    #ratha = Fraction(((800 * lunar_haragon(year, m)) - Fraction(year, 193) - 17742), 292207)
    #ans = ratha % 1 # KYAMMATS from solar new year to 0th day of the month
    
    #return ans

#def thokdadein(year, m):
    #'''Returns days since midnight of solar new year'''
    # Irwin, 4:68
    # when calling this function, subtract 1100 from the year for the maths to work
    #year = int(year) # Ratha
    #m = int(m) # number of the month. Tagu is 0

    #return floor(kyammat_pon(year, m) // 800) # days since midnight of solar new year

#def ata_kyammat(year, m):
    #'''Returns the difference between the 0th day of the month and solar new year plus thokdadein'''
    # Irwin, 4:68
    # whel calling this function, subtract 1100 from the year for the maths to work
    #year = int(year) # Ratha
    #m = int(m) # number of the month. Tagu is 0

    #return (Fraction(kyammat_pon, 800) % 1)

def lny(year):
    '''Return the nominal Julian Day of 1 Tagu (lunar new year) for a given year'''
    # when calling this function, subtract 1100 from the year for the maths to work.

    return (epoch + lunar_haragon(int(year), 0))

def sny(year):
    '''Return the Julian Day of Meṣa Saṁkranti (solar new year) for a given year'''
    # when calling this function, subtract 1100 from the year for the maths to work

    return (epoch + solar_haragon(int(year)))

def year_length(year):
    '''Return the number of days in the year, and the actual date of 1 Tagu'''
    # Irwin describes the formal rules for the number of days in the year in 4:79—99
    # But because I have a computer, I can directly compute the Julian Days when each lunar year begins
    # and subtract one from the other
    #
    # this function returns a tuple, called ans
    # ans(0) is the days in the year
    # ans(1) is the number of days which lny(year) must be adjusted by to start on the correct day
    #
    # it's honestly a bit kludgey but I think it works
    year = int(year)

    if (lny(year + 1) - lny(year) == 383):
        # year too short, so needs to take a day from the next or previous year (inclusive OR)
        if ( (lny(year) - lny(year - 1) == 355) and (lny(year + 2) - lny(year + 1) == 355) ):
            # flanked by years which would be 355 days long
            # move lunar new year back one day, and moved next year's lunar new year forward one day
            ans = (385, lny(year) - 1)
        elif (lny(year) - lny(year - 1) == 355):
            # last year was too long, so its lunar new year is moved back one day
            # but next year is the right length, so this year is only 384 days long, not 385
            ans = (384, lny(year) - 1)
        else:
            # last year is the right length, so this year's lunar new year doesn't get pushed back one day
            ans = (384, lny(year))
    elif (lny(year + 1) - lny(year) == 355):
        # year is too long, so needs to give up a day to the previous xor next year
        if (lny(year) - lny(year - 1) == 354):
            # last year was the right length, so can't take a day from it
            ans = (354, lny(year))
        elif (lny(year + 2) - lny(year + 1) == 354):
            # next year is the right length, so need to give up a day to last year, moving lunar new year forward a day
            ans = (354, lny(year) + 1)
        elif (lny(year) - lny(year - 1) < 385):
            # move lunar new year forward a day to make last year the right length
            ans = (354, lny(year) + 1)
        elif (lny(year + 1) - lny(year) < 385):
        #else:
            # give up the last day of the year to make next year the right length
            ans = (354, lny(year))
        else:
            print("Something you haven't accounted for!")
    else:
        # no adjustment necessary
        ans = ( (lny(year + 1) - lny(year)), lny(year) )
    return ans

def fromjd(jday):
    '''Convert a Julian Day into a date in the Thandeikta calendar'''
    jday = int(jday) # Julian Day in question

    # compute the year
    year = (jday - epoch) // sid_year
    while (year_length(year)[1] > jday):
        year -= 1
    while (year_length(year + 1)[1] <= jday):
        year += 1
    figures = year_length(year)        
    if (jday < sny(year)):
        # specified day comes before solar new year
        year = str(year + 1100 - 1) + '*'
    else:
        # specified day is after solar new year
        year += 1100

    # compute the month
    newmoon = figures[1] # 1 Tagu
    m = 0
    while (newmoon + MONTH_LENGTHS[figures[0]][m] <= jday):
        newmoon += MONTH_LENGTHS[figures[0]][m]
        m += 1
    month = MONTHS[m]

    # compute the day
    day = jday - newmoon + 1 # add 1 because humans don't count from 0

    return (day, month, year)

def tojd(day, month, year):
    '''Convert a date in the Thandeikta calendar to a Julian Day'''
    day = int(day) - 1 # subtract 1 because computers count from 0
    month = str(month)
    year = str(year)
    # remove the asterisk from the year
    if (year[len(year) - 1:] == '*'):
        year = int(year[:len(year) - 1]) + 1
    else:
        year = int(year)
    year -= 1100 # account for the epoch being in 1100 ME

    # account for the year
    figures = year_length(year)
    jday = figures[1]

    # account for the month
    m = 0
    if ( (month == "Wahso 2") and (figures[0] == 354)):
        # user specified the leap month in a normal year
        month = "Wahso"
    while (MONTHS[m] != month):
        jday += MONTH_LENGTHS[figures[0]][m]
        m += 1

    # account for the day
    jday += day
    return jday
