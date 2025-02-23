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

ALCYONE = Star( Decimal('56.87115417'), # ra
                Decimal('24.10513611'), # dec
                136, # distance
                (Decimal('5.40') / 977792), # rv
                (Decimal('19.34') * mas2rad), #dra
                0 - (Decimal('43.67') * mas2rad)) # ddec

ALDEBARAN = Star( (4 * 15) + (35 * Decimal(15/60)) + (Decimal('55.23907') * Decimal(15/(60 * 60))), # ra
                  16 + Decimal(30/60) + (Decimal('33.4885') / 3600), # dec
                  20, # distance
                  Decimal('54.26') / 977792, # rv
                  Decimal('63.45') * mas2rad, # dra
                  Decimal('-188.94') * mas2rad) # ddec

ALNILAM = Star( (5 * 15) + (36 * Decimal(15/60)) + (Decimal('12.8') * Decimal(15/3600)), # ra
                (-1) - Decimal(12/60) - (Decimal('6.9') / 3600), # dec
                361, # distance
                Decimal('25.9') / 977792, # rv
                Decimal('1.49') * mas2rad, # dra
                Decimal('-1.06') * mas2rad) # ddec

ALNITAK = Star( (5 * 15) + (40 * Decimal(15/60)) + (Decimal('45.52666') * Decimal(15/3600)), # ra
                (-1) - (Decimal(56/60)) - (Decimal('34.2649') / 3600), # dec
                387, # distance
                Decimal('18.5')	/ 977792, # rv
                Decimal('3.19') * mas2rad, # dra
                Decimal('2.03') * mas2rad) # ddec

# Aries values are for 4 Arietis, the star with the smallest right ascension
ARIES = Star( Decimal('27.0454166667'), # ra
              Decimal('16.9556388889'), # dec
              87, # distance
              Decimal('5.7') / 977792, # rv
              (Decimal('65.608') * mas2rad), # dra
              0 - (Decimal('29.291') * mas2rad)) # ddec

BAQUA = Star( Decimal('322.889715458'), # ra
              Decimal('-5.57117555556'), # dec
              167, # distance
              Decimal('6.451') / 977792, # rv
              (Decimal('18.77') * mas2rad), # dra
              0 - (Decimal('8.21') * mas2rad)) # ddec

BELLATRIX = Star( (5 * 15) + (25 * Decimal(15/60)) + (Decimal('7.86325') * Decimal(15/3600)), # ra
                  6 + Decimal(20/60) + (Decimal('58.9318') / 3600), # dec
                  77, # distance
                  Decimal('18.2') / 977792, # rv
                  Decimal('-8.11') * mas2rad, # dra
                  Decimal('-12.88') * mas2rad) # ddec

BETELGEUSE = Star( (5 * 15) + (55 * Decimal(15/60)) + (Decimal('10.30536') * Decimal(15/3600)), # ra
                   7 + Decimal(24/60) + (Decimal('25.4304') / 3600), # dec
                   125, # distance; there is scientific controversy, with some evidence pointing to 168.1 parsecs
                   Decimal('21.91') / 977792, # rv
                   Decimal('26.42') * mas2rad, # dra
                   Decimal('9.60') * mas2rad) # ddec

HAMAL = Star( (30 + (7 * Decimal(15/60)) + (Decimal('10.4057') * Decimal(15/(60 * 60)))), # ra
              (23 + Decimal(27/60) + (Decimal('44.7032') / 3600)), # dec
              Decimal('20.2'), # distance
              Decimal('-14.2') / 977792, # rv
              Decimal('188.55') * mas2rad, # dra
              Decimal('-148.08') * mas2rad) # ddec

MINTAKA = Star( (5 * 15) + (32 * Decimal(15/60)) + (Decimal('0.40009') * Decimal(15/3600)), # ra
                0 - Decimal(17/60) - (Decimal('56.7424') / 3600), # dec
                380, # distance
                Decimal('18.5') / 977792, # rv
                Decimal('0.64') * mas2rad, # dra
                Decimal('-0.69') * mas2rad) # ddec

# alpha trianguli
MOTHALLA = Star( (1 * 15) + (53 * Decimal(15/60)) + (Decimal('4.90710') * Decimal(15/3600)), # ra
                 29 + Decimal(34/60) + (Decimal('43.7801') / 3600), # dec
                 Decimal('19.42'), # distance
                 Decimal('-12.6') / 977792, # rv
                 Decimal('10.82') * mas2rad, # dra
                 Decimal('-234.24') * mas2rad) # ddec
                                        

PROCYON = Star( 15 * (7 + Decimal(39/60) + (Decimal('18.1195') / 3600)), # ra
                5 + Decimal(13/60) + (Decimal('29.9552') / 3600), # dec
                Decimal('3.51'), # distance
                Decimal('-3.2') / 977792, # rv
                Decimal('-714.59') * mas2rad, # dra
                (0 - Decimal('1036.8')) * mas2rad) # ddec

REVATI = Star( Decimal('18.4382'), # ra
               Decimal('7.578382361'), # dec
               53, #distance
               Decimal('15.0') / 977792, # rv
               (Decimal('181.78') * mas2rad), # dra
               0 - (Decimal('40.34') * mas2rad)) # ddec

RIGEL = Star( ((5 * 15) + (14 * Decimal(15/60)) + (Decimal('32.27210') * Decimal(15/(60 * 60))) ), # ra
              (-8) - Decimal(12/60) - (Decimal('5.8981') / 3600), # dec
              260, # distance
              Decimal('17.8') / 977792, # rv
              Decimal('1.31') * mas2rad, # dra
              Decimal('0.5') * mas2rad) # ddec

SHERATAN = Star( (15 + (54 * Decimal(15/60)) + (Decimal('38.41099') * Decimal(15/(60 * 60)))), # ra
                 20 + Decimal(48/60) + (Decimal('28.9133') / 3600), # dec
                 Decimal('17.91'), # distance
                 Decimal('-1.9') / 977792, # rv
                 Decimal('98.74') * mas2rad, #dra
                 Decimal('-110.41') * mas2rad) # ddec


# Shravishtha refers to Sualocin, AKA the brightest star in Alpha Delphini
SHRAVISHTHA = Star( ((20 * 15) + (39 * Decimal(15/60)) + (Decimal('38.28720') * Decimal(15/(60 * 60)))), # ra
                    15 + Decimal(54/60) + (Decimal('43.4637') / 3600), # dec
                    78, # distance
                    Decimal('-3.40'), # rv
                    Decimal('53.82'), # dra
                    Decimal('8.47')) # ddec

SIRIUS = Star( Decimal('101.2871553'), # ra
               Decimal('-16.71611586'), # dec
               Decimal('2.67'), # distance
               0 - (Decimal('5.50') / Decimal(977792)), # rv
               0 - (Decimal('546.01') * mas2rad), # dra
               0 - (Decimal('1223.07') * mas2rad)) # ddec

SPICA = Star( Decimal('201.2982458'), # ra
              0 - Decimal('11.16131944'), # dec
              77, # distance
              (Decimal(1) / Decimal(977792)), # rv
              0 - (Decimal('42.35') * mas2rad), # dra
              0 - (Decimal('30.67') * mas2rad)) # dded

# synonyms
ASHVIN = HAMAL
PLEIADES = ALCYONE
