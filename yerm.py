#!/usr/bin/python3

# Convert between Julian Days and Karl Palmen's Yerm calendar

epoch = 2450399

y17 = (9 * 30) + (8 * 29)
y15 = (8 * 30) + (7 * 29)
cycle3 = y17 + y17 + y15
cycle52 = (17 * cycle3) + y17



def fromjd(jday):
    '''Convert a Julian Day to a date in the Yerm calendar'''
    jday = int(jday)

    # compute the yerm
    cycles = (jday - epoch) // cycle52
    yerm = 52 * cycles
    newmoon = epoch + (cycles * cycle52)
    while (newmoon + cycle52 <= jday):
        newmoon += cycle52
        yerm += 52
    while (newmoon > jday):
        newmoon -= cycle52
        yerm -= 52
    while (newmoon + cycle3 <= jday):
        newmoon += cycle3
        yerm += 3
    while (newmoon + y17 <= jday):
        newmoon += y17
        yerm += 1

    # compute the month
    month = 2 * ((jday - newmoon) // 59)
    newmoon += 59 * (month // 2)
    if (newmoon + 30 <= jday):
        newmoon += 30
        month += 1
    month += 1 # add 1 because computers count from 0

    # compute the night
    night = jday - newmoon + 1 # add 1 because computers count from 0

    return (night, month, yerm)

def tojd(night, month, yerm):
    '''Convert a date in the Yerm calendar to a Julian Day'''
    night = int(night) - 1 # subtract 1 because humans don't count from 0
    month = int(month) - 1 # subtract 1 because humans don't count from 0
    yerm = int(yerm)

    # account for the yerm
    cycles = yerm // 52
    jday = epoch + (cycles * cycle52)
    y = 52 * cycles
    while (y + 52 <= yerm):
        jday += cycle52
        y += 52
    while (y > yerm):
        jday -= cycle52
        y -= 52
    while (y + 3 <= yerm):
        jday += cycle3
        y += 3
    while (y < yerm):
        jday += y17
        y += 1

    # account for the month
    jday += (59 * (month // 2))
    if (month % 2 == 1):
        jday += 30

    # account for the night
    jday += night

    return jday
