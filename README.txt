This is calconv, a program to convert between various calendars. It's my first real program, started in order to teach myself Python when I had downtime during the 2020 Covid-19 pandemic.

REQUIREMENTS
============

calconv is written mostly in Python 3, and uses Fortran for some of the more intense number crunching. It uses NumPy's f2py module to all Python scripts to interface with Fortran binaries, and the Tkinter toolkit to generate the GUI. Due to issues with f2py, I can't guarantee that calconv will run properly on Microsoft Windows.

The specific programs you will need to compile and run calconv are:
* A Python 3 interpreter. This comes as standard with Linux, BSD, and I believe Mac.
* The NumPy library. The Anaconda Python distribution comes with NumPy built in.
* The Tkinter library
* A Fortran compiler. The standard Fortran compiler on Unix-like operating systems is gfortran; on Windows, ifort is more common, but my Fortran makes use of features which ifort might not include

All these components should be available through your package manager (called an "app store" on Mac and Windows). If you do not wish to use a graphical program to install everything, you can enter the following commands on the command line in Linux:

Arch (Chakra, Manjaro):

    $ sudo pacman -Syu python tk python-numpy gcc-fortran

Debian (Ubuntu, Mint):

    $ sudo apt-get install python3 python3-tk python3-numpy gfortran

Fedora (CentOS, Red Hat Enterprise Linux, PCLinuxOS):

    $ sudo dnf install python3 python3-tk python3-numpy gcc-gfortran

MS Windows users can download the components from the following links:
* Python (including NumPy and Tk): https://www.anaconda.com/products/individual
* gfortran: http://www.equation.com/servlet/equation.cmd?fa=fortran

COMPILING
=========

Before you can run calconv, you will need to compile the Fortran code. In the command line, navigate to the folder where you unpacked the source code (which should be the one containing this Readme file) and type the following:

    f2py -c sunmoon.f90 -m sunmoon
    f2py -c zodiac.f90 -m zodiac
    f2py -c tibetan.f90 -m tibetan

(This only needs to be done once; however, if Python is updated to a new version number, it can break compatibility with binary code, and so a recompile will be necessary)

RUNNING
=======

From the command line, navigate to the folder where you unpacked the program and type:

    ./calconv.py

On Windows, you can instead double-click on calconv.bat

Dates are entered in the indicated text boxes in the order Day, Month, Year; if there is only one text box, input is a simple number. For now, months must be written in full, and entered exactly as listed here, including punctuation and diacritical marks. A later version will replace the text entry fields with selectable dropdown menus. Years before the calendar epoch are entered as negative numbers; so, for example, the year 44 BC would be input as '-44'.

Julian, Gregorian, Parker, Goucher-Parker, Serbian Church, World, International Fixed, Pax, Gorman, Georgian (Christian era), ADA, Holocene, and Byzantine Calendars:
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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
* Georgy (Georgian calendar only)
* Christmas (Georgian calendar only)
* Olympiad (Georgian calendar only)

Ethiopian Calendar:
-------------------

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
----------------

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

Egyptian and Sothic Calendars:
------------------------------

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

Lunar Hijri, Tabular Islamic, and Pre-Islamic Arab calendars:
---------------------------------------------------------------

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
* Nasiʾ (Pre-Islamic Arab calendar only)

Jalali, Solar Hijri, Ahmad Birashk's, Iranian National, Qadimi, Shenshai, Oshmurtik, Vihezakik, Shahanshahi, Fasli, Young Avestan Calendars:
--------------------------------------------------------------------------------------------------------------------------------------------

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
* Kabizeh (Young Avestan, Shahanshahi, and Vihezakik calendars only)

Armenian Calendar:
------------------

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
------------------------

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

Babylonian Calendars:
---------------------

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

Hebrew (Jewish and Samaritan) calendars:
----------------------------------------

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
that the year number increments. I have listed the months in this order to avoid confusion. Nisan is the first
month of the year in the Samaritan and Karaite calendars).

Kurdish calendar:
-----------------

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
-----------------

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

Rumi (Ottoman fiscal) calendar:
-------------------------------

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
---------

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
-------------------

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
----------------------------

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
----------------

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

