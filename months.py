#!/usr/bin/python

# This is a set of months for use in calconv

# Months for the Julian and Gregorian Calendars
#
# The Gregorian Calendar begins on Julian Day 1721425.
# The Julian Calendar begins on Julian Day 1721423.

CAESAR_MONTHS_NORMAL = {"January":31,
                         "February": 28,
                         "March": 31,
                         "April": 30,
                         "May": 31,
                         "June": 30,
                         "July": 31,
                         "August": 31,
                         "September": 30,
                         "October": 31,
                         "November": 30,
                         "December": 31}

CAESAR_MONTHS_LEAP = {"January":31,
                      "February": 29,
                      "March": 31,
                      "April": 30,
                      "May": 31,
                      "June": 30,
                      "July": 31,
                      "August": 31,
                      "September": 30,
                      "October": 31,
                      "November": 30,
                      "December": 31}

# Months for the Ethiopian and Coptic Calendars
# Each year is associated with one of the four gospel authors, following the cycle John, Matthew, Mark, Luke (Luke years are leap years)

# The Ethiopian calendar starts on Gregorian date 29/08/8, which is Julian Day 1724222.
# Like with the Julian and Coptic Calendars, years divisible by 4 are leap years
# Apparently it does have a year 0, which makes calculations easier
ETHIOPIAN_MONTHS_NORMAL = {"Mäskäräm": 30,
                            "Ṭəqəmt": 30,
                            "Ḫədar": 30,
                            "Taḫśaś": 30,
                            "Ṭərr(": 30,
                            "Yäkatit": 30,
                            "Mägabit": 30,
                            "Miyazya": 30,
                            "Gənbo": 30,
                            "Säne": 30,
                            "Ḥamle": 30,
                            "Nähase": 30,
                            "Ṗagume": 30,
                            "Extra Days": 5}

ETHIOPIAN_MONTHS_LEAP = {"Mäskäräm": 30,
                         "Ṭəqəmt": 30,
                         "Ḫədar": 30,
		         "Taḫśaś": 30,
                         "Ṭərr(": 30,
                         "Yäkatit": 30,
                         "Mägabit": 30,
                         "Miyazya": 30,
                         "Gənbo": 30,
                         "Säne": 30,
                         "Ḥamle": 30,
                         "Nähase": 30,
                         "Ṗagume": 30,
                         "Extra Days": 6}

# The Coptic Calendar starts on 29/Aug/284 by the Julian Calendar, which is Julian Day 1824676
# As in the Julian year, every AD year that is divisible by 4 is a leap year (this required a careful reading of
# various online sources, which say that the year "preceding the Julian leap year" is a Coptic leap year. Julian year
# 284 was a leap year, which means that Coptic year -1 was a leap year. The upshot of this is that we can just use
# the same algorithm for the Julian and Coptic years, changing only which set of months are used.

COPTIC_MONTHS_NORMAL = {"Thout": 30,
                         "Paopi": 30,
                         "Hathor": 30,
                         "Koiak": 30,
                         "Tobi": 30,
                         "Meshir": 30,
                         "Paremhat": 30,
                         "Parmouti": 30,
                         "Pashons": 30,
                         "Paoni": 30,
                         "Epip": 30,
                         "Mesori": 30,
                         "Extra Days": 5}

COPTIC_MONTHS_LEAP = {"Thout": 30,
                      "Paopi": 30,
                      "Hathor": 30,
                      "Koiak": 30,
                      "Tobi": 30,
                      "Meshir": 30,
                      "Paremhat": 30,
                      "Parmouti": 30,
                      "Pashons": 30,
                      "Paoni": 30,
                      "Epip": 30,
                      "Mesori": 30,
                      "Extra Days": 6}

# The Egyptian civil calendar was exactly 365 days long because they never figured out leap years.
# Pharaonic Year 6291 began on 11/Sep/2017 according to this article:
# https://www.egypttoday.com/Article/4/22184/September-11-marks-the-beginning-of-a-new-Egyptian-year
# This means that day 1 of the Egyptian civil calendar is Julian Day 160332.

EGYPTIAN_MONTHS = {"Thoth": 30,
                   "Phaophi": 30,
                   "Hathor": 30,
                   "Choak": 30,
                   "Tybi": 30,
                   "Mechir": 30,
                   "Phamenoth": 30,
                   "Pharmuthi": 30,
                   "Pachons": 30,
                   "Payni": 30,
                   "Spiphi": 30,
                   "Mesore": 30,
                   "Extra Days": 5}

