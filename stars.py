#!/usr/bin/python3

# This is a list of stars and their attributes for use in sidereal calculations.
#
# Unless otherwise stated, data is correct for J2000.0 and it taken from Wikipedia

# Attributes:
## ra2000: right ascension, in degrees
## dec2000: declination, in degrees
## distance: distance from the sun, in parsecs
## rv: radial velocity, in parsecs per year
## deltara: RA component of proper motion, in arcseconds per year
## deltadec: Dec component of proper motion, in arcseconds per year

from decimal import Decimal
from math import pi

mas2rad = Decimal(pi) / Decimal(180 * 3600000) # convert milliarcseconds to radians

class Star(object):
    """A celestial body, usually a star, but also works for planets, moons, and galaxies"""
    def __init__(self, ra, dec, distance, rv, dra, ddec):
        self.ra = ra # right ascension as of J2000.0, in DEGREES
        self.dec = dec # declination as of J2000.0, in DEGREES
        self.distance = distance # distance from the sun as of J2000.0, in PARSECS
        self.rv = rv # radial velocity as of J2000.0, in PARSECS PER YEAR
        self.dra = dra # deltaRA, right ascension component of proper motion, in RADIANS PER YEAR
        self.ddec = ddec # deltaDEC, declination component of peoper motion, in RADIANS PER YEAR

SIRIUS = Star( Decimal('101.2871553'), # ra
               Decimal('-16.71611586'), # dec
               Decimal('2.67'), # distance
               0 - (Decimal('5.50') / Decimal(977792)), # rv
               0 - (Decimal('546.01') * mas2rad), # dra
               0 - (Decimal('1223.07') * mas2rad)) # ddec

# Pleiades values are for Alcyone, the brightest star in the cluster
PLEIADES = Star( Decimal('56.87115417'), # ra
                 Decimal('24.10513611'), # dec
                 136, # distance
                 (Decimal('5.40') / 977792), # rv
                 (Decimal('19.34') * mas2rad), #dra
                 0 - (Decimal('43.67') * mas2rad)) # ddec

SPICA = Star( Decimal('201.2982458'), # ra
              0 - Decimal('11.16131944'), # dec
              77, # distance
              (Decimal(1) / Decimal(977792)), # rv
              0 - (Decimal('42.35') * mas2rad), # dra
              0 - (Decimal('30.67') * mas2rad)) # dded

BAQUA = Star( Decimal('322.889715458'), # ra
              Decimal('-5.57117555556'), # dec
              167, # distance
              Decimal('6.451') / 977792, # rv
              (Decimal('18.77') * mas2rad), # dra
              0 - (Decimal('8.21') * mas2rad)) # ddec

# Aries values are for 4 Arietis, the star with the smallest right ascension
ARIES = Star( Decimal('27.0454166667'), # ra
              Decimal('16.9556388889'), # dec
              87, # distance
              Decimal('5.7') / 977792, # rv
              (Decimal('65.608') * mas2rad), # dra
              0 - (Decimal('29.291') * mas2rad)) # ddec

REVATI = Star( Decimal('18.4382'), # ra
               Decimal('7.578382361'), # dec
               53, #distance
               Decimal('15.0') / 977792, # rv
               (Decimal('181.78') * mas2rad), # dra
               0 - (Decimal('40.34') * mas2rad)) # ddec

# Ashvin refers to Hamal, AKA Alpha Arietis
ASHVIN = Star( (30 + (7 * Decimal(15/60)) + (Decimal('10.4057') * Decimal(15/(60 * 60)))), # ra
               (23 + Decimal(27/60) + (Decimal('44.7032') / (60 * 60))), # dec
               Decimal('20.2'), # distance
               Decimal('-14.2') / 977792, # rv
               Decimal('188.55') * mas2rad, # dra
               Decimal('-148.08') * mas2rad) # ddec
               
# Shravishtha refers to Sualocin, AKA the brightest star in Alpha Delphini
SHRAVISHTHA = Star( ((20 * 15) + (39 * Decimal(15/60)) + (Decimal('38.28720') * Decimal(15/(60 * 60)))), # ra
                    (15 + Decimal(54/60) + (Decimal('43.4637') /(60 * 60))), # dec
                    78, # distance
                    Decimal('-3.40'), # rv
                    Decimal('53.82'), # dra
                    Decimal('8.47')) # ddec
