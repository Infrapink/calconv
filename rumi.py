#!/usr/bin/python3

#
# Convert between the skipping Rumi Calendar and Julian Day
#

import months
import tab_islamic

cycle4 = (4 * 365) + 1
skip_epoch = 1948303
neo_epoch = 2393178
skip_years = (13,47,80,114,147,181,214,248,282,315,349,382,416,449,483,517,550,584,617,651,684,718,751,785,819,852,886,819,953,986,1020,1053,1087,1121,1154,1188,1221,1255)


def tojd(day, month, year):

    day = int(day)
    month = month.title()
    year = int(year)

    if year >= 1256:
        # years after the abolition of skipping
        jday = neo_epoch # 1 Mart 1256
        y = 1256
        cycles = (year - y) // 4
        y += (4 * cycles)
        jday += (cycle4 * cycles)

        while y < year:
            if y % 4 == 3:
                jday += 366
            else:
                jday += 365
            y += 1

        if year % 4 == 3:
            m = months.TURKISH_LEAP
        else:
            m = months.TURKISH_NORMAL
        

    elif year > 0:
        # positive years when skipping was carried out
        jday = skip_epoch
        skip = 0 # used to calculate leap years

        if year in skip_years:
            year += 1

        y = 1
        z = 1
        cycles = (year - y) // 4
        y += (4 * cycles)
        jday = skip_epoch + (cycle4 * cycles)

        while z <= y:
            if z in skip_years:
                y += 1
                skip += 1
            z += 1

        while y < year:
            if y in skip_years:
                skip += 1                
            elif (y - skip) % 4 == 1:
                jday += 366
            else:
                jday += 365
            y += 1

        if (year - skip) % 4 == 1:
            m = months.TURKISH_LEAP
        else:
            m = months.TURKISH_NORMAL

    else:
        # negative years.
        nyd = skip_epoch
        y = 0

        res = tab_islamic.tojd(1, "Muharram", year)
        next_res = tab_islamic.tojd(1, "Muharram", (year + 1))

        cycles = (nyd - res) // cycle4
        nyd -= (cycle4 * cycles)
        y -= (4 * cycles)

        while nyd > res:
            y -= 1
            if abs(y) % 4 == 3:
                nyd -= 366
            else:
                nyd -= 365

        if abs(y) % 4 == 3:
            next_nyd = nyd + 366
            m = months.TURKISH_LEAP
        else:
            next_nyd = nyd + 365
            m = months.TURKISH_NORMAL

        if res > nyd and next_res < next_nyd:
            jday = next_nyd
        else:
            jday = nyd

        
    for i in m.keys():
        if i == month:
            jday += day - 1
            break
        else:
            jday += m[i]
                
    return jday

def fromjd(jday, m_year):
    """Convert a Julian day to a date in the Rumi calendar."""
    jday = int(jday)
    m_year = int(m_year)
    
    year = 0
    month = ""
    day = 0

    if jday >= neo_epoch:
        # positive dates after skipping was abolished
        nyd = neo_epoch
        curryear = False
        year = 1256
        cycles = (jday - nyd) // cycle4
        year += (4 * cycles)
        nyd += (cycle4 * cycles)
        while curryear == False:
            if year % 4 == 3:
                if jday - nyd < 366:
                    curryear = True
                else:
                    year += 1
                    nyd += 366
            else:
                if jday - nyd < 365:
                    curryear = True
                else:
                    year += 1
                    nyd += 365

        if year % 4 == 3:
            m = months.TURKISH_LEAP
        else:
            m = months.TURKISH_NORMAL

    elif jday >= skip_epoch:
        # positive dates during the skipping era
        nyd = skip_epoch
        skip = 0 # used to calculate leap years
        curryear = False
        year = 1
        cycles = (jday - nyd) // cycle4
        year += (4 * cycles)
        nyd += (cycle4 * cycles)

        y = 1
        while y <= year:
            if y in skip_years:
                year += 1
                skip += 1
            y += 1

        while curryear == False:
            if year in skip_years:
                skip += 1
                year += 1
            elif (year - skip) % 4 == 1:
                if jday - nyd < 366:
                    curryear = True
                else:
                    nyd += 366
                    year += 1
            else:
                if jday - nyd < 365:
                    curryear = True
                else:
                    nyd += 365
                    year += 1

        if (year - skip) % 4 == 2:
            m = months.TURKISH_LEAP
        else:
            m = months.TURKISH_NORMAL
        
        
    else:
        # negative dates
        y = 0
        nyd = skip_epoch
        
        m_nyd = tab_islamic.tojd(1, "Muharram", m_year)
        k_nyd = tab_islamic.tojd(1, "Muharram", (m_year + 1))

        cycles = (nyd - jday) // cycle4
        y -= (4 * cycles)
        nyd -= (cycle4 * cycles)
        
        while nyd > jday:
            y -= 1
            if abs(y) % 4 == 3:
                nyd -= 366
            else:
                nyd -= 365

        if abs(y) % 4 == 3:
            next_nyd = nyd + 366
        else:
            next_nyd = nyd + 365

        if next_nyd > k_nyd:
            year = m_year + 1
        else:
            year = m_year
        
        if abs(y) % 4 == 3:
            m = months.TURKISH_LEAP
        else:
            m = months.TURKISH_NORMAL

    delta = jday - nyd
    for i in m.keys():
        if delta <= m[i]:
            month = i
            day = delta + 1
            break
        else:
            delta -= m[i]

    return (day,month,year)