# Months of the Lunar Hijri Calendar
# Traditionally, the Lunar Hijri (or Islamic) calendar is observational, with each month beginning on the observation of the crescent moon.
# This can cause trouble when it's cloudy, or when peple in different places observe the crescent moon on different days.
# This program uses the tabular calendar, in which the date is determined entirely algorithmically without recourse to direct observations
# There are a few algorithms to decide on a leap year. The most common is a 30-year cycle in which a leap year falls in months 2, 5, 7, 10, 13, 16, 18, 21, 24, 26 and 29

LUNAR_HIJRI_MONTHS_NORMAL = {"Muharram": 30,
                              "Safar": 29,
                              "Rabi' al-awwal": 30,
                              "Rabi' al-Thani": 29,
                              "Jumada al-awwal": 30,
                              "Jumada al-Thani": 29,
                              "Rajab": 30,
                              "Sha'ban": 29,
                              "Ramadan": 30,
                              "Shawwal": 29,
                              "Dhu al-Qidah": 30,
                              "Dhu al-Hijjah": 29}

LUNAR_HIJRI_MONTHS_LEAP = {"Muharram": 30,
                           "Safar": 29,
                           "Rabi' al-awwal": 30,
                           "Rabi' al-Thani":	29,
                           "Jumada al-awwal": 30,
                           "Jumada al-Thani": 29,
                           "Rajab": 30,
                           "Sha'ban": 29,
                           "Ramadan": 30,
                           "Shawwal": 29,
                           "Dhu al-Qidah": 30,
                           "Dhu al-Hijjah": 30}

# Months of the Iranian Calendars. Farsi names are used.
#
# The Solar Hijri Calendar begins on the Vernal Equinox as observed in Tehran. This means there's no way to algorithmically calculate the Solar Hijri leap years. However, there are ways to closely approximate this
# Things get more confusing when one dives into the rabbit hole of defining the astronomical year. The Solar Hijri Year is defined as the exact interval between two vernal equinoxes,
# with Nowruz falling on the full day whose midnight falls closest to the moment of equinox. The moment of equinox varies from year to year, falling at a different time of day every time.
# The mean equinox year is 365.2424 days
#
# This must not be confused with the tropical year, which is defined as the time over which the ecliptic longitude of the Sun increases by 360 degrees.
# The mean tropical year is 365.2422 days, abut 16 seconds shorter than the equinox year; this is the basis for Ahmad Birashk's calendar, which does not properly line up with the equinoxes.
#
# See http://aramis.obspm.fr/~heydari/divers/ir-cal-eng.html for much more information.
#
# Khayyam's scheme operates on a 33-year cycle, in which the following years are leap: 5, 9, 13, 17, 21, 25, 29, 33. This reasonably approximates the actual calendar used in Iran and Afghanistan.
# This is accurate to about 1 day in 16,000 years.
#
# Birashk's calendar is based on the tropical year, which is about 16 seconds shorter than the time between two vernal equinoxes due to orbital mechanics.
# It works on a cycle of 2,820 years.
# This 2820-year cycle is subdivided into cycles of 128 and 132 years.
# The 128-year cycle is itself subdivided into cycles of 29 and 33 years.
# The 132-year cycle is itself subdivided into cycles of 29, 33, and 37 years.
# 21 128-year cycles followed by 1 132-year cycle make up the great 2820-year cycle.
# The cycles of 29, 33, and 37 years have leap years in years 5, 9, 13, 17, 21, 25, 29, 33, and 37, omitting as appropriate.

SOLAR_HIJRI_MONTHS_NORMAL = {"Farvardin": 31,
                              "Ordibehesht": 31,
                              "Khordad": 31,
                              "Tir": 31,
                              "Mordad": 31,
                              "Shahrivar": 31,
                              "Mehr": 30,
                              "Aban": 30,
                              "Azar": 30,
                              "Dey": 30,
                              "Bahman": 30,
                              "Esfand": 29}

SOLAR_HIJRI_MONTHS_LEAP = {"Farvardin": 31,
                           "Ordibehesht": 31,
                           "Khordad": 31,
                           "Tir": 31,
                           "Mordad": 31,
                           "Shahrivar": 31,
                           "Mehr": 30,
                           "Aban": 30,
                           "Azar": 30,
                           "Dey": 30,
                           "Bahman": 30,
                           "Esfand": 30}