Igbo calendar
-------------

* Mbụ
* Abụo
* Ife Eke
* Anọ
* Agwụ
* Ifejiọkụ
* Alọm Chi
* Ilo Mmụọ
* Ana
* Okike
* Ajana
* Ede Ajana
* Ụzọ Alụsị

Roman calendar
--------------

* Martius
* Aprilis
* Maia
* Iunius
* Quintilis
* Sextilis
* Septembris
* Octobris
* Novembris
* Decembris
* Ianuarius
* Februarius

Macedonian and Seleucid calendars:
----------------------------------

* Dios
* Apellaiios
* Audunaios
* Peritios
* Dystros
* Xanthikos
* Xandikos Embolimos (leap years only)
* Artemisios
* Daisios
* Panamos
* Lōios
* Gorpiaios
* Hyperberetaios
* Hyperberetaios Embolimos (only in some leap years)

Georgian calendar (Georgian Era)
--------------------------------

* Peter
* Andrew
* James the Great
* John
* Philip
* Bartholomew
* Thomas
* Matthew
* James the Less
* Jude
* Simon
* Matthias
* Paul

Korean:
-------

* Il-wol
* I-wol
* Sam-wol
* Sa-wol
* O-wol
* Yu-wol
* Chil-wol
* Pal-wol
* Gu-wol
* Si-wol
* Sibil-wol
* Sibi-wol

To get the leap month, add "Yun " before the name of the month.

Inca:
-----

* Intiraymipacha
* Pachacyahuarllamapacha
* Yapuypacha
* Coyaraymipacha
* Paramañaypacha
* Ayamarcaypacha
* Capacintiraymipacha
* Huacapacha
* Huarachicuypacha
* Paraypacha
* Rinrituccinapacha
* Aymuraypacha
* Intihuatapacyapanapacha (leap years only in the civil calendar)

Chinese lunisolar calendars:
----------------------------

* Zhēngyuè
* Èryuè
* Sānyuè
* Sìyuè
* Wǔyuè
* Liùyuè
* Qīyuè
* Bāyuè
* Jiǔyuè
* Shíyuè
* Shíyīyuè
* Làyuè

To get the leap month in the Chinese lunisolar calendar, precede it with "Rùn", for example "Rùn Zhēngyuè". In the Chinese lunisolar calendar, the leap month can occur anywhere in the year. For this reason, if a leap month is specified in a non-leap year, the algorithm assumes the user means the corresponding regular month; conversely, if an incorrect leap month is specified in a leap year, the algorithm assumes that the user means the actual leap month.

Chinese solar calendars:
------------------------

* Lìchūn
* Yǔshuı̌
* Jı̄ngzhé
* Chūnfēn
* Qı̄ngmíng
* Gǔyǔ
* Lìxià
* Xiǎomǎn
* Mángzhòng
* Xiàzhì
* Xiǎoshǔ
* Dàshǔ
* Lìqiū
* Chǔshǔ
* Báilù
* Qiūfēn
* Hánlù
* Shuāngjiàng
* Lìdōng
* Xiǎoxuě
* Dàxuě
* Dōngzhì
* Xiǎohán
* Dàhán

Older Chinese calendars:
------------------------

* Zōuyuè
* Xìngyuè
* Táoyuè
* Méiyuè
* Liúyuè
* Héyuè
* Lányuè
* Guìyuè
* Júyuè
* Lùyuè
* Dōngyuè
* Bīngyuè
* Rùnyuè (leap years only in the ancient calendars only)

Leap months in the Metonic calendars from the Han dynasty onwards are named by prefixing the month name with Rùn.

Vietnamese calendar:
--------------------

* Tháng Giêng
* Tháng Hai
* Tháng Ba
* Tháng Tư
* Tháng Năm
* Tháng Sáu
* Tháng Bảy
* Tháng Tám
* Tháng Chín
* Tháng Mười
* Tháng Mười Một
* Tháng Chạp
* Tháng Nhuận (leap years only)

Japanese calendars:
-------------------

