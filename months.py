#!/usr/bin/python

# This is a set of months for use in calconv

# GREGORIAN AND JULIAN CALENDARS
#
# The Gregorian Calendar begins on Julian Day 1721425.
# The Julian Calendar begins on Julian Day 1721423.

CAESAR_MONTHS_NORMAL = {"January": 31,
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

CAESAR_MONTHS_LEAP = {"January": 31,
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

# ETHIOPIAN AND ERITREAN CALENDAR (Ethiopian months are used)
# Each year is associated with one of the four gospel authors, following the cycle John, Matthew, Mark, Luke (Luke years are leap years)

# The Ethiopian calendar starts on Gregorian date 29/08/8, which is Julian Day 1724222.
# Like with the Julian and Coptic Calendars, years divisible by 4 are leap years
# Apparently it does have a year 0, which makes calculations easier
ETHIOPIAN_MONTHS_NORMAL = {"Mäskäräm": 30,
                            "Ṭəqəmt": 30,
                            "Ḫədar": 30,
                            "Taḫśaś": 30,
                            "Ṭərr": 30,
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
                         "Ṭərr": 30,
                         "Yäkatit": 30,
                         "Mägabit": 30,
                         "Miyazya": 30,
                         "Gənbo": 30,
                         "Säne": 30,
                         "Ḥamle": 30,
                         "Nähase": 30,
                         "Ṗagume": 30,
                         "Extra Days": 6}

# COPTIC CALENDAR
#
# The Coptic Calendar starts on 29/Aug/284 by the Julian Calendar, which is Julian Day 1825028
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

# EGYPTIAN CALENDAR
#
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
                   "Extra days": 5}

# LUNAR HIJRI CALENDAR

# Traditionally, the Lunar Hijri (or Islamic) calendar is observational, with each month beginning on the observation of the crescent moon.
# This can cause trouble when it's cloudy, or when peple in different places observe the crescent moon on different days.
# This program uses the tabular calendar, in which the date is determined entirely algorithmically without recourse to direct observations
# There are a few algorithms to decide on a leap year. The most common is a 30-year cycle in which a leap year falls in years 2, 5, 7, 10, 13, 16, 18, 21, 24, 26 and 29
# Day 1 is Julian Day 1948439, which means day 0 is 1948438. It appears that the Hijri calendars do in fact have a year 0.

ARAB_MONTHS_NORMAL = {"Muharram": 30,
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

ARAB_MONTHS_LEAP = {"Muharram": 30,
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
                           "Dhu al-Hijjah": 30}

# IRANIAN CALENDARS (Farsi names are used)
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


# ARMENIAN CALENDAR
#
# The Armenian calendar was used in Armenian until the 11th century, when
# the Julian calendar was introduced.
# The original calendar was notionally established by Hayk, the legendary
# founder of Armenia, in 2492 BC to commemorate his defeat of General
# Belos of Babylon; academic consensus appears to be that it was established
# by Artaxias (188 BC - 161 BC)
#
# Much like the Egyptian calendar, the Armenian calendar consists of
# 30 * 12-day months plus five extra days at the end of the year.
#
# The Armenian calendar epoch is Julian Day 1922867, basically to make
# it easier to work out the date of Easter.
#
# Sources:
# https://en.wikipedia.org/wiki/Armenian_calendar
# http://haytomar.com/calendar.php
# http://www.rahamasha.net/uploads/2/3/2/8/2328777/armenian_calendar.pdf
# http://www.armeniapedia.org/wiki/Armenian_calendar

ARMENIAN_MONTHS = {"Nawasard": 30,
                   "Hoṙi": 30,
                   "Sahmi": 30,
                   "Trē": 30,
                   "Kʿałocʿ": 30,
                   "Arac'": 30,
                   "Mehekan": 30,
                   "Areg": 30,
                   "Ahekan": 30,
                   "Mareri": 30,
                   "Margac'": 30,
                   "Hrotic'": 30,
                   "Extra days": 5}

# ASSYRIAN MONTHS
#
# The Akkadian successor states did not themselves use calendar epochs, instead
# dating events by the name of whoever performed the New Year ceremony that year
# (Assyria) or by the year of the current king's reign (Babylon, and also
# Assyria later on). Various online sources report that modern Assyrian people
# take 4750 BC as their calendar epoch, based on the work of Nimrod Simono and
# Jean Alkhus which etablished that # year as the year of the mythical Flood. 
# However, all online sources are consistent in that the convert between
# Assyrian and Gregorian years, you add 4750 to the Gregorian year so that,
# for example, 2020 AD = 6770 PD. But because the Gregorian calendar does not
# have a year 0, this only works in the Gregorian and Assyrian year are bot
# positive. Based on this, I will take the Assyrian calendar epoch to be
# Julian Day -13388, which means that day 0 is Julian Day -13389.
#
# I couldn't find any direct information about modern Assyrian leap years
# However, it looks like the Assyrian calendar follows the same scheme as
# the Gregorian, so I'll just do the same and add one day to the last month
# if the corresponding Gregorian year is also a leap year.
#
# Sources:
# http://www.nineveh.com/Assyrian%20Calendar.html
# https://en.wikipedia.org/wiki/Assyrian_calendar
# https://web.archive.org/web/20100728001440/http://www.assyriatimes.com/engine/modules/news/article.php?storyid=3410
# 

ASSYRIAN_MONTHS_NORMAL = {"Nīsān": 31,
                          "ʾĪyār": 31,
                          "Ḥzīrān": 31,
                          "Tammūz": 31,
                          "Ṭabbāḥ": 31,
                          "ʾĪlūl": 31,
                          "Tešrīn Qḏīm": 30,
                          "Tešrīn Ḥrāy": 30,
                          "Kānōn Qḏīm": 30,
                          "Kānōn Ḥrāy": 30,
                          "Šḇāṭ": 30,
                          "Āḏar": 29}

ASSYRIAN_MONTHS_LEAP = {"Nīsān": 31,
                        "ʾĪyār": 31,
                        "Ḥzīrān": 31,
                        "Tammūz": 31,
                        "Ṭabbāḥ": 31,
                        "ʾĪlūl": 31,
                        "Tešrīn Qḏīm": 30,
                        "Tešrīn Ḥrāy": 30,
                        "Kānōn Qḏīm":	30,
                        "Kānōn Ḥrāy": 30,
                        "Šḇāṭ": 30,
                        "Āḏar": 30}


# BABYLONIAN MONTHS
#
# In ancient times, the Babylonian calendar operated on a purely obversational
# basis. Each month started when the first crescent moon was visible in the sky,
# and intercalary months were added whenever the priests figured it was about
# time. In 1120 BH (499BC), they switched to an algorithmic system based on the 19-year
# Metonic cycle, in whcih years 3, 6, 8, 11, 14, 17, and 19 are leap years.
# This is also the system used in the Hebrew calendar. I'm going to assume,
# based on the Hebrew calendar, that the Babylonian months start with 30
# days and thereafter alternate 29 and 30.
#
# In year 17, the intercalary month comes after Ululu rather than Adar.
#
# 2019 AD was 7319 PD by the Babylonian calendar according to this source:
# https://chaldeannation.com/blog/2019/03/31/akitu-7319-chaldean-new-year/
#
# The average year length is 365.0526315789473684210526316 days, which
# works out to 365 days 1 hour 15 minutes 47.37 seconds, and as such
# it gains 1 day every 5.27 years.


BABYLONIAN_MONTHS_NORMAL = {"Nisānu": 30,
                            "Āru": 29,
                            "Simanu": 30,
                            "Dumuzu": 29,
                            "Abu": 30,
                            "Ulūlu": 29,
                            "Tišritum": 30,
                            "Samnu": 29,
                            "Kislimu": 30,
                            "Ṭebētum": 29,
                            "Šabaṭu": 30,
                            "Addaru": 29}
                          
BABYLONIAN_MONTHS_LEAP = {"Nisānu": 30,
                          "Āru": 29,
                          "Simanu": 30,
                          "Dumuzu": 29,
                          "Abu": 30,
                          "Ulūlu": 29,
                          "Tišritum": 30,
                          "Samnu": 29,
                          "Kislimu": 30,
                          "Ṭebētum": 29,
                          "Šabaṭu": 30,
                          "Addaru": 30,
                          "Addaru Arku": 29}

BABYLONIAN_MONTHS_LEAP_17 = {"Nisānu": 30,
                             "Āru": 29,
                             "Simanu": 30,
                             "Dumuzu": 29,
                             "Abu": 30,
                             "Ulūlu": 29,
                             "Ulūlu Arku": 30,
                             "Tišritum": 30,
                             "Samnu": 29,
                             "Kislimu": 30,
                             "Ṭebētum": 29,
                             "Šabaṭu": 30,
                             "Addaru": 29}

# HEBREW MONTHS
#
# The Hebrew Calendar is complicated.
#
# For one thing, while Nisan is the first month, 1 Nisan is only the religious new year; civil new year happens six
# months later on 1 Tishrei.
#
# The calendar epoch is 1 Tishrei 1, which corresponds to 7 October 3761 BC by the Julian Calendar, which is Julian
# Day 347997 (Gregorian: 7 September 3761 BC, Solar Hijri: 16 Shahrivar 4382 BH). This is about 1 year prior to
# the traditional date of the creation of the world described in Genesis.
#
# There is no year 0. Years 3, 6, 8, 11, 14, 17, and 19 of the 19-year Metonic cycle are leap years and have the
# extra month.
#
# Due to the intricate complexity, the pattern of leap years only repeats exactly every 689,472 years!

HEBREW_MONTHS_DEFICIENT_NORMAL = {"Tishrei": 30,
                                  "Marcheshvan": 29,
                                  "Kislev": 29,
                                  "Tevet": 29,
                                  "Shevat": 30,
                                  "Adar": 29,
                                  "Nisan": 30,
                                  "Iyar": 29,
                                  "Sivan": 30,
                                  "Tammuz": 29,
                                  "Av": 30,
                                  "Elul": 29}

HEBREW_MONTHS_DEFICIENT_LEAP = {"Tishrei": 30,
                                "Marcheshvan":	29,
                                "Kislev": 29,
                                "Tevet": 29,
                                "Shevat": 30,
                                "Adar": 30,
                                "Veadar": 29,
                                "Nisan": 30,
                                "Iyar": 29,
                                "Sivan": 30,
                                "Tammuz": 29,
                                "Av": 30,
                                "Elul": 29}

HEBREW_MONTHS_REGULAR_NORMAL = {"Tishrei": 30,
                                "Marcheshvan": 30,
                                "Kislev": 29,
                                "Tevet": 29,
                                "Shevat": 30,
                                "Adar": 29,
                                "Nisan": 30,
                                "Iyar": 29,
                                "Sivan": 30,
                                "Tammuz": 29,
                                "Av": 30,
                                "Elul": 29}

HEBREW_MONTHS_REGULAR_LEAP = {"Tishrei": 30,
                               "Marcheshvan": 30,
                               "Kislev": 29,
                               "Tevet": 29,
                               "Shevat": 30,
                               "Adar": 30,
                               "Veadar": 29,
                               "Nisan": 30,
                               "Iyar": 29,
                               "Sivan": 30,
                               "Tammuz": 29,
                               "Av": 30,
                               "Elul": 29}

HEBREW_MONTHS_ABUNDANT_NORMAL = {"Tishrei": 30,
                                 "Marcheshvan": 30,
                                 "Kislev": 30,
                                 "Tevet": 29,
                                 "Shevat": 30,
                                 "Adar": 29,
                                 "Nisan": 30,
                                 "Iyar": 29,
                                 "Sivan": 30,
                                 "Tammuz": 29,
                                 "Av": 30,
                                 "Elul": 29}

HEBREW_MONTHS_ABUNDANT_LEAP = {"Tishrei": 30,
                               "Marcheshvan": 30,
                               "Kislev": 30,
                               "Tevet": 29,
                               "Shevat": 30,
                               "Adar": 30,
                               "Veadar": 29,
                               "Nisan": 30,
                               "Iyar": 29,
                               "Sivan": 30,
                               "Tammuz": 29,
                               "Av": 30,
                               "Elul": 29}

# SAMARITAN MONTHS

SAMARITAN_MONTHS_NORMAL = {"Nisan": 30,
                            "Iyar": 29,
                            "Sivan": 30,
                            "Tammuz": 29,
                            "Av": 30,
                            "Elul": 29,
                            "Tishrei": 30,
                            "Marcheshvan": 29,
                            "Kislev": 30,
                            "Tevet": 29,
                            "Shevat": 30,
                            "Adar": 29}

SAMARITAN_MONTHS_LEAP = {"Nisan": 30,
                         "Iyar": 29,
                         "Sivan": 30,
                         "Tammuz": 29,
                         "Av": 30,
                         "Elul": 29,
                         "Tishrei": 30,
                         "Marcheshvan": 29,
                         "Kislev": 30,
                         "Tevet": 29,
                         "Shevat": 30,
                         "Adar": 30,
                         "Veadar": 29}

#KURDISH MONTHS

KURDISH_MONTHS_NORMAL = {"Jejhnan": 31,
                         "Gullan": 31,
                         "Zerdan": 31,
                         "Púshperr": 31,
                         "Gelawéjh": 31,
                         "Xermanan": 31,
                         "Beran": 30,
                         "Xezan": 30,
                         "Saran": 30,
                         "Befran": 30,
                         "Rébandan": 30,
                         "Reshemé": 29}

KURDISH_MONTHS_LEAP = {"Jejhnan": 31,
                      "Gullan": 31,
                      "Zerdan": 31,
                      "Púshperr": 31,
                      "Gelawéjh": 31,
                      "Xermanan": 31,
                      "Beran": 30,
                      "Xezan": 30,
                      "Saran": 30,
                      "Befran": 30,
                      "Rébandan": 30,
                      "Reshemé": 30}

# Amazigh months
AMAZIGH_MONTHS_NORMAL = {"Yennayer": 31,
                         "Yebrayer": 28,
                         "Mares": 31,
                         "Yebrir": 30,
                         "May": 31,
                         "Yunyu": 30,
                         "Yulyuz": 31,
                         "Ɣuct": 31,
                         "Shutembir": 30,
                         "Ktuber": 31,
                         "Nwambir": 30,
                         "Dujembir": 31}

AMAZIGH_MONTHS_LEAP = {"Yennayer": 31,
                       "Yebrayer": 28,
                       "Mares": 31,
                       "Yebrir": 30,
                       "May":	31,
                       "Yunyu": 30,
                       "Yulyuz": 31,
                       "Ɣuct": 31,
                       "Shutembir": 30,
                       "Ktuber": 31,
                       "Nwambir": 30,
                       "Dujembir": 32}

# Turkish months

TURKISH_MONTHS_NORMAL = {"Kânûn-ı Sânî": 31,
                         "Şubat": 28,
                         "Mart": 31,
                         "Nisan": 30,
                         "Mayıs": 31,
                         "Haziran": 30,
                         "Temmuz": 31,
                         "Ağustos": 31,
                         "Eylül": 30,
                         "Teşrin-i Evvel": 31,
                         "Teşrin-i Sânî": 30,
                         "Kânûn-ı Evvel": 31}


TURKISH_MONTHS_LEAP =  {"Kânûn-ı Sânî": 31,
                       "Şubat": 29,
                       "Mart": 31,
                       "Nisan": 30,
                       "Mayıs": 31,
                       "Haziran": 30,
                       "Temmuz": 31,
                       "Ağustos": 31,
                       "Eylül": 30,
                       "Teşrin-i Evvel": 31,
                       "Teşrin-i Sânî": 30,
                       "Kânûn-ı Evvel": 31}

