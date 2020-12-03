#!/usr/bin/python

# Convert between the Mesoamerican Long Count and Julian Day.

kinlen = 1
uinlen = 20
tunlen = 360
katlen = 20 * tunlen
baklen = 20 * katlen
piklen = 20 * baklen

epoch = 584282

def tojd(piktun, baktun, katun, tun, uinal, kin):
    piktun = int(piktun)
    baktun = int(baktun)
    katun = int(katun)
    tun = int(tun)
    uinal = int(uinal)
    kin = int(kin)

    days = (piktun * piklen) + (baktun * baklen) + (katun * katlen) + (tun * tunlen) + (uinal * uinlen) + (kin * kinlen)
    jday = epoch + days
    return jday

def fromjd(jday):
    jday = int(jday)

    if jday >= epoch:
        # non-negative piktun
        delta = jday - epoch
        piktun = delta // piklen
        delta %= piklen
    else:
        # negative piktun
        pstart = epoch
        piktun = 0
        while pstart > jday:
            pstart -= piklen
            piktun -= 1
        delta = jday - pstart

    baktun = delta // baklen
    delta %= baklen

    katun = delta // katlen
    delta %= katlen

    tun = delta // tunlen
    delta %= tunlen

    uinal = delta // uinlen
    kin = delta % uinlen

    return (piktun, baktun, katun, tun, uinal, kin)