* Ichigatsu
* Nigatsu
* Sangatsu
* Shigatsu
* Gogatsu
* Rokugatsu
* Shichigatsu
* Hachigatsu
* Kugatsu
* Juugatsu
* Juuichigatsu
* Juunigatsu
* Uruzuki (lunisolar calendar, leap years only)

Mongolian traditional calendar:
-------------------------------

* Negdugeer sar
* Khoyordugaar sar
* Guravdugaar sar
* Dörövdugeer sar
* Tarvdugaar sar
* Zurgadugaar sar
* Doldugaar sar
* Naĭmdugaar sar
* Yesdugeer sar
* Aravdugaar sar
* Arvannegdugeer sar
* Arvanchaërdugaar sar

To get the leap month, prefix the month name with "Shün ", such as "Shün Negdugeer sar"

Bahá'í calendars:
-----------------

* Bahá
* Jalál
* Jamál
* ʻAẓamat
* Núr
* Raḥmat
* Kalimát
* Kamál
* Asmáʼ
* ʻIzzat
* Mas͟híyyat
* ʻIlm
* Qudrat
* Qawl
* Masáʼil
* S͟haraf
* Sulṭán
* Mulk
* Ayyám-ul Há
* ʻAláʼ

Old Avestan calendars:
----------------------

* Ādukanaisha
* Thūravāhara
* Thāigracish
* Garmapada
* Thurnabadish
* Garbashiyash
* Bāgayādish
* Vrkazana
* Āçiyādiya
* Anāmaka
* Thwayauvā
* Vixayana
* Kabizeh (leap years only)
* Kabizeh 2 (double leap years only)

Sogdian calendar:
-----------------

* Nausardh
* Xorezhnic
* Nisanic
* Pusākic
* Shnāk-Xandic
* Xazānānc
* Baghakānic
* Āpānc
* Bōghic
* Mushboghic
* Zhimdic
* Xshūmic
* Extra days

Indian solar calendars:
-----------------------
* Meṣa
* Vṛṣabha
* Mithuna
* Karkaṭa
* Siṃha
* Kanyā
* Tulā
* Vṛścika
* Dhanu
* Makara
* Kumbha
* Mīna

(Note: In the Keralite/Malayam calendars, Siṃha is the first month)

Indian lunisolar calendars:
---------------------------

* Chaitra
* Vaisākha
* Jyēshtha
* Āshādha
* Shrāvana
* Bhādra
* Āshwin
* Kārtika
* Agrahāyana
* Pausha
* Māgha
* Phālguna
* Adhikmasa (Vedāṅga Jyotiṣa only)

(Note: In some calendars, Vaisākha is the first month). To specify a leap month in a lunisolar calendar, prefix the month name with "Adhik ".

Malayam calendar (Uthara Malayala Panchangam):
----------------------------------------------

* Kanni
* Thulam
* Vrischikam
* Dhanu
* Makaram
* Kumbham
* Meenam
* Medam
* Edavam
* Midhunam
* Karkitaka
* Chingam

Tamil calendar:
---------------
* Chittirai
* Vaikāsi
* Āni
* Ādi
* Āvani
* Purattāsi
* Aippasi
* Kartikai
* Mārgazhi
* Thai
* Māsi
* Panguni

Bengali calendars:
------------------
* Bôishakh
* Jyôishțhô
* Āshāḍh
* Srabôn
* Bhadrô
* Aśvin
* Kartik
* Ôgrôhayôn
* Poush
* Magh
* Falgun
* Chôitrô

Assamese calendar:
------------------
* Böhag
* Zeth
* Ahar
* Xaün
* Bhado
* Ahin
* Kati
* Aghün
* Puh
* Magh
* Fagun
* Söt

Odia calendar:
--------------
* Baiśākha
* Jyeṣṭha
* Āṣāḍha
* Śrābaṇa
* Bhādraba
* Āświna
* Kārttika
* Mārgaśira
* Pauṣa
* Māgha
* Phālguna
* Caitra

Manipuri calendar:
------------------
* Sajibhu
* Kalen
* Inga
* Ingel
* Thawan
* Langban
* Mera
* Hiyangei
* Poineu
* Wakching
* Phairen
* Lamda

Mandaean calendar:
------------------

