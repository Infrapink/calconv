This is calconv, a program to convert between various calendars. It's my first real program, started in order to teach myself Python when I had downtime during the 2020 Covid-19 pandemic.

REQUIREMENTS

To run calconv, you must have the Python programming language and the Tkinter toolkit installed. If you're running a Unix or Unix-like operating system, they probably came with your OS. If not, they should be available through your package manager (called an "app store" on Mac and Windows). If you can't find it in your package manager, you can download it from the following link:

https://www.python.org/downloads/release/python-383/

RUNNING

From the command line, navigate to the folder where you unpacked the program and type:

./calconv.py

On Windows, you can instead double-click on calconv.bat

Dates are entered in the indicated text boxes in the order Day, Month, Year (except for the Julian Day, which is just a number). For now, months must be written in full, and entered exactly as listed here, including punctuation and diacritical marks. A later version will replace the text entry fields with selectable dropdown menus. Years before the calendar epoch are entered as negative numbers; so, for example, the year 44 BC would be input as -44.

Julian Day:
* This is a simple number.

Julian calendars, Gregorian calendars, Parker, Goucher-Parker, Serbian Church, World, International Fixed, Pax, Gorman, and Holocene Calendars:
* January
* February
* Gormanuary (Gorman calendar only)
* Intermission (Gorman calendar only)
* March
* April
* May
* June
* Sol (International Fixed calendar only)
* July
* August
* September
* October
* November
* Pax (Pax calendar only)
* December
* Worldsday (World calendar only)
* Year Day (International Fixed calendar only)
* Leap day (World and International Fixed calendars only)

Ethiopian Calendar:
* Mäskäräm
* Ṭəqəmt
* Ḫədar
* Taḫśaś
* Ṭərr
* Yäkatit
* Mägabit
* Miyazya
* Gənbo
* Säne
* Ḥamle
* Nähase
* Ṗagume
* Extra Days

Coptic Calendar:
* Thout
* Paopi
* Hathor
* Koiak
* Tobi
* Meshir
* Paremhat
* Parmouti
* Pashons
* Paoni
* Epip
* Mesori
* Extra days

Egyptian Calendar:
* Thoth
* Phaophi
* Hathor
* Choak
* Tybi
* Mechir
* Phamenoth
* Pharmuthi
* Pachons
* Payni
* Spiphi
* Mesore
* Extra days

Lunar Hijri Calendar:
* Muharram
* Safar
* Rabi' al-awwal
* Rabi' al-Thani
* Jumada al-awwal
* Jumada al-Thani
* Rajab
* Sha'ban
* Ramadan
* Shawwal
* Dhu al-Qidah
* Dhu al-Hijjah

Jalali, Solar Hijri and Ahmad Birashk's Calendars:
* Farvardin
* Ordibehesht
* Khordad
* Tir
* Mordad
* Shahrivar
* Mehr
* Aban
* Azar
* Dey
* Bahman
* Esfand

Armenian Calendar:
* Nawasard
* Hoṙi
* Sahmi
* Trē
* Kʿałocʿ
* Arac
* Mehekan
* Areg
* Ahekan
* Mareri
* Margac
* Hrotic'
* Extra days

Modern Assyrian Calendar
* Nīsān
* ʾĪyār
* Ḥzīrān
* Tammūz
* Ṭabbāḥ
* ʾĪlūl
* Tešrīn Qḏīm
* Tešrīn Ḥrāy
* Kānōn Qḏīm
* Kānōn Ḥrāy
* Šḇāṭ
* Āḏar

Babylonian Calendar:
* Nisānu
* Āru
* Simanu
* Dumuzu
* Abu
* Ulūlu
* Ulūlu Arku (only in the 17th year of the Metonic cycle)
* Tišritum
* Samnu
* Kislimu
* Ṭebētum
* Šabaṭu
* Addaru
* Addaru Arku (leap years only)

Hebrew and Samaritan calendars:
* Tishrei
* Marcheshvan
* Kislev
* Tevet
* Shevat
* Adar
* Veadar (leap years only)
* Nisan
* Iyar
* Sivan
* Tammuz
* Av
* Elul

(Note: Everyone else lists Nisan as the first month of the year, and Adar/Veadar as the last. This is for Jewish
cultural reasons; however, Tishrei is the first month of the civil Hebrew calendar, as it is on 1 Tishrei
that theyear number increments. I have listed the months in this order to avoid confusion. Nisan is the first day of the year in the Samaritan calendar).

Kurdish calendar:
* Jejhnan
* Gullan
* Zerdan
* Púshperr
* Gelawéjh
* Xermanan
* Beran
* Xezan
* Saran
* Befran
* Rébandan
* Reshemé

Amazigh calendar:
* Yennayer
* Yebrayer
* Mares
* Yebrir
* May
* Yunyu
* Yulyuz
* Ɣuct
* Shutembir
* Ktuber
* Nwambir
* Dujembir

Rumi calendars:
* Mart
* Nisan
* Mayıs
* Haziran
* Temmuz
* Ağustos
* Eylül
* Teşrin-i Evvel
* Teşrin-i Sânî
* Kânûn-ı Evve
* Kânûn-ı Sânî
* Şubat

Pax 2020:
* Initium
* Rutilante
* Semen
* Gaudium
* Apes
* Serenium
* Coleum
* Amare
* Messis
* Follium
* Nixcumumis
* Pax
* Requiem

Positivist calendar
* Moses
* Homer
* Aristotle
* Archimedes
* Caesar
* St. Paul
* Charlemagne
* Dante
* Gutenberg
* Shakespeare
* Descartes
* Frederick II
* Bichat
* Festival of All the Dead
* Festival of Holy Women

French Republican calendars:
* Vendémiaire
* Brumaire
* Frimaire
* Nivôse
* Pluviôse
* Ventôse
* Germinal
* Floréal
* Prairial
* Messidor
* Thermidor
* Fructidor
* Sans-culottides

Thellid calendar
* Alvakku
* Bethanis
* Duvadda
* Emovvi
* Forkithal
* Kalvazzi
* Irentos
* Jukennuk
* Miskullen
* Ossakov
* Raikkaved
* Underro
* Zithebbe
* Leap Day (leap years only)
* Old Year's Day

LICENSE

calconv is copyright Chris McCrohan.

calconv is licensed under the GNU General Public License version 3.0 or, at your option, any later version. Full details are contained in the LICENSE file. In short, you are free to alter, copy, and redistribute this software (and even charge a fee for it) as you please, and anybody who received a copy from you has the same rights.

FUTURE GOALS

Replace the text boxes for months with dropdown menus.

Add the following calendars:
* Old Roman
* Byzantine
* Mayan
* Chinese Lunisolar
* Shire Reckoning
* Buddhist
* Indian
* ISO
* Baha'í
* Saka
* Bengali
* Myanmar
* Discordian
* Vikram Samvat
* Shaka Samvat
* Kali Yuga
* Celtic
* Igbo
* Javanese
* Korean
* Minguo
* ROC
* Nanakshahi
* Thai
* Tibetan
* Julian Period
