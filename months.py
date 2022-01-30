#!/usr/bin/python3

# This is a set of months for use in calconv

# GREGORIAN AND JULIAN CALENDARS

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