* Daula
* Nuna
* 'mbra
* Taura
* Ṣilmia
* Sarṭana
* Aria
* Shumbulta
* Extra days
* Qaina
* Arqba
* Hiṭia
* Gadia

Nanakshahi calendars:
---------------------
* Chet
* Vaisakh
* Jeth
* Harh
* Sawan
* Bhadon
* Asu
* Kartik
* Maghar
* Poh
* Magh
* Phagun

Nepali calendars:
-----------------
* Kachhalā
* Thinlā
* Pwanhelā
* Silā
* Chilā
* Chaulā
* Bachhalā
* Tachhalā
* Dilā
* Gunlā
* Tanlā
* Kaulā
* Analā (leap years in the lunisolar calendar only)

Tibetan and Bhutanese calendars:
--------------------------------
* Mchu
* Dbo
* Nag pa
* Sa ga
* Snron
* Chu stod
* Gro Bzhin
* Khrums
* Tha skar
* Smin drug
* Mgo
* Rgyal

To specify a leap month, put "Leap " before the month name

Myanmar calendars:
------------------
* Tagu
* Kason
* Nayon
* Wahso
* Wahgaung
* Tawthalin
* Thadinkyut
* Tazaungmon
* Natdaw
* Pyatho
* Tabodwe
* Tabaung

Leap months are indicated by adding " 2" to the end of Wahso (or Tagu in the case of the Arakan calendar). If it's a date in Tagu before solar new year, add an "*" to the year number to indicate that the lunar year has begun but the year number has not yet incremented. The Kayin calendar year begins on 1 Pyatho, and not on solar near year.

Thai sidereal calendars:
------------------------
* Meesaă
* Phrɯ́tsaphaa
* Míthùnaa
* Kàrákàdaa
* Sǐnghǎa
* Kanyaa
* Tùlaa
* Phrɯ́tsacìkaa
* Thanwaa
* Mákàraa
* Kumphaa
* Miinaa

Thai tropical calendars:
------------------------
* Mákàraa-khom
* Kumphaa-phan
* Miinaa-khom
* Meesaǎ-yon
* Phrɯ́tsaphaa-khom
* Míthùnaa-yon
* Kàrákàdaa-khom
* Sǐnghǎa-khom
* Kanyaa-yon
* Tùlaa-khom
* Phrɯ́tsacìkaa-yon
* Thanwaa-khom

Thai lunisolar calendars:
-------------------------
* Deuan hâa
* Deuan hòk
* Deuan jèt
* Deuan bpàaet
* Deuan gâo
* Deuan sip
* Deuan sip nùeng
* Deuan sip sǎawng
* Deuan aai
* Deuan yi
* Deuan sǎam
* Deuan sì

Thai months are a bit weird. Deuan aai means "Month the first", but the year doesn't increment until Songkran, or solar new year, which falls several months afterward. The lunar month containing solar year year is called Deuan hâa in Laos and Central Thailand, Deuan hòk in Keng Tung, and Deuan jèt in Chiang Mai; note that these are the same month and all correspond to the Indian Chaitra, it's just that the month called "Month 5" in Central Thailand is called "Month 6" in Keng Tung and "Month 7" in Chiang Mai.

The leap month always follows the 5th month of lunar year; it is formed by appending " song khan" to the end. Thus, it is called Deuan bpàaet song khan in Central Thailand and Laos, Deuan gào song khan in Keng Tung, and Deuan sip song khan in Chiang Mai.

To specify that a date comes on or after lunar new year but before solar new year, add an '*' to the year to specify that the year number has yet to increment.

Cambodian months:
-----------------
* Chaet
* Vesak
* Jais
* Ashad (technically not in leap years)
* Bhadamasad (replaces Ashad in leap years)
* Thutiyasad (leap month)
* Srap
* Phutrobot
* Asuj
* Kadhek
* Mekasay
* Bos
* Meak
* Phagaun

Balinese calendars:
-------------------
* Mangsa Kasadasa
* Mangsa Desta
* Mangsa Saddha
* Mangsa Kasa
* Mangsa Karo
* Mangsa Katelu
* Mangsa Kapat
* Mangsa Kalima
* Mangsa Kanem
* Mangsa Kapitu
* Mangsa Kawolu
* Mangsa Kasanga

