#!/usr/bin/python

# Convert between the Mandaean calendar and Julian Day

epoch = -175444147

MONTHNO = {"Daula": 0,
           "Nuna": 1,
           "'mbra": 2,
           "Taura": 3,
           "Ṣilmia": 4,
           "Sarṭana": 5,
           "Aria": 6,
           "Shumbulta": 7,
           "Extra days": 8,
           "Qaina": 9,
           "Arqba": 10,
           "Hiṭia": 11,
           "Gadia": 12}

NUMON = {0: "Daula",
         1: "Nuna",
         2: "'mbra",
         3: "Taura",
         4: "Ṣilmia",
         5: "Sarṭana",
         6: "Aria",
         7: "Shumbulta",
         8: "Extra days",
         9: "Qaina",
         10: "Arqba",
         11: "Hiṭia",
         12: "Gadia"}

def tojd(day, month, year):
    day = int(day)
    month = str(month)
    year = int(year)

    if year >= 0:
        jday = epoch + ((year - 1) * 365)
    else:
        jday = epoch + (year * 365)

    jday = jday + (30 * MONTHNO[month])
    if MONTHNO[month] > 8:
        jday -= 25
    jday += (day - 1)
    return jday

def fromjd(jday):
    jday = int(jday)

    year = (jday - epoch) // 365
    dehwa = epoch + (365 * year)
    if year >= 0:
        year += 1
    while dehwa > jday:
        year -= 1
        dehwa -= 365
    while (dehwa + 365) <= jday:
        year += 1
        dehwa += 365
        
    if (jday - dehwa) <= 244:
        m = (jday - dehwa) // 30
        day = 1 + ((jday - dehwa) % 30)
    else:
        m = 9 + ((jday - dehwa - 245) // 30)
        day = 1 + ((jday - dehwa - 245) % 30)

    month = NUMON[m]

    return(day, month, year)
