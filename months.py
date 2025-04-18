#!/usr/bin/python3

# This is a set of months and weekdays for use in calconv

# Weekdays
WEEKDAYS_EN = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
DAYNO_EN = {"Monday":    0,
            "Tuesday":   1,
            "Wednesday": 2,
            "Thursday":  3,
            "Friday":    4,
            "Saturday":  5,
            "Sunday":    6}

# GREGORIAN AND JULIAN CALENDARS

CAESAR = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

CAESAR_LENGTHS = {365: (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31), # normal years
                  366: (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)} # leap years

CAESAR_NORMAL = {"January": 31,
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

CAESAR_LEAP = {"January": 31,
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

ETHIOPIAN_NORMAL = {"Mäskäräm": 30,
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

ETHIOPIAN_LEAP = {"Mäskäräm": 30,
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

COPTIC_NORMAL = {"Thout": 30,
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

COPTIC_LEAP = {"Thout": 30,
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

EGYPTIAN = {"Thoth": 30,
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

ARAB_NORMAL = {"Muharram": 30,
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

ARAB_LEAP = {"Muharram": 30,
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

IRANIAN_NORMAL = {"Farvardin": 31,
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

IRANIAN_LEAP = {"Farvardin": 31,
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

ARMENIAN = {"Nawasard": 30,
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

ASSYRIAN_NORMAL = {"Nīsān": 31,
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

ASSYRIAN_LEAP = {"Nīsān": 31,
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

BABYLONIAN_NORMAL = {"Nisānu": 30,
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

BABYLONIAN_LEAP = {"Nisānu": 30,
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

BABYLONIAN_LEAP_17 = {"Nisānu": 30,
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

HEBREW = ("Tishrei", "Marcheshvan", "Kislev", "Tevet", "Shevat", "Adar", "Veadar", "Nisan", "Iyar", "Sivan", "Tammuz", "Av", "Elul") # begins with Jewish Rosh Hashanah. Samaritans start at month 6.

JEWISH_LENGTHS = {353: (30, 29, 29, 29, 30, 29,  0, 30, 29, 30, 29, 30, 29), # deficient normal year
                  354: (30, 29, 30, 29, 30, 29,  0, 30, 29, 30, 29, 30, 29), # regular normal year
                  355: (30, 30, 30, 29, 30, 29,  0, 30, 29, 30, 29, 30, 29), # abundant normal year
                  383: (30, 29, 29, 29, 30, 30, 29, 30, 29, 30, 29, 30, 29), # deficient leap year
                  384: (30, 29, 30, 29, 30, 30, 29, 30, 29, 30, 29, 30, 29), # regular leap year
                  385: (30, 30, 30, 29, 30, 30, 29, 30, 29, 30, 29, 30, 29)} # abundant leap year

HEBREW_DEFICIENT_NORMAL = {"Tishrei": 30,
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

HEBREW_DEFICIENT_LEAP = {"Tishrei": 30,
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

HEBREW_REGULAR_NORMAL = {"Tishrei": 30,
                         "Marcheshvan": 29,
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

HEBREW_REGULAR_LEAP = {"Tishrei": 30,
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

HEBREW_ABUNDANT_NORMAL = {"Tishrei": 30,
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

HEBREW_ABUNDANT_LEAP = {"Tishrei": 30,
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

SAMARITAN_DEFICIENT_NORMAL = {"Nisan": 30,
                              "Iyar": 29,
                              "Sivan": 30,
                              "Tammuz": 29,
                              "Av": 30,
                              "Elul": 29,
                              "Tishrei": 30,
                              "Marcheshvan": 29,
                              "Kislev": 29,
                              "Tevet": 29,
                              "Shevat": 30,
                              "Adar": 29}

SAMARITAN_REGULAR_NORMAL = {"Nisan": 30,
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

SAMARITAN_ABUNDANT_NORMAL = {"Nisan": 30,
                             "Iyar": 29,
                             "Sivan": 30,
                             "Tammuz": 29,
                             "Av": 30,
                             "Elul": 29,
                             "Tishrei": 30,
                             "Marcheshvan": 30,
                             "Kislev": 30,
                             "Tevet": 29,
                             "Shevat": 30,
                             "Adar": 29}

SAMARITAN_DEFICIENT_LEAP = {"Nisan": 30,
                            "Iyar": 29,
                            "Sivan": 30,
                            "Tammuz": 29,
                            "Av": 30,
                            "Elul": 29,
                            "Tishrei": 30,
                            "Marcheshvan": 29,
                            "Kislev": 29,
                            "Tevet": 29,
                            "Shevat": 30,
                            "Adar": 29}

SAMARITAN_REGULAR_LEAP = {"Nisan": 30,
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

SAMARITAN_ABUNDANT_LEAP = {"Nisan": 30,
                           "Iyar": 29,
                           "Sivan": 30,
                           "Tammuz": 29,
                           "Av": 30,
                           "Elul": 29,
                           "Tishrei": 30,
                           "Marcheshvan": 30,
                           "Kislev": 30,
                           "Tevet": 29,
                           "Shevat": 30,
                           "Adar": 29}

# KURDISH MONTHS

KURDISH_NORMAL = {"Jejhnan": 31,
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

KURDISH_LEAP = {"Jejhnan": 31,
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

# AMAZIGH MONTHS
AMAZIGH_NORMAL = {"Yennayer": 31,
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

AMAZIGH_LEAP = {"Yennayer": 31,
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

# TURKISH MONTHS

TURKISH_NORMAL = {"Mart": 31,
                  "Nisan": 30,
                  "Mayıs": 31,
                  "Haziran": 30,
                  "Temmuz": 31,
                  "Ağustos": 31,
                  "Eylül": 30,
                  "Teşrin-i Evvel": 31,
                  "Teşrin-i Sânî": 30,
                  "Kânûn-ı Evvel": 31,
                  "Kânûn-ı Sânî": 31,
                  "Şubat": 28}


TURKISH_LEAP =  {"Mart": 31,
                 "Nisan": 30,
                 "Mayıs": 31,
                 "Haziran": 30,
                 "Temmuz": 31,
                 "Ağustos": 31,
                 "Eylül": 30,
                 "Teşrin-i Evvel": 31,
                 "Teşrin-i Sânî": 30,
                 "Kânûn-ı Evvel": 31,
                 "Kânûn-ı Sânî": 31,
                 "Şubat": 29}

# WORLD MONTHS

WORLD_NORMAL = {"January": 31,
                "February": 30,
                "March": 30,
                "April": 31,
                "May": 30,
                "June": 30,
                "July": 31,
                "August": 30,
                "September": 30,
                "October": 31,
                "November": 30,
                "December": 30,
                "Worldsday": 1}

WORLD_LEAP = {"January": 31,
              "February": 30,
              "March": 30,
              "April": 31,
              "May": 30,
              "June": 30,
              "Leap Day": 1,
              "July": 31,
              "August": 30,
              "September": 30,
              "October": 31,
              "November": 30,
              "December": 30,
              "Worldsday": 1}

# INTERNATIONAL FIXED CALENDAR

IFC_NORMAL = {"January": 28,
              "February": 28,
              "March": 28,
              "April": 28,
              "May": 28,
              "June": 28,
              "Sol": 28,
              "July": 28,
              "August": 28,
              "September": 28,
              "October": 28,
              "November": 28,
              "December": 28,
              "Year Day": 1}

IFC_LEAP = {"January":	28,
            "February": 28,
            "March": 28,
            "April": 28,
            "May": 28,
            "June": 28,
            "Leap Day": 1,
            "Sol": 28,
            "July": 28,
            "August": 28,
            "September": 28,
            "October":	28,
            "November": 28,
            "December": 28,
            "Year Day": 1}

# PAX CALENDAR

PAX_NORMAL = {"January": 28,
              "February": 28,
              "March": 28,
              "April": 28,
              "May": 28,
              "June": 28,
              "July": 28,
              "August": 28,
              "September": 28,
              "October": 28,
              "November": 28,
              "Columbus": 28,
              "December": 28}

PAX_LEAP = {"January": 28,
            "February": 28,
            "March": 28,
            "April": 28,
            "May": 28,
            "June": 28,
            "July": 28,
            "August": 28,
            "September": 28,
            "October": 28,
            "November": 28,
            "Columbus": 28,
            "Pax": 7,
            "December": 28}

# GORMAN CALENDAR

GORMAN_NORMAL = {"March": 28,
                 "April": 28,
                 "May": 28,
                 "June": 28,
                 "Quintilis": 28,
                 "Sextilis": 28,
                 "September": 28,
                 "October": 28,
                 "November": 28,
                 "December": 28,
                 "January": 28,
                 "February": 28,
                 "Gormanuary": 28,
                 "Intermission": 1}

GORMAN_LEAP = {"March": 28,
               "April": 28,
               "May": 28,
               "June":	28,
               "Quintilis": 28,
               "Sextilis": 28,
               "September": 28,
               "October": 28,
               "November": 28,
               "December": 28,
	       "January": 28,
               "February": 28,
               "Gormanuary": 28,
               "Intermission": 2}

# PAX 2020

PAX2_NORMAL = {"Initium": 28,
               "Rutilante": 28,
               "Semen": 28,
               "Gaudium": 28,
               "Apes": 28,
               "Serenium": 28,
               "Coleum": 28,
               "Amare": 28,
               "Messis": 28,
               "Follium": 28,
               "Nixcumumis": 28,
               "Pax": 28,
               "Requiem": 29}

PAX2_LEAP = {"Initium": 28,
             "Rutilante": 28,
             "Semen": 28,
             "Gaudium": 28,
             "Apes": 28,
             "Serenium": 28,
             "Coleum": 28,
             "Amare": 28,
             "Messis": 28,
             "Follium": 28,
             "Nixcumumis": 28,
             "Pax": 28,
             "Requiem": 30}

# POSITIVIST CALENDAR

POSITIVIST_NORMAL = {"Moses": 28,
                     "Homer": 28,
                     "Aristotle": 28,
                     "Archimedes": 28,
                     "Caesar": 28,
                     "St. Paul": 28,
                     "Charlemagne": 28,
                     "Dante": 28,
                     "Gutenberg": 28,
                     "Shakespeare": 28,
                     "Descartes": 28,
                     "Frederick II": 28,
                     "Bichat": 28,
                     "Festival of All the Dead": 1}

POSITIVIST_LEAP = {"Moses": 28,
                   "Homer": 28,
                   "Aristotle": 28,
                   "Archimedes": 28,
                   "Caesar": 28,
                   "St. Paul": 28,
                   "Charlemagne": 28,
                   "Dante": 28,
                   "Gutenberg": 28,
                   "Shakespeare": 28,
                   "Descartes": 28,
                   "Frederick II": 28,
                   "Bichat": 28,
                   "Festival of All the Dead": 1,
                   "Festival of Holy Women": 1}

# NEX CALENDAR

NEX_NORMAL = {"January": 31,
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
              "December": 30}

NEX_LEAP = {"January": 31,
            "February": 29,
            "March": 31,
            "April": 30,
            "May": 31,
            "June": 30,
            "July": 31,
            "August":	31,
            "September": 30,
            "October": 31,
            "November": 30,
            "December": 31}

FRENCH_NORMAL = {"Vendémiaire": 30,
                 "Brumaire": 30,
                 "Frimaire": 30,
                 "Nivôse": 30,
                 "Pluviôse": 30,
                 "Ventôse": 30,
                 "Germinal": 30,
                 "Floréal": 30,
                 "Prairial": 30,
                 "Messidor": 30,
                 "Thermidor": 30,
                 "Fructidor": 30,
                 "Sans-culottides": 5}

FRENCH_LEAP = {"Vendémiaire": 30,
               "Brumaire": 30,
               "Frimaire": 30,
               "Nivôse": 30,
               "Pluviôse": 30,
	       "Ventôse": 30,
               "Germinal": 30,
               "Floréal": 30,
               "Prairial": 30,
               "Messidor": 30,
               "Thermidor": 30,
               "Fructidor": 30,
               "Sans-culottides": 6}

THELLID_NORMAL = {"Alvakku": 28,
                  "Bethanis": 28,
                  "Duvadda": 28,
                  "Emovvi": 28,
                  "Forkithal": 28,
                  "Kalvazzi": 28,
                  "Irentos": 28,
                  "Jukennuk": 28,
                  "Miskullen": 28,
                  "Ossakov": 28,
                  "Raikkaved": 28,
                  "Underro": 28,
                  "Zithebbe": 28,
                  "Old Year's Day": 1}

THELLID_LEAP = {"Alvakku": 28,
                "Bethanis": 28,
                "Duvadda": 28,
                "Emovvi": 28,
                "Forkithal": 28,
                "Kalvazzi": 28,
                "Irentos": 28,
                "Jukennuk": 28,
                "Miskullen": 28,
                "Ossakov": 28,
                "Raikkaved": 28,
                "Underro": 28,
                "Zithebbe": 28,
                "Leap Day": 1,
                "Old Year's Day": 1}

IGBO = {"Mbụ": 28,
        "Abụo": 28,
        "Ife Eke": 28,
        "Anọ": 28,
        "Agwụ": 28,
        "Ifejiọkụ": 28,
        "Alọm Chi": 28,
        "Ilo Mmụọ": 28,
        "Ana": 28,
        "Okike": 28,
        "Ajana": 28,
        "Ede Ajana": 28,
        "Ụzọ Alụsị": 28}

ROMAN_NORMAL = {"Martius": 31,
                "Aprilis": 29,
                "Maia": 31,
                "Iunius": 29,
                "Quintilis": 31,
                "Sextilis": 29,
                "Septembris": 29,
                "Octobris": 31,
                "Novembris": 29,
                "Decembris": 29,
                "Ianuarius": 29,
                "Ferbruarius": 28}

ROMAN_2 = {"Martius": 31,
           "Aprilis": 29,
           "Maia": 31,
           "Iunius": 29,
           "Quintilis": 31,
           "Sextilis": 29,
           "Septembris": 29,
           "Octobris": 31,
           "Novembris": 29,
           "Decembris": 29,
           "Ianuarius": 29,
           "Ferbruarius": 23,
           "Mercedonius": 27}

ROMAN_4 = {"Martius": 31,
	   "Aprilis": 29,
	   "Maia": 31,
	   "Iunius": 29,
	   "Quintilis": 31,
	   "Sextilis": 29,
	   "Septembris": 29,
	   "Octobris": 31,
	   "Novembris": 29,
	   "Decembris": 29,
	   "Ianuarius": 29,
	   "Ferbruarius": 24,
           "Mercedonius": 27}

# GEORGIAN CALENDAR

GEORGIAN_C_NORMAL = {"Peter": 28,
                     "Andrew": 28,
                     "James the Great": 28,
                     "John": 28,
                     "Philip": 28,
                     "Bartholomew": 28,
                     "Thomas": 28,
                     "Matthew": 28,
                     "James the Less": 28,
                     "Jude": 28,
                     "Simon": 28,
                     "Matthias": 28,
                     "Paul": 28,
                     "Christmas": 1}

GEORGIAN_C_LEAP = {"Peter": 28,
                   "Andrew": 28,
                   "James the Great": 28,
                   "John": 28,
                   "Philip": 28,
                   "Bartholomew": 28,
                   "Thomas": 28,
                   "Matthew": 28,
                   "James the Less": 28,
                   "Jude": 28,
                   "Simon": 28,
                   "Matthias": 28,
                   "Paul": 28,
                   "Christmas": 1,
                   "Olympiad": 1}

GEORGIAN_G_NORMAL = {"January": 28,
                     "February": 28,
                     "March": 28,
                     "April": 28,
                     "May": 28,
                     "June": 28,
                     "July": 28,
                     "August": 28,
                     "September": 28,
                     "October": 28,
                     "November": 28,
                     "December": 28,
                     "Georgy": 28,
                     "Christmas": 1}

GEORGIAN_G_LEAP = {"January": 28,
                   "February": 28,
                   "March": 28,
                   "April": 28,
                   "May": 28,
                   "June": 28,
                   "July": 28,
                   "August": 28,
                   "September": 28,
                   "October": 28,
                   "November": 28,
                   "December": 28,
                   "Georgy": 28,
                   "Christmas": 1,
                   "Olympiad": 1}

INCA_SOLAR_NORMAL = {"Intiraymipacha": 30,
                     "Pachacyahuarllamapacha": 30,
                     "Yapuypacha": 30,
                     "Coyaraymipacha": 30,
                     "Paramañaypacha": 30,
                     "Ayamarcaypacha": 30,
                     "Capacintiraymipacha": 30,
                     "Huacapacha": 30,
                     "Huarachicuypacha": 30,
                     "Paraypacha": 30,
                     "Rinrituccinapacha": 30,
                     "Aymuraypacha": 30,
                     "Intihuatapacyapanapacha": 5}

INCA_SOLAR_LEAP = {"Intiraymipacha": 30,
                   "Pachacyahuarllamapacha": 30,
                   "Yapuypacha": 30,
                   "Coyaraymipacha": 30,
                   "Paramañaypacha":	30,
                   "Ayamarcaypacha": 30,
                   "Capacintiraymipacha": 30,
                   "Huacapacha": 30,
                   "Huarachicuypacha": 30,
                   "Paraypacha": 30,
                   "Rinrituccinapacha": 30,
                   "Aymuraypacha": 30,
                   "Intihuatapacyapanapacha": 6}

KOREAN_NORMAL = {"Il-wol": 31,
                   "I-wol": 28,
                   "Sam-wol": 31,
                   "Sa-wol": 30,
                   "O-wol": 31,
                   "Yu-wol": 30,
                   "Chil-wol": 31,
                   "Pal-wol": 31,
                   "Gu-wol": 30,
                   "Si-wol": 31,
                   "Sibil-wol": 30,
                   "Sibi-wol": 31}


KOREAN_LEAP = {"Il-wol": 31,
                 "I-wol": 29,
	         "Sam-wol": 31,
                 "Sa-wol": 30,
                 "O-wol": 31,
                 "Yu-wol": 30,
                 "Chil-wol": 31,
	         "Pal-wol": 31,
                 "Gu-wol": 30,
                 "Si-wol": 31,
                 "Sibil-wol": 30,
                 "Sibi-wol": 31}

# Solar terms, for use in the Chinese solar calendars.
# These dictionaries list the angle rather than the days

JIEQI = {"Lìchūn": 315,      # Beginning of spring
         "Yǔshuı̌": 330,      # Rain water
         "Jı̄ngzhé": 345,     # Waking of insects
         "Chūnfēn": 0,       # Spring equinox
         "Qı̄ngmíng": 15,     # Pure brightness
         "Gǔyǔ": 30,         # Grain rain
         "Lìxià": 45,        # Beginning of summer
         "Xiǎomǎn": 60,       # Grain full
         "Mángzhòng": 75,    # Grain in ear
         "Xiàzhì": 90,       # Summer solstice
         "Xiǎoshǔ": 105,     # Slight heat
         "Dàshǔ": 120,       # Great heat
         "Lìqiū": 135,       # Beginning of autumn
         "Chǔshǔ": 150,      # Limit of heat
         "Báilù": 165,       # White dew
         "Qiūfēn": 180,      # Autumn equinox
         "Hánlù": 195,       # Cold dew
         "Shuāngjiàng": 210, # Descent of frost
         "Lìdōng": 225,      # Beginning of winter
         "Xiǎoxuě": 240,     # Slight snow
         "Dàxuě": 255,       # Great snow
         "Dōngzhì": 270,     # Winter solstice
         "Xiǎohán": 285,     # Slight cold
         "Dàhán": 300}       # Great cold

SOLAR_TERMS = {0:   "Chūnfēn",
               15:  "Qı̄ngmíng",
               30:  "Gǔyǔ",
               45:  "Lìxià",
               60:  "Xiǎomǎn",
               75:  "Mángzhòng",
               90:  "Xiàzhì",
               105: "Xiǎoshǔ",
               120: "Dàshǔ",
               135: "Lìqiū",
               150: "Chǔshǔ",
               165: "Báilù",
               180: "Qiūfēn",
               195: "Hánlù",
               210: "Shuāngjiàng",
               225: "Lìdōng",
               240: "Xiǎoxuě",
               255: "Dàxuě",
               270: "Dōngzhì",
               285: "Xiǎohán",
               300: "Dàhán",
               315: "Lìchūn",
               330: "Yǔshuı̌",
               345: "Jı̄ngzhé"}

JAPANESE_NORMAL = {"Ichigatsu": 31,
                   "Nigatsu": 28,
                   "Sangatsu": 31,
                   "Shigatsu": 30,
                   "Gogatsu": 31,
                   "Rokugatsu": 30,
                   "Shichigatsu": 31,
                   "Hachigatsu": 31,
                   "Kugatsu": 30,
                   "Juugatsu": 31,
                   "Juuichigatsu": 30,
                   "Juunigatsu": 31}

JAPANESE_LEAP = {"Ichigatsu": 31,
                 "Nigatsu": 29,
                 "Sangatsu": 31,
                 "Shigatsu": 30,
                 "Gogatsu": 31,
                 "Rokugatsu": 30,
                 "Shichigatsu": 31,
                 "Hachigatsu": 31,
                 "Kugatsu": 30,
                 "Juugatsu": 31,
                 "Juuichigatsu": 30,
                 "Juunigatsu": 31}


BAHAI_NORMAL = {"Bahá": 19,
                "Jalál": 19,
                "Jamál": 19,
                "ʻAẓamat": 19,
                "Núr": 19,
                "Raḥmat": 19,
                "Kalimát": 19,
                "Kamál": 19,
                "Asmáʼ": 19,
                "ʻIzzat": 19,
                "Mas͟híyyat": 19,
                "ʻIlm": 19,
                "Qudrat": 19,
                "Qawl": 19,
                "Masáʼil": 19,
                "S͟haraf": 19,
                "Sulṭán": 19,
                "Mulk": 19,
                "Ayyám-ul Há": 4,
                "ʻAláʼ": 19}

BAHAI_LEAP = {"Bahá": 19,
              "Jalál": 19,
              "Jamál": 19,
              "ʻAẓamat": 19,
              "Núr": 19,
              "Raḥmat": 19,
              "Kalimát": 19,
              "Kamál": 19,
              "Asmáʼ": 19,
              "ʻIzzat": 19,
              "Mas͟híyyat": 19,
              "ʻIlm": 19,
              "Qudrat": 19,
              "Qawl": 19,
              "Masáʼil": 19,
              "S͟haraf": 19,
              "Sulṭán": 19,
              "Mulk": 19,
              "Ayyám-ul Há": 5,
              "ʻAláʼ": 19}

ZOROASTRIAN_NUM = {"Farvardin": 0,
                   "Ordibehesht": 1,
                   "Khordad": 2,
                   "Tir": 3,
                   "Mordad": 4,
                   "Shahrivar": 5,
                   "Mehr": 6,
                   "Aban": 7,
                   "Azar": 8,
                   "Dey": 9,
                   "Bahman": 10,
                   "Esfand": 11,
                   "Gathas": 12}

NUM_ZOROASTRIAN = {0: "Farvardin",
                   1: "Ordibehesht",
                   2: "Khordad",
                   3: "Tir",
                   4: "Mordad",
                   5: "Shahrivar",
                   6: "Mehr",
                   7: "Aban",
                   8: "Azar",
                   9: "Dey",
                   10: "Bahman",
                   11: "Esfand",
                   12: "Gathas"}

YOUNG_AVESTAN_NUM = {"Farvardin": 0,
                     "Ordibehesht": 1,
                     "Khordad": 2,
                     "Tir": 3,
                     "Mordad": 4,
                     "Shahrivar": 5,
                     "Mehr": 6,
                     "Aban": 7,
                     "Gathas": 8,
                     "Azar": 9,
                     "Dey": 10,
                     "Bahman": 11,
                     "Esfand": 12}

NUM_YOUNG_AVESTAN = {0: "Farvardin",
                     1: "Ordibehesht",
                     2: "Khordad",
                     3: "Tir",
                     4: "Mordad",
                     5: "Shahrivar",
                     6: "Mehr",
                     7: "Aban",
                     8: "Gathas",
                     9: "Azar",
                     10: "Dey",
                     11: "Bahman",
                     12: "Esfand"}

OLD_AVESTAN_NUM = {"Ādukanaisha": 0,
                   "Thūravāhara": 1,
                   "Thāigracish": 2,
                   "Garmapada": 3,
                   "Thurnabadish": 4,
                   "Garbashiyash": 5,
                   "Bāgayādish": 6,
                   "Vrkazana": 7,
                   "Āçiyādiya": 8,
                   "Anāmaka": 9,
                   "Thwayauvā": 10,                   
                   "Vixayana": 11,
                   "Kabizeh": 12,
                   "Kabizeh 2": 13}

NUM_OLD_AVESTAN = {0: "Ādukanaisha",
                   1: "Thūravāhara",
                   2: "Thāigracish",
                   3: "Garmapada",
                   4: "Thurnabadish",
                   5: "Garbashiyash",
                   6: "Bāgayādish",
                   7: "Vrkazana",
                   8: "Āçiyādiya",
                   9: "Anāmaka",
                   10: "Thwayauvā",
                   11: "Vixayana",
                   12: "Kabizeh",
                   13: "Kabizeh 2"}

SOGDIAN_NUM = {"Nausardh": 0,
               "Xorezhnic": 1,
               "Nisanic": 2,
               "Pusākic": 3,
               "Shnāk-Xandic": 4,
               "Xazānānc": 5,
               "Baghakānic": 6,
               "Āpānc": 7,
               "Bōghic": 8,
               "Mushboghic": 9,
               "Zhimdic": 10,
               "Xshūmic": 11,
               "Extra days": 12}

NUM_SOGDIAN = {0: "Nausardh",
               1: "Xorezhnic",
               2: "Nisanic",
               3: "Pusākic",
               4: "Shnāk-Xandic",
               5: "Xazānānc",
               6: "Baghakānic",
               7: "Āpānc",
               8: "Bōghic",
               9: "Mushboghic",
               10: "Zhimdic",
               11: "Xshūmic",
               12: "Extra days"}

BAHAI_NUM = {"Bahá": 0,
              "Jalál": 1,
              "Jamál": 2,
              "ʻAẓamat": 3,
              "Núr": 4,
              "Raḥmat": 5,
              "Kalimát": 6,
              "Kamál": 7,
              "Asmáʼ": 8,
              "ʻIzzat": 9,
              "Mas͟híyyat": 10,
              "ʻIlm": 11,
              "Qudrat": 12,
              "Qawl": 13,
              "Masáʼil": 14,
              "S͟haraf": 15,
              "Sulṭán": 16,
              "Mulk": 17,
              "Ayyám-ul Há": 18,
              "ʻAláʼ": 19}

NUM_BAHAI = {0: "Bahá",
              1: "Jalál",
              2: "Jamál",
              3: "ʻAẓamat",
              4: "Núr",
              5: "Raḥmat",
              6: "Kalimát",
              7: "Kamál",
              8: "Asmáʼ",
              9: "ʻIzzat",
              10: "Mas͟híyyat",
              11: "ʻIlm",
              12: "Qudrat",
              13: "Qawl",
              14: "Masáʼil",
              15: "S͟haraf",
              16: "Sulṭán",
              17: "Mulk",
              18: "Ayyám-ul Há",
              19: "ʻAláʼ"}

EGYPTIAN_NUM = {"Thoth": 0,
                "Phaophi": 1,
                "Hathor": 2,
                "Choak": 3,
                "Tybi": 4,
                "Mechir": 5,
                "Phamenoth": 6,
                "Pharmuthi": 7,
                "Pachons": 8,
                "Payni": 9,
                "Spiphi": 10,
                "Mesore": 11,
                "Extra days": 12}

NUM_EGYPTIAN = {0: "Thoth",
                1: "Phaophi",
                2: "Hathor",
                3: "Choak",
                4: "Tybi",
                5: "Mechir",
                6: "Phamenoth",
                7: "Pharmuthi",
                8: "Pachons",
                9: "Payni",
                10: "Spiphi",
                11: "Mesore",
                12: "Extra days"}

INDIAN_LUNAR_NUM = {0: "Chaitra",
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

NUM_INDIAN_LUNAR = {"Chaitra": 0,
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

INDIAN_SOLAR_NUM = {0: "Meṣa",
                    1: "Vṛṣabha",
                    2: "Mithuna",
                    3: "Karkaṭa",
                    4: "Siṃha",
                    5: "Kanyā",
                    6: "Tulā",
                    7: "Vṛścika",
                    8: "Dhanu",
                    9: "Makara",
                    10: "Kumbha",
                    11: "Mīna"}

NUM_INDIAN_SOLAR = {"Meṣa": 0,
                    "Vṛṣabha": 1,
                    "Mithuna": 2,
                    "Karkaṭa": 3,
                    "Siṃha": 4,
                    "Kanyā": 5,
                    "Tulā": 6,
                    "Vṛścika": 7,
                    "Dhanu": 8,
                    "Makara": 9,
                    "Kumbha": 10,
                    "Mīna": 11}


BENGALI_NUM = ("Bôishakh", "Jyôishțhô", "Āshāḍh", "Srabôn", "Bhadrô", "Aśvin", "Kartik", "Ôgrôhayôn", "Poush", "Magh", "Falgun", "Choitrô")

NUM_BENGALI = {"Bôishakh": 0,
               "Jyôishțhô": 1,
               "Āshāḍh": 2,
               "Srabôn": 3,
               "Bhadrô": 4,
               "Aśvin": 5,
               "Kartik": 6,
               "Ôgrôhayôn": 7,
               "Poush": 8,
               "Magh": 9,
               "Falgun": 10,
               "Chôitrô": 11}

NUM_NANAKSHAHI = ("Chet", "Vaisakh", "Jeth", "Harh", "Sawan", "Bhadon", "Asu", "Katik", "Maghar", "Poh", "Magh", "Phagun")

NANAKSHAHI_NUM = {"Chet": 0,
                  "Vaisakh": 1,
                  "Jeth": 2,
                  "Harh": 3,
                  "Sawan": 4,
                  "Bhadon": 5,
                  "Asu": 6,
                  "Kartik": 7,
                  "Maghar": 8,
                  "Poh": 9,
                  "Magh": 10,
                  "Phagun": 11}

NUM_NEPALI = ("Kachhalā", "Thinlā", "Pwanhelā", "Silā", "Chilā", "Chaulā", "Bachhalā", "Tachhalā", "Dilā", "Gunlā", "Tanlā", "Kaulā", "Analā")

NEPALI_NUM = {"Kachhalā": 1,
              "Thinlā": 2,
              "Pwanhelā": 3,
              "Silā": 4,
              "Chilā": 5,
              "Chaulā": 6,
              "Bachhalā": 7,
              "Tachhalā": 8,
              "Dilā": 9,
              "Gunlā": 10,
              "Tanlā": 11,
              "Kaulā": 12,
              "Analā": 13}

NUM_TIBETAN = ("Mchu", "Dbo", "Nag pa", "Sa ga", "Snron", "Chu stod", "Gro Bzhin", "Khrums", "Tha skar", "Smin drug", "Mgo", "Rgyal")

TIBETAN_NUM = {"Mchu": 0,
	       "Dbo": 1,
               "Nag pa": 2,
               "Sa ga": 3,
               "Snron": 4,
               "Chu stod": 5,
               "Gro Bzhin": 6,
               "Khrums": 7,
               "Tha skar": 8,
               "Smin drug": 9,
               "Mgo": 10,
               "Rgyal": 11}

MYANMAR = ("Tagu", "Kason", "Nayon", "Wahso", "Wahso 2", "Wahgaung", "Tawthalin", "Thadinkyut", "Tazaungmon", "Natdaw", "Pyatho", "Tabodwe", "Tabaung")
MYANMAR_MONTH_LENGTHS = {354: (29, 30, 29, 30,  0, 29, 30, 29, 30, 29, 30, 29, 30), # normal year
                         384: (29, 30, 29, 30, 30, 29, 30, 29, 30, 29, 30, 29, 30), # leap year without a leap day
                         385: (29, 30, 30, 30, 30, 29, 30, 29, 30, 29, 30, 29, 30)} # leap year with leap day

MYANMAR_NORMAL = {"Tagu": 29,
                  "Kason": 30,
                  "Nayon": 29,
                  "Wahso": 30,
                  "Wahgaung": 29,
                  "Tawthalin": 30,
                  "Thadinkyut": 29,
                  "Tazaungmon": 30,
                  "Natdaw": 29,
                  "Pyatho": 30,
                  "Tabodwe": 29,
                  "Tabaung": 30}

MYANMAR_LEAP = {"Tagu": 29,
                "Kason": 30,
                "Nayon": 29,
                "Wahso": 30,
                "Wahso 2": 30,
                "Wahgaung": 29,
                "Tawthalin": 30,
                "Thadinkyut":	29,
                "Tazaungmon":	30,
                "Natdaw": 29,
                "Pyatho": 30,
                "Tabodwe": 29,
                "Tabaung": 30}

MYANMAR_LONG = {"Tagu": 29,
                "Kason": 30,
                "Nayon": 30,
                "Wahso": 30,
                "Wahso 2": 30,
                "Wahgaung": 29,
                "Tawthalin": 30,
                "Thadinkyut":   29,
                "Tazaungmon":   30,
                "Natdaw": 29,
                "Pyatho": 30,
                "Tabodwe": 29,
		"Tabaung": 30}

ARAKAN_LEAP = {"Tagu": 29,
               "Tagu 2": 30,
               "Kason": 30,
               "Nayon": 29,
               "Wahso": 30,
               "Wahgaung": 29,
               "Tawthalin": 30,
               "Thadinkyut": 29,
               "Tazaungmon": 30,
               "Natdaw": 29,
               "Pyatho": 30,
               "Tabodwe": 29,
               "Tabaung": 30}

ARAKAN_LONG = {"Tagu": 29,
               "Tagu 2": 30,
               "Kason": 30,
               "Nayon": 30,
               "Wahso": 30,
               "Wahgaung": 29,
               "Tawthalin": 30,
               "Thadinkyut": 29,
               "Tazaungmon": 30,
               "Natdaw": 29,
               "Pyatho": 30,
               "Tabodwe": 29,
	       "Tabaung": 30}

THAI_SID = ("Meesaă", "Phrɯ́tsaphaa", "Míthùnaa", "Kàrákàdaa", "Sǐnghǎa", "Kanyaa", "Tùlaa", "Phrɯ́tsacìkaa", "Thanwaa", "Mákàraa", "Kumphaa", "Miinaa")

THAI_SID_NUM = {"Meesaă": 0,
                "Phrɯ́tsaphaa": 1,
                "Míthùnaa": 2,
                "Kàrákàdaa": 3,
                "Sǐnghǎa": 4,
                "Kanyaa": 5,
                "Tùlaa": 6,
                "Phrɯ́tsacìkaa": 7,
                "Thanwaa": 8,
                "Mákàraa": 9,
                "Kumphaa": 10,
                "Miinaa": 11}

THAI_TROPICAL_NORMAL = {"Mákàraa-khom": 31,
                        "Kumphaa-phan": 28,
                        "Miinaa-khom": 31,
                        "Meesaǎ-yon": 30,
                        "Phrɯ́tsaphaa-khom": 31,
                        "Míthùnaa-yon": 30,
                        "Kàrákàdaa-khom": 31,
                        "Sǐnghǎa-khom": 31,
                        "Kanyaa-yon": 30,
                        "Tùlaa-khom": 31,
                        "Phrɯ́tsacìkaa-yon": 30,
                        "Thanwaa-khom": 31}

THAI_TROPICAL_LEAP = {"Mákàraa-khom": 31,
                      "Kumphaa-phan": 28,
                      "Miinaa-khom": 31,
                      "Meesaǎ-yon": 30,
                      "Phrɯ́tsaphaa-khom": 31,
                      "Míthùnaa-yon": 30,
                      "Kàrákàdaa-khom": 31,
                      "Sǐnghǎa-khom": 31,
                      "Kanyaa-yon": 30,
                      "Tùlaa-khom": 31,
                      "Phrɯ́tsacìkaa-yon": 30,
                      "Thanwaa-khom": 31}

# note that the Thai lunar calendar increments in the month numbered 5 in Central Thailand, 6 in Keng Tung, and 7 in Chaing Mai
THAI_LUNAR_NORMAL = ("Deuan hâa",              #  5
                     "Deuan hòk",              #  6
                     "Deuan jèt",              #  7
                     "Deuan bpàaet",           #  8
                     "Deuan gâo",              #  9
                     "Deuan sip",              # 10
                     "Deuan sip nùeng",        # 11
                     "Deuan sip sǎawng",       # 12
                     "Deuan aai",              #  1
                     "Deuan yi",               #  2
                     "Deuan sǎam",             #  3
                     "Deuan sìi")              #  4

THAI_LUNAR_LEAP = ("Deuan hâa",              #  5                                                                  
                   "Deuan hòk",              #  6                                                                  
                   "Deuan jèt",              #  7                                                                  
                   "Deuan bpàaet",           #  8                                                                  
                   "Deuan bpàaet song khan", #  8.2                                                                
                   "Deuan gâo",              #  9
                   "Deuan sip",              # 10                                                           
                   "Deuan sip nùeng",        # 11                                                                  
                   "Deuan sip sǎawng",       # 12                                                                  
                   "Deuan aai",     	     #  1                                                                 
                   "Deuan yi",      	     #  2                                                                 
                   "Deuan sǎam",             #  3                                                                 
                   "Deuan sìi")     	     #  4

KENG_TUNG_LEAP = ("Deuan hòk",              #  6                                                                    
                  "Deuan jèt",              #  7                                                                    
                  "Deuan bpàaet",           #  8                                                                    
                  "Deuan gâo",              #  9
                  "Deuan gào song khan",    #  9.2
                  "Deuan sip",              # 10                                                                    
                  "Deuan sip nùeng",        # 11                                                                    
                  "Deuan sip sǎawng",       # 12                                                                    
                  "Deuan aai",              #  1                                                                    
                  "Deuan yi",               #  2                                                                    
                  "Deuan sǎam",             #  3                                                                    
                  "Deuan sìi",              #  4
                  "Deuan hâa")              #  5

CHIANG_MAI_LEAP = ("Deuan jèt",              #  7                                                                   
                   "Deuan bpàaet",           #  8                                                                   
                   "Deuan gâo",              #  9                                                                   
                   "Deuan sip",              # 10
                   "Deuan sip song khan",    # 10.2
                   "Deuan sip nùeng",        # 11                                                                   
                   "Deuan sip sǎawng",       # 12                                                                   
                   "Deuan aai",              #  1                                                                   
                   "Deuan yi",               #  2                                                                   
                   "Deuan sǎam",             #  3                                                                  
                   "Deuan sìi",              #  4
                   "Deuan hâa",              #  5
                   "Deuan hòk")              #  6

KHMER_NORMAL = ("Chaet", "Vesak", "Jais", "Ashad",                    "Srap", "Phutrobot", "Asuj", "Kadhek", "Mekasay", "Bos", "Meak", "Phagaun")
KHMER_LEAP  =  ("Chaet", "Vesak", "Jais", "Bhadamasad", "Thutiyasad", "Srap", "Phutrobot", "Asuj", "Kadhek", "Mekasay", "Bos", "Meak", "Phagaun")

BALINESE_LUNAR = ("Mengsa Kadasa", "Mengsa Desta", "Mengsa Sada", "Mengsa Kaso", "Mengsa Karo", "Mengsa Katiga", "Mengsa Kapat", "Mengsa Kalima", "Mengsa Kanem", "Mengsa Kapitu", "Mengsa Kaulu", "Mengsa Kasanga")

NUM_BALINESE = {"Mengsa Kadasa":   0,
                "Mengsa Desta":    1,
                "Mengsa Sada":     2,
                "Mengsa Kaso":     3,
                "Mengsa Karo":     4,
                "Mengsa Katiga":   5,
                "Mengsa Kapat":    6,
                "Mengsa Kalima":   7,
                "Mengsa Kanem":    8,
                "Mengsa Kapitu":   9,
                "Mengsa Kaulu":   10,
                "Mengsa Kasanga": 11}

JAVANESE = ("Sura", "Sapar", "Mulud", "Bakda Mulud", "Jumadil Awal", "Jumadil Akhir", "Rejeb", "Ruwah", "Pasa", "Sawal", "Dulkangidah", "Besar")


OLD_CHINESE = ("Zōuyuè", "Xìngyuè", "Táoyuè", "Méiyuè", "Liúyuè", "Héyuè", "Lányuè", "Guìyuè", "Júyuè", "Lùyuè", "Dōngyuè", "Bīngyuè")

NUM_OLD_CHINESE = {"Dōngyuè": 10,
                   "Bīngyuè": 11,
                   "Zōuyuè":   0,
                   "Xìngyuè":  1,
                   "Táoyuè":   2,
                   "Méiyuè":   3,
                   "Liúyuè":   4,
                   "Héyuè":    5,
                   "Lányuè":   6,
                   "Guìyuè":   7,
                   "Júyuè":    8,
                   "Lùyuè":    9}

CHINESE = ("Zhēngyuè", "Èryuè", "Sānyuè", "Sìyuè", "Wǔyuè", "Liùyuè", "Qīyuè", "Bāyuè", "Jiǔyuè", "Shíyuè", "Shíyīyuè", "Làyuè")

NUM_CHINESE = {"Zhēngyuè":  0,
               "Èryuè":     1,
               "Sānyuè":    2,
               "Sìyuè":     3,
               "Wǔyuè":     4,
               "Liùyuè":    5,
               "Qīyuè":     6,
               "Bāyuè":     7,
               "Jiǔyuè":    8,
               "Shíyuè":    9,
               "Shíyīyuè": 10,
               "Làyuè":    11}

# Hawai'ian month names
HAWAIIAN = ("Welehu", "Makaliʻi", "Kāʻelo", "Kaulua", "Nana", "Welo", "Ikiiki", "Kaʻaona", "Hinaiaʻeleʻele", "Māhoe Mua", "Māhoe Hope", "ʻIkuā")

NUM_HAWAIIAN = {"Welehu":         0,
                "Makaliʻi":       1,
                "Kāʻelo":         2,
                "Kaulua":         3,
                "Nana":           4,
                "Welo":           5,
                "Ikiiki":         6,
                "Kaʻaona":        7,
                "Hinaiaʻeleʻele": 8,
                "Māhoe Mua":      9,
                "Māhoe Hope":    10,
                "ʻIkuā":         11}

KAUAI = ("Hilinamā", "Hilinehu", "Hilioholo", "Hilionalu", "Hukipau", "ʻIkuā", "Welehu", "Kāʻelo", "Ikiiki", "Hinaiaʻeleʻele", "Māhoe Mua", "Māhoe Hope")

NUM_KAUAI = {"Hilinamā":       0,
             "Hilinehu":       1,
             "Hilioholo":      2,
             "Hilionalu":      3,
             "Hukipau":        4,
             "ʻIkuā":          5,
             "Welehu":         6,
             "Kāʻelo":         7,
             "Ikiiki":         8,
             "Hinaiaʻeleʻele": 9,
             "Māhoe Mua":     10,
             "Māhoe Hope":    11}

NAPOOPOO = ("Nana", "Welo", "Ikiiki", "Kaʻaona", "Hinaiaʻeleʻele", "Māhoe Mua", "Māhoe ʻe Lua", "ʻIkuā", "Kāʻelo", "Makaliʻi", "Welehu", "Kaulua")

NUM_NAPOOPOO = {"Nana":           0,
                "Welo":           1,
                "Ikiiki":         2,
                "Kaʻaona":        3,
                "Hinaiaʻeleʻele": 4,
                "Māhoe Mua":      5,
                "Māhoe ʻe Lua":   6,
                "ʻIkuā":          7,
                "Kāʻelo":         8,
                "Makaliʻi":       9,
                "Welehu":        10,
                "Kaulua":        11}

# Māori month names
TUHOE = ("Pipiri", "Hōngongoi", "Here-turi-kōkā", "Mahuru", "Whiringa-ā-nuku", "Whiringa-ā-rangi", "Hakihea", "Kohitātea", "Hui-tanguru", "Poutū-te-rangi", "Paenga-whāwhā", "Haratua")

NUM_TUHOE = {"Pipiri":           0,
             "Hōngongoi":        1,
             "Here-turi-kōkā":   2,
             "Mahuru":           3,
             "Whiringa-ā-nuku":  4,
             "Whiringa-ā-rangi": 5,
             "Hakihea":          6,
             "Kohitātea":        7,
             "Hui-tanguru":      8,
             "Poutū-te-rangi":   9,
             "Paenga-whāwhā":   10,
             "Haratua":         11}

NGATIAWA = ("Te Tahi o Pipiri", "Te Rua o Takurua", "Te Toru o Here-turi-koka", "Te Wha o Mahuru", "Te Rima o Kopu", "Whitianaunau", "Hakihea", "Kai-tatea", "Ruhi-te-rangi", "Poutu-te-rangi", "Paenga-whawha", "Haki-haratua")

NUM_NGATIAWA = {"Te Tahi o Pipiri":         0,
                "Te Rua o Takurua":         1,
                "Te Toru o Here-turi-koka": 2,
                "Te Wha o Mahuru":          3,
                "Te Rima o Kopu":           4,
                "Whitianaunau":             5,
                "Hakihea":                  6,
                "Kai-tatea":                7,
                "Ruhi-te-rangi":            8,
                "Poutu-te-rangi":           9,
                "Paenga-whawha":           10,
                "Haki-haratua":            11}

KAHUNGUNU = ("Aonui", "Te Aho-turuturu", "Te Ihomatua", "Tapere-wai", "Tatau-urutahi", "Tatau-uruora", "Akāka-nui", "Akuahu-mataora", "Te Ihonui", "Putoki-nui-o-tau", "Tikaka-muturangi", "Uruwhenhua")

NUM_KAHUNGUNU = {"Aonui":             0,
                 "Te Aho-turuturu":   1,
                 "Te Ihomatua":       2,
                 "Tapere-wai":        3,
                 "Tatau-urutahi":     4,
                 "Tatau-uruora":      5,
                 "Akāka-nui":         6,
                 "Akuahu-mataora":    7,
                 "Te Ihonui":         8,
                 "Putoki-nui-o-tau":  9,
                 "Tikaka-muturangi": 10,
                 "Uruwhenhua":       11}

SOUTH_MAORI = ("Matahi o Pouaka", "Maruaroa", "Te Toru", "Te Wha", "Te Rima", "Te Ono", "Te Whitu", "Te Waru", "Te Iwa", "Te Ngahuru", "Ngahuru-nui", "Matahi o te tau", "Matahi o Mahurihuri")

NUM_SOUTH_MAORI = {"Matahi o Pouaka":      0,
                   "Maruaroa":             1,
                   "Te Toru":              2,
                   "Te Wha":               3,
                   "Te Rima":              4,
                   "Te Ono":               5,
                   "Te Whitu":             6,
                   "Te Waru":              7,
                   "Te Iwa":               8,
                   "Te Ngahuru":           9,
                   "Ngahuru-nui":         10,
                   "Matahi o te tau":     11,
                   "Matahi o Mahurihuri": 12}

MORIORI = ("Kahu", "Rongo", "Tahei", "Keitanga", "Tauaropoti", "Wareahe", "Tchuhe a Takarore", "Wairehu", "Moro", "Mihi-torekau", "Ta Upoko o T'etchiao", "Tumatehea")

NUM_MORIORI = {"Kahu":                  0,
               "Rongo":                 1,
               "Tahei":                 2,
               "Keitanga":              3,
               "Tauaropoti":            4,
               "Wareahe":               5,
               "Tchuhe a Takarore":     6,
               "Wairehu":               7,
               "Moro":                  8,
               "Mihi-torekau":          9,
               "Ta Upoko o T'etchiao": 10,
               "Tumatehea":            11}

SAMOAN = ("Toe-taumafa", "Utuva-mua", "Utuva-muli", "Fa'aafu", "Lo", "Aununu", "Oloamanu", "Palolo-mua", "Palolo-muli", "Mulifa", "Lotuanga", "Taumafa-mua", "Leap month")

NUM_SAMOAN = {"Toe-taumafa":  0,
              "Utuva-mua":    1,
              "Utuva-muli":   2,
              "Fa'aafu":      3,
              "Lo":           4,
              "Aununu":       5,
              "Oloamanu":     6,
              "Palolo-mua":   7,
              "Palolo-muli":  8,
              "Mulifa":       9,
              "Lotuanga":    10,
              "Taumafa-mua": 11,
              "Leap month":  12}

RAPANUI = ("Anekena", "Hora-iti", "Hora-nui", "Tangarouri", "Kotuti", "Ruti", "Koro", "Tuaharo", "Tetuupu", "Tarahao", "Vaitu-nui", "Vaitu-poto", "Maro")

NUM_RAPANUI = {"Anekena":     0,
               "Hora-iti":    1,
               "Hora-nui":    2,
               "Tangarouri":  3,
               "Kotuti":      4,
               "Ruti":        5,
               "Koro":        6,
               "Tuaharo":     7,
               "Tetuupu":     8,
               "Tarahao":     9,
               "Vaitu-nui":  10,
               "Vaitu-poto": 11,
               "Maro":       12}

FIJI = ("Vula i Kelikeli", "Vula i Gasau", "Vula i Doi", "Vula i Werewere", "Vula i Cukicuki", "Vula i Se-ni-drala", "Vula i Vavakada", "Vula i Balolo Lailai", "Vula i Balolo Levu", "Vula i Nuqa Lailai", "Vula i Nuqa Levu", "Vula i Sevu")

NUM_FIJI = {"Vula i Kelikeli":      0,
            "Vula i Gasau":         1,
            "Vula i Doi":           2,
            "Vula i Werewere":      3,
            "Vula i Cukicuki":      4,
            "Vula i Se-ni-drala":   5,
            "Vula i Vavakada":      6,
            "Vula i Balolo Lailai": 7,
            "Vula i Balolo Levu":   8,
            "Vula i Nuqa Lailai":   9,
            "Vula i Nuqa Levu":    10,
            "Vula i Sevu":         11}

TAHITIAN = ("Te-tai", "Avarehu", "Fā‘ahu", "Pipiri", "Tāoa", "Aununu", "Apa‘apa", "Paroro mua", "Paroro mui", "Muriaha", "Hiaia", "Tema", "Te-eri")

NUM_TAHITIAN = {"Avarehu":    1,
                "Fā‘ahu":     2,
                "Pipiri":     3,
                "Tāoa":       4,
                "Aununu":     5,
                "Apa‘apa":    6,
                "Paroro mua": 7,
                "Paroro mui": 8,
                "Muriaha":    9,
                "Hiaia":     10,
                "Tema":      11,
                "Te-eri":    12,
                "Te-tai":     0}

PASHTO = ("Hamal", "Sawr", "Jawza", "Saratan", "Asad", "Sunbula", "Mizan", "'Aqrab", "Qaws", "Jaddi", "Dalwa", "Hout")

NUM_PASHTO = {"Hamal":   0,
              "Sawr":    1,
              "Jawza":   2,
              "Saratan": 3,
              "Asad":    4,
              "Sunbula": 5,
              "Mizan":   6,
              "'Aqrab":  7,
              "Qaws":    8,
              "Jaddi":   9,
              "Dalwa":  10,
              "Hout":   11}

ATHENIAN = ("Hekatombaion", "Metageitnion", "Boedromion", "Pyanepsion", "Maimakterion", "Poseideon", "Gamelion", "Anthesterion", "Elaphebolion", "Mounichion", "Thargelion", "Skirophorion")

NUM_ATHENIAN = {"Hekatombaion":  0,
                "Metageitnion":  1,
                "Boedromion":    2,
                "Pyanepsion":    3,
                "Maimakterion":  4,
                "Poseideon":     5,
                "Gamelion":      6,
                "Anthesterion":  7,
                "Elaphebolion":  8,
                "Mounichion":    9,
                "Thargelion":   10,
                "Skirophorion": 11}

DELIAN = ("Lenaion", "Hieros", "Galaxion", "Artemision", "Thargelion", "Panemos", "Hekatombaion", "Metageitnion", "Bouphonion", "Apatourion", "Aresion", "Poseideon")

NUM_DELIAN = {"Lenaion":      0,
              "Hieros":       1,
              "Galaxion":     2,
              "Artemision":   3,
              "Thargelion":   4,
              "Panemos":      5,
              "Hekatombaion": 6,
              "Metageitnion": 7,
              "Bouphonion":   8,
              "Apatourion":   9,
              "Aresion":     10,
              "Poseideon":   11}

BOEOTIAN = ("Bukátios", "Hermaíos", "Prostatḗrios", "Agriṓnios", "Homolṓios", "Theiloúthios", "Hippodrómios", "Pánamos", "Pamboiṓtios", "Damátrios", "Alalkoménios", "Thiouios")

NUM_BOEOTIAN = {"Bukátios":      0,
                "Hermaíos":      1,
                "Prostatḗrios":  2,
                "Agriṓnios":     3,
                "Homolṓios":     4,
                "Theiloúthios":  5,
                "Hippodrómios":  6,
                "Pánamos":       7,
                "Pamboiṓtios":   8,
                "Damátrios":     9,
                "Alalkoménios": 10,
                "Thiouios":     11}

DELPHIAN = ("Apellaios", "Boukatios", "Boathoos", "Heraios", "Daidaphorios", "Poitropios", "Amalios", "Bysios", "Theoxenios", "Endyspoitropios", "Herakleios", "Ilaios")

NUM_DELPHIAN = {"Apellaios":       0,
                "Boukatios":       1,
                "Boathoos":        2,
                "Heraios":         3,
                "Daidaphorios":    4,
                "Poitropios":      5,
                "Amalios":         6,
                "Bysios":          7,
                "Theoxenios":      8,
                "Endyspoitropios": 9,
                "Herakleios":     10,
                "Ilaios":         11}

AITOLIAN = ("Athanaios", "Boukatios", "Dios", "Euthaios", "Homoloios", "Hermaios", "Dionysios", "Agyeios", "Hippodromios", "Laphraios", "Panamos", "Prokyklios")

NUM_AITOLIAN = {"Athanaios":    0,
                "Boukatios":    1,
                "Dios":         2,
                "Euthaios":     3,
                "Homoloios":    4,
                "Hermaios":     5,
                "Dionysios":    6,
                "Agyeios":      7,
                "Hippodromios": 8,
                "Laphraios":    9,
                "Panamos":     10,
                "Prokyklios":  11}

MACEDONIAN = ("Dios", "Apellaios", "Audnaios", "Peritios", "Dystros", "Xandikos", "Artemisios", "Daisios", "Panemos", "Loios", "Gorpiaios", "Hyperberetaios")

NUM_MACEDONIAN = {"Dios":            0,
                  "Apellaios":       1,
                  "Audnaios":        2,
                  "Peritios":        3,
                  "Dystros":         4,
                  "Xandikos":        5,
                  "Artemisios":      6,
                  "Daisios":         7,
                  "Panemos":         8,
                  "Loios":           9,
                  "Gorpiaios":      10,
                  "Hyperberetaios": 11}

ROMAN = ("Ianuarius", "Februarius", "Mercedonius", "Martius", "Aprilis", "Maia", "Iunius", "Quintilis", "Sextilis", "Septembris", "Octobris", "Novembris", "Decembris")

ROMAN_LENGTHS = {355: (29, 28,  0, 31, 29, 31, 29, 31, 29, 29, 31, 29, 29), # normal year
                 377: (29, 23, 27, 31, 29, 31, 29, 31, 29, 29, 31, 29, 29), # leap year, Mercedonius before regifugium
                 378: (29, 23, 28, 31, 29, 31, 29, 31, 29, 29, 31, 29, 29)} # leap year, Mercedonius afer Regifugium