In the case of leap years, add a " 2" to the end of the repeated month.

Javanese calendars:
-------------------
* Sura
* Sapar
* Mulud
* Bakda Mulud
* Jumadil Awal
* Jumadil Akhir
* Rejeb
* Ruwah
* Pasa
* Sawa
* Dulkangidah
* Besar

In the Jabvali calendar, add a "Leap " before a month name to specify the leap month.

Hawai'ian calendars:
--------------------
* Welehu
* Makaliʻi
* Kāʻelo
* Kaulua
* Nana
* Welo
* Ikiiki
* Kaʻaona
* Hinaiaʻeleʻele
* Māhoe Mua
* Māhoe Hope
* ʻIkuā
* Malama Pili (leap years only)
* Extra days (solar calendar only)

Kaua'i:
-------
* Hilinamā
* Hilinehu
* Hilioholo
* Hilionalu
* Hukipau
* ʻIkuā
* Welehu
* Kāʻelo
* Ikiiki
* Hinaiaʻeleʻele
* Māhoe Mua
* Māhoe Hope
* Malama Pili (leap years only)

Tūhoe and Te Tai Tokenau Māori:
-------------------------------
* Pipiri
* Hōngongoi
* Here-turi-kōkā
* Mahuru
* Whiringa-ā-nuku
* Whiringa-ā-rangi
* Hakihea
* Kohitātea
* Hui-tanguru
* Poutū-te-rangi
* Paenga-whāwhā
* Haratua
* Te Tahi o Pipiri

Ngāti Awa Māori:
----------------
* Te Tahi o Pipiri
* Te Rua o Takurua
* Te Toru o Here-turi-koka
* Te Wha o Mahuru
* Te Rima o Kopu
* Whitianaunau
* Hakihea
* Kai-tatea
* Ruhi-te-rangi
* Poutu-te-rangi
* Paenga-whawha
* Haki-haratua
* Matahi o Mahurikuri (leap years only)

Kahununu Māori:
---------------
* Aonui
* Te Aho-turuturu
* Te Ihomatua
* Tapere-wai
* Tatau-urutahi
* Tatau-uruora
* Akāka-nui
* Akuahu-mataora
* Te Ihonui
* Putoki-nui-o-tau
* Tikaka-muturangi
* Uruwhenhua
* Te Tahi o Aonui (leap years only)

South Island Māori:
-------------------
* Matahi o Pouaka
* Maruaroa
* Te Toru
* Te Wha
* Te Rima
* Te Ono
* Te Whitu
* Te Waru
* Te Iwa
* Te Ngahuru
* Ngahuru-nui
* Matahi o te tau
* Matahi o Mahurihuri (leap years only)

Moriori:
--------
* Kahu
* Rongo
* Tahei
* Keitanga
* Tauaropoti
* Wareahe
* Tchuhe a Takarore
* Wairehu
* Moro
* Mihi-torekau
* Ta Upoko o T'etchiao
* Tumatehea
* Leap month

Tahitian:
---------
* Te-tai
* Avarehu
* Fā‘ahu
* Pipiri
* Tāoa
* Aununu
* Apa‘apa
* Paroro mua
* Paroro mui
* Muriaha
* Hiaia
* Tema
* Te-eri

Yerm128
-------
* Chang'e
* S^n
* Tecciztecatl
* Hina
* Chía
* Quilla
* Khonsu
* Gleti
* Küyen
* Mayari
* Dalnim
* Anumati

LICENSE
=======

calconv is copyright Chris McCrohan.

calconv is licensed under the GNU General Public License version 3.0 or, at your option, any later version. Full details are contained in the LICENSE file. In short, you are free to alter, copy, and redistribute this software (and even charge a fee for it) as you please, and anybody who received a copy from you has the same rights.

FUTURE GOALS
============

Replace the text boxes for months with dropdown menus.

Add the following calendars:

* Shire Reckoning
* Discordian
* Julian Period
* Muisca
* Mandean (Reingold and Dershowitz, p 129)
* Pawukon
* Akan