#!/usr/bin/python3

# Convert between the Indian national calendar and Julian Day

epoch = 1749629
quad = (4 * 365) + 1 # four years, including leap year
century = (100 * 365) + 24 # 100 years, with leap years
qc = (400 * 365) + 97 # 400 years, with leap years
j23 = (5 * quad) + (3 * 365)

MONTHNO = {"Chaitra": 0,
           "Vaisākha": 1,
           "Jyēshtha": 2,
           "Āshādha": 3,
           "Shrāvana": 4,
           "Bhādra": 5,
           "Āshwin": 6,
           "Kārtika": 7,
           "Agrahāyana": 8,
           "Pausha": 9,
           "Māgha": 10,
           "Phālguna": 11}

NUMON = {0: "Chaitra",
         1: "Vaisākha",
         2: "Jyēshtha",
         3: "Āshādha",
         4: "Shrāvana",
         5: "Bhādra",
         6: "Āshwin",
         7: "Kārtika",
         8: "Agrahāyana",
         9: "Pausha",
         10: "Māgha",
         11: "Phālguna"}

def yearlen(year):
    '''Is it a leap year or a normal year?'''
    year = int(year)

    if year % 400 == 322:
        ans = 366
    elif year % 100 == 22:
        ans = 365
    elif year % 4 == 2:
        ans = 366
    else:
        ans = 365

    return ans

def fromjd(jday):
    '''Convert a Julian Day into a date in hte Indian national caldndar'''
    jday = int(jday)

    cycles = (jday - epoch) // qc
    year = 400 * cycles
    sankranti = epoch + (cycles * qc)
    while sankranti > jday:
        year -= 400
        sankranti -= qc
    while sankranti + qc <= jday:
        year += 400
        sankranti += qc

    # jump over the non-leap year
    if (jday - sankranti) >= j23:
        sankranti += j23
        year += 23

    if (jday - sankranti) >= (2 * century):
        sankranti += 2 * century
        year += 200
    elif (jday - sankranti) >= century:
        sankranti += century
        year += 100

    quads = (jday - sankranti) // quad
    year += (4 * quads)
    sankranti += (quads * quad)

    while sankranti + yearlen(year) <= jday:
        sankranti += yearlen(year)
        year += 1

    # sankranti is now equal to New Year's Day

    if yearlen(year) == 366:
        # leap year
        if jday - sankranti < (6 * 31):
            month = NUMON[(jday - sankranti) // 31]
            day = ((jday - sankranti) % 31) + 1
        else:
            alpha = sankranti + (6 * 31)
            m = (jday - alpha) // 30
            month = NUMON[m + 6]
            day = ((jday - alpha) % 30) + 1
    else:
        # normal year
        if jday - sankranti < 30:
            month = "Chaitra"
            day = jday - sankranti + 1
        elif jday < sankranti + 30 + (5 * 31):
            alpha = sankranti + 30
            m = (jday - alpha) // 31
            month = NUMON[m + 1]
            day = ((jday - alpha) % 31) + 1
        else:
            alpha = sankranti + 30 + (5 * 31)
            m = (jday - alpha) // 30
            month = NUMON[m + 6]
            day = ((jday - alpha) % 30) + 1

    return(day, month, year)

def tojd(day, month, year):
    '''Convert a date in the Indian national calendar to a Julian DAy'''
    day = int(day)
    month = str(month)
    year = int(year)

    cycles = year // 400
    jday = epoch + (cycles * qc)
    y = 400 * cycles
    while y > year:
        y -= 400
        jday -= qc
    while y + 400 <= year:
        y += 400
        jday += qc

    if year - y >= 23:
        y += 23
        jday += j23

    if year - y >= 200:
        y += 200
        jday += (2 * century)
    elif year - y >= 100:
        y += 100
        jday += century

    quads = (year - y) // 4
    y += (4 * quads)
    jday += (quads * quad)

    while y < year:
        jday += yearlen(y)
        y += 1

    if yearlen(year) == 366:
        # leap year
        if MONTHNO[month] < 6:
            jday += (31 * MONTHNO[month])
        else:
            jday += (6 * 31)
            jday += (31 * (MONTHNO[month] - 6))
    else:
        # normal year
        if month == "Chaitra":
            jday += 0
        elif MONTHNO[month] < 6:
            jday += 30
            jday += (31 * (MONTHNO[month] - 1))
        else:
            jday += 30 + (5 * 31)
            jday += (30 * (MONTHNO[month] - 6))

    jday = jday + day - 1

    return jday
