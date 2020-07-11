#!/usr/bin/python

from tkinter import *
from decimal import *

import julian
import gregorian
import coptic
import ethiopian
import egyptian
import armenian
import lunar_hijri
import solar_hijri
import birashk
import assyrian
import babylonian
import hebrew
import samaritan
import kurdish
import amazigh
import rumi_n
import rev_gregorian
import parker
import goucher
import serbian_church
import rev_julian
import world
import ifc
import gorman
import pax
import pax2

import months

class Application(Frame):
    """A GUI application with various widgets"""

    def __init__(self, master):
        """Initialise the Frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def cons_day_julian_tojd(self):
        """Take the input into the Julian Day box andtojd it into the other date formats"""
        day = Decimal(self.cons_day_julian_ent.get())
    
        # Convert a Julian Day to a date in the Julian Calendar
        julian_date = julian.fromjd(day)
        julian_day_value = julian_date[0]
        julian_month_value = julian_date[1]
        julian_year_value = julian_date[2]
        self.julian_day_ent.delete(0, END)
        self.julian_month_ent.delete(0, END)
        self.julian_year_ent.delete(0, END)
        self.julian_day_ent.insert(0, julian_day_value)
        self.julian_month_ent.insert(0, julian_month_value)
        self.julian_year_ent.insert(0, julian_year_value)

        # Convert a Julian Day to a date in the Gregorian Calendar
        gregorian_date = gregorian.fromjd(day)
        gregorian_day_value = gregorian_date[0]
        gregorian_month_value = gregorian_date[1]
        gregorian_year_value = gregorian_date[2]
        self.gregorian_day_ent.delete(0, END)
        self.gregorian_month_ent.delete(0, END)
        self.gregorian_year_ent.delete(0, END)
        self.gregorian_day_ent.insert(0, gregorian_day_value)
        self.gregorian_month_ent.insert(0, gregorian_month_value)
        self.gregorian_year_ent.insert(0, gregorian_year_value)

        # Convert a Julian Day to a date in the Coptic Calendar
        coptic_date = coptic.fromjd(day)
        coptic_day_value = coptic_date[0]
        coptic_month_value = coptic_date[1]
        coptic_year_value = coptic_date[2]
        self.coptic_day_ent.delete(0, END)
        self.coptic_month_ent.delete(0, END)
        self.coptic_year_ent.delete(0, END)
        self.coptic_day_ent.insert(0, coptic_day_value)
        self.coptic_month_ent.insert(0, coptic_month_value)
        self.coptic_year_ent.insert(0, coptic_year_value)

        # Convert a Julian Day to a date in the Ethiopian Calendar
        ethiopian_date = ethiopian.fromjd(day)
        ethiopian_day_value = ethiopian_date[0]
        ethiopian_month_value = ethiopian_date[1]
        ethiopian_year_value = ethiopian_date[2]
        self.ethiopian_day_ent.delete(0, END)
        self.ethiopian_month_ent.delete(0, END)
        self.ethiopian_year_ent.delete(0, END)
        self.ethiopian_day_ent.insert(0, ethiopian_day_value)
        self.ethiopian_month_ent.insert(0, ethiopian_month_value)
        self.ethiopian_year_ent.insert(0, ethiopian_year_value)

        # Convert a Julian Day to a date in the Egyptian Calendar
        egyptian_date = egyptian.fromjd(day)
        egyptian_day_value = egyptian_date[0]
        egyptian_month_value = egyptian_date[1]
        egyptian_year_value = egyptian_date[2]
        self.egyptian_day_ent.delete(0, END)
        self.egyptian_month_ent.delete(0, END)
        self.egyptian_year_ent.delete(0, END)
        self.egyptian_day_ent.insert(0, egyptian_day_value)
        self.egyptian_month_ent.insert(0, egyptian_month_value)
        self.egyptian_year_ent.insert(0, egyptian_year_value)

        # Convert a Julian Day to a date in the Armenian Calendar
        armenian_date = armenian.fromjd(day)
        armenian_day_value = armenian_date[0]
        armenian_month_value = armenian_date[1]
        armenian_year_value = armenian_date[2]
        self.armenian_day_ent.delete(0, END)
        self.armenian_month_ent.delete(0, END)
        self.armenian_year_ent.delete(0, END)
        self.armenian_day_ent.insert(0, armenian_day_value)
        self.armenian_month_ent.insert(0, armenian_month_value)
        self.armenian_year_ent.insert(0, armenian_year_value)

        # Convert a Julian Day to a date in the Lunar Hijri Calendar
        lunar_hijri_date = lunar_hijri.fromjd(day)
        lunar_hijri_day_value = lunar_hijri_date[0]
        lunar_hijri_month_value = lunar_hijri_date[1]
        lunar_hijri_year_value = lunar_hijri_date[2]
        self.lunar_hijri_day_ent.delete(0, END)
        self.lunar_hijri_month_ent.delete(0, END)
        self.lunar_hijri_year_ent.delete(0, END)
        self.lunar_hijri_day_ent.insert(0, lunar_hijri_day_value)
        self.lunar_hijri_month_ent.insert(0, lunar_hijri_month_value)
        self.lunar_hijri_year_ent.insert(0, lunar_hijri_year_value)

        # Convert a Julian Day to a date in the Solar Hijri calendar
        solar_hijri_date = solar_hijri.fromjd(day)
        solar_hijri_day_value = solar_hijri_date[0]
        solar_hijri_month_value = solar_hijri_date[1]
        solar_hijri_year_value = solar_hijri_date[2]
        self.solar_hijri_day_ent.delete(0, END)
        self.solar_hijri_month_ent.delete(0, END)
        self.solar_hijri_year_ent.delete(0, END)
        self.solar_hijri_day_ent.insert(0, solar_hijri_day_value)
        self.solar_hijri_month_ent.insert(0, solar_hijri_month_value)
        self.solar_hijri_year_ent.insert(0, solar_hijri_year_value)

        # Convert a Julian Day to a date in Birashk's calendar
        birashk_date = birashk.fromjd(day)
        birashk_day_value = birashk_date[0]
        birashk_month_value = birashk_date[1]
        birashk_year_value = birashk_date[2]
        self.birashk_day_ent.delete(0, END)
        self.birashk_month_ent.delete(0, END)
        self.birashk_year_ent.delete(0, END)
        self.birashk_day_ent.insert(0, birashk_day_value)
        self.birashk_month_ent.insert(0, birashk_month_value)
        self.birashk_year_ent.insert(0, birashk_year_value)

        # Convert a Julian Day to a date in the Assyrian calendar
        assyrian_date = assyrian.fromjd(day)
        assyrian_day_value = assyrian_date[0]
        assyrian_month_value = assyrian_date[1]
        assyrian_year_value = assyrian_date[2]
        self.assyrian_day_ent.delete(0, END)
        self.assyrian_month_ent.delete(0, END)
        self.assyrian_year_ent.delete(0, END)
        self.assyrian_day_ent.insert(0, assyrian_day_value)
        self.assyrian_month_ent.insert(0, assyrian_month_value)
        self.assyrian_year_ent.insert(0, assyrian_year_value)

        # Convert a Julian Day to a date in the Babylonian calendar
        babylonian_date = babylonian.fromjd(day)
        babylonian_day_value = babylonian_date[0]
        babylonian_month_value = babylonian_date[1]
        babylonian_year_value = babylonian_date[2]
        self.babylonian_day_ent.delete(0, END)
        self.babylonian_month_ent.delete(0, END)
        self.babylonian_year_ent.delete(0, END)
        self.babylonian_day_ent.insert(0, babylonian_day_value)
        self.babylonian_month_ent.insert(0, babylonian_month_value)
        self.babylonian_year_ent.insert(0, babylonian_year_value)

        # Convert a Julian Day to a date in the Hebrew calendar
        hebrew_date = hebrew.fromjd(day)
        hebrew_day_value = hebrew_date[0]
        hebrew_month_value = hebrew_date[1]
        hebrew_year_value = hebrew_date[2]
        self.hebrew_day_ent.delete(0, END)
        self.hebrew_month_ent.delete(0, END)
        self.hebrew_year_ent.delete(0, END)
        self.hebrew_day_ent.insert(0, hebrew_day_value)
        self.hebrew_month_ent.insert(0, hebrew_month_value)
        self.hebrew_year_ent.insert(0, hebrew_year_value)

        # Convert a Julian Day to a date in the Samaritan calendar
        samaritan_date = samaritan.fromjd(day)
        samaritan_day_value = samaritan_date[0]
        samaritan_month_value = samaritan_date[1]
        samaritan_year_value = samaritan_date[2]
        self.samaritan_day_ent.delete(0, END)
        self.samaritan_month_ent.delete(0, END)
        self.samaritan_year_ent.delete(0, END)
        self.samaritan_day_ent.insert(0, samaritan_day_value)
        self.samaritan_month_ent.insert(0, samaritan_month_value)
        self.samaritan_year_ent.insert(0, samaritan_year_value)

        # Convert a Julian Day to a date in the Kurdish calendar
        kurdish_date = kurdish.fromjd(day)
        kurdish_day_value = kurdish_date[0]
        kurdish_month_value = kurdish_date[1]
        kurdish_year_value = kurdish_date[2]
        self.kurdish_day_ent.delete(0,END)
        self.kurdish_month_ent.delete(0,END)
        self.kurdish_year_ent.delete(0,END)
        self.kurdish_day_ent.insert(0,kurdish_day_value)
        self.kurdish_month_ent.insert(0,kurdish_month_value)
        self.kurdish_year_ent.insert(0,kurdish_year_value)

        # True Julian Day
        tjday = int(day) + Decimal(0.5)
        self.day_julian_ent.delete(0,END)
        self.day_julian_ent.insert(0,tjday)

        # Reduced Julian Day
        rjday = int(day) + Decimal(0.5) - 2400000
        self.red_day_julian_ent.delete(0,END)
        self.red_day_julian_ent.insert(0,rjday)

        # Modified Julian Day
        mjday = int(day) - 2400000
        self.mod_day_julian_ent.delete(0,END)
        self.mod_day_julian_ent.insert(0,mjday)

        # Truncated Julian Day
        tjday = int(day) - 2440000
        self.trun_day_julian_ent.delete(0,END)
        self.trun_day_julian_ent.insert(0,tjday)

        # Dublin Julian Day
        djday = int(day) + Decimal(0.5) - 2415020
        self.dub_day_julian_ent.delete(0,END)
        self.dub_day_julian_ent.insert(0,djday)

        # CNES Julian Day
        cnes = int(day) - 2433282
        self.cnes_ent.delete(0,END)
        self.cnes_ent.insert(0,cnes)

        # CCSDS Julian Day
        ccsds = int(day) - 2436204
        self.ccsds_ent.delete(0,END)
        self.ccsds_ent.insert(0,ccsds)

        # Lilian Day
        lday = int(day) - 2299159
        self.day_lilian_ent.delete(0,END)
        self.day_lilian_ent.insert(0,lday)

        # Rata Die
        rday = int(day) - 1721424
        self.rata_die_ent.delete(0,END)
        self.rata_die_ent.insert(0,rday)

        # Unix time
        unix = (int(day) - 2440587) * 86400
        self.unix_time_ent.delete(0,END)
        self.unix_time_ent.insert(0,unix)

        # Julian Sol
        sol_gangale = round((int(day) - Decimal('2405520.5')) / Decimal(1.02749))
        self.sol_gangale_ent.delete(0,END)
        self.sol_gangale_ent.insert(0,sol_gangale)

        # LOP Julian day
        lop = int(day) - 2448622
        self.lop_ent.delete(0,END)
        self.lop_ent.insert(0,lop)

        # Convert a Julian day to a date in the Amazigh calendar
        amazigh_date = amazigh.fromjd(day)
        self.amazigh_day_ent.delete(0,END)
        self.amazigh_month_ent.delete(0,END)
        self.amazigh_year_ent.delete(0,END)
        self.amazigh_day_ent.insert(0, amazigh_date[0])
        self.amazigh_month_ent.insert(0, amazigh_date[1])
        self.amazigh_year_ent.insert(0, amazigh_date[2])

        # Convert a Julian day to a date in the Rumi calendar
        rumi_n_date = rumi_n.fromjd(day)
        self.rumi_n_day_ent.delete(0,END)
        self.rumi_n_month_ent.delete(0,END)
        self.rumi_n_year_ent.delete(0,END)
        self.rumi_n_day_ent.insert(0, rumi_n_date[0])
        self.rumi_n_month_ent.insert(0, rumi_n_date[1])
        self.rumi_n_year_ent.insert(0, rumi_n_date[2])

        # Convert a Julian day to a date in the revised Gregorian calendar
        rev_gregorian_date = rev_gregorian.fromjd(day)
        self.rev_gregorian_day_ent.delete(0, END)
        self.rev_gregorian_month_ent.delete(0, END)
        self.rev_gregorian_year_ent.delete(0, END)
        self.rev_gregorian_day_ent.insert(0, rev_gregorian_date[0])
        self.rev_gregorian_month_ent.insert(0, rev_gregorian_date[1])
        self.rev_gregorian_year_ent.insert(0, rev_gregorian_date[2])

        # Convert a Julian day to a date in the Parker calendar
        parker_date = parker.fromjd(day)
        self.parker_day_ent.delete(0, END)
        self.parker_month_ent.delete(0, END)
        self.parker_year_ent.delete(0, END)
        self.parker_day_ent.insert(0, parker_date[0])
        self.parker_month_ent.insert(0, parker_date[1])
        self.parker_year_ent.insert(0, parker_date[2])

        # Convert a Julian day to a date in the Goucher-Parker calendar
        goucher_date = goucher.fromjd(day)
        self.goucher_day_ent.delete(0, END)
        self.goucher_month_ent.delete(0, END)
        self.goucher_year_ent.delete(0, END)
        self.goucher_day_ent.insert(0, goucher_date[0])
        self.goucher_month_ent.insert(0, goucher_date[1])
        self.goucher_year_ent.insert(0, goucher_date[2])

        # Convert a Julian day to a date in the Serbian church calendar
        serbian_church_date = serbian_church.fromjd(day)
        self.serbian_church_day_ent.delete(0, END)
        self.serbian_church_month_ent.delete(0, END)
        self.serbian_church_year_ent.delete(0, END)
        self.serbian_church_day_ent.insert(0, serbian_church_date[0])
        self.serbian_church_month_ent.insert(0, serbian_church_date[1])
        self.serbian_church_year_ent.insert(0, serbian_church_date[2])

        # Convert a Julain day to a date in the revised Julian calendar
        rev_julian_date = rev_julian.fromjd(day)
        self.rev_julian_day_ent.delete(0, END)
        self.rev_julian_month_ent.delete(0, END)
        self.rev_julian_year_ent.delete(0, END)
        self.rev_julian_day_ent.insert(0, rev_julian_date[0])
        self.rev_julian_month_ent.insert(0, rev_julian_date[1])
        self.rev_julian_year_ent.insert(0, rev_julian_date[2])

        # Convert a Julian day to  a date in the World calendar
        world_date = world.fromjd(day)
        self.world_day_ent.delete(0, END)
        self.world_month_ent.delete(0, END)
        self.world_year_ent.delete(0, END)
        self.world_day_ent.insert(0, world_date[0])
        self.world_month_ent.insert(0, world_date[1])
        self.world_year_ent.insert(0, world_date[2])

        # Convert a Julian day to a date in the International Fixed calendar
        ifc_date = ifc.fromjd(day)
        self.ifc_day_ent.delete(0, END)
        self.ifc_month_ent.delete(0, END)
        self.ifc_year_ent.delete(0, END)
        self.ifc_day_ent.insert(0, ifc_date[0])
        self.ifc_month_ent.insert(0, ifc_date[1])
        self.ifc_year_ent.insert(0, ifc_date[2])

        # Convert a Julian day to a date in the Pax calendar
        pax_date = pax.fromjd(day)
        self.pax_day_ent.delete(0, END)
        self.pax_month_ent.delete(0, END)
        self.pax_year_ent.delete(0, END)
        self.pax_day_ent.insert(0, pax_date[0])
        self.pax_month_ent.insert(0, pax_date[1])
        self.pax_year_ent.insert(0, pax_date[2])

        # Convert a Julian day to a date in the Gorman calendar
        gorman_date = gorman.fromjd(day)
        self.gorman_day_ent.delete(0, END)
        self.gorman_month_ent.delete(0, END)
        self.gorman_year_ent.delete(0, END)
        self.gorman_day_ent.insert(0, gorman_date[0])
        self.gorman_month_ent.insert(0, gorman_date[1])
        self.gorman_year_ent.insert(0, gorman_date[2])

        # Convert a Julian day to a date in the Pax 2020 calendar
        pax2_date = pax2.fromjd(day)
        self.pax2_day_ent.delete(0, END)
        self.pax2_month_ent.delete(0, END)
        self.pax2_year_ent.delete(0, END)
        self.pax2_day_ent.insert(0, pax2_date[0])
        self.pax2_month_ent.insert(0, pax2_date[1])
        self.pax2_year_ent.insert(0, pax2_date[2])
        
        
    def cons_day_julian_plus(self):
        day = self.cons_day_julian_ent.get()
        day = int(day) + 1
        self.cons_day_julian_ent.delete(0, END)
        self.cons_day_julian_ent.insert(0, day)
        self.cons_day_julian_tojd()
        
    def cons_day_julian_minus(self):
        day = self.cons_day_julian_ent.get()
        day = int(day) - 1
        self.cons_day_julian_ent.delete(0, END)
        self.cons_day_julian_ent.insert(0, day)
        self.cons_day_julian_tojd()

    def julian_converter(self):
        """Convert a date in the Julian Calendar to a Julian Day."""
        day = self.julian_day_ent.get()
        month = self.julian_month_ent.get()
        year = self.julian_year_ent.get()
        jday = julian.tojd(day, month, year)
        self.cons_day_julian_ent.delete(0, END)
        self.cons_day_julian_ent.insert(0, jday)
        self.cons_day_julian_tojd()
        
    def gregorian_converter(self):
        """Convert a date in the Gregorian Calendar to a Julian  Day."""
        day = self.gregorian_day_ent.get()
        month = self.gregorian_month_ent.get()
        year = self.gregorian_year_ent.get()
        jday = gregorian.tojd(day, month, year)
        self.cons_day_julian_ent.delete(0, END)
        self.cons_day_julian_ent.insert(0, jday)
        self.cons_day_julian_tojd()
        
    def coptic_converter(self):
        """Convert a date in the Coptic Calendar to a Julian Day."""
        day = self.coptic_day_ent.get()
        month = self.coptic_month_ent.get()
        year = self.coptic_year_ent.get()
        jday = coptic.tojd(day, month, year)
        self.cons_day_julian_ent.delete(0, END)
        self.cons_day_julian_ent.insert(0, jday)
        self.cons_day_julian_tojd()
        
    def ethiopian_converter(self):
        """Convert a date in the Ethiopian Calendar to a Julian day."""
        day = self.ethiopian_day_ent.get()
        month = self.ethiopian_month_ent.get()
        year = self.ethiopian_year_ent.get()
        jday = ethiopian.tojd(day,month,year)
        self.cons_day_julian_ent.delete(0, END)
        self.cons_day_julian_ent.insert(0, jday)
        self.cons_day_julian_tojd()
        
    def egyptian_converter(self):
        """Convert a date in the Egyptian Calendar to a Julian Day."""
        day = self.egyptian_day_ent.get()
        month = self.egyptian_month_ent.get()
        year = self.egyptian_year_ent.get()
        jday = egyptian.tojd(day, month, year)
        self.cons_day_julian_ent.delete(0, END)
        self.cons_day_julian_ent.insert(0, jday)
        self.cons_day_julian_tojd()
        
    def armenian_converter(self):
        """Convert a date in the Armenian Calendar to a Julian Day."""
        day = self.armenian_day_ent.get()
        month = self.armenian_month_ent.get()
        year = self.armenian_year_ent.get()
        jday = armenian.tojd(day, month, year)
        self.cons_day_julian_ent.delete(0, END)
        self.cons_day_julian_ent.insert(0, jday)
        self.cons_day_julian_tojd()
        
    def lunar_hijri_converter(self):
        """Convert a date in the Lunar Hijri Calendar to a Julian DAy."""
        day = self.lunar_hijri_day_ent.get()
        month = self.lunar_hijri_month_ent.get()
        year = self.lunar_hijri_year_ent.get()
        jday = lunar_hijri.tojd(day, month, year)
        self.cons_day_julian_ent.delete(0, END)
        self.cons_day_julian_ent.insert(0, jday)
        self.cons_day_julian_tojd()
        
    def solar_hijri_converter(self):
        """Convert a date in the Solar Hijri Calendar to a Julian Day."""
        day = self.solar_hijri_day_ent.get()
        month = self.solar_hijri_month_ent.get()
        year = self.solar_hijri_year_ent.get()
        jday = solar_hijri.tojd(day, month, year)
        self.cons_day_julian_ent.delete(0, END)
        self.cons_day_julian_ent.insert(0, jday)
        self.cons_day_julian_tojd()
        
    def birashk_converter(self):
        """Convert a date in Birashk's calendar to a Julian Day."""
        day = self.birashk_day_ent.get()
        month = self.birashk_month_ent.get()
        year = self.birashk_year_ent.get()
        jday = birashk.tojd(day, month, year)
        self.cons_day_julian_ent.delete(0, END)
        self.cons_day_julian_ent.insert(0, jday)
        self.cons_day_julian_tojd()
        
    def assyrian_converter(self):
        """Convert a date in the Assyrian calendar to a Julian Day."""
        day = self.assyrian_day_ent.get()
        month = self.assyrian_month_ent.get()
        year = self.assyrian_year_ent.get()
        jday = assyrian.tojd(day, month, year)
        self.cons_day_julian_ent.delete(0, END)
        self.cons_day_julian_ent.insert(0, jday)
        self.cons_day_julian_tojd()
        
    def babylonian_converter(self):
        """Convert a date in the Babylonian calendar to a Julian Day."""
        day = self.babylonian_day_ent.get()
        month = self.babylonian_month_ent.get()
        year = self.babylonian_year_ent.get()
        jday = babylonian.tojd(day, month, year)
        self.cons_day_julian_ent.delete(0, END)
        self.cons_day_julian_ent.insert(0, jday)
        self.cons_day_julian_tojd()
        
    def hebrew_converter(self):
        """Convert a date in the Hebrew calendar to a Julian Day."""
        day = self.hebrew_day_ent.get()
        month = self.hebrew_month_ent.get()
        year = self.hebrew_year_ent.get()
        jday = hebrew.tojd(day, month, year)
        self.cons_day_julian_ent.delete(0, END)
        self.cons_day_julian_ent.insert(0, jday)
        self.cons_day_julian_tojd()
        
    def samaritan_converter(self):
        """Convert a date in the Samaritan Hebrew calendar to a Julian Day"""
        day = self.samaritan_day_ent.get()
        month = self.samaritan_month_ent.get()
        year = self.samaritan_year_ent.get()
        jday = samaritan.tojd(day,month,year)
        self.cons_day_julian_ent.delete(0, END)
        self.cons_day_julian_ent.insert(0, jday)
        self.cons_day_julian_tojd()
        
    def kurdish_converter(self):
        """Convert a date in the Kurdish calendar to a Julian Day."""
        day = self.kurdish_day_ent.get()
        month = self.kurdish_month_ent.get()
        year = self.kurdish_year_ent.get()
        jday = kurdish.tojd(day,month,year)
        self.cons_day_julian_ent.delete(0,END)
        self.cons_day_julian_ent.insert(0,jday)
        self.cons_day_julian_tojd()
        
    def true_day_julian_converter(self):
        """Convert a Julian Day to a True Julian Day."""
        jday = Decimal(self.day_julian_ent.get()) + Decimal('0.5')
        self.cons_day_julian_ent.delete(0,END)
        self.cons_day_julian_ent.insert(0,jday)
        self.cons_day_julian_tojd()
        
    def red_day_julian_converter(self):
        """Convert a Reduced Julian Day to a Consecutive Julian Day."""
        jday = Decimal(self.red_day_julian_ent.get()) + 2400000 - Decimal('0.5')
        self.cons_day_julian_ent.delete(0,END)
        self.cons_day_julian_ent.insert(0,jday)
        self.cons_day_julian_tojd()
        
    def mod_day_julian_converter(self):
        """Convert a Modified Julian Day to a Consecutive Julian Day."""
        jday = int(self.mod_day_julian_ent.get()) + 2400000
        self.cons_day_julian_ent.delete(0,END)
        self.cons_day_julian_ent.insert(0,jday)
        self.cons_day_julian_tojd()
        
    def trun_day_julian_converter(self):
        """Convert a Truncated Julian Day to a Consecutive Julian Day."""
        jday = int(self.trun_day_julian_ent.get()) + 2440000
        self.cons_day_julian_ent.delete(0,END)
        self.cons_day_julian_ent.insert(0,jday)
        self.cons_day_julian_tojd()
        
    def dub_day_julian_converter(self):
        """Convert a Dublin Julian Day to a Consecutive Julian DAy."""
        jday = Decimal(self.dub_day_julian_ent.get()) + 2415020 - Decimal('0.5')
        self.cons_day_julian_ent.delete(0,END)
        self.cons_day_julian_ent.insert(0,jday)
        self.cons_day_julian_tojd()
        
    def cnes_converter(self):
        """Convert a CNES Julian Day into a Consecutive Julian Day."""
        jday = int(self.cnes_ent.get())+ 2433282
        self.cons_day_julian_ent.delete(0,END)
        self.cons_day_julian_ent.insert(0,jday)
        self.cons_day_julian_tojd()
        
    def ccsds_converter(self):
        jday = int(self.ccsds_ent.get()) + 2436204
        self.cons_day_julian_ent.delete(0,END)
        self.cons_day_julian_ent.insert(0,jday)
        self.cons_day_julian_tojd()
        
    def day_lilian_converter(self):
        jday = int(self.day_lilian_ent.get()) + 2299159
        self.cons_day_julian_ent.delete(0,END)
        self.cons_day_julian_ent.insert(0,jday)
        self.cons_day_julian_tojd()
        
    def rata_die_converter(self):
        jday = int(self.rata_die_ent.get()) + 1721424
        self.cons_day_julian_ent.delete(0,END)
        self.cons_day_julian_ent.insert(0,jday)
        self.cons_day_julian_tojd()
        
    def unix_time_converter(self):
        jday = (int(self.unix_time_ent.get()) // 86400) + 2440587
        self.cons_day_julian_ent.delete(0,END)
        self.cons_day_julian_ent.insert(0,jday)
        self.cons_day_julian_tojd()
        
    def sol_gangale_converter(self):
        jday = round(Decimal(self.sol_gangale_ent.get()) * Decimal('1.02749')) + 2405521
        self.cons_day_julian_ent.delete(0,END)
        self.cons_day_julian_ent.insert(0,jday)
        self.cons_day_julian_tojd()
        
    def lop_converter(self):
        jday = int(self.lop_ent.get()) + 2448622
        self.cons_day_julian_ent.delete(0,END)
        self.cons_day_julian_ent.insert(0,jday)
        self.cons_day_julian_tojd()
        
    def amazigh_converter(self):
        """Convert a date in the Amazigh calendar to a Julian day."""
        day = int(self.amazigh_day_ent.get())
        month = self.amazigh_month_ent.get()
        year = int(self.amazigh_year_ent.get())
        jday = amazigh.tojd(day,month,year)
        self.cons_day_julian_ent.delete(0,END)
        self.cons_day_julian_ent.insert(0,jday)
        self.cons_day_julian_tojd()
        
    def rumi_n_converter(self):
        """Convert a date in the Rumi calendar to a Julian day."""
        day = int(self.rumi_n_day_ent.get())
        month = self.rumi_n_month_ent.get()
        year = int(self.rumi_n_year_ent.get())
        jday = rumi_n.tojd(day, month, year)
        self.cons_day_julian_ent.delete(0,END)
        self.cons_day_julian_ent.insert(0, jday)
        self.cons_day_julian_tojd()
        
    def rev_gregorian_converter(self):
        """Convert a date in the revised Gregorian calendar to a Julian day."""
        day = int(self.rev_gregorian_day_ent.get())
        month = self.rev_gregorian_month_ent.get()
        year = int(self.rev_gregorian_year_ent.get())
        jday = rev_gregorian.tojd(day, month, year)
        self.cons_day_julian_ent.delete(0, END)
        self.cons_day_julian_ent.insert(0, jday)
        self.cons_day_julian_tojd()
        
    def parker_converter(self):
        """Convert a date in the Parker calendar to a Julian day."""
        day = int(self.parker_day_ent.get())
        month = self.parker_month_ent.get()
        year = int(self.parker_year_ent.get())
        jday = parker.tojd(day, month, year)
        self.cons_day_julian_ent.delete(0, END)
        self.cons_day_julian_ent.insert(0, jday)
        self.cons_day_julian_tojd()
        
    def goucher_converter(self):
        """Convert a date in the Goucher calendar to a Julian day."""
        day = int(self.goucher_day_ent.get())
        month = self.goucher_month_ent.get()
        year = int(self.goucher_year_ent.get())
        jday = goucher.tojd(day, month, year)
        self.cons_day_julian_ent.delete(0, END)
        self.cons_day_julian_ent.insert(0, jday)
        self.cons_day_julian_tojd()
        
    def serbian_church_converter(self):
        day = int(self.serbian_church_day_ent.get())
        month = self.serbian_church_month_ent.get()
        year = int(self.serbian_church_year_ent.get())
        jday = serbian_church.tojd(day, month, year)
        self.cons_day_julian_ent.delete(0, END)
        self.cons_day_julian_ent.insert(0, jday)
        self.cons_day_julian_tojd()
        
    def rev_julian_converter(self):
        day = int(self.rev_julian_day_ent.get())
        month = self.rev_julian_month_ent.get()
        year = int(self.rev_julian_year_ent.get())
        jday = rev_julian.tojd(day, month, year)
        self.cons_day_julian_ent.delete(0, END)
        self.cons_day_julian_ent.insert(0, jday)
        self.cons_day_julian_tojd()

    def world_converter(self):
        day = int(self.world_day_ent.get())
        month = self.world_month_ent.get()
        year = int(self.world_year_ent.get())
        jday = world.tojd(day, month, year)
        self.cons_day_julian_ent.delete(0, END)
        self.cons_day_julian_ent.insert(0, jday)
        self.cons_day_julian_tojd()

    def ifc_converter(self):
        day = int(self.ifc_day_ent.get())
        month = self.ifc_month_ent.get()
        year = int(self.ifc_year_ent.get())
        jday = ifc.tojd(day, month, year)
        self.cons_day_julian_ent.delete(0, END)
        self.cons_day_julian_ent.insert(0, jday)
        self.cons_day_julian_tojd()

    def pax_converter(self):
        day = int(self.pax_day_ent.get())
        month = self.pax_month_ent.get()
        year = int(self.pax_year_ent.get())
        jday = pax.tojd(day, month, year)
        self.cons_day_julian_ent.delete(0, END)
        self.cons_day_julian_ent.insert(0, jday)
        self.cons_day_julian_tojd()

    def gorman_converter(self):
        day = int(self.gorman_day_ent.get())
        month = self.gorman_month_ent.get()
        year = int(self.gorman_year_ent.get())
        jday = gorman.tojd(day, month, year)
        self.cons_day_julian_ent.delete(0, END)
        self.cons_day_julian_ent.insert(0, jday)
        self.cons_day_julian_tojd()

    def pax2_converter(self):
        day = int(self.pax2_day_ent.get())
        month = self.pax2_month_ent.get()
        year = int(self.pax2_year_ent.get())
        jday = pax2.tojd(day, month, year)
        self.cons_day_julian_ent.delete(0, END)
        self.cons_day_julian_ent.insert(0, jday)
        self.cons_day_julian_tojd()

        
    def create_widgets(self):
        """Generate various widgets."""
        # For now, months will just have to be typed manually until I can figure out how to use dropdown menus.
        
        # Julian Day
        self.cons_day_julian_lbl = Label(self, text = "Chronological Julian Day").grid(row = 0, column = 0, columnspan = 3, sticky = W)
        self.cons_day_julian_desc_lbl = Label(self, text = "Day").grid (row = 1, column = 0, columnspan = 3, sticky = W)
        self.cons_day_julian_ent = Entry(self)
        self.cons_day_julian_ent.grid(row = 2, column = 0, sticky = W)
        self.cons_day_julian_bttn = Button(self, text = "Calculate", command = self.cons_day_julian_tojd)
        self.cons_day_julian_bttn.grid(row = 3, column = 0, columnspan = 3, sticky = W)

        # Plus and Minus buttons
        self.cons_day_julian_plus_bttn = Button(self, text = "+", command = self.cons_day_julian_plus)
        self.cons_day_julian_plus_bttn.grid(row = 2, column = 1, sticky = W)
        self.cons_day_julian_minus_bttn = Button(self, text = "-", command = self.cons_day_julian_minus)
        self.cons_day_julian_minus_bttn.grid(row = 3, column = 1, sticky = W)

        # Julian Calendar
        self.julian_lbl = Label(self, text = "Julian Calendar").grid(row = 0, column = 3, columnspan = 3, sticky = W)
        self.julian_day_lbl = Label(self, text = "Day").grid(row = 1, column = 3, columnspan = 3, sticky = W)
        self.julian_day_ent = Entry(self)
        self.julian_day_ent.grid(row = 2, column = 3, sticky = W)
        self.julian_month_lbl = Label(self, text = "Month").grid(row = 1, column = 4, sticky = W)
        self.julian_month_ent = Entry(self)
        self.julian_month_ent.grid(row = 2, column = 4, sticky = W)
        self.julian_year_lbl = Label(self, text = "Year").grid(row = 1, column = 5, sticky = W)
        self.julian_year_ent = Entry(self)
        self.julian_year_ent.grid(row = 2, column = 5, sticky = W)
        self.julian_bttn = Button(self, text = "Calculate", command = self.julian_converter)
        self.julian_bttn.grid(row = 3, column = 3, columnspan = 3, sticky = W)

        # Gregorian Calendar
        self.gregorian_lbl = Label(self, text = "Gregorian Calendar").grid(row = 0, column = 6, columnspan = 3, sticky = W)
        self.gregorian_day_lbl = Label(self, text = "Day").grid(row = 1, column = 6, sticky = W)
        self.gregorian_day_ent = Entry(self)
        self.gregorian_day_ent.grid(row = 2, column = 6, sticky = W)
        self.gregroian_month_lbl = Label(self, text = "Month").grid(row = 1, column = 7, sticky = W)
        self.gregorian_month_ent = Entry(self)
        self.gregorian_month_ent.grid(row = 2, column = 7, sticky = W)
        self.gregorian_year_lbl = Label(self, text = "Year").grid(row = 1, column = 8, sticky = W)
        self.gregorian_year_ent = Entry(self)
        self.gregorian_year_ent.grid(row = 2, column = 8, sticky = W)
        self.gregorian_bttn = Button(self, text = "Calculate", command = self.gregorian_converter)
        self.gregorian_bttn.grid(row = 3, column = 6, columnspan = 3, sticky = W)

        # Coptic Calendar
        self.coptic_lbl = Label(self, text = "Coptic Calendar").grid(row = 0, column = 9, columnspan = 3, sticky = W)
        self.coptic_day_lbl = Label(self, text = "Day").grid(row = 1, column = 9, sticky = W)
        self.coptic_day_ent = Entry(self)
        self.coptic_day_ent.grid(row = 2, column = 9, sticky = W)
        self.coptic_month_lbl = Label(self, text = "Month").grid(row = 1, column = 10, sticky = W)
        self.coptic_month_ent = Entry(self)
        self.coptic_month_ent.grid(row = 2, column = 10, sticky = W)
        self.coptic_year_lbl = Label(self, text = "Year").grid(row = 1, column = 11, sticky = W)
        self.coptic_year_ent = Entry(self)
        self.coptic_year_ent.grid(row = 2, column = 11, sticky = W)
        self.coptic_bttn = Button(self, text = "Calculate", command = self.coptic_converter).grid(row = 3, column = 9, columnspan = 3, sticky = W)

        # Ethiopian Calendar
        self.ethiopian_lbl = Label(self, text = "Ethiopian Calendar").grid(row = 0, column = 12, columnspan = 3, sticky = W)
        self.ethiopian_day_lbl = Label(self, text = "Day").grid(row = 1, column = 12, sticky = W)
        self.ethiopian_day_ent = Entry(self)
        self.ethiopian_day_ent.grid(row = 2, column = 12, sticky = W)
        self.ethiopian_month_lbl = Label(self, text = "Month").grid(row = 1, column = 13, sticky = W)
        self.ethiopian_month_ent = Entry(self)
        self.ethiopian_month_ent.grid(row = 2, column = 13, sticky = W)
        self.ethiopian_year_lbl = Label(self, text = "Year").grid(row = 1, column = 11, sticky = W)
        self.ethiopian_year_ent = Entry(self)
        self.ethiopian_year_ent.grid(row = 2, column = 14, sticky = W)
        self.ethiopian_bttn = Button(self, text = "Calculate", command = self.ethiopian_converter).grid(row = 3, column = 12, columnspan = 3, sticky = W)

        # Egyptian Calendar
        self.egyptian_lbl = Label(self, text = "Egyptian Calendar").grid(row = 5, column = 0, columnspan = 3, sticky = W)
        self.egyptian_day_lbl = Label(self, text = "Day").grid(row = 6, column = 0, sticky = W)
        self.egyptian_day_ent = Entry(self)
        self.egyptian_day_ent.grid(row = 7, column = 0, sticky = W)
        self.egyptian_month_lbl = Label(self, text = "Month").grid(row = 6, column = 1, sticky = W)
        self.egyptian_month_ent = Entry(self)
        self.egyptian_month_ent.grid(row = 7, column = 1, sticky = W)
        self.egyptian_year_lbl = Label(self, text = "Year").grid(row = 6, column = 2, sticky = W)
        self.egyptian_year_ent = Entry(self)
        self.egyptian_year_ent.grid(row = 7, column = 2, sticky = W)
        self.egyptian_bttn = Button(self, text = "Calculate", command = self.egyptian_converter).grid(row = 8, column = 0, columnspan = 3, sticky = W)

        # Armenian Calendar
        self.armenian_lbl = Label(self, text = "Armenian Calendar").grid(row = 5, column = 3, columnspan = 3, sticky = W)
        self.armenian_day_lbl = Label(self, text = "Day").grid(row = 6, column = 3, sticky = W)
        self.armenian_day_ent = Entry(self)
        self.armenian_day_ent.grid(row = 7, column = 3, sticky = W)
        self.armenian_month_lbl = Label(self, text = "Month").grid(row = 6, column = 4, sticky = W)
        self.armenian_month_ent = Entry(self)
        self.armenian_month_ent.grid(row = 7, column = 4, sticky = W)
        self.armenian_year_lbl = Label(self, text = "Year").grid(row = 6, column = 5, sticky = W)
        self.armenian_year_ent = Entry(self)
        self.armenian_year_ent.grid(row = 7, column = 5, sticky = W)
        self.armenian_bttn = Button(self, text = "Calculate", command = self.armenian_converter).grid(row = 8, column = 3, columnspan = 3, sticky = W)

        # Lunar Hijri Calendar
        self.lunar_hijri_lbl = Label(self, text = "Lunar Hijri (Islamic) Calendar").grid(row = 5, column = 6, columnspan = 3, sticky = W)
        self.lunar_hijri_day_lbl = Label(self, text = "Day").grid(row = 6, column = 6, sticky = W)
        self.lunar_hijri_day_ent = Entry(self)
        self.lunar_hijri_day_ent.grid(row = 7, column = 6, sticky = W)
        self.lunar_hijri_month_lbl = Label(self, text = "Month").grid(row = 6, column = 7, sticky = W)
        self.lunar_hijri_month_ent = Entry(self)
        self.lunar_hijri_month_ent.grid(row = 7, column = 7, sticky = W)
        self.lunar_hijri_year_lbl = Label(self, text = "Year").grid(row = 6, column = 8, sticky = W)
        self.lunar_hijri_year_ent = Entry(self)
        self.lunar_hijri_year_ent.grid(row = 7, column = 8, sticky = W)
        self.lunar_hijri_bttn = Button(self, text = "Calculate", command = self.lunar_hijri_converter).grid(row = 8, column = 6, columnspan = 3, sticky = W)

        # Solar Hijir Calendar
        self.solar_hijri_lbl = Label(self, text = "Solar Hijri Calendar").grid(row = 5, column = 9, columnspan = 3, sticky = W)
        self.solar_hijri_day_lbl = Label(self, text = "Day").grid(row = 6, column = 9, sticky = W)
        self.solar_hijri_day_ent = Entry(self)
        self.solar_hijri_day_ent.grid(row = 7, column = 9, sticky = W)
        self.solar_hijri_month_lbl = Label(self, text = "Month").grid(row = 6, column = 10, sticky = W)
        self.solar_hijri_month_ent = Entry(self)
        self.solar_hijri_month_ent.grid(row = 7, column = 10, sticky = W)
        self.solar_hijri_year_lbl = Label(self, text = "Year").grid(row = 6, column = 11, sticky = W)
        self.solar_hijri_year_ent = Entry(self)
        self.solar_hijri_year_ent.grid(row = 7, column = 11, sticky = W)
        self.solar_hijri_bttn = Button(self, text = "Calculate", command = self.solar_hijri_converter).grid(row = 8, column = 9, columnspan = 3, sticky = W)

        # Birashk's calendar
        self.birashk_lbl = Label(self, text = "Ahmad Birashk's Calendar").grid(row = 5, column = 12, columnspan = 3, sticky = W)
        self.birashk_day_lbl = Label(self, text = "Day").grid(row = 6, column = 12, sticky = W)
        self.birashk_day_ent = Entry(self)
        self.birashk_day_ent.grid(row = 7, column = 12, sticky = W)
        self.birashk_month_lbl = Label(self, text = "Month").grid(row = 6, column = 13, sticky = W)
        self.birashk_month_ent = Entry(self)
        self.birashk_month_ent.grid(row = 7, column = 13, sticky = W)
        self.birashk_year_lbl = Label(self, text = "Year").grid(row = 6, column = 14, sticky = W)
        self.birashk_year_ent = Entry(self)
        self.birashk_year_ent.grid(row = 7, column = 14, sticky = W)
        self.birashk_bttn = Button(self, text = "Calculate", command = self.birashk_converter).grid(row = 8, column = 12, columnspan = 3, sticky = W)

        # Assyrian calendar
        self.assyrian_lbl = Label(self, text = "Modern Assyrian Calendar").grid(row = 10, column = 0, columnspan = 3, sticky = W)
        self.assyrian_day_lbl = Label(self, text = "Day").grid(row = 11, column = 0, sticky = W)
        self.assyrian_day_ent = Entry(self)
        self.assyrian_day_ent.grid(row = 12, column = 0, sticky = W)
        self.assyrian_month_lbl = Label(self, text = "Month").grid(row = 11, column = 1, sticky = W)
        self.assyrian_month_ent = Entry(self)
        self.assyrian_month_ent.grid(row = 12, column = 1, sticky = W)
        self.assyrian_year_lbl = Label(self, text = "Year").grid(row = 11, column = 2, sticky = W)
        self.assyrian_year_ent = Entry(self)
        self.assyrian_year_ent.grid(row = 12, column = 2, sticky = W)
        self.assyrian_bttn = Button(self, text = "Calculate", command = self.assyrian_converter).grid(row = 13, column = 0, columnspan = 3, sticky = W)

        # Babylonian Calendar
        self.babylonian_lbl = Label(self, text = "Babylonian Calendar").grid(row = 10, column = 3, columnspan = 3, sticky = W)
        self.babylonian_day_lbl = Label(self, text = "Day").grid(row = 11, column = 3, sticky = W)
        self.babylonian_day_ent = Entry(self)
        self.babylonian_day_ent.grid(row = 12, column = 3, sticky = W)
        self.babylonian_month_lbl = Label(self, text = "Month").grid(row = 11, column = 4, sticky = W)
        self.babylonian_month_ent = Entry(self)
        self.babylonian_month_ent.grid(row = 12, column = 4, sticky = W)
        self.babylonian_year_lbl = Label(self, text = "Year").grid(row = 11, column = 5, sticky = W)
        self.babylonian_year_ent = Entry(self)
        self.babylonian_year_ent.grid(row = 12, column = 5, sticky = W)
        self.babylonian_bttn = Button(self, text = "Calculate", command = self.babylonian_converter).grid(row = 13, column = 3, columnspan = 3, sticky = W)

        # Hebrew (Jewish) Calendar
        self.hebrew_lbl = Label(self, text = "Jewish Hebrew Calendar").grid(row = 10, column = 6, columnspan = 3, sticky = W)
        self.hebrew_day_lbl = Label(self, text = "Day").grid(row = 11, column = 6, sticky = W)
        self.hebrew_day_ent = Entry(self)
        self.hebrew_day_ent.grid(row = 12, column = 6, sticky = W)
        self.hebrew_month_lbl = Label(self, text = "Month").grid(row = 11, column = 7, sticky = W)
        self.hebrew_month_ent = Entry(self)
        self.hebrew_month_ent.grid(row = 12, column = 7, sticky = W)
        self.hebrew_year_lbl = Label(self, text = "Year").grid(row = 11, column = 8, sticky = W)
        self.hebrew_year_ent = Entry(self)
        self.hebrew_year_ent.grid(row = 12, column = 8, sticky = W)
        self.hebrew_bttn = Button(self, text = "Calculate", command = self.hebrew_converter).grid(row = 13, column = 6, columnspan = 3, sticky = W)

        # Samaritan Calendar
        self.samaritan_lbl = Label(self, text = "Samaritan Hebrew Calendar (estimated)").grid(row = 10, column = 9, columnspan = 3, sticky = W)
        self.samaritan_day_lbl = Label(self, text = "Day").grid(row = 11, column = 9, sticky = W)
        self.samaritan_day_ent = Entry(self)
        self.samaritan_day_ent.grid(row = 12, column = 9, sticky = W)
        self.samaritan_month_lbl = Label(self, text = "Month").grid(row = 11, column = 10, sticky = W)
        self.samaritan_month_ent = Entry(self)
        self.samaritan_month_ent.grid(row = 12, column = 10, sticky = W)
        self.samaritan_year_lbl = Label(self, text = "Year").grid(row = 11, column = 11, sticky = W)
        self.samaritan_year_ent = Entry(self)
        self.samaritan_year_ent.grid(row = 12, column = 11, sticky = W)
        self.samaritan_bttn = Button(self, text = "Calculate", command = self.samaritan_converter).grid(row = 13, column = 9, columnspan = 3, sticky = W)

        # Kurdish Calendar
        self.kurdish_lbl = Label(self, text = "Kurdish Calendar").grid(row = 10, column = 12, columnspan = 3, sticky = W)
        self.kurdish_day_lbl = Label(self, text = "Day").grid(row = 11, column = 12, sticky = W)
        self.kurdish_day_ent = Entry(self)
        self.kurdish_day_ent.grid(row = 12, column = 12, sticky = W)
        self.kurdish_month_lbl = Label(self, text = "Month")
        self.kurdish_month_ent = Entry(self)
        self.kurdish_month_ent.grid(row = 12, column = 13, sticky = W)
        self.kurdish_year_lbl = Label(self, text = "Year").grid(row = 11, column = 14, sticky = W)
        self.kurdish_year_ent = Entry(self)
        self.kurdish_year_ent.grid(row = 12, column = 14, sticky = W)
        self.kurdish_bttn = Button(self, text = "Calculate", command = self.kurdish_converter).grid(row = 13, column = 12, columnspan = 3, sticky = W)

        # True Julian Day
        self.day_julian_lbl = Label(self, text = "True Julian Day").grid(row = 14, column = 0, sticky = W)
        self.day_julian_ent = Entry(self)
        self.day_julian_ent.grid(row = 15, column = 0, sticky = W)
        self.day_julian_bttn = Button(self, text = "Calculate", command = self.true_day_julian_converter).grid(row = 16, column = 0, sticky = W)

        # Reduced Julian Day
        self.red_day_julian_lbl = Label(self, text = "Reduced Julian Day").grid(row = 14, column = 1, sticky = W)
        self.red_day_julian_ent = Entry(self)
        self.red_day_julian_ent.grid(row = 15, column = 1, sticky = W)
        self.red_day_julian_bttn = Button(self, text = "Calculate", command = self.red_day_julian_converter).grid(row = 16, column = 1, sticky	= W)

        # Modified Julian Day
        self.mod_day_julian_lbl = Label(self, text = "Modified Julian Day").grid(row = 14, column = 2, sticky = W)
        self.mod_day_julian_ent = Entry(self)
        self.mod_day_julian_ent.grid(row = 15, column = 2, sticky = W)
        self.mod_day_julian_bttn = Button(self, text = "Calculate", command = self.mod_day_julian_converter).grid(row = 16, column = 2, sticky	= W)

        # Truncated Julian Day                                                                                      
        self.trun_day_julian_lbl = Label(self, text = "Truncated Julian Day").grid(row = 14, column =3, sticky = W)
        self.trun_day_julian_ent = Entry(self)
        self.trun_day_julian_ent.grid(row = 15, column = 3, sticky = W)
        self.trun_day_julian_bttn = Button(self, text = "Calculate", command = self.trun_day_julian_converter).grid(row = 16, column = 3, sticky = W)

        # Dublin Julian Day                                                                                         
        self.dub_day_julian_lbl = Label(self, text = "Dublin Julian Day").grid(row = 14, column = 4, sticky = W)
        self.dub_day_julian_ent = Entry(self)
        self.dub_day_julian_ent.grid(row = 15, column = 4, sticky = W)
        self.dub_day_julian_bttn = Button(self, text = "Calculate", command = self.dub_day_julian_converter).grid(row = 16, column = 4, sticky	= W)

        # CNES Julian Day                                                                                           
        self.cnes_lbl = Label(self, text = "CNES Julian Day").grid(row = 14, column = 5, sticky = W)
        self.cnes_ent = Entry(self)
        self.cnes_ent.grid(row = 15, column = 5, sticky = W)
        self.cnes_bttn = Button(self, text = "Calculate", command = self.cnes_converter).grid(row = 16, column = 5, sticky	= W)

        # CCSDS Julian Day                                                                                       
        self.ccsds_lbl = Label(self, text = "CCSDS Julian Day").grid(row = 14, column = 6, sticky = W)
        self.ccsds_ent = Entry(self)
        self.ccsds_ent.grid(row = 15, column = 6, sticky = W)
        self.ccsds_bttn = Button(self, text = "Calculate", command = self.ccsds_converter).grid(row = 16, column = 6, sticky	= W)

        # Lilian Day                                                                                           
        self.day_lilian_lbl = Label(self, text = "Lilian Day").grid(row = 14, column = 7, sticky = W)
        self.day_lilian_ent = Entry(self)
        self.day_lilian_ent.grid(row = 15, column = 7, sticky = W)
        self.day_lilian_bttn = Button(self, text = "Calculate", command = self.day_lilian_converter).grid(row = 16, column = 7, sticky	= W)

        # Rata Die
        self.rata_die_lbl = Label(self, text = "Rata Die").grid(row = 14, column = 8, sticky = W)
        self.rata_die_ent = Entry(self)
        self.rata_die_ent.grid(row = 15, column = 8, sticky = W)
        self.rata_die_bttn = Button(self, text = "Calculate", command = self.rata_die_converter).grid(row = 16, column = 8, sticky = W)

        # Unix time
        self.unix_time_lbl = Label(self, text = "Unix time").grid(row = 14, column = 9, sticky = W)
        self.unix_time_ent = Entry(self)
        self.unix_time_ent.grid(row = 15, column =9, sticky = W)
        self.unix_time_bttn = Button(self, text = "Calculate", command = self.unix_time_converter).grid(row = 16, column = 9, sticky	= W)

        # Gangale sol
        self.sol_gangale_lbl = Label(self, text = "Consecutive Martian sol").grid(row = 14, column = 10, sticky = W)
        self.sol_gangale_ent = Entry(self)
        self.sol_gangale_ent.grid(row = 15, column = 10, sticky = W)
        self.sol_gangale_bttn = Button(self, text = "Calculate", command = self.sol_gangale_converter).grid(row = 16, column = 10, sticky = W)

        # LOP day
        self.lop_lbl = Label(self, text = "LOP Julian day").grid(row = 14, column = 11, sticky = W)
        self.lop_ent = Entry(self)
        self.lop_ent.grid(row = 15, column = 11, sticky = W)
        self.lop_bttn = Button(self, text = "Calculate", command = self.lop_converter).grid(row = 16, column = 11, sticky = W)

        # Amazigh calendar
        self.amazigh_lbl = Label(self, text = "Amazigh calendar").grid(row = 18, column = 0, columnspan = 3, sticky = W)
        self.amazigh_day_lbl = Label(self, text = "Day").grid(row = 19, column = 0, sticky = W)
        self.amazigh_day_ent = Entry(self)
        self.amazigh_day_ent.grid(row = 20, column = 0, sticky = W)
        self.amazigh_month_lbl = Label(self, text = "Month").grid(row = 19, column = 1, sticky = W)
        self.amazigh_month_ent = Entry(self)
        self.amazigh_month_ent.grid(row = 20, column = 1, sticky = W)
        self.amazigh_year_lbl = Label(self, text = "Year").grid(row = 19, column = 2, sticky = W)
        self.amazigh_year_ent = Entry(self)
        self.amazigh_year_ent.grid(row = 20, column = 2, sticky = W)
        self.amazigh_bttn = Button(self, text = "Calculate", command = self.amazigh_converter).grid(row = 21, column = 0, sticky = W)

        # Rumi calendar
        self.rumi_n_lbl = Label(self, text = "Rumi calendar (non-skipping)").grid(row = 18, column = 3, columnspan = 3, sticky = W)
        self.rumi_n_day_lbl = Label(self, text = "Day").grid(row = 19, column = 3, sticky = W)
        self.rumi_n_day_ent = Entry(self)
        self.rumi_n_day_ent.grid(row = 20, column = 3, sticky = W)
        self.rumi_n_month_lbl = Label(self, text = "Month").grid(row = 19, column = 4, sticky = W)
        self.rumi_n_month_ent = Entry(self)
        self.rumi_n_month_ent.grid(row = 20, column = 4, sticky = W)
        self.rumi_n_year_lbl = Label(self, text = "Year").grid(row = 19, column = 5, sticky = W)
        self.rumi_n_year_ent = Entry(self)
        self.rumi_n_year_ent.grid(row = 20, column = 5, sticky = W)
        self.rumi_n_bttn = Button(self, text = "Calculate", command = self.rumi_n_converter).grid(row = 21, column = 3, columnspan = 3, sticky = W)

        # Revised Gregorian calendar
        self.rev_gregorian_lbl = Label(self, text = "Revised Gregorian calendar").grid(row = 18, column = 6, columnspan = 3, sticky = W)
        self.rev_gregorian_day_lbl = Label(self, text = "Day").grid(row = 19, column = 6, sticky = W)
        self.rev_gregorian_day_ent = Entry(self)
        self.rev_gregorian_day_ent.grid(row = 20, column = 6, sticky = W)
        self.rev_gregorian_month_lbl = Label(self, text = "Months").grid(row = 19, column = 7, sticky = W)
        self.rev_gregorian_month_ent = Entry(self)
        self.rev_gregorian_month_ent.grid(row = 20, column = 7, sticky = W)
        self.rev_gregorian_year_lbl = Label(self, text = "Year").grid(row = 19, column = 8, sticky = W)
        self.rev_gregorian_year_ent = Entry(self)
        self.rev_gregorian_year_ent.grid(row = 20, column = 8, sticky = W)
        self.rev_gregorian_bttn = Button(self, text = "Calculate", command = self.rev_gregorian_converter).grid(row = 21, column = 6, columnspan = 3, sticky = W)

        # Parker calendar
        self.parker_lbl = Label(self, text = "Parker calendar").grid(row = 18, column = 9, columnspan = 3, sticky = W)
        self.parker_day_lbl = Label(self, text = "Day").grid(row = 19, column = 9, sticky = W)
        self.parker_day_ent = Entry(self)
        self.parker_day_ent.grid(row = 20, column = 9, sticky = W)
        self.parker_month_lbl = Label(self, text = "Month").grid(row = 19, column = 10, sticky = W)
        self.parker_month_ent = Entry(self)
        self.parker_month_ent.grid(row = 20, column = 10, sticky = W)
        self.parker_year_lbl = Label(self, text = "Year").grid(row = 19, column = 11, sticky = W)
        self.parker_year_ent = Entry(self)
        self.parker_year_ent.grid(row = 20, column = 11, sticky = W)
        self.parker_bttn = Button(self, text = "Calculate", command = self.parker_converter).grid(row = 21, column = 9, columnspan = 3, sticky = W)

        # Goucher-Parker calendar
        self.goucher_lbl = Label(self, text = "Goucher-Parker calendar").grid(row = 18, column = 12, columnspan = 3, sticky = W)
        self.goucher_day_lbl = Label(self, text = "Day").grid(row = 19, column = 12, sticky = W)
        self.goucher_day_ent = Entry(self)
        self.goucher_day_ent.grid(row = 20, column = 12, sticky = W)
        self.goucher_month_lbl = Label(self, text = "Month").grid(row = 19, column = 13, sticky = W)
        self.goucher_month_ent = Entry(self)
        self.goucher_month_ent.grid(row = 20, column = 13, sticky = W)
        self.goucher_year_lbl = Label(self, text = "Year").grid(row = 19, column = 14, sticky = W)
        self.goucher_year_ent = Entry(self)
        self.goucher_year_ent.grid(row = 20, column = 14, sticky = W)
        self.goucher_bttn = Button(self, text = "Calculate", command = self.goucher_converter).grid(row = 21, column =12, columnspan = 3)

        # Serbian church calendar
        self.serbian_church_lbl = Label(self, text = "Serbian church calendar").grid(row = 23, column = 0, columnspan = 3, sticky = W)
        self.serbian_church_day_lbl = Label(self, text = "Day").grid(row = 24, column = 0, sticky = W)
        self.serbian_church_day_ent = Entry(self)
        self.serbian_church_day_ent.grid(row = 25, column = 0, sticky = W)
        self.serbian_church_month_lbl = Label(self, text = "Month").grid(row = 24, column = 1, sticky = W)
        self.serbian_church_month_ent = Entry(self)
        self.serbian_church_month_ent.grid(row = 25, column = 1, sticky = W)
        self.serbian_church_year_lbl = Label(self, text = "Year").grid(row = 24, column = 2, sticky = W)
        self.serbian_church_year_ent = Entry(self)
        self.serbian_church_year_ent.grid(row = 25, column = 2, sticky = W)
        self.serbian_church_bttn = Button(self, text = "Calculate", command = self.serbian_church_converter).grid(row = 26, column = 0, columnspan = 3, sticky = W)

        # Revised Julian calendar
        self.rev_julian_lbl = Label(self, text = "Revised Julian calendar").grid(row = 23, column = 3, columnspan = 3, sticky = W)
        self.rev_julian_day_lbl = Label(self, text = "Day").grid(row = 24, column = 3, sticky = W)
        self.rev_julian_day_ent = Entry(self)
        self.rev_julian_day_ent.grid(row = 25, column = 3, sticky = W)
        self.rev_julian_month_lbl = Label(self, text = "Month").grid(row = 24, column = 4, sticky = W)
        self.rev_julian_month_ent = Entry(self)
        self.rev_julian_month_ent.grid(row = 25, column = 4, sticky = W)
        self.rev_julian_year_lbl = Label(self, text = "Year").grid(row = 24, column = 5, sticky = W)
        self.rev_julian_year_ent = Entry(self)
        self.rev_julian_year_ent.grid(row = 25, column = 5, sticky = W)
        self.rev_julian_bttn = Button(self, text = "Calculate", command = self.rev_julian_converter).grid(row = 26, column = 3, sticky = W)

        # World calendar
        self.world_lbl = Label(self, text = "World Calendar").grid(row = 23, column = 6, columnspan = 3, sticky = W)
        self.world_day_lbl = Label(self, text = "Day").grid(row = 24, column = 6, sticky = W)
        self.world_day_ent = Entry(self)
        self.world_day_ent.grid(row = 25, column = 6, sticky = W)
        self.world_month_lbl = Label(self, text = "Month").grid(row = 24, column = 7, sticky = W)
        self.world_month_ent = Entry(self)
        self.world_month_ent.grid(row = 25, column = 7, sticky = W)
        self.world_year_lbl = Label(self, text = "Year").grid(row = 24, column = 8, sticky = W)
        self.world_year_ent = Entry(self)
        self.world_year_ent.grid(row = 25, column = 8, sticky = W)
        self.world_bttn = Button(self, text = "Calculate", command = self.world_converter).grid(row = 26, column = 6, columnspan = 3, sticky = W)

        # International Fixed Calendar
        self.ifc_lbl = Label(self, text = "International Fixed Calendar").grid(row = 23, column = 9, columnspan = 3, sticky = W)
        self.ifc_day_lbl = Label(self, text = "Day").grid(row = 24, column = 9, sticky = W)
        self.ifc_day_ent = Entry(self)
        self.ifc_day_ent.grid(row = 25, column = 9, sticky = W)
        self.ifc_month_lbl = Label(self, text = "Month").grid(row = 24, column = 10, sticky = W)
        self.ifc_month_ent = Entry(self)
        self.ifc_month_ent.grid(row = 25, column = 10, sticky = W)
        self.ifc_year_lbl = Label(self, text = "Year").grid(row = 24, column = 11, sticky = W)
        self.ifc_year_ent = Entry(self)
        self.ifc_year_ent.grid(row = 25, column = 11, sticky = W)
        self.ifc_bttn = Button(self, text = "Calculate", command = self.ifc_converter).grid(row = 26, column = 9, columnspan = 3, sticky = W)

        # Pax calendr
        self.pax_lbl = Label(self, text = "Pax calendar").grid(row = 23, column = 12, columnspan = 3, sticky = W)
        self.pax_day_lbl = Label(self, text = "Day").grid(row = 24, column = 12, sticky = W)
        self.pax_day_ent = Entry(self)
        self.pax_day_ent.grid(row = 25, column = 12, sticky = W)
        self.pax_month_lbl = Label(self, text = "Month").grid(row = 24, column = 13, sticky = W)
        self.pax_month_ent = Entry(self)
        self.pax_month_ent.grid(row = 25, column = 13, sticky = W)
        self.pax_year_lbl = Label(self, text = "Year").grid(row = 24, column = 14, sticky = W)
        self.pax_year_ent = Entry(self)
        self.pax_year_ent.grid(row = 25, column = 14, sticky = W)
        self.pax_bttn = Button(self, text = "Calculate", command = self.pax_converter).grid(row = 26, column = 12, sticky = W)

        # Gorman calendar
        self.gorman_lbl = Label(self, text = "Gorman calendar").grid(row = 28, column = 0, columnspan = 3, sticky = W)
        self.gorman_day_lbl = Label(self, text = "Day").grid(row = 29, column = 0, sticky = W)
        self.gorman_day_ent = Entry(self)
        self.gorman_day_ent.grid(row = 30, column = 0, sticky = W)
        self.gorman_month_lbl = Label(self, text = "Month").grid(row = 29, column = 1, sticky = W)
        self.gorman_month_ent = Entry(self)
        self.gorman_month_ent.grid(row = 30, column = 1, sticky = W)
        self.gorman_year_lbl = Label(self, text = "Year").grid(row = 29, column = 2, sticky = W)
        self.gorman_year_ent = Entry(self)
        self.gorman_year_ent.grid(row = 30, column = 2, sticky = W)
        self.gorman_bttn = Button(self, text = "Calculate", command = self.gorman_converter).grid(row = 31, column = 0, columnspan = 3, sticky = W)

        # Pax 2020 calendar
        self.pax2_lbl = Label(self, text = "Pax 2020 calendar").grid(row = 28, column = 3, columnspan = 3, sticky = W)
        self.pax2_day_lbl = Label(self, text = "Day").grid(row = 29, column = 3, sticky = W)
        self.pax2_day_ent = Entry(self)
        self.pax2_day_ent.grid(row = 30, column = 3, sticky = W)
        self.pax2_month_lbl = Label(self, text = "Month").grid(row = 29, column = 4, sticky = W)
        self.pax2_month_ent = Entry(self)
        self.pax2_month_ent.grid(row = 30, column = 4, sticky = W)
        self.pax2_year_lbl = Label(self, text = "Year").grid(row = 29, column = 5, sticky = W)
        self.pax2_year_ent = Entry(self)
        self.pax2_year_ent.grid(row = 30, column = 5, sticky = W)
        self.pax2_bttn = Button(self, text = "Calculate", command = self.pax2_converter).grid(row = 31, column = 3, columnspan = 3, sticky = W)
        
        
# create the root window
root = Tk()
app = Application(root)
root.title("Calendar Converter 0.15.0")
root.mainloop()
