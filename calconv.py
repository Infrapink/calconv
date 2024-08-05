#!/usr/bin/python3

from tkinter import *
from tkinter import ttk
from decimal import *
from math import ceil

import months

import julian
import gregorian
import coptic
import ethiopian
import egyptian
import armenian
import tab_islamic
import jalali
import birashk
import assyrian
import babylonian
import jewish
import samaritan
import kurdish
import amazigh
import lucis
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
import ast_gregorian
import nex
import positivist
import holocene
import ada
import obs_french
import alg_french
import solar_hijri
import thellid
import lunar_hijri
import arab
import inventionis
import rumi
import roman
import macedonian
import seleucid
import fixed_babylonian
import maya
import georgian_g
import georgian_c
import juche
import inca_lunar
import inca_solar
import chinese_lunisolar_huangdi
import chinese_lunisolar_yao
import chinese_lunisolar_confucius
import chinese_lunisolar_gonghe
import chinese_lunisolar_qin
import chinese_solar_huangdi
import chinese_solar_yao
import chinese_solar_confucius
import chinese_solar_gonghe
import chinese_solar_qin
import zhou
import zhuanxu
import xia
import shang
import lu
import yin
import taichu
import santong
import sifen
import qianxiang
import jingchu
import sanji
import yuanjia
import xuanshi
import daming
import zhengguang
import xinghe
import tianbao
import tianhe
import daxiang
import kaihuang
import daye
import wuyin
import xuanming
import vietnamese
import korean
import dangun
import japanese
import japanese_lunisolar
import mongolian
import bahai_alg
import bahai_obs
import cyrus
import qadimi_yz
import qadimi_az
import qadimi_zre
import shenshai_yz
import shenshai_az
import shenshai_zre
import young_avestan_iran_yz
import young_avestan_iran_az
import young_avestan_iran_zre
import young_avestan_india_yz
import young_avestan_india_az
import young_avestan_india_zre
import shahanshahi_yz
import shahanshahi_az
import shahanshahi_zre
import old_avestan_yz
import old_avestan_az
import old_avestan_zre
import fasli_yz
import fasli_az
import fasli_zre
import sogdian
import indian
import mandaean
import bahai_sid
import sothic
import madhyama_solar_ky
import madhyama_solar_vs
import madhyama_solar_se
import madhyama_lunar_ky
import madhyama_lunar_vs
import madhyama_lunar_se
import siddhantic_solar_ky
import siddhantic_solar_se
import siddhantic_solar_vs
import siddhantic_lunisolar_ky
import siddhantic_lunisolar_se
import siddhantic_lunisolar_vs
import obs_indian_solar_ky
import obs_indian_solar_se
import obs_indian_solar_vs
import obs_indian_lunisolar_ky
import obs_indian_lunisolar_se
import obs_indian_lunisolar_vs
import sid_malayam
import obs_malayam
import alt_malayam
import tamil
import sid_bengali
import obs_bengali
import bangladeshi1373
import bangladeshi1426
import sid_tripuri
import trop_tripuri
import mughal
import odia
import trop_indian_solar
import trop_indian_lunisolar
import jalgaon
import gujarat
import kutch
import manipuri
import sid_purnimanta
import obs_purnimanta
import mool_nanakshahi
import sid_nanakshahi
import jain_shvetambara
import jain_digambaras
import vj
import newar
import nepali_solar
import karana
import phugpa
import tsurphu
import bhutanese
import sherab_ling
import sarnath
import yellow

def cons_day_julian_todate():
        """Take the input into the Julian Day box andtojd it into the other date formats"""
        day = Decimal(cons_day_julian_ent.get())

    
        # Convert a Julian Day to a date in the Julian Calendar
        julian_date = julian.fromjd(day)
        julian_day_value = julian_date[0]
        julian_month_value = julian_date[1]
        julian_year_value = julian_date[2]
        julian_day_ent.delete(0, END)
        julian_month_ent.delete(0, END)
        julian_year_ent.delete(0, END)
        julian_day_ent.insert(0, julian_day_value)
        julian_month_ent.insert(0, julian_month_value)
        julian_year_ent.insert(0, julian_year_value)

        # Convert a Julian Day to a date in the Gregorian Calendar
        gregorian_date = gregorian.fromjd(day)
        gregorian_day_value = gregorian_date[0]
        gregorian_month_value = gregorian_date[1]
        gregorian_year_value = gregorian_date[2]
        gregorian_day_ent.delete(0, END)
        gregorian_month_ent.delete(0, END)
        gregorian_year_ent.delete(0, END)
        gregorian_day_ent.insert(0, gregorian_day_value)
        gregorian_month_ent.insert(0, gregorian_month_value)
        gregorian_year_ent.insert(0, gregorian_year_value)

        # Convert a Julian Day to a date in the Coptic Calendar
        coptic_date = coptic.fromjd(day)
        coptic_day_value = coptic_date[0]
        coptic_month_value = coptic_date[1]
        coptic_year_value = coptic_date[2]
        coptic_day_ent.delete(0, END)
        coptic_month_ent.delete(0, END)
        coptic_year_ent.delete(0, END)
        coptic_day_ent.insert(0, coptic_day_value)
        coptic_month_ent.insert(0, coptic_month_value)
        coptic_year_ent.insert(0, coptic_year_value)

        # Convert a Julian Day to a date in the Ethiopian Calendar
        ethiopian_date = ethiopian.fromjd(day)
        ethiopian_day_value = ethiopian_date[0]
        ethiopian_month_value = ethiopian_date[1]
        ethiopian_year_value = ethiopian_date[2]
        ethiopian_day_ent.delete(0, END)
        ethiopian_month_ent.delete(0, END)
        ethiopian_year_ent.delete(0, END)
        ethiopian_day_ent.insert(0, ethiopian_day_value)
        ethiopian_month_ent.insert(0, ethiopian_month_value)
        ethiopian_year_ent.insert(0, ethiopian_year_value)

        # Convert a Julian Day to a date in the Egyptian Calendar
        egyptian_date = egyptian.fromjd(day)
        egyptian_day_value = egyptian_date[0]
        egyptian_month_value = egyptian_date[1]
        egyptian_year_value = egyptian_date[2]
        egyptian_day_ent.delete(0, END)
        egyptian_month_ent.delete(0, END)
        egyptian_year_ent.delete(0, END)
        egyptian_day_ent.insert(0, egyptian_day_value)
        egyptian_month_ent.insert(0, egyptian_month_value)
        egyptian_year_ent.insert(0, egyptian_year_value)

        # Convert a Julian Day to a date in the Armenian Calendar
        armenian_date = armenian.fromjd(day)
        armenian_day_value = armenian_date[0]
        armenian_month_value = armenian_date[1]
        armenian_year_value = armenian_date[2]
        armenian_day_ent.delete(0, END)
        armenian_month_ent.delete(0, END)
        armenian_year_ent.delete(0, END)
        armenian_day_ent.insert(0, armenian_day_value)
        armenian_month_ent.insert(0, armenian_month_value)
        armenian_year_ent.insert(0, armenian_year_value)

        # Convert a Julian Day to a date in the Tabular Islamic Calendar
        tab_islamic_date = tab_islamic.fromjd(day)
        tab_islamic_day_value = tab_islamic_date[0]
        tab_islamic_month_value = tab_islamic_date[1]
        tab_islamic_year_value = tab_islamic_date[2]
        tab_islamic_day_ent.delete(0, END)
        tab_islamic_month_ent.delete(0, END)
        tab_islamic_year_ent.delete(0, END)
        tab_islamic_day_ent.insert(0, tab_islamic_day_value)
        tab_islamic_month_ent.insert(0, tab_islamic_month_value)
        tab_islamic_year_ent.insert(0, tab_islamic_year_value)

        m_year = int(tab_islamic_year_ent.get())        

        # Convert a Julian Day to a date in the Jalali calendar
        jalali_date = jalali.fromjd(day)
        jalali_day_value = jalali_date[0]
        jalali_month_value = jalali_date[1]
        jalali_year_value = jalali_date[2]
        jalali_day_ent.delete(0, END)
        jalali_month_ent.delete(0, END)
        jalali_year_ent.delete(0, END)
        jalali_day_ent.insert(0, jalali_day_value)
        jalali_month_ent.insert(0, jalali_month_value)
        jalali_year_ent.insert(0, jalali_year_value)

        # Convert a Julian Day to a date in Birashk's calendar
        birashk_date = birashk.fromjd(day)
        birashk_day_value = birashk_date[0]
        birashk_month_value = birashk_date[1]
        birashk_year_value = birashk_date[2]
        birashk_day_ent.delete(0, END)
        birashk_month_ent.delete(0, END)
        birashk_year_ent.delete(0, END)
        birashk_day_ent.insert(0, birashk_day_value)
        birashk_month_ent.insert(0, birashk_month_value)
        birashk_year_ent.insert(0, birashk_year_value)

        # Convert a Julian Day to a date in the Assyrian calendar
        assyrian_date = assyrian.fromjd(day)
        assyrian_day_value = assyrian_date[0]
        assyrian_month_value = assyrian_date[1]
        assyrian_year_value = assyrian_date[2]
        assyrian_day_ent.delete(0, END)
        assyrian_month_ent.delete(0, END)
        assyrian_year_ent.delete(0, END)
        assyrian_day_ent.insert(0, assyrian_day_value)
        assyrian_month_ent.insert(0, assyrian_month_value)
        assyrian_year_ent.insert(0, assyrian_year_value)

        # Convert a Julian Day to a date in the Babylonian calendar
        babylonian_date = babylonian.fromjd(day)
        babylonian_day_value = babylonian_date[0]
        babylonian_month_value = babylonian_date[1]
        babylonian_year_value = babylonian_date[2]
        babylonian_day_ent.delete(0, END)
        babylonian_month_ent.delete(0, END)
        babylonian_year_ent.delete(0, END)
        babylonian_day_ent.insert(0, babylonian_day_value)
        babylonian_month_ent.insert(0, babylonian_month_value)
        babylonian_year_ent.insert(0, babylonian_year_value)

        # Convert a Julian Day to a date in the Hebrew calendar
        jewish_date = jewish.fromjd(day)
        jewish_day_value = jewish_date[0]
        jewish_month_value = jewish_date[1]
        jewish_year_value = jewish_date[2]
        jewish_day_ent.delete(0, END)
        jewish_month_ent.delete(0, END)
        jewish_year_ent.delete(0, END)
        jewish_day_ent.insert(0, jewish_day_value)
        jewish_month_ent.insert(0, jewish_month_value)
        jewish_year_ent.insert(0, jewish_year_value)

        # Convert a Julian Day to a date in the Samaritan calendar
        samaritan_date = samaritan.fromjd(day)
        samaritan_day_value = samaritan_date[0]
        samaritan_month_value = samaritan_date[1]
        samaritan_year_value = samaritan_date[2]
        samaritan_day_ent.delete(0, END)
        samaritan_month_ent.delete(0, END)
        samaritan_year_ent.delete(0, END)
        samaritan_day_ent.insert(0, samaritan_day_value)
        samaritan_month_ent.insert(0, samaritan_month_value)
        samaritan_year_ent.insert(0, samaritan_year_value)

        # Convert a Julian Day to a date in the Kurdish calendar
        kurdish_date = kurdish.fromjd(day)
        kurdish_day_value = kurdish_date[0]
        kurdish_month_value = kurdish_date[1]
        kurdish_year_value = kurdish_date[2]
        kurdish_day_ent.delete(0,END)
        kurdish_month_ent.delete(0,END)
        kurdish_year_ent.delete(0,END)
        kurdish_day_ent.insert(0,kurdish_day_value)
        kurdish_month_ent.insert(0,kurdish_month_value)
        kurdish_year_ent.insert(0,kurdish_year_value)

        # True Julian Day
        tjday = ceil(day) - Decimal(0.5)
        day_julian_ent.delete(0,END)
        day_julian_ent.insert(0,tjday)

        # Reduced Julian Day
        rjday = ceil(day) - Decimal(0.5) - 2400000
        red_day_julian_ent.delete(0,END)
        red_day_julian_ent.insert(0,rjday)

        # Modified Julian Day
        mjday = ceil(day) - 2400001
        mod_day_julian_ent.delete(0,END)
        mod_day_julian_ent.insert(0,mjday)

        # Truncated Julian Day
        tjday = ceil(day) - 2440000
        trun_day_julian_ent.delete(0,END)
        trun_day_julian_ent.insert(0,tjday)

        # Dublin Julian Day
        djday = ceil(day) - Decimal(0.5) - 2415020
        dub_day_julian_ent.delete(0,END)
        dub_day_julian_ent.insert(0,djday)

        # CNES Julian Day
        cnes = ceil(day) - 2433282
        cnes_ent.delete(0,END)
        cnes_ent.insert(0,cnes)

        # CCSDS Julian Day
        ccsds = ceil(day) - 2436204
        ccsds_ent.delete(0,END)
        ccsds_ent.insert(0,ccsds)

        # Lilian Day
        lday = ceil(day) - 2299159
        day_lilian_ent.delete(0,END)
        day_lilian_ent.insert(0,lday)

        # Rata Die
        rday = ceil(day) - 1721424
        rata_die_ent.delete(0,END)
        rata_die_ent.insert(0,rday)

        # Unix time
        unix = (ceil(day) - 2440587) * 86400
        unix_time_ent.delete(0,END)
        unix_time_ent.insert(0,unix)

        # Julian Sol
        sol_gangale = round((ceil(day) - Decimal('2405520.5')) / Decimal('1.02749'))
        sol_gangale_ent.delete(0,END)
        sol_gangale_ent.insert(0,sol_gangale)

        # LOP Julian day
        lop = ceil(day) - 2448622
        lop_ent.delete(0,END)
        lop_ent.insert(0,lop)

        # VMS time
        vms = (ceil(day) - 2396349) * 86400 * 10000000
        vms_time_ent.delete(0,END)
        vms_time_ent.insert(9,vms)

        # Convert a Julian day to a date in the Amazigh calendar
        amazigh_date = amazigh.fromjd(day)
        amazigh_day_ent.delete(0,END)
        amazigh_month_ent.delete(0,END)
        amazigh_year_ent.delete(0,END)
        amazigh_day_ent.insert(0, amazigh_date[0])
        amazigh_month_ent.insert(0, amazigh_date[1])
        amazigh_year_ent.insert(0, amazigh_date[2])

        # Convert a Julian day to a n Anno Lucis date
        lucis_date = lucis.fromjd(day)
        lucis_day_ent.delete(0,END)
        lucis_month_ent.delete(0,END)
        lucis_year_ent.delete(0,END)
        lucis_day_ent.insert(0, lucis_date[0])
        lucis_month_ent.insert(0, lucis_date[1])
        lucis_year_ent.insert(0, lucis_date[2])

        # Convert a Julian day to a date in the revised Gregorian calendar
        rev_gregorian_date = rev_gregorian.fromjd(day)
        rev_gregorian_day_ent.delete(0, END)
        rev_gregorian_month_ent.delete(0, END)
        rev_gregorian_year_ent.delete(0, END)
        rev_gregorian_day_ent.insert(0, rev_gregorian_date[0])
        rev_gregorian_month_ent.insert(0, rev_gregorian_date[1])
        rev_gregorian_year_ent.insert(0, rev_gregorian_date[2])

        # Convert a Julian day to a date in the Parker calendar
        parker_date = parker.fromjd(day)
        parker_day_ent.delete(0, END)
        parker_month_ent.delete(0, END)
        parker_year_ent.delete(0, END)
        parker_day_ent.insert(0, parker_date[0])
        parker_month_ent.insert(0, parker_date[1])
        parker_year_ent.insert(0, parker_date[2])

        # Convert a Julian day to a date in the Goucher-Parker calendar
        goucher_date = goucher.fromjd(day)
        goucher_day_ent.delete(0, END)
        goucher_month_ent.delete(0, END)
        goucher_year_ent.delete(0, END)
        goucher_day_ent.insert(0, goucher_date[0])
        goucher_month_ent.insert(0, goucher_date[1])
        goucher_year_ent.insert(0, goucher_date[2])

        # Convert a Julian day to a date in the Serbian church calendar
        serbian_church_date = serbian_church.fromjd(day)
        serbian_church_day_ent.delete(0, END)
        serbian_church_month_ent.delete(0, END)
        serbian_church_year_ent.delete(0, END)
        serbian_church_day_ent.insert(0, serbian_church_date[0])
        serbian_church_month_ent.insert(0, serbian_church_date[1])
        serbian_church_year_ent.insert(0, serbian_church_date[2])

        # Convert a Julain day to a date in the revised Julian calendar
        rev_julian_date = rev_julian.fromjd(day)
        rev_julian_day_ent.delete(0, END)
        rev_julian_month_ent.delete(0, END)
        rev_julian_year_ent.delete(0, END)
        rev_julian_day_ent.insert(0, rev_julian_date[0])
        rev_julian_month_ent.insert(0, rev_julian_date[1])
        rev_julian_year_ent.insert(0, rev_julian_date[2])

        # Convert a Julian day to  a date in the World calendar
        world_date = world.fromjd(day)
        world_day_ent.delete(0, END)
        world_month_ent.delete(0, END)
        world_year_ent.delete(0, END)
        world_day_ent.insert(0, world_date[0])
        world_month_ent.insert(0, world_date[1])
        world_year_ent.insert(0, world_date[2])

        # Convert a Julian day to a date in the International Fixed calendar
        ifc_date = ifc.fromjd(day)
        ifc_day_ent.delete(0, END)
        ifc_month_ent.delete(0, END)
        ifc_year_ent.delete(0, END)
        ifc_day_ent.insert(0, ifc_date[0])
        ifc_month_ent.insert(0, ifc_date[1])
        ifc_year_ent.insert(0, ifc_date[2])

        # Convert a Julian day to a date in the Pax calendar
        pax_date = pax.fromjd(day)
        pax_day_ent.delete(0, END)
        pax_month_ent.delete(0, END)
        pax_year_ent.delete(0, END)
        pax_day_ent.insert(0, pax_date[0])
        pax_month_ent.insert(0, pax_date[1])
        pax_year_ent.insert(0, pax_date[2])

        # Convert a Julian day to a date in the Gorman calendar
        gorman_date = gorman.fromjd(day)
        gorman_day_ent.delete(0, END)
        gorman_month_ent.delete(0, END)
        gorman_year_ent.delete(0, END)
        gorman_day_ent.insert(0, gorman_date[0])
        gorman_month_ent.insert(0, gorman_date[1])
        gorman_year_ent.insert(0, gorman_date[2])

        # Convert a Julian day to a date in the Pax 2020 calendar
        pax2_date = pax2.fromjd(day)
        pax2_day_ent.delete(0, END)
        pax2_month_ent.delete(0, END)
        pax2_year_ent.delete(0, END)
        pax2_day_ent.insert(0, pax2_date[0])
        pax2_month_ent.insert(0, pax2_date[1])
        pax2_year_ent.insert(0, pax2_date[2])

        # Convert a Julian day to a date in the Positivist calendar
        positivist_date = positivist.fromjd(day)
        positivist_day_ent.delete(0, END)
        positivist_month_ent.delete(0, END)
        positivist_year_ent.delete(0, END)
        positivist_day_ent.insert(0, positivist_date[0])
        positivist_month_ent.insert(0, positivist_date[1])
        positivist_year_ent.insert(0, positivist_date[2])

        # Convert a Julian day to a date in the astronomical Gregorian calendar
        ast_gregorian_date = ast_gregorian.fromjd(day)
        ast_gregorian_day_ent.delete(0, END)
        ast_gregorian_month_ent.delete(0, END)
        ast_gregorian_year_ent.delete(0, END)
        ast_gregorian_day_ent.insert(0, ast_gregorian_date[0])
        ast_gregorian_month_ent.insert(0, ast_gregorian_date[1])
        ast_gregorian_year_ent.insert(0, ast_gregorian_date[2])

        # Convert a Julian day to a date in the Nex calendar
        nex_date = nex.fromjd(day)
        nex_day_ent.delete(0, END)
        nex_month_ent.delete(0, END)
        nex_year_ent.delete(0, END)
        nex_day_ent.insert(0, nex_date[0])
        nex_month_ent.insert(0, nex_date[1])
        nex_year_ent.insert(0, nex_date[2])

        # Convert a Julian day to a date in the Holocene era
        holocene_date = holocene.fromjd(day)
        holocene_day_ent.delete(0, END)
        holocene_month_ent.delete(0, END)
        holocene_year_ent.delete(0, END)
        holocene_day_ent.insert(0, holocene_date[0])
        holocene_month_ent.insert(0, holocene_date[1])
        holocene_year_ent.insert(0, holocene_date[2])

        # Convert a Julian day to an ADA date
        ada_date = ada.fromjd(day)
        ada_day_ent.delete(0, END)
        ada_month_ent.delete(0, END)
        ada_year_ent.delete(0, END)
        ada_day_ent.insert(0, ada_date[0])
        ada_month_ent.insert(0, ada_date[1])
        ada_year_ent.insert(0, ada_date[2])

        # Convert a Julian day to a date in the observational Frenchench Republican calendar
        obs_french_date = obs_french.fromjd(day)
        obs_french_day_ent.delete(0, END)
        obs_french_month_ent.delete(0, END)
        obs_french_year_ent.delete(0, END)
        obs_french_day_ent.insert(0, obs_french_date[0])
        obs_french_month_ent.insert(0, obs_french_date[1])
        obs_french_year_ent.insert(0, obs_french_date[2])

        # Convert a Julian day to a date in the algorithmic French Republican calendar
        alg_french_date = alg_french.fromjd(day)
        alg_french_day_ent.delete(0, END)
        alg_french_month_ent.delete(0, END)
        alg_french_year_ent.delete(0, END)
        alg_french_day_ent.insert(0, alg_french_date[0])
        alg_french_month_ent.insert(0, alg_french_date[1])
        alg_french_year_ent.insert(0, alg_french_date[2])

        # Convert a Julian day to a date in the Solar Hijri calendar
        solar_hijri_date = solar_hijri.fromjd(day)
        solar_hijri_day_ent.delete(0, END)
        solar_hijri_month_ent.delete(0, END)
        solar_hijri_year_ent.delete(0, END)
        solar_hijri_day_ent.insert(0, solar_hijri_date[0])
        solar_hijri_month_ent.insert(0, solar_hijri_date[1])
        solar_hijri_year_ent.insert(0, solar_hijri_date[2])

        # Convert a Julian day to a date in the thellid calendar
        thellid_date = thellid.fromjd(day)
        thellid_day_ent.delete(0, END)
        thellid_month_ent.delete(0, END)
        thellid_year_ent.delete(0, END)
        thellid_day_ent.insert(0, thellid_date[0])
        thellid_month_ent.insert(0, thellid_date[1])
        thellid_year_ent.insert(0, thellid_date[2])

        # Convert a Julian day to a date in the lunar_hijri calendar
        lunar_hijri_date = lunar_hijri.fromjd(day)
        lunar_hijri_day_ent.delete(0, END)
        lunar_hijri_month_ent.delete(0, END)
        lunar_hijri_year_ent.delete(0, END)
        lunar_hijri_day_ent.insert(0, lunar_hijri_date[0])
        lunar_hijri_month_ent.insert(0, lunar_hijri_date[1])
        lunar_hijri_year_ent.insert(0, lunar_hijri_date[2])

        # Convert a Julian day to a date in the Pre-Islamic Arab calendar
        arab_date = arab.fromjd(day)
        arab_day_ent.delete(0, END)
        arab_month_ent.delete(0, END)
        arab_year_ent.delete(0, END)
        arab_day_ent.insert(0, arab_date[0])
        arab_month_ent.insert(0, arab_date[1])
        arab_year_ent.insert(0, arab_date[2])

        # Convert a Julian day to a date in the Archmasonic calendar
        inventionis_date = inventionis.fromjd(day)
        inventionis_day_ent.delete(0, END)
        inventionis_month_ent.delete(0, END)
        inventionis_year_ent.delete(0, END)
        inventionis_day_ent.insert(0, inventionis_date[0])
        inventionis_month_ent.insert(0, inventionis_date[1])
        inventionis_year_ent.insert(0, inventionis_date[2])

        # Convert a Julian day to a date in the Ottoman fiscal calendar
        rumi_date = rumi.fromjd(day, m_year)
        rumi_day_ent.delete(0, END)
        rumi_month_ent.delete(0, END)
        rumi_year_ent.delete(0, END)
        rumi_day_ent.insert(0, rumi_date[0])
        rumi_month_ent.insert(0, rumi_date[1])
        rumi_year_ent.insert(0, rumi_date[2])

        # Convert a Julian day to a date in the Roman calendar
        roman_date = roman.fromjd(day)
        roman_day_ent.delete(0, END)
        roman_month_ent.delete(0, END)
        roman_year_ent.delete(0, END)
        roman_day_ent.insert(0, roman_date[0])
        roman_month_ent.insert(0, roman_date[1])
        roman_year_ent.insert(0, roman_date[2])

        # Convert a Julian day to a date in the Macedonian calendar
        macedonian_date = macedonian.fromjd(day)
        macedonian_day_ent.delete(0, END)
        macedonian_month_ent.delete(0, END)
        macedonian_year_ent.delete(0, END)
        macedonian_day_ent.insert(0, macedonian_date[0])
        macedonian_month_ent.insert(0, macedonian_date[1])
        macedonian_year_ent.insert(0, macedonian_date[2])

        # Convert a Julian day to a date in the Seleucid calendar
        seleucid_date = seleucid.fromjd(day)
        seleucid_day_ent.delete(0, END)
        seleucid_month_ent.delete(0, END)
        seleucid_year_ent.delete(0, END)
        seleucid_day_ent.insert(0, seleucid_date[0])
        seleucid_month_ent.insert(0, seleucid_date[1])
        seleucid_year_ent.insert(0, seleucid_date[2])

        # Convert a Julian day to a date in the Fixed Babylonian calendar
        fixed_babylonian_date = fixed_babylonian.fromjd(day)
        fixed_babylonian_day_ent.delete(0, END)
        fixed_babylonian_month_ent.delete(0, END)
        fixed_babylonian_year_ent.delete(0, END)
        fixed_babylonian_day_ent.insert(0, fixed_babylonian_date[0])
        fixed_babylonian_month_ent.insert(0, fixed_babylonian_date[1])
        fixed_babylonian_year_ent.insert(0, fixed_babylonian_date[2])

        # Convert a Julian Day to a Long Count date
        maya_date = maya.fromjd(day)
        maya_piktun_ent.delete(0, END)
        maya_baktun_ent.delete(0, END)
        maya_katun_ent.delete(0, END)
        maya_tun_ent.delete(0, END)
        maya_uinal_ent.delete(0, END)
        maya_kin_ent.delete(0, END)
        maya_piktun_ent.insert(0, maya_date[0])
        maya_baktun_ent.insert(0, maya_date[1])
        maya_katun_ent.insert(0, maya_date[2])
        maya_tun_ent.insert(0, maya_date[3])
        maya_uinal_ent.insert(0, maya_date[4])
        maya_kin_ent.insert(0, maya_date[5])

        # Convert a Julian day to a date in the original Georgian calendar
        georgian_g_date = georgian_g.fromjd(day)
        georgian_g_day_ent.delete(0, END)
        georgian_g_month_ent.delete(0, END)
        georgian_g_year_ent.delete(0, END)
        georgian_g_day_ent.insert(0, georgian_g_date[0])
        georgian_g_month_ent.insert(0, georgian_g_date[1])
        georgian_g_year_ent.insert(0, georgian_g_date[2])

        # Convert a Julian day to a date in the revised Georgian calendar
        georgian_c_date = georgian_c.fromjd(day)
        georgian_c_day_ent.delete(0, END)
        georgian_c_month_ent.delete(0, END)
        georgian_c_year_ent.delete(0, END)
        georgian_c_day_ent.insert(0, georgian_c_date[0])
        georgian_c_month_ent.insert(0, georgian_c_date[1])
        georgian_c_year_ent.insert(0, georgian_c_date[2])

        # Convert a Julian day to a date in the Juche calendar
        juche_date = juche.fromjd(day)
        juche_day_ent.delete(0, END)
        juche_month_ent.delete(0, END)
        juche_year_ent.delete(0, END)
        juche_day_ent.insert(0, juche_date[0])
        juche_month_ent.insert(0, juche_date[1])
        juche_year_ent.insert(0, juche_date[2])

        # Convert a Julian day to a date in the Inca civil calendar
        inca_lunar_date = inca_lunar.fromjd(day)
        inca_lunar_day_ent.delete(0, END)
        inca_lunar_month_ent.delete(0, END)
        inca_lunar_year_ent.delete(0, END)
        inca_lunar_day_ent.insert(0, inca_lunar_date[0])
        inca_lunar_month_ent.insert(0, inca_lunar_date[1])
        inca_lunar_year_ent.insert(0, inca_lunar_date[2])

        # Convert a Julian day to a date in the Inca agricultural calendar
        inca_solar_date = inca_solar.fromjd(day)
        inca_solar_day_ent.delete(0, END)
        inca_solar_month_ent.delete(0, END)
        inca_solar_year_ent.delete(0, END)
        inca_solar_day_ent.insert(0, inca_solar_date[0])
        inca_solar_month_ent.insert(0, inca_solar_date[1])
        inca_solar_year_ent.insert(0, inca_solar_date[2])

        # Convert a Julian day to a date in the Old Bahá'í calendar
        bahai_alg_date = bahai_alg.fromjd(day)
        bahai_alg_day_ent.delete(0, END)
        bahai_alg_month_ent.delete(0, END)
        bahai_alg_year_ent.delete(0, END)
        bahai_alg_day_ent.insert(0, bahai_alg_date[0])
        bahai_alg_month_ent.insert(0, bahai_alg_date[1])
        bahai_alg_year_ent.insert(0, bahai_alg_date[2])

        # Convert a Julian day to a date in the Iranian national calendar
        cyrus_date = cyrus.fromjd(day)
        cyrus_day_ent.delete(0, END)
        cyrus_month_ent.delete(0, END)
        cyrus_year_ent.delete(0, END)
        cyrus_day_ent.insert(0, cyrus_date[0])
        cyrus_month_ent.insert(0, cyrus_date[1])
        cyrus_year_ent.insert(0, cyrus_date[2])

        # Convert a Julian day to a date in the New Bahí'í calendar
        bahai_obs_date = bahai_obs.fromjd(day)
        bahai_obs_day_ent.delete(0, END)
        bahai_obs_month_ent.delete(0, END)
        bahai_obs_year_ent.delete(0, END)
        bahai_obs_day_ent.insert(0, bahai_obs_date[0])
        bahai_obs_month_ent.insert(0, bahai_obs_date[1])
        bahai_obs_year_ent.insert(0, bahai_obs_date[2])

        # Convert a Julian day to a date in the Chinese lunisolar calendar (Huangdi era)
        chinese_lunisolar_huangdi_date = chinese_lunisolar_huangdi.fromjd(day)
        chinese_lunisolar_huangdi_day_ent.delete(0, END)
        chinese_lunisolar_huangdi_month_ent.delete(0, END)
        chinese_lunisolar_huangdi_year_ent.delete(0, END)
        chinese_lunisolar_huangdi_day_ent.insert(0, chinese_lunisolar_huangdi_date[0])
        chinese_lunisolar_huangdi_month_ent.insert(0, chinese_lunisolar_huangdi_date[1])
        chinese_lunisolar_huangdi_year_ent.insert(0, chinese_lunisolar_huangdi_date[2])

        # Convert a Julian day to a date in the Chinese lunisolar calendar (Yao era)
        chinese_lunisolar_yao_date = chinese_lunisolar_yao.fromjd(day)
        chinese_lunisolar_yao_day_ent.delete(0, END)
        chinese_lunisolar_yao_month_ent.delete(0, END)
        chinese_lunisolar_yao_year_ent.delete(0, END)
        chinese_lunisolar_yao_day_ent.insert(0, chinese_lunisolar_yao_date[0])
        chinese_lunisolar_yao_month_ent.insert(0, chinese_lunisolar_yao_date[1])
        chinese_lunisolar_yao_year_ent.insert(0, chinese_lunisolar_yao_date[2])

        # Convert a Julian day to a date in the Chinese lunisolar calendar (Confucian era)
        chinese_lunisolar_confucius_date = chinese_lunisolar_confucius.fromjd(day)
        chinese_lunisolar_confucius_day_ent.delete(0, END)
        chinese_lunisolar_confucius_month_ent.delete(0, END)
        chinese_lunisolar_confucius_year_ent.delete(0, END)
        chinese_lunisolar_confucius_day_ent.insert(0, chinese_lunisolar_confucius_date[0])
        chinese_lunisolar_confucius_month_ent.insert(0, chinese_lunisolar_confucius_date[1])
        chinese_lunisolar_confucius_year_ent.insert(0, chinese_lunisolar_confucius_date[2])

        # Convert a Julian day to a date in the Chinese lunisolar calendar (Gonghe era)
        chinese_lunisolar_gonghe_date = chinese_lunisolar_gonghe.fromjd(day)
        chinese_lunisolar_gonghe_day_ent.delete(0, END)
        chinese_lunisolar_gonghe_month_ent.delete(0, END)
        chinese_lunisolar_gonghe_year_ent.delete(0, END)
        chinese_lunisolar_gonghe_day_ent.insert(0, chinese_lunisolar_gonghe_date[0])
        chinese_lunisolar_gonghe_month_ent.insert(0, chinese_lunisolar_gonghe_date[1])
        chinese_lunisolar_gonghe_year_ent.insert(0, chinese_lunisolar_gonghe_date[2])

        # Convert a Julian day to a date in the Chinese lunisolar calendar (Qin era)
        chinese_lunisolar_qin_date = chinese_lunisolar_qin.fromjd(day)
        chinese_lunisolar_qin_day_ent.delete(0, END)
        chinese_lunisolar_qin_month_ent.delete(0, END)
        chinese_lunisolar_qin_year_ent.delete(0, END)
        chinese_lunisolar_qin_day_ent.insert(0, chinese_lunisolar_qin_date[0])
        chinese_lunisolar_qin_month_ent.insert(0, chinese_lunisolar_qin_date[1])
        chinese_lunisolar_qin_year_ent.insert(0, chinese_lunisolar_qin_date[2])

        # Convert a Julian day to a date in the Chinese solar calendar (Yellow Emperor era)
        chinese_solar_huangdi_date = chinese_solar_huangdi.fromjd(day)
        chinese_solar_huangdi_day_ent.delete(0, END)
        chinese_solar_huangdi_month_ent.delete(0, END)
        chinese_solar_huangdi_year_ent.delete(0, END)
        chinese_solar_huangdi_day_ent.insert(0, chinese_solar_huangdi_date[0])
        chinese_solar_huangdi_month_ent.insert(0, chinese_solar_huangdi_date[1])
        chinese_solar_huangdi_year_ent.insert(0, chinese_solar_huangdi_date[2])

        # Convert a Julian day to a date in the Chinese solar calendar (Yao era)
        chinese_solar_yao_date = chinese_solar_yao.fromjd(day)
        chinese_solar_yao_day_ent.delete(0, END)
        chinese_solar_yao_month_ent.delete(0, END)
        chinese_solar_yao_year_ent.delete(0, END)
        chinese_solar_yao_day_ent.insert(0, chinese_solar_yao_date[0])
        chinese_solar_yao_month_ent.insert(0, chinese_solar_yao_date[1])
        chinese_solar_yao_year_ent.insert(0, chinese_solar_yao_date[2])

        # Convert a Julian day to a date in the Chinese solar calendar (Confucian era)
        chinese_solar_confucius_date = chinese_solar_confucius.fromjd(day)
        chinese_solar_confucius_day_ent.delete(0, END)
        chinese_solar_confucius_month_ent.delete(0, END)
        chinese_solar_confucius_year_ent.delete(0, END)
        chinese_solar_confucius_day_ent.insert(0, chinese_solar_confucius_date[0])
        chinese_solar_confucius_month_ent.insert(0, chinese_solar_confucius_date[1])
        chinese_solar_confucius_year_ent.insert(0, chinese_solar_confucius_date[2])

        # Convert a Julian day to a date in the Chinese solar calendar (Gonghe era)
        chinese_solar_gonghe_date = chinese_solar_gonghe.fromjd(day)
        chinese_solar_gonghe_day_ent.delete(0, END)
        chinese_solar_gonghe_month_ent.delete(0, END)
        chinese_solar_gonghe_year_ent.delete(0, END)
        chinese_solar_gonghe_day_ent.insert(0, chinese_solar_gonghe_date[0])
        chinese_solar_gonghe_month_ent.insert(0, chinese_solar_gonghe_date[1])
        chinese_solar_gonghe_year_ent.insert(0, chinese_solar_gonghe_date[2])

        # Convert a Julian day to a date in the Chinese solar calendar (Qin era)
        chinese_solar_qin_date = chinese_solar_qin.fromjd(day)
        chinese_solar_qin_day_ent.delete(0, END)
        chinese_solar_qin_month_ent.delete(0, END)
        chinese_solar_qin_year_ent.delete(0, END)
        chinese_solar_qin_day_ent.insert(0, chinese_solar_qin_date[0])
        chinese_solar_qin_month_ent.insert(0, chinese_solar_qin_date[1])
        chinese_solar_qin_year_ent.insert(0, chinese_solar_qin_date[2])

        # Convert a Julian day to a date in the Zhou calendar
        zhou_date = zhou.fromjd(day)
        zhou_day_ent.delete(0, END)
        zhou_month_ent.delete(0, END)
        zhou_year_ent.delete(0, END)
        zhou_day_ent.insert(0, zhou_date[0])
        zhou_month_ent.insert(0, zhou_date[1])
        zhou_year_ent.insert(0, zhou_date[2])

       # Convert a Julian day to a date in the Zhuanxu calendar
        zhuanxu_date = zhuanxu.fromjd(day)
        zhuanxu_day_ent.delete(0, END)
        zhuanxu_month_ent.delete(0, END)
        zhuanxu_year_ent.delete(0, END)
        zhuanxu_day_ent.insert(0, zhuanxu_date[0])
        zhuanxu_month_ent.insert(0, zhuanxu_date[1])
        zhuanxu_year_ent.insert(0, zhuanxu_date[2])

        # Convert a Julian day to a date in the Xia calendar
        xia_date = xia.fromjd(day)
        xia_day_ent.delete(0, END)
        xia_month_ent.delete(0, END)
        xia_year_ent.delete(0, END)
        xia_day_ent.insert(0, xia_date[0])
        xia_month_ent.insert(0, xia_date[1])
        xia_year_ent.insert(0, xia_date[2])

        # Convert a Julian day to a date in the Shang calendar
        shang_date = shang.fromjd(day)
        shang_day_ent.delete(0, END)
        shang_month_ent.delete(0, END)
        shang_year_ent.delete(0, END)
        shang_day_ent.insert(0, shang_date[0])
        shang_month_ent.insert(0, shang_date[1])
        shang_year_ent.insert(0, shang_date[2])

        # Convert a Julian day to a date in the Lu calendar
        lu_date = lu.fromjd(day)
        lu_day_ent.delete(0, END)
        lu_month_ent.delete(0, END)
        lu_year_ent.delete(0, END)
        lu_day_ent.insert(0, lu_date[0])
        lu_month_ent.insert(0, lu_date[1])
        lu_year_ent.insert(0, lu_date[2])

        # Convert a Julian day to a date in the Yin calendar
        yin_date = yin.fromjd(day)
        yin_day_ent.delete(0, END)
        yin_month_ent.delete(0, END)
        yin_year_ent.delete(0, END)
        yin_day_ent.insert(0, yin_date[0])
        yin_month_ent.insert(0, yin_date[1])
        yin_year_ent.insert(0, yin_date[2])

        # Convert a Julian day to a date in the Taichu calendar
        taichu_date = taichu.fromjd(day)
        taichu_day_ent.delete(0, END)
        taichu_month_ent.delete(0, END)
        taichu_year_ent.delete(0, END)
        taichu_day_ent.insert(0, taichu_date[0])
        taichu_month_ent.insert(0, taichu_date[1])
        taichu_year_ent.insert(0, taichu_date[2])

        # Convert a Julian day to a date in the Santong calendar
        santong_date = santong.fromjd(day)
        santong_day_ent.delete(0, END)
        santong_month_ent.delete(0, END)
        santong_year_ent.delete(0, END)
        santong_day_ent.insert(0, santong_date[0])
        santong_month_ent.insert(0, santong_date[1])
        santong_year_ent.insert(0, santong_date[2])

        # Convert a Julian day to a date in the Han Quarter Remainder calendar
        sifen_date = sifen.fromjd(day)
        sifen_day_ent.delete(0, END)
        sifen_month_ent.delete(0, END)
        sifen_year_ent.delete(0, END)
        sifen_day_ent.insert(0, sifen_date[0])
        sifen_month_ent.insert(0, sifen_date[1])
        sifen_year_ent.insert(0, sifen_date[2])

        # Convert a Julian day to a date in the Qianxiang calendar
        qianxiang_date = qianxiang.fromjd(day)
        qianxiang_day_ent.delete(0, END)
        qianxiang_month_ent.delete(0, END)
        qianxiang_year_ent.delete(0, END)
        qianxiang_day_ent.insert(0, qianxiang_date[0])
        qianxiang_month_ent.insert(0, qianxiang_date[1])
        qianxiang_year_ent.insert(0, qianxiang_date[2])

        # Convert a Julian day to a date in the Jingchu calendar
        jingchu_date = jingchu.fromjd(day)
        jingchu_day_ent.delete(0, END)
        jingchu_month_ent.delete(0, END)
        jingchu_year_ent.delete(0, END)
        jingchu_day_ent.insert(0, jingchu_date[0])
        jingchu_month_ent.insert(0, jingchu_date[1])
        jingchu_year_ent.insert(0, jingchu_date[2])

        # Convert a Julian day to a date in the Sanji calendar
        sanji_date = sanji.fromjd(day)
        sanji_day_ent.delete(0, END)
        sanji_month_ent.delete(0, END)
        sanji_year_ent.delete(0, END)
        sanji_day_ent.insert(0, sanji_date[0])
        sanji_month_ent.insert(0, sanji_date[1])
        sanji_year_ent.insert(0, sanji_date[2])

        # Convert a Julian day to a date in the Yuanjia calendar
        yuanjia_date = yuanjia.fromjd(day)
        yuanjia_day_ent.delete(0, END)
        yuanjia_month_ent.delete(0, END)
        yuanjia_year_ent.delete(0, END)
        yuanjia_day_ent.insert(0, yuanjia_date[0])
        yuanjia_month_ent.insert(0, yuanjia_date[1])
        yuanjia_year_ent.insert(0, yuanjia_date[2])

        # Convert a Julian day to a date in the Xuanshi calendar
        xuanshi_date = xuanshi.fromjd(day)
        xuanshi_day_ent.delete(0, END)
        xuanshi_month_ent.delete(0, END)
        xuanshi_year_ent.delete(0, END)
        xuanshi_day_ent.insert(0, xuanshi_date[0])
        xuanshi_month_ent.insert(0, xuanshi_date[1])
        xuanshi_year_ent.insert(0, xuanshi_date[2])

        # Convert a Julian day to a date in the Daming calendar
        daming_date = daming.fromjd(day)
        daming_day_ent.delete(0, END)
        daming_month_ent.delete(0, END)
        daming_year_ent.delete(0, END)
        daming_day_ent.insert(0, daming_date[0])
        daming_month_ent.insert(0, daming_date[1])
        daming_year_ent.insert(0, daming_date[2])

        # Convert a Julian day to a date in the Zhengguang calendar
        zhengguang_date = zhengguang.fromjd(day)
        zhengguang_day_ent.delete(0, END)
        zhengguang_month_ent.delete(0, END)
        zhengguang_year_ent.delete(0, END)
        zhengguang_day_ent.insert(0, zhengguang_date[0])
        zhengguang_month_ent.insert(0, zhengguang_date[1])
        zhengguang_year_ent.insert(0, zhengguang_date[2])

        # Convert a Julian day to a date in the Xinghe calendar
        xinghe_date = xinghe.fromjd(day)
        xinghe_day_ent.delete(0, END)
        xinghe_month_ent.delete(0, END)
        xinghe_year_ent.delete(0, END)
        xinghe_day_ent.insert(0, xinghe_date[0])
        xinghe_month_ent.insert(0, xinghe_date[1])
        xinghe_year_ent.insert(0, xinghe_date[2])

        # Convert a Julian day to a date in the Tianbao calendar
        tianbao_date = tianbao.fromjd(day)
        tianbao_day_ent.delete(0, END)
        tianbao_month_ent.delete(0, END)
        tianbao_year_ent.delete(0, END)
        tianbao_day_ent.insert(0, tianbao_date[0])
        tianbao_month_ent.insert(0, tianbao_date[1])
        tianbao_year_ent.insert(0, tianbao_date[2])

        # Convert a Julian day to a date in the Tianhe calendar
        tianhe_date = tianhe.fromjd(day)
        tianhe_day_ent.delete(0, END)
        tianhe_month_ent.delete(0, END)
        tianhe_year_ent.delete(0, END)
        tianhe_day_ent.insert(0, tianhe_date[0])
        tianhe_month_ent.insert(0, tianhe_date[1])
        tianhe_year_ent.insert(0, tianhe_date[2])

        # Convert a Julian day to a date in the Daxiang calendar
        daxiang_date = daxiang.fromjd(day)
        daxiang_day_ent.delete(0, END)
        daxiang_month_ent.delete(0, END)
        daxiang_year_ent.delete(0, END)
        daxiang_day_ent.insert(0, daxiang_date[0])
        daxiang_month_ent.insert(0, daxiang_date[1])
        daxiang_year_ent.insert(0, daxiang_date[2])

        # Convert a Julian day to a date in the Kaihuang calendar
        kaihuang_date = kaihuang.fromjd(day)
        kaihuang_day_ent.delete(0, END)
        kaihuang_month_ent.delete(0, END)
        kaihuang_year_ent.delete(0, END)
        kaihuang_day_ent.insert(0, kaihuang_date[0])
        kaihuang_month_ent.insert(0, kaihuang_date[1])
        kaihuang_year_ent.insert(0, kaihuang_date[2])

        # Convert a Julian day to a date in the Daye calendar
        daye_date = daye.fromjd(day)
        daye_day_ent.delete(0, END)
        daye_month_ent.delete(0, END)
        daye_year_ent.delete(0, END)
        daye_day_ent.insert(0, daye_date[0])
        daye_month_ent.insert(0, daye_date[1])
        daye_year_ent.insert(0, daye_date[2])

        # Convert a Julian day to a date in the Wuyin calendar
        wuyin_date = wuyin.fromjd(day)
        wuyin_day_ent.delete(0, END)
        wuyin_month_ent.delete(0, END)
        wuyin_year_ent.delete(0, END)
        wuyin_day_ent.insert(0, wuyin_date[0])
        wuyin_month_ent.insert(0, wuyin_date[1])
        wuyin_year_ent.insert(0, wuyin_date[2])

        # Convert a Julian day to a date in the Xuanming calendar
        xuanming_date = xuanming.fromjd(day)
        xuanming_day_ent.delete(0, END)
        xuanming_month_ent.delete(0, END)
        xuanming_year_ent.delete(0, END)
        xuanming_day_ent.insert(0, xuanming_date[0])
        xuanming_month_ent.insert(0, xuanming_date[1])
        xuanming_year_ent.insert(0, xuanming_date[2])

        # Convert a Julian day to a date in the Vietnamese lunisolar calendar
        vietnamese_date = vietnamese.fromjd(day)
        vietnamese_day_ent.delete(0, END)
        vietnamese_month_ent.delete(0, END)
        vietnamese_year_ent.delete(0, END)
        vietnamese_day_ent.insert(0, vietnamese_date[0])
        vietnamese_month_ent.insert(0, vietnamese_date[1])
        vietnamese_year_ent.insert(0, vietnamese_date[2])

        # Convert a Julian day to a date in the Royal Korean calendar
        korean_date = korean.fromjd(day)
        korean_day_ent.delete(0, END)
        korean_month_ent.delete(0, END)
        korean_year_ent.delete(0, END)
        korean_day_ent.insert(0, korean_date[0])
        korean_month_ent.insert(0, korean_date[1])
        korean_year_ent.insert(0, korean_date[2])

        # Convert a Julian day to a date in the Dangun (Korean lunisolar) calendar
        dangun_date = dangun.fromjd(day)
        dangun_day_ent.delete(0, END)
        dangun_month_ent.delete(0, END)
        dangun_year_ent.delete(0, END)
        dangun_day_ent.insert(0, dangun_date[0])
        dangun_month_ent.insert(0, dangun_date[1])
        dangun_year_ent.insert(0, dangun_date[2])

        # Convert a Julian day to a date in the Japanese lunisolar calendar
        japanese_lunisolar_date = japanese_lunisolar.fromjd(day)
        japanese_lunisolar_day_ent.delete(0, END)
        japanese_lunisolar_month_ent.delete(0, END)
        japanese_lunisolar_year_ent.delete(0, END)
        japanese_lunisolar_day_ent.insert(0, japanese_lunisolar_date[0])
        japanese_lunisolar_month_ent.insert(0, japanese_lunisolar_date[1])
        japanese_lunisolar_year_ent.insert(0, japanese_lunisolar_date[2])

        # Convert a Julian day to a date in the Imperial Japanese calendar
        japanese_date = japanese.fromjd(day)
        japanese_day_ent.delete(0, END)
        japanese_month_ent.delete(0, END)
        japanese_year_ent.delete(0, END)
        japanese_day_ent.insert(0, japanese_date[0])
        japanese_month_ent.insert(0, japanese_date[1])
        japanese_year_ent.insert(0, japanese_date[2])

        # Convert a Julian day to a date in the Mongolian traditional calendar
        mongolian_date = mongolian.fromjd(day)
        mongolian_day_ent.delete(0, END)
        mongolian_month_ent.delete(0, END)
        mongolian_year_ent.delete(0, END)
        mongolian_day_ent.insert(0, mongolian_date[0])
        mongolian_month_ent.insert(0, mongolian_date[1])
        mongolian_year_ent.insert(0, mongolian_date[2])

        # Convert a Julian day to a date in the Qadimi calendar (Yazdegerdi era) calendar
        qadimi_yz_date = qadimi_yz.fromjd(day)
        qadimi_yz_day_ent.delete(0, END)
        qadimi_yz_month_ent.delete(0, END)
        qadimi_yz_year_ent.delete(0, END)
        qadimi_yz_day_ent.insert(0, qadimi_yz_date[0])
        qadimi_yz_month_ent.insert(0, qadimi_yz_date[1])
        qadimi_yz_year_ent.insert(0, qadimi_yz_date[2])

        # Convert a Julian day to a date in the Qadimi calendar (Anno Zoroastres) calendar
        qadimi_az_date = qadimi_az.fromjd(day)
        qadimi_az_day_ent.delete(0, END)
        qadimi_az_month_ent.delete(0, END)
        qadimi_az_year_ent.delete(0, END)
        qadimi_az_day_ent.insert(0, qadimi_az_date[0])
        qadimi_az_month_ent.insert(0, qadimi_az_date[1])
        qadimi_az_year_ent.insert(0, qadimi_az_date[2])

        # Convert a Julian day to a date in the Qadimi calendar (Zoroastrian Religious Era)
        qadimi_zre_date = qadimi_zre.fromjd(day)
        qadimi_zre_day_ent.delete(0, END)
        qadimi_zre_month_ent.delete(0, END)
        qadimi_zre_year_ent.delete(0, END)
        qadimi_zre_day_ent.insert(0, qadimi_zre_date[0])
        qadimi_zre_month_ent.insert(0, qadimi_zre_date[1])
        qadimi_zre_year_ent.insert(0, qadimi_zre_date[2])

        # Convert a Julian day to a date in the Shenshai calendar (Yazdegerdi era)
        shenshai_yz_date = shenshai_yz.fromjd(day)
        shenshai_yz_day_ent.delete(0, END)
        shenshai_yz_month_ent.delete(0, END)
        shenshai_yz_year_ent.delete(0, END)
        shenshai_yz_day_ent.insert(0, shenshai_yz_date[0])
        shenshai_yz_month_ent.insert(0, shenshai_yz_date[1])
        shenshai_yz_year_ent.insert(0, shenshai_yz_date[2])

        # Convert a Julian day to a date in the Shenshai calendar (Anno Zoroastres)
        shenshai_az_date = shenshai_az.fromjd(day)
        shenshai_az_day_ent.delete(0, END)
        shenshai_az_month_ent.delete(0, END)
        shenshai_az_year_ent.delete(0, END)
        shenshai_az_day_ent.insert(0, shenshai_az_date[0])
        shenshai_az_month_ent.insert(0, shenshai_az_date[1])
        shenshai_az_year_ent.insert(0, shenshai_az_date[2])

        # Convert a Julian day to a date in the Shenshai calendar (Zoroastrian religious era)
        shenshai_zre_date = shenshai_zre.fromjd(day)
        shenshai_zre_day_ent.delete(0, END)
        shenshai_zre_month_ent.delete(0, END)
        shenshai_zre_year_ent.delete(0, END)
        shenshai_zre_day_ent.insert(0, shenshai_zre_date[0])
        shenshai_zre_month_ent.insert(0, shenshai_zre_date[1])
        shenshai_zre_year_ent.insert(0, shenshai_zre_date[2])

        # Convert a Julian day to a date in the Young Avestan calendar (Yazdegerdi era)
        young_avestan_iran_yz_date = young_avestan_iran_yz.fromjd(day)
        young_avestan_iran_yz_day_ent.delete(0, END)
        young_avestan_iran_yz_month_ent.delete(0, END)
        young_avestan_iran_yz_year_ent.delete(0, END)
        young_avestan_iran_yz_day_ent.insert(0, young_avestan_iran_yz_date[0])
        young_avestan_iran_yz_month_ent.insert(0, young_avestan_iran_yz_date[1])
        young_avestan_iran_yz_year_ent.insert(0, young_avestan_iran_yz_date[2])

        # Convert a Julian day to a date in the Young Avestan calendar (Iran, Anno Zoroastres)
        young_avestan_iran_az_date = young_avestan_iran_az.fromjd(day)
        young_avestan_iran_az_day_ent.delete(0, END)
        young_avestan_iran_az_month_ent.delete(0, END)
        young_avestan_iran_az_year_ent.delete(0, END)
        young_avestan_iran_az_day_ent.insert(0, young_avestan_iran_az_date[0])
        young_avestan_iran_az_month_ent.insert(0, young_avestan_iran_az_date[1])
        young_avestan_iran_az_year_ent.insert(0, young_avestan_iran_az_date[2])

        # Convert a Julian day to a date in the Young Avestan calendar (Iran, Zoroastrian Religious Era)
        young_avestan_iran_zre_date = young_avestan_iran_zre.fromjd(day)
        young_avestan_iran_zre_day_ent.delete(0, END)
        young_avestan_iran_zre_month_ent.delete(0, END)
        young_avestan_iran_zre_year_ent.delete(0, END)
        young_avestan_iran_zre_day_ent.insert(0, young_avestan_iran_zre_date[0])
        young_avestan_iran_zre_month_ent.insert(0, young_avestan_iran_zre_date[1])
        young_avestan_iran_zre_year_ent.insert(0, young_avestan_iran_zre_date[2])

        # Convert a Julian day to a date in the Young Avestan Calendar (India, Yazdegerdi era)
        young_avestan_india_yz_date = young_avestan_india_yz.fromjd(day)
        young_avestan_india_yz_day_ent.delete(0, END)
        young_avestan_india_yz_month_ent.delete(0, END)
        young_avestan_india_yz_year_ent.delete(0, END)
        young_avestan_india_yz_day_ent.insert(0, young_avestan_india_yz_date[0])
        young_avestan_india_yz_month_ent.insert(0, young_avestan_india_yz_date[1])
        young_avestan_india_yz_year_ent.insert(0, young_avestan_india_yz_date[2])

        # Convert a Julian day to a date in the Young Avestan calendar (India, Anno Zoroastres)
        young_avestan_india_az_date = young_avestan_india_az.fromjd(day)
        young_avestan_india_az_day_ent.delete(0, END)
        young_avestan_india_az_month_ent.delete(0, END)
        young_avestan_india_az_year_ent.delete(0, END)
        young_avestan_india_az_day_ent.insert(0, young_avestan_india_az_date[0])
        young_avestan_india_az_month_ent.insert(0, young_avestan_india_az_date[1])
        young_avestan_india_az_year_ent.insert(0, young_avestan_india_az_date[2])

        # Convert a Julian day to a date in the Young Avestan calendar (India, Zoroastrian Religious Era)
        young_avestan_india_zre_date = young_avestan_india_zre.fromjd(day)
        young_avestan_india_zre_day_ent.delete(0, END)
        young_avestan_india_zre_month_ent.delete(0, END)
        young_avestan_india_zre_year_ent.delete(0, END)
        young_avestan_india_zre_day_ent.insert(0, young_avestan_india_zre_date[0])
        young_avestan_india_zre_month_ent.insert(0, young_avestan_india_zre_date[1])
        young_avestan_india_zre_year_ent.insert(0, young_avestan_india_zre_date[2])

        # Convert a Julian day to a date in the Shahanshahi calendar (Yazdegerdi era)
        shahanshahi_yz_date = shahanshahi_yz.fromjd(day)
        shahanshahi_yz_day_ent.delete(0, END)
        shahanshahi_yz_month_ent.delete(0, END)
        shahanshahi_yz_year_ent.delete(0, END)
        shahanshahi_yz_day_ent.insert(0, shahanshahi_yz_date[0])
        shahanshahi_yz_month_ent.insert(0, shahanshahi_yz_date[1])
        shahanshahi_yz_year_ent.insert(0, shahanshahi_yz_date[2])

        # Convert a Julian day to a date in the Shahanshahi calendar (Anno Zoroastres)
        shahanshahi_az_date = shahanshahi_az.fromjd(day)
        shahanshahi_az_day_ent.delete(0, END)
        shahanshahi_az_month_ent.delete(0, END)
        shahanshahi_az_year_ent.delete(0, END)
        shahanshahi_az_day_ent.insert(0, shahanshahi_az_date[0])
        shahanshahi_az_month_ent.insert(0, shahanshahi_az_date[1])
        shahanshahi_az_year_ent.insert(0, shahanshahi_az_date[2])

        # Convert a Julian day to a date in the Shahanshahi calendar (Zoroastrian Religous Era)
        shahanshahi_zre_date = shahanshahi_zre.fromjd(day)
        shahanshahi_zre_day_ent.delete(0, END)
        shahanshahi_zre_month_ent.delete(0, END)
        shahanshahi_zre_year_ent.delete(0, END)
        shahanshahi_zre_day_ent.insert(0, shahanshahi_zre_date[0])
        shahanshahi_zre_month_ent.insert(0, shahanshahi_zre_date[1])
        shahanshahi_zre_year_ent.insert(0, shahanshahi_zre_date[2])

        # Convert a Julian day to a date in the Old Avestan calendar (Yazdegerdi era)
        old_avestan_yz_date = old_avestan_yz.fromjd(day)
        old_avestan_yz_day_ent.delete(0, END)
        old_avestan_yz_month_ent.delete(0, END)
        old_avestan_yz_year_ent.delete(0, END)
        old_avestan_yz_day_ent.insert(0, old_avestan_yz_date[0])
        old_avestan_yz_month_ent.insert(0, old_avestan_yz_date[1])
        old_avestan_yz_year_ent.insert(0, old_avestan_yz_date[2])

        # Convert a Julian day to a date in the Old Avestan calendar (Anno Zoroastres)
        old_avestan_az_date = old_avestan_az.fromjd(day)
        old_avestan_az_day_ent.delete(0, END)
        old_avestan_az_month_ent.delete(0, END)
        old_avestan_az_year_ent.delete(0, END)
        old_avestan_az_day_ent.insert(0, old_avestan_az_date[0])
        old_avestan_az_month_ent.insert(0, old_avestan_az_date[1])
        old_avestan_az_year_ent.insert(0, old_avestan_az_date[2])

        # Convert a Julian day to a date in the Old Avestan calendar (Zarathushtrian Religious Era)
        old_avestan_zre_date = old_avestan_zre.fromjd(day)
        old_avestan_zre_day_ent.delete(0, END)
        old_avestan_zre_month_ent.delete(0, END)
        old_avestan_zre_year_ent.delete(0, END)
        old_avestan_zre_day_ent.insert(0, old_avestan_zre_date[0])
        old_avestan_zre_month_ent.insert(0, old_avestan_zre_date[1])
        old_avestan_zre_year_ent.insert(0, old_avestan_zre_date[2])

        # Convert a Julian day to a date in the Fasli calendar (Yazdegerdi era)
        fasli_yz_date = fasli_yz.fromjd(day)
        fasli_yz_day_ent.delete(0, END)
        fasli_yz_month_ent.delete(0, END)
        fasli_yz_year_ent.delete(0, END)
        fasli_yz_day_ent.insert(0, fasli_yz_date[0])
        fasli_yz_month_ent.insert(0, fasli_yz_date[1])
        fasli_yz_year_ent.insert(0, fasli_yz_date[2])

        # Convert a Julian day to a date in the Fasli calendar (Anno Zoroastres)
        fasli_az_date = fasli_az.fromjd(day)
        fasli_az_day_ent.delete(0, END)
        fasli_az_month_ent.delete(0, END)
        fasli_az_year_ent.delete(0, END)
        fasli_az_day_ent.insert(0, fasli_az_date[0])
        fasli_az_month_ent.insert(0, fasli_az_date[1])
        fasli_az_year_ent.insert(0, fasli_az_date[2])

        # Convert a Julian day to a date in the Fasli calendar (ZRE)
        fasli_zre_date = fasli_zre.fromjd(day)
        fasli_zre_day_ent.delete(0, END)
        fasli_zre_month_ent.delete(0, END)
        fasli_zre_year_ent.delete(0, END)
        fasli_zre_day_ent.insert(0, fasli_zre_date[0])
        fasli_zre_month_ent.insert(0, fasli_zre_date[1])
        fasli_zre_year_ent.insert(0, fasli_zre_date[2])

        # Convert a Julian day to a date in the Sogdian calendar
        sogdian_date = sogdian.fromjd(day)
        sogdian_day_ent.delete(0, END)
        sogdian_month_ent.delete(0, END)
        sogdian_year_ent.delete(0, END)
        sogdian_day_ent.insert(0, sogdian_date[0])
        sogdian_month_ent.insert(0, sogdian_date[1])
        sogdian_year_ent.insert(0, sogdian_date[2])

        # Convert a Julian day to a date in the Indian national calendar
        indian_date = indian.fromjd(day)
        indian_day_ent.delete(0, END)
        indian_month_ent.delete(0, END)
        indian_year_ent.delete(0, END)
        indian_day_ent.insert(0, indian_date[0])
        indian_month_ent.insert(0, indian_date[1])
        indian_year_ent.insert(0, indian_date[2])

        # Convert a Julian day to a date in the Mandaean calendar
        mandaean_date = mandaean.fromjd(day)
        mandaean_day_ent.delete(0, END)
        mandaean_month_ent.delete(0, END)
        mandaean_year_ent.delete(0, END)
        mandaean_day_ent.insert(0, mandaean_date[0])
        mandaean_month_ent.insert(0, mandaean_date[1])
        mandaean_year_ent.insert(0, mandaean_date[2])

        # Convert a Julian day to a date in the Sidereal Bahá'í calendar
        bahai_sid_date = bahai_sid.fromjd(day)
        bahai_sid_day_ent.delete(0, END)
        bahai_sid_month_ent.delete(0, END)
        bahai_sid_year_ent.delete(0, END)
        bahai_sid_day_ent.insert(0, bahai_sid_date[0])
        bahai_sid_month_ent.insert(0, bahai_sid_date[1])
        bahai_sid_year_ent.insert(0, bahai_sid_date[2])

        # Convert a Julian day to a date in the Sothic calendar
        sothic_date = sothic.fromjd(day)
        sothic_day_ent.delete(0, END)
        sothic_month_ent.delete(0, END)
        sothic_year_ent.delete(0, END)
        sothic_day_ent.insert(0, sothic_date[0])
        sothic_month_ent.insert(0, sothic_date[1])
        sothic_year_ent.insert(0, sothic_date[2])

        # Convert a Julian day to a date in the Madhyama solar calendar (Kali Yuga)
        madhyama_solar_ky_date = madhyama_solar_ky.fromjd(day)
        madhyama_solar_ky_day_ent.delete(0, END)
        madhyama_solar_ky_month_ent.delete(0, END)
        madhyama_solar_ky_year_ent.delete(0, END)
        madhyama_solar_ky_day_ent.insert(0, madhyama_solar_ky_date[0])
        madhyama_solar_ky_month_ent.insert(0, madhyama_solar_ky_date[1])
        madhyama_solar_ky_year_ent.insert(0, madhyama_solar_ky_date[2])

        # Convert a Julian day to a date in the Madhyama solar calendar (Vikram Samvat)
        madhyama_solar_vs_date = madhyama_solar_vs.fromjd(day)
        madhyama_solar_vs_day_ent.delete(0, END)
        madhyama_solar_vs_month_ent.delete(0, END)
        madhyama_solar_vs_year_ent.delete(0, END)
        madhyama_solar_vs_day_ent.insert(0, madhyama_solar_vs_date[0])
        madhyama_solar_vs_month_ent.insert(0, madhyama_solar_vs_date[1])
        madhyama_solar_vs_year_ent.insert(0, madhyama_solar_vs_date[2])

        # Convert a Julian day to a date in the Madhyama solar calendar (Shaka Era)
        madhyama_solar_se_date = madhyama_solar_se.fromjd(day)
        madhyama_solar_se_day_ent.delete(0, END)
        madhyama_solar_se_month_ent.delete(0, END)
        madhyama_solar_se_year_ent.delete(0, END)
        madhyama_solar_se_day_ent.insert(0, madhyama_solar_se_date[0])
        madhyama_solar_se_month_ent.insert(0, madhyama_solar_se_date[1])
        madhyama_solar_se_year_ent.insert(0, madhyama_solar_se_date[2])

        # Convert a Julian day to a date in the Madhyama lunisolar calendar (Kali Yuga)
        madhyama_lunar_ky_date = madhyama_lunar_ky.fromjd(day)
        madhyama_lunar_ky_day_ent.delete(0, END)
        madhyama_lunar_ky_month_ent.delete(0, END)
        madhyama_lunar_ky_year_ent.delete(0, END)
        madhyama_lunar_ky_day_ent.insert(0, madhyama_lunar_ky_date[0])
        madhyama_lunar_ky_month_ent.insert(0, madhyama_lunar_ky_date[1])
        madhyama_lunar_ky_year_ent.insert(0, madhyama_lunar_ky_date[2])

        # Convert a Julian day to a date in the Madhyama lunisolar calendar (Vikram Samvat)
        madhyama_lunar_vs_date = madhyama_lunar_vs.fromjd(day)
        madhyama_lunar_vs_day_ent.delete(0, END)
        madhyama_lunar_vs_month_ent.delete(0, END)
        madhyama_lunar_vs_year_ent.delete(0, END)
        madhyama_lunar_vs_day_ent.insert(0, madhyama_lunar_vs_date[0])
        madhyama_lunar_vs_month_ent.insert(0, madhyama_lunar_vs_date[1])
        madhyama_lunar_vs_year_ent.insert(0, madhyama_lunar_vs_date[2])

        # Convert a Julian day to a date in the Madhyama lunisolar calendar (Shaka Era)
        madhyama_lunar_se_date = madhyama_lunar_se.fromjd(day)
        madhyama_lunar_se_day_ent.delete(0, END)
        madhyama_lunar_se_month_ent.delete(0, END)
        madhyama_lunar_se_year_ent.delete(0, END)
        madhyama_lunar_se_day_ent.insert(0, madhyama_lunar_se_date[0])
        madhyama_lunar_se_month_ent.insert(0, madhyama_lunar_se_date[1])
        madhyama_lunar_se_year_ent.insert(0, madhyama_lunar_se_date[2])

        # Convert a Julian day to a date in the traditional Bengali calendar
        sid_bengali_date = sid_bengali.fromjd(day)
        sid_bengali_day_ent.delete(0, END)
        sid_bengali_month_ent.delete(0, END)
        sid_bengali_year_ent.delete(0, END)
        sid_bengali_day_ent.insert(0, sid_bengali_date[0])
        sid_bengali_month_ent.insert(0, sid_bengali_date[1])
        sid_bengali_year_ent.insert(0, sid_bengali_date[2])

        # Convert a Julian day to a date in the modern Bengali calendar
        obs_bengali_date = obs_bengali.fromjd(day)
        obs_bengali_day_ent.delete(0, END)
        obs_bengali_month_ent.delete(0, END)
        obs_bengali_year_ent.delete(0, END)
        obs_bengali_day_ent.insert(0, obs_bengali_date[0])
        obs_bengali_month_ent.insert(0, obs_bengali_date[1])
        obs_bengali_year_ent.insert(0, obs_bengali_date[2])

        # Convert a Julian day to a date in the Tamil calendar
        tamil_date = tamil.fromjd(day)
        tamil_day_ent.delete(0, END)
        tamil_month_ent.delete(0, END)
        tamil_year_ent.delete(0, END)
        tamil_day_ent.insert(0, tamil_date[0])
        tamil_month_ent.insert(0, tamil_date[1])
        tamil_year_ent.insert(0, tamil_date[2])

        # Convert a Julian day to a date in the traditional Indian solar calendar (Kali Yuga)
        siddhantic_solar_ky_date = siddhantic_solar_ky.fromjd(day)
        siddhantic_solar_ky_day_ent.delete(0, END)
        siddhantic_solar_ky_month_ent.delete(0, END)
        siddhantic_solar_ky_year_ent.delete(0, END)
        siddhantic_solar_ky_day_ent.insert(0, siddhantic_solar_ky_date[0])
        siddhantic_solar_ky_month_ent.insert(0, siddhantic_solar_ky_date[1])
        siddhantic_solar_ky_year_ent.insert(0, siddhantic_solar_ky_date[2])

        # Convert a Julian day to a date in the traditional Indian solar calendar (Saka Era)
        siddhantic_solar_se_date = siddhantic_solar_se.fromjd(day)
        siddhantic_solar_se_day_ent.delete(0, END)
        siddhantic_solar_se_month_ent.delete(0, END)
        siddhantic_solar_se_year_ent.delete(0, END)
        siddhantic_solar_se_day_ent.insert(0, siddhantic_solar_se_date[0])
        siddhantic_solar_se_month_ent.insert(0, siddhantic_solar_se_date[1])
        siddhantic_solar_se_year_ent.insert(0, siddhantic_solar_se_date[2])

        # Convert a Julian day to a date in the traditional Indian solar calendar (Vikram Samvat)
        siddhantic_solar_vs_date = siddhantic_solar_vs.fromjd(day)
        siddhantic_solar_vs_day_ent.delete(0, END)
        siddhantic_solar_vs_month_ent.delete(0, END)
        siddhantic_solar_vs_year_ent.delete(0, END)
        siddhantic_solar_vs_day_ent.insert(0, siddhantic_solar_vs_date[0])
        siddhantic_solar_vs_month_ent.insert(0, siddhantic_solar_vs_date[1])
        siddhantic_solar_vs_year_ent.insert(0, siddhantic_solar_vs_date[2])        

	# Convert a Julian day to a date in the traditional Indian lunicalendar (Kali Yuga)
        siddhantic_lunisolar_ky_date = siddhantic_lunisolar_ky.fromjd(day)
        siddhantic_lunisolar_ky_day_ent.delete(0, END)
        siddhantic_lunisolar_ky_month_ent.delete(0, END)
        siddhantic_lunisolar_ky_year_ent.delete(0, END)
        siddhantic_lunisolar_ky_day_ent.insert(0, siddhantic_lunisolar_ky_date[0])
        siddhantic_lunisolar_ky_month_ent.insert(0, siddhantic_lunisolar_ky_date[1])
        siddhantic_lunisolar_ky_year_ent.insert(0, siddhantic_lunisolar_ky_date[2])

        # Convert a Julian day to a date in the traditional Indian lunisolar calendar (Ṡaka Era)
        siddhantic_lunisolar_se_date = siddhantic_lunisolar_se.fromjd(day)
        siddhantic_lunisolar_se_day_ent.delete(0, END)
        siddhantic_lunisolar_se_month_ent.delete(0, END)
        siddhantic_lunisolar_se_year_ent.delete(0, END)
        siddhantic_lunisolar_se_day_ent.insert(0, siddhantic_lunisolar_se_date[0])
        siddhantic_lunisolar_se_month_ent.insert(0, siddhantic_lunisolar_se_date[1])
        siddhantic_lunisolar_se_year_ent.insert(0, siddhantic_lunisolar_se_date[2])

        # Convert a Julian day to a date in the traditional Indian lunisolar calendar (Vikram Samvat)
        siddhantic_lunisolar_vs_date = siddhantic_lunisolar_vs.fromjd(day)
        siddhantic_lunisolar_vs_day_ent.delete(0, END)
        siddhantic_lunisolar_vs_month_ent.delete(0, END)
        siddhantic_lunisolar_vs_year_ent.delete(0, END)
        siddhantic_lunisolar_vs_day_ent.insert(0, siddhantic_lunisolar_vs_date[0])
        siddhantic_lunisolar_vs_month_ent.insert(0, siddhantic_lunisolar_vs_date[1])
        siddhantic_lunisolar_vs_year_ent.insert(0, siddhantic_lunisolar_vs_date[2])

       # Convert a Julian day to a date in the observational Indian solar calendar (Kali Yuga)
        obs_indian_solar_ky_date = obs_indian_solar_ky.fromjd(day)
        obs_indian_solar_ky_day_ent.delete(0, END)
        obs_indian_solar_ky_month_ent.delete(0, END)
        obs_indian_solar_ky_year_ent.delete(0, END)
        obs_indian_solar_ky_day_ent.insert(0, obs_indian_solar_ky_date[0])
        obs_indian_solar_ky_month_ent.insert(0, obs_indian_solar_ky_date[1])
        obs_indian_solar_ky_year_ent.insert(0, obs_indian_solar_ky_date[2])

        # Convert a Julian day to a date in the observational Indian solar calendar (Śaka Era)
        obs_indian_solar_se_date = obs_indian_solar_se.fromjd(day)
        obs_indian_solar_se_day_ent.delete(0, END)
        obs_indian_solar_se_month_ent.delete(0, END)
        obs_indian_solar_se_year_ent.delete(0, END)
        obs_indian_solar_se_day_ent.insert(0, obs_indian_solar_se_date[0])
        obs_indian_solar_se_month_ent.insert(0, obs_indian_solar_se_date[1])
        obs_indian_solar_se_year_ent.insert(0, obs_indian_solar_se_date[2])

        # Convert a Julian day to a date in the observational Indian solar calendar (Vikram Samvat)
        obs_indian_solar_vs_date = obs_indian_solar_vs.fromjd(day)
        obs_indian_solar_vs_day_ent.delete(0, END)
        obs_indian_solar_vs_month_ent.delete(0, END)
        obs_indian_solar_vs_year_ent.delete(0, END)
        obs_indian_solar_vs_day_ent.insert(0, obs_indian_solar_vs_date[0])
        obs_indian_solar_vs_month_ent.insert(0, obs_indian_solar_vs_date[1])
        obs_indian_solar_vs_year_ent.insert(0, obs_indian_solar_vs_date[2])

        # Convert a Julian day to a date in the observational Indian lunisolar calendar (Kali Yuga)
        obs_indian_lunisolar_ky_date = obs_indian_lunisolar_ky.fromjd(day)
        obs_indian_lunisolar_ky_day_ent.delete(0, END)
        obs_indian_lunisolar_ky_month_ent.delete(0, END)
        obs_indian_lunisolar_ky_year_ent.delete(0, END)
        obs_indian_lunisolar_ky_day_ent.insert(0, obs_indian_lunisolar_ky_date[0])
        obs_indian_lunisolar_ky_month_ent.insert(0, obs_indian_lunisolar_ky_date[1])
        obs_indian_lunisolar_ky_year_ent.insert(0, obs_indian_lunisolar_ky_date[2])

        # Convert a Julian day to a date in the observational Indian lunisolar calendar (Śaka Era)
        obs_indian_lunisolar_se_date = obs_indian_lunisolar_se.fromjd(day)
        obs_indian_lunisolar_se_day_ent.delete(0, END)
        obs_indian_lunisolar_se_month_ent.delete(0, END)
        obs_indian_lunisolar_se_year_ent.delete(0, END)
        obs_indian_lunisolar_se_day_ent.insert(0, obs_indian_lunisolar_se_date[0])
        obs_indian_lunisolar_se_month_ent.insert(0, obs_indian_lunisolar_se_date[1])
        obs_indian_lunisolar_se_year_ent.insert(0, obs_indian_lunisolar_se_date[2])

        # Convert a Julian day to a date in the observational Indian lunisolar calendar (Vikram Samvat)
        obs_indian_lunisolar_vs_date = obs_indian_lunisolar_vs.fromjd(day)
        obs_indian_lunisolar_vs_day_ent.delete(0, END)
        obs_indian_lunisolar_vs_month_ent.delete(0, END)
        obs_indian_lunisolar_vs_year_ent.delete(0, END)
        obs_indian_lunisolar_vs_day_ent.insert(0, obs_indian_lunisolar_vs_date[0])
        obs_indian_lunisolar_vs_month_ent.insert(0, obs_indian_lunisolar_vs_date[1])
        obs_indian_lunisolar_vs_year_ent.insert(0, obs_indian_lunisolar_vs_date[2])

        # Convert a Julian day to a date in the traditional Malayam calendar
        sid_malayam_date = sid_malayam.fromjd(day)
        sid_malayam_day_ent.delete(0, END)
        sid_malayam_month_ent.delete(0, END)
        sid_malayam_year_ent.delete(0, END)
        sid_malayam_day_ent.insert(0, sid_malayam_date[0])
        sid_malayam_month_ent.insert(0, sid_malayam_date[1])
        sid_malayam_year_ent.insert(0, sid_malayam_date[2])

        # Convert a Julian day to a date in the modern Malayam calendar
        obs_malayam_date = obs_malayam.fromjd(day)
        obs_malayam_day_ent.delete(0, END)
        obs_malayam_month_ent.delete(0, END)
        obs_malayam_year_ent.delete(0, END)
        obs_malayam_day_ent.insert(0, obs_malayam_date[0])
        obs_malayam_month_ent.insert(0, obs_malayam_date[1])
        obs_malayam_year_ent.insert(0, obs_malayam_date[2])

        # Convert a Julian day to a date in the alternative Malayam calendar
        alt_malayam_date = alt_malayam.fromjd(day)
        alt_malayam_day_ent.delete(0, END)
        alt_malayam_month_ent.delete(0, END)
        alt_malayam_year_ent.delete(0, END)
        alt_malayam_day_ent.insert(0, alt_malayam_date[0])
        alt_malayam_month_ent.insert(0, alt_malayam_date[1])
        alt_malayam_year_ent.insert(0, alt_malayam_date[2])

        # Convert a Julian day to a date in the Bangladeshi calendar (1373) calendar
        bangladeshi1373_date = bangladeshi1373.fromjd(day)
        bangladeshi1373_day_ent.delete(0, END)
        bangladeshi1373_month_ent.delete(0, END)
        bangladeshi1373_year_ent.delete(0, END)
        bangladeshi1373_day_ent.insert(0, bangladeshi1373_date[0])
        bangladeshi1373_month_ent.insert(0, bangladeshi1373_date[1])
        bangladeshi1373_year_ent.insert(0, bangladeshi1373_date[2])

        # Convert a Julian day to a date in the Bangladeshi calendar (1426) calendar
        bangladeshi1426_date = bangladeshi1426.fromjd(day)
        bangladeshi1426_day_ent.delete(0, END)
        bangladeshi1426_month_ent.delete(0, END)
        bangladeshi1426_year_ent.delete(0, END)
        bangladeshi1426_day_ent.insert(0, bangladeshi1426_date[0])
        bangladeshi1426_month_ent.insert(0, bangladeshi1426_date[1])
        bangladeshi1426_year_ent.insert(0, bangladeshi1426_date[2])

        # Convert a Julian day to a date in the Sidereal Tripuri calendar
        sid_tripuri_date = sid_tripuri.fromjd(day)
        sid_tripuri_day_ent.delete(0, END)
        sid_tripuri_month_ent.delete(0, END)
        sid_tripuri_year_ent.delete(0, END)
        sid_tripuri_day_ent.insert(0, sid_tripuri_date[0])
        sid_tripuri_month_ent.insert(0, sid_tripuri_date[1])
        sid_tripuri_year_ent.insert(0, sid_tripuri_date[2])

        # Convert a Julian day to a date in the Tropical Tripuri calendar
        trop_tripuri_date = trop_tripuri.fromjd(day)
        trop_tripuri_day_ent.delete(0, END)
        trop_tripuri_month_ent.delete(0, END)
        trop_tripuri_year_ent.delete(0, END)
        trop_tripuri_day_ent.insert(0, trop_tripuri_date[0])
        trop_tripuri_month_ent.insert(0, trop_tripuri_date[1])
        trop_tripuri_year_ent.insert(0, trop_tripuri_date[2])

        # Convert a Julian day to a date in the Mughal Faṣlī calendar
        mughal_date = mughal.fromjd(day)
        mughal_day_ent.delete(0, END)
        mughal_month_ent.delete(0, END)
        mughal_year_ent.delete(0, END)
        mughal_day_ent.insert(0, mughal_date[0])
        mughal_month_ent.insert(0, mughal_date[1])
        mughal_year_ent.insert(0, mughal_date[2])

        # Convert a Julian day to a date in the Odia calendar
        odia_date = odia.fromjd(day)
        odia_day_ent.delete(0, END)
        odia_month_ent.delete(0, END)
        odia_year_ent.delete(0, END)
        odia_day_ent.insert(0, odia_date[0])
        odia_month_ent.insert(0, odia_date[1])
        odia_year_ent.insert(0, odia_date[2])

        # Convert a Julian day to a date in the Tropical Indian solar calendar
        trop_indian_solar_date = trop_indian_solar.fromjd(day)
        trop_indian_solar_day_ent.delete(0, END)
        trop_indian_solar_month_ent.delete(0, END)
        trop_indian_solar_year_ent.delete(0, END)
        trop_indian_solar_day_ent.insert(0, trop_indian_solar_date[0])
        trop_indian_solar_month_ent.insert(0, trop_indian_solar_date[1])
        trop_indian_solar_year_ent.insert(0, trop_indian_solar_date[2])

        # Convert a Julian day to a date in the Tropical Indian lunisolar calendar
        trop_indian_lunisolar_date = trop_indian_lunisolar.fromjd(day)
        trop_indian_lunisolar_day_ent.delete(0, END)
        trop_indian_lunisolar_month_ent.delete(0, END)
        trop_indian_lunisolar_year_ent.delete(0, END)
        trop_indian_lunisolar_day_ent.insert(0, trop_indian_lunisolar_date[0])
        trop_indian_lunisolar_month_ent.insert(0, trop_indian_lunisolar_date[1])
        trop_indian_lunisolar_year_ent.insert(0, trop_indian_lunisolar_date[2])

        # Convert a Julian day to a date in the Jalgaon calendar
        jalgaon_date = jalgaon.fromjd(day)
        jalgaon_day_ent.delete(0, END)
        jalgaon_month_ent.delete(0, END)
        jalgaon_year_ent.delete(0, END)
        jalgaon_day_ent.insert(0, jalgaon_date[0])
        jalgaon_month_ent.insert(0, jalgaon_date[1])
        jalgaon_year_ent.insert(0, jalgaon_date[2])

        # Convert a Julian day to a date in the Manipuri calendar
        manipuri_date = manipuri.fromjd(day)
        manipuri_day_ent.delete(0, END)
        manipuri_month_ent.delete(0, END)
        manipuri_year_ent.delete(0, END)
        manipuri_day_ent.insert(0, manipuri_date[0])
        manipuri_month_ent.insert(0, manipuri_date[1])
        manipuri_year_ent.insert(0, manipuri_date[2])

        # Convert a Julian day to a date in the Gujarat calendar
        gujarat_date = gujarat.fromjd(day)
        gujarat_day_ent.delete(0, END)
        gujarat_month_ent.delete(0, END)
        gujarat_year_ent.delete(0, END)
        gujarat_day_ent.insert(0, gujarat_date[0])
        gujarat_month_ent.insert(0, gujarat_date[1])
        gujarat_year_ent.insert(0, gujarat_date[2])

        # Convert a Julian day to a date in the Kutch calendar
        kutch_date = kutch.fromjd(day)
        kutch_day_ent.delete(0, END)
        kutch_month_ent.delete(0, END)
        kutch_year_ent.delete(0, END)
        kutch_day_ent.insert(0, kutch_date[0])
        kutch_month_ent.insert(0, kutch_date[1])
        kutch_year_ent.insert(0, kutch_date[2])

        # Convert a Julian day to a date in the Traditional Indian lunisolar calendar (purnimanta)
        sid_purnimanta_date = sid_purnimanta.fromjd(day)
        sid_purnimanta_day_ent.delete(0, END)
        sid_purnimanta_month_ent.delete(0, END)
        sid_purnimanta_year_ent.delete(0, END)
        sid_purnimanta_day_ent.insert(0, sid_purnimanta_date[0])
        sid_purnimanta_month_ent.insert(0, sid_purnimanta_date[1])
        sid_purnimanta_year_ent.insert(0, sid_purnimanta_date[2])

        # Convert a Julian day to a date in the Indian lunisolar calendar (purnimanta)
        obs_purnimanta_date = obs_purnimanta.fromjd(day)
        obs_purnimanta_day_ent.delete(0, END)
        obs_purnimanta_month_ent.delete(0, END)
        obs_purnimanta_year_ent.delete(0, END)
        obs_purnimanta_day_ent.insert(0, obs_purnimanta_date[0])
        obs_purnimanta_month_ent.insert(0, obs_purnimanta_date[1])
        obs_purnimanta_year_ent.insert(0, obs_purnimanta_date[2])

        # Convert a Julian day to a date in the Original Nnanakshahi calendar
        mool_nanakshahi_date = mool_nanakshahi.fromjd(day)
        mool_nanakshahi_day_ent.delete(0, END)
        mool_nanakshahi_month_ent.delete(0, END)
        mool_nanakshahi_year_ent.delete(0, END)
        mool_nanakshahi_day_ent.insert(0, mool_nanakshahi_date[0])
        mool_nanakshahi_month_ent.insert(0, mool_nanakshahi_date[1])
        mool_nanakshahi_year_ent.insert(0, mool_nanakshahi_date[2])

        # Convert a Julian day to a date in the Sidereal Nnanakshahi calendar
        sid_nanakshahi_date = sid_nanakshahi.fromjd(day)
        sid_nanakshahi_day_ent.delete(0, END)
        sid_nanakshahi_month_ent.delete(0, END)
        sid_nanakshahi_year_ent.delete(0, END)
        sid_nanakshahi_day_ent.insert(0, sid_nanakshahi_date[0])
        sid_nanakshahi_month_ent.insert(0, sid_nanakshahi_date[1])
        sid_nanakshahi_year_ent.insert(0, sid_nanakshahi_date[2])

        # Convert a Julian day to a date in the Śvetāmbara Jain calendar
        jain_shvetambara_date = jain_shvetambara.fromjd(day)
        jain_shvetambara_day_ent.delete(0, END)
        jain_shvetambara_month_ent.delete(0, END)
        jain_shvetambara_year_ent.delete(0, END)
        jain_shvetambara_day_ent.insert(0, jain_shvetambara_date[0])
        jain_shvetambara_month_ent.insert(0, jain_shvetambara_date[1])
        jain_shvetambara_year_ent.insert(0, jain_shvetambara_date[2])

        # Convert a Julian day to a date in the Digambaras Jain calendar
        jain_digambaras_date = jain_digambaras.fromjd(day)
        jain_digambaras_day_ent.delete(0, END)
        jain_digambaras_month_ent.delete(0, END)
        jain_digambaras_year_ent.delete(0, END)
        jain_digambaras_day_ent.insert(0, jain_digambaras_date[0])
        jain_digambaras_month_ent.insert(0, jain_digambaras_date[1])
        jain_digambaras_year_ent.insert(0, jain_digambaras_date[2])

        # Convert a Julian day to a date in the Vedāṅga Jyotiṣa calendar
        vj_date = vj.fromjd(day)
        vj_day_ent.delete(0, END)
        vj_month_ent.delete(0, END)
        vj_year_ent.delete(0, END)
        vj_day_ent.insert(0, vj_date[0])
        vj_month_ent.insert(0, vj_date[1])
        vj_year_ent.insert(0, vj_date[2])

        # Convert a Julian day to a date in the Nepali lunisolar calendar
        newar_date = newar.fromjd(day)
        newar_day_ent.delete(0, END)
        newar_month_ent.delete(0, END)
        newar_year_ent.delete(0, END)
        newar_day_ent.insert(0, newar_date[0])
        newar_month_ent.insert(0, newar_date[1])
        newar_year_ent.insert(0, newar_date[2])

        # Convert a Julian day to a date in the Nepali solar calendar
        nepali_solar_date = nepali_solar.fromjd(day)
        nepali_solar_day_ent.delete(0, END)
        nepali_solar_month_ent.delete(0, END)
        nepali_solar_year_ent.delete(0, END)
        nepali_solar_day_ent.insert(0, nepali_solar_date[0])
        nepali_solar_month_ent.insert(0, nepali_solar_date[1])
        nepali_solar_year_ent.insert(0, nepali_solar_date[2])

        # Convert a Julian day to a date in the Karana calendar
        karana_date = karana.fromjd(day)
        karana_day_ent.delete(0, END)
        karana_month_ent.delete(0, END)
        karana_year_ent.delete(0, END)
        karana_day_ent.insert(0, karana_date[0])
        karana_month_ent.insert(0, karana_date[1])
        karana_year_ent.insert(0, karana_date[2])

        # Convert a Julian day to a date in the Yellow Tibetan calendar
        phugpa_date = phugpa.fromjd(day)
        phugpa_day_ent.delete(0, END)
        phugpa_month_ent.delete(0, END)
        phugpa_year_ent.delete(0, END)
        phugpa_day_ent.insert(0, phugpa_date[0])
        phugpa_month_ent.insert(0, phugpa_date[1])
        phugpa_year_ent.insert(0, phugpa_date[2])

        # Convert a Julian day to a date in the Tibetan calendar (Tsurphu tradition)
        tsurphu_date = tsurphu.fromjd(day)
        tsurphu_day_ent.delete(0, END)
        tsurphu_month_ent.delete(0, END)
        tsurphu_year_ent.delete(0, END)
        tsurphu_day_ent.insert(0, tsurphu_date[0])
        tsurphu_month_ent.insert(0, tsurphu_date[1])
        tsurphu_year_ent.insert(0, tsurphu_date[2])

        # Convert a Julian day to a date in the Mongolian calendar
        mongolian_date = mongolian.fromjd(day)
        mongolian_day_ent.delete(0, END)
        mongolian_month_ent.delete(0, END)
        mongolian_year_ent.delete(0, END)
        mongolian_day_ent.insert(0, mongolian_date[0])
        mongolian_month_ent.insert(0, mongolian_date[1])
        mongolian_year_ent.insert(0, mongolian_date[2])

        # Convert a Julian day to a date in the Bhutanese calendar
        bhutanese_date = bhutanese.fromjd(day)
        bhutanese_day_ent.delete(0, END)
        bhutanese_month_ent.delete(0, END)
        bhutanese_year_ent.delete(0, END)
        bhutanese_day_ent.insert(0, bhutanese_date[0])
        bhutanese_month_ent.insert(0, bhutanese_date[1])
        bhutanese_year_ent.insert(0, bhutanese_date[2])

        # Convert a Julian day to a date in the Yellow Tibetan calendar
        yellow_date = yellow.fromjd(day)
        yellow_day_ent.delete(0, END)
        yellow_month_ent.delete(0, END)
        yellow_year_ent.delete(0, END)
        yellow_day_ent.insert(0, yellow_date[0])
        yellow_month_ent.insert(0, yellow_date[1])
        yellow_year_ent.insert(0, yellow_date[2])

        # Convert a Julian day to a date in the Sherab Ling calendar
        sherab_ling_date = sherab_ling.fromjd(day)
        sherab_ling_day_ent.delete(0, END)
        sherab_ling_month_ent.delete(0, END)
        sherab_ling_year_ent.delete(0, END)
        sherab_ling_day_ent.insert(0, sherab_ling_date[0])
        sherab_ling_month_ent.insert(0, sherab_ling_date[1])
        sherab_ling_year_ent.insert(0, sherab_ling_date[2])

        # Convert a Julian day to a date in the Sarnath calendar
        sarnath_date = sarnath.fromjd(day)
        sarnath_day_ent.delete(0, END)
        sarnath_month_ent.delete(0, END)
        sarnath_year_ent.delete(0, END)
        sarnath_day_ent.insert(0, sarnath_date[0])
        sarnath_month_ent.insert(0, sarnath_date[1])
        sarnath_year_ent.insert(0, sarnath_date[2])

def cons_day_julian_plus():
        day = cons_day_julian_ent.get()
        day = int(day) + 1
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, day)
        cons_day_julian_todate()
        
def cons_day_julian_minus():
        day = cons_day_julian_ent.get()
        day = int(day) - 1
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, day)
        cons_day_julian_todate()

def julian_converter():
        """Convert a date in the Julian Calendar to a Julian Day."""
        day = julian_day_ent.get()
        month = julian_month_ent.get()
        year = julian_year_ent.get()
        jday = julian.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()
        
def gregorian_converter():
        """Convert a date in the Gregorian Calendar to a Julian  Day."""
        day = gregorian_day_ent.get()
        month = gregorian_month_ent.get()
        year = gregorian_year_ent.get()
        jday = gregorian.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()
        
def coptic_converter():
        """Convert a date in the Coptic Calendar to a Julian Day."""
        day = coptic_day_ent.get()
        month = coptic_month_ent.get()
        year = coptic_year_ent.get()
        jday = coptic.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()
        
def ethiopian_converter():
        """Convert a date in the Ethiopian Calendar to a Julian day."""
        day = ethiopian_day_ent.get()
        month = ethiopian_month_ent.get()
        year = ethiopian_year_ent.get()
        jday = ethiopian.tojd(day,month,year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()
        
def egyptian_converter():
        """Convert a date in the Egyptian Calendar to a Julian Day."""
        day = egyptian_day_ent.get()
        month = egyptian_month_ent.get()
        year = egyptian_year_ent.get()
        jday = egyptian.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()
        
def armenian_converter():
        """Convert a date in the Armenian Calendar to a Julian Day."""
        day = armenian_day_ent.get()
        month = armenian_month_ent.get()
        year = armenian_year_ent.get()
        jday = armenian.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()
        
def tab_islamic_converter():
        """Convert a date in the Lunar Hijri Calendar to a Julian DAy."""
        day = tab_islamic_day_ent.get()
        month = tab_islamic_month_ent.get()
        year = tab_islamic_year_ent.get()
        jday = tab_islamic.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()
        
def jalali_converter():
        """Convert a date in the Solar Hijri Calendar to a Julian Day."""
        day = jalali_day_ent.get()
        month = jalali_month_ent.get()
        year = jalali_year_ent.get()
        jday = jalali.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()
        
def birashk_converter():
        """Convert a date in Birashk's calendar to a Julian Day."""
        day = birashk_day_ent.get()
        month = birashk_month_ent.get()
        year = birashk_year_ent.get()
        jday = birashk.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()
        
def assyrian_converter():
        """Convert a date in the Assyrian calendar to a Julian Day."""
        day = assyrian_day_ent.get()
        month = assyrian_month_ent.get()
        year = assyrian_year_ent.get()
        jday = assyrian.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()
        
def babylonian_converter():
        """Convert a date in the Babylonian calendar to a Julian Day."""
        day = babylonian_day_ent.get()
        month = babylonian_month_ent.get()
        year = babylonian_year_ent.get()
        jday = babylonian.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()
        
def jewish_converter():
        """Convert a date in the Hebrew calendar to a Julian Day."""
        day = jewish_day_ent.get()
        month = jewish_month_ent.get()
        year = jewish_year_ent.get()
        jday = jewish.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()
        
def samaritan_converter():
        """Convert a date in the Samaritan Hebrew calendar to a Julian Day"""
        day = samaritan_day_ent.get()
        month = samaritan_month_ent.get()
        year = samaritan_year_ent.get()
        jday = samaritan.tojd(day,month,year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()
        
def kurdish_converter():
        """Convert a date in the Kurdish calendar to a Julian Day."""
        day = kurdish_day_ent.get()
        month = kurdish_month_ent.get()
        year = kurdish_year_ent.get()
        jday = kurdish.tojd(day,month,year)
        cons_day_julian_ent.delete(0,END)
        cons_day_julian_ent.insert(0,jday)
        cons_day_julian_todate()
        
def true_day_julian_converter():
        """Convert a Julian Day to a True Julian Day."""
        jday = int(Decimal(day_julian_ent.get()) - Decimal('0.5'))
        cons_day_julian_ent.delete(0,END)
        cons_day_julian_ent.insert(0,jday)
        cons_day_julian_todate()
        
def red_day_julian_converter():
        """Convert a Reduced Julian Day to a Consecutive Julian Day."""
        jday = Decimal(red_day_julian_ent.get()) + 2400000 - Decimal('0.5')
        cons_day_julian_ent.delete(0,END)
        cons_day_julian_ent.insert(0,jday)
        cons_day_julian_todate()
        
def mod_day_julian_converter():
        """Convert a Modified Julian Day to a Consecutive Julian Day."""
        jday = int(mod_day_julian_ent.get()) + 2400000
        cons_day_julian_ent.delete(0,END)
        cons_day_julian_ent.insert(0,jday)
        cons_day_julian_todate()
        
def trun_day_julian_converter():
        """Convert a Truncated Julian Day to a Consecutive Julian Day."""
        jday = int(trun_day_julian_ent.get()) + 2440000
        cons_day_julian_ent.delete(0,END)
        cons_day_julian_ent.insert(0,jday)
        cons_day_julian_todate()
        
def dub_day_julian_converter():
        """Convert a Dublin Julian Day to a Consecutive Julian DAy."""
        jday = Decimal(dub_day_julian_ent.get()) + 2415020 - Decimal('0.5')
        cons_day_julian_ent.delete(0,END)
        cons_day_julian_ent.insert(0,jday)
        cons_day_julian_todate()
        
def cnes_converter():
        """Convert a CNES Julian Day into a Consecutive Julian Day."""
        jday = int(cnes_ent.get())+ 2433282
        cons_day_julian_ent.delete(0,END)
        cons_day_julian_ent.insert(0,jday)
        cons_day_julian_todate()
        
def ccsds_converter():
        jday = int(ccsds_ent.get()) + 2436204
        cons_day_julian_ent.delete(0,END)
        cons_day_julian_ent.insert(0,jday)
        cons_day_julian_todate()
        
def day_lilian_converter():
        jday = int(day_lilian_ent.get()) + 2299159
        cons_day_julian_ent.delete(0,END)
        cons_day_julian_ent.insert(0,jday)
        cons_day_julian_todate()
        
def rata_die_converter():
        jday = int(rata_die_ent.get()) + 1721424
        cons_day_julian_ent.delete(0,END)
        cons_day_julian_ent.insert(0,jday)
        cons_day_julian_todate()
        
def unix_time_converter():
        unix = int(unix_time_ent.get())
        jday = (unix // 86400) + 2440587
        cons_day_julian_ent.delete(0,END)
        cons_day_julian_ent.insert(0,jday)
        cons_day_julian_todate()

        unix_time_ent.delete(0,END)
        unix_time_ent.insert(0,unix)

        vms = unix + (86400 * (2440587 - 2396349))
        vms *= 10000000
        vms_time_ent.delete(0,END)
        vms_time_ent.insert(0,vms)
        
def sol_gangale_converter():
        jday = round(Decimal(sol_gangale_ent.get()) * Decimal('1.02749')) + 2405521
        cons_day_julian_ent.delete(0,END)
        cons_day_julian_ent.insert(0,jday)
        cons_day_julian_todate()
        
def lop_converter():
        jday = int(lop_ent.get()) + 2448622
        cons_day_julian_ent.delete(0,END)
        cons_day_julian_ent.insert(0,jday)
        cons_day_julian_todate()

def vms_time_converter():
        vms = int(vms_time_ent.get())
        jday = (vms // (86400 * 10000000)) + 2396349
        cons_day_julian_ent.delete(0,END)
        cons_day_julian_ent.insert(0,jday)
        cons_day_julian_todate()

        vms_time_ent.delete(0,END)
        vms_time_ent.insert(0,vms)

        unix = vms // 10000000
        unix -= (86400 * (2440587 - 2396349))
        unix_time_ent.delete(0,END)
        unix_time_ent.insert(0,unix)
        
def amazigh_converter():
        """Convert a date in the Amazigh calendar to a Julian day."""
        day = int(amazigh_day_ent.get())
        month = amazigh_month_ent.get()
        year = int(amazigh_year_ent.get())
        jday = amazigh.tojd(day,month,year)
        cons_day_julian_ent.delete(0,END)
        cons_day_julian_ent.insert(0,jday)
        cons_day_julian_todate()
        
def lucis_converter():
        """Convert a Masonic date to a Julian day."""
        day = int(lucis_day_ent.get())
        month = lucis_month_ent.get()
        year = int(lucis_year_ent.get())
        jday = lucis.tojd(day, month, year)
        cons_day_julian_ent.delete(0,END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()
        
def rev_gregorian_converter():
        """Convert a date in the revised Gregorian calendar to a Julian day."""
        day = int(rev_gregorian_day_ent.get())
        month = rev_gregorian_month_ent.get()
        year = int(rev_gregorian_year_ent.get())
        jday = rev_gregorian.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()
        
def parker_converter():
        """Convert a date in the Parker calendar to a Julian day."""
        day = int(parker_day_ent.get())
        month = parker_month_ent.get()
        year = int(parker_year_ent.get())
        jday = parker.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()
        
def goucher_converter():
        """Convert a date in the Goucher calendar to a Julian day."""
        day = int(goucher_day_ent.get())
        month = goucher_month_ent.get()
        year = int(goucher_year_ent.get())
        jday = goucher.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()
        
def serbian_church_converter():
        day = int(serbian_church_day_ent.get())
        month = serbian_church_month_ent.get()
        year = int(serbian_church_year_ent.get())
        jday = serbian_church.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()
        
def rev_julian_converter():
        day = int(rev_julian_day_ent.get())
        month = rev_julian_month_ent.get()
        year = int(rev_julian_year_ent.get())
        jday = rev_julian.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def world_converter():
        day = int(world_day_ent.get())
        month = world_month_ent.get()
        year = int(world_year_ent.get())
        jday = world.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def ifc_converter():
        day = int(ifc_day_ent.get())
        month = ifc_month_ent.get()
        year = int(ifc_year_ent.get())
        jday = ifc.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def pax_converter():
        day = int(pax_day_ent.get())
        month = pax_month_ent.get()
        year = int(pax_year_ent.get())
        jday = pax.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def gorman_converter():
        day = int(gorman_day_ent.get())
        month = gorman_month_ent.get()
        year = int(gorman_year_ent.get())
        jday = gorman.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def pax2_converter():
        day = pax2_day_ent.get()
        day = int(day)
        month = pax2_month_ent.get()
        year = int(pax2_year_ent.get())
        jday = pax2.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def positivist_converter():
        day = int(positivist_day_ent.get())
        month = positivist_month_ent.get()
        year = int(positivist_year_ent.get())
        jday = positivist.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def ast_gregorian_converter():
        day = int(ast_gregorian_day_ent.get())
        month = ast_gregorian_month_ent.get()
        year = int(ast_gregorian_year_ent.get())
        jday = ast_gregorian.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def nex_converter():
        day = int(nex_day_ent.get())
        month = nex_month_ent.get()
        year = int(nex_year_ent.get())
        jday = nex.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def holocene_converter():
        day = int(holocene_day_ent.get())
        month = holocene_month_ent.get()
        year = int(holocene_year_ent.get())
        jday = holocene.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def ada_converter():
        day = int(ada_day_ent.get())
        month = ada_month_ent.get()
        year = int(ada_year_ent.get())
        jday = ada.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def obs_french_converter():
        day = int(obs_french_day_ent.get())
        month = obs_french_month_ent.get()
        year = int(obs_french_year_ent.get())
        jday = obs_french.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def alg_french_converter():
        day = int(alg_french_day_ent.get())
        month = alg_french_month_ent.get()
        year = int(alg_french_year_ent.get())
        jday = alg_french.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def solar_hijri_converter():
        day = int(solar_hijri_day_ent.get())
        month = solar_hijri_month_ent.get()
        year = int(solar_hijri_year_ent.get())
        jday = solar_hijri.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def thellid_converter():
        day = int(thellid_day_ent.get())
        month = thellid_month_ent.get()
        year = int(thellid_year_ent.get())
        jday = thellid.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def lunar_hijri_converter():
        day = int(lunar_hijri_day_ent.get())
        month = lunar_hijri_month_ent.get()
        year = int(lunar_hijri_year_ent.get())
        jday = lunar_hijri.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def arab_converter():
        day = int(arab_day_ent.get())
        month = arab_month_ent.get()
        year = int(arab_year_ent.get())
        jday = arab.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def inventionis_converter():
        """Convert a date in the Archmasonic calendar to a Julian Day."""
        day = inventionis_day_ent.get()
        month = inventionis_month_ent.get()
        year = inventionis_year_ent.get()
        jday = inventionis.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def rumi_converter():
        day = int(rumi_day_ent.get())
        month = rumi_month_ent.get()
        year = int(rumi_year_ent.get())
        jday = rumi.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def roman_converter():
        day = int(roman_day_ent.get())
        month = roman_month_ent.get()
        year = int(roman_year_ent.get())
        jday = roman.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def macedonian_converter():
        day = int(macedonian_day_ent.get())
        month = macedonian_month_ent.get()
        year = int(macedonian_year_ent.get())
        jday = macedonian.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def seleucid_converter():
        day = int(seleucid_day_ent.get())
        month = seleucid_month_ent.get()
        year = int(seleucid_year_ent.get())
        jday = seleucid.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def fixed_babylonian_converter():
        day = int(fixed_babylonian_day_ent.get())
        month = fixed_babylonian_month_ent.get()
        year = int(fixed_babylonian_year_ent.get())
        jday = fixed_babylonian.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()



def maya_converter():
        piktun = int(maya_piktun_ent.get())
        baktun = int(maya_baktun_ent.get())
        katun = int(maya_katun_ent.get())
        tun = int(maya_tun_ent.get())
        uinal = int(maya_uinal_ent.get())
        kin = int(maya_kin_ent.get())
        jday = maya.tojd(piktun, baktun, katun, tun, uinal, kin)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def georgian_g_converter():
        day = int(georgian_g_day_ent.get())
        month = georgian_g_month_ent.get()
        year = int(georgian_g_year_ent.get())
        jday = georgian_g.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def georgian_c_converter():
        day = int(georgian_c_day_ent.get())
        month = georgian_c_month_ent.get()
        year = int(georgian_c_year_ent.get())
        jday = georgian_c.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def juche_converter():
        day = int(juche_day_ent.get())
        month = juche_month_ent.get()
        year = int(juche_year_ent.get())
        jday = juche.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def inca_lunar_converter():
        day = int(inca_lunar_day_ent.get())
        month = inca_lunar_month_ent.get()
        year = int(inca_lunar_year_ent.get())
        jday = inca_lunar.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def inca_solar_converter():
        day = int(inca_solar_day_ent.get())
        month = inca_solar_month_ent.get()
        year = int(inca_solar_year_ent.get())
        jday = inca_solar.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def bahai_alg_converter():
        day = int(bahai_alg_day_ent.get())
        month = bahai_alg_month_ent.get()
        year = int(bahai_alg_year_ent.get())
        jday = bahai_alg.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def bahai_obs_converter():
        day = int(bahai_obs_day_ent.get())
        month = bahai_obs_month_ent.get()
        year = int(bahai_obs_year_ent.get())
        jday = bahai_obs.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def cyrus_converter():
        day = int(cyrus_day_ent.get())
        month = cyrus_month_ent.get()
        year = int(cyrus_year_ent.get())
        jday = cyrus.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def chinese_lunisolar_huangdi_converter():
        day = int(chinese_lunisolar_huangdi_day_ent.get())
        month = chinese_lunisolar_huangdi_month_ent.get()
        year = int(chinese_lunisolar_huangdi_year_ent.get())
        jday = chinese_lunisolar_huangdi.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def chinese_lunisolar_yao_converter():
        day = int(chinese_lunisolar_yao_day_ent.get())
        month = chinese_lunisolar_yao_month_ent.get()
        year = int(chinese_lunisolar_yao_year_ent.get())
        jday = chinese_lunisolar_yao.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def chinese_lunisolar_confucius_converter():
        day = int(chinese_lunisolar_confucius_day_ent.get())
        month = chinese_lunisolar_confucius_month_ent.get()
        year = int(chinese_lunisolar_confucius_year_ent.get())
        jday = chinese_lunisolar_confucius.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def chinese_lunisolar_gonghe_converter():
        day = int(chinese_lunisolar_gonghe_day_ent.get())
        month = chinese_lunisolar_gonghe_month_ent.get()
        year = int(chinese_lunisolar_gonghe_year_ent.get())
        jday = chinese_lunisolar_gonghe.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def chinese_lunisolar_qin_converter():
        day = int(chinese_lunisolar_qin_day_ent.get())
        month = chinese_lunisolar_qin_month_ent.get()
        year = int(chinese_lunisolar_qin_year_ent.get())
        jday = chinese_lunisolar_qin.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def chinese_solar_huangdi_converter():
        day = int(chinese_solar_huangdi_day_ent.get())
        month = chinese_solar_huangdi_month_ent.get()
        year = int(chinese_solar_huangdi_year_ent.get())
        jday = chinese_solar_huangdi.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def chinese_solar_yao_converter():
        day = int(chinese_solar_yao_day_ent.get())
        month = chinese_solar_yao_month_ent.get()
        year = int(chinese_solar_yao_year_ent.get())
        jday = chinese_solar_yao.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def chinese_solar_gonghe_converter():
        day = int(chinese_solar_gonghe_day_ent.get())
        month = chinese_solar_gonghe_month_ent.get()
        year = int(chinese_solar_gonghe_year_ent.get())
        jday = chinese_solar_gonghe.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def chinese_solar_qin_converter():
        day = int(chinese_solar_qin_day_ent.get())
        month = chinese_solar_qin_month_ent.get()
        year = int(chinese_solar_qin_year_ent.get())
        jday = chinese_solar_qin.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def chinese_solar_confucius_converter():
        day = int(chinese_solar_confucius_day_ent.get())
        month = chinese_solar_confucius_month_ent.get()
        year = int(chinese_solar_confucius_year_ent.get())
        jday = chinese_solar_confucius.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def zhou_converter():
        day = int(zhou_day_ent.get())
        month = zhou_month_ent.get()
        year = int(zhou_year_ent.get())
        jday = zhou.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def zhuanxu_converter():
        day = int(zhuanxu_day_ent.get())
        month = zhuanxu_month_ent.get()
        year = int(zhuanxu_year_ent.get())
        jday = zhuanxu.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def xia_converter():
        day = int(xia_day_ent.get())
        month = xia_month_ent.get()
        year = int(xia_year_ent.get())
        jday = xia.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def shang_converter():
        day = int(shang_day_ent.get())
        month = shang_month_ent.get()
        year = int(shang_year_ent.get())
        jday = shang.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def lu_converter():
        day = int(lu_day_ent.get())
        month = lu_month_ent.get()
        year = int(lu_year_ent.get())
        jday = lu.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def yin_converter():
        day = int(yin_day_ent.get())
        month = yin_month_ent.get()
        year = int(yin_year_ent.get())
        jday = yin.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def taichu_converter():
        day = int(taichu_day_ent.get())
        month = taichu_month_ent.get()
        year = int(taichu_year_ent.get())
        jday = taichu.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()


def santong_converter():
        day = int(santong_day_ent.get())
        month = santong_month_ent.get()
        year = int(santong_year_ent.get())
        jday = santong.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def sifen_converter():
        day = int(sifen_day_ent.get())
        month = sifen_month_ent.get()
        year = int(sifen_year_ent.get())
        jday = sifen.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def qianxiang_converter():
        day = int(qianxiang_day_ent.get())
        month = qianxiang_month_ent.get()
        year = int(qianxiang_year_ent.get())
        jday = qianxiang.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def jingchu_converter():
        day = int(jingchu_day_ent.get())
        month = jingchu_month_ent.get()
        year = int(jingchu_year_ent.get())
        jday = jingchu.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def sanji_converter():
        day = int(sanji_day_ent.get())
        month = sanji_month_ent.get()
        year = int(sanji_year_ent.get())
        jday = sanji.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def yuanjia_converter():
        day = int(yuanjia_day_ent.get())
        month = yuanjia_month_ent.get()
        year = int(yuanjia_year_ent.get())
        jday = yuanjia.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def xuanshi_converter():
        day = int(xuanshi_day_ent.get())
        month = xuanshi_month_ent.get()
        year = int(xuanshi_year_ent.get())
        jday = xuanshi.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def daming_converter():
        day = int(daming_day_ent.get())
        month = daming_month_ent.get()
        year = int(daming_year_ent.get())
        jday = daming.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def zhengguang_converter():
        day = int(zhengguang_day_ent.get())
        month = zhengguang_month_ent.get()
        year = int(zhengguang_year_ent.get())
        jday = zhengguang.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def xinghe_converter():
        day = int(xinghe_day_ent.get())
        month = xinghe_month_ent.get()
        year = int(xinghe_year_ent.get())
        jday = xinghe.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def tianbao_converter():
        day = int(tianbao_day_ent.get())
        month = tianbao_month_ent.get()
        year = int(tianbao_year_ent.get())
        jday = tianbao.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def tianhe_converter():
        day = int(tianhe_day_ent.get())
        month = tianhe_month_ent.get()
        year = int(tianhe_year_ent.get())
        jday = tianhe.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def daxiang_converter():
        day = int(daxiang_day_ent.get())
        month = daxiang_month_ent.get()
        year = int(daxiang_year_ent.get())
        jday = daxiang.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def kaihuang_converter():
        day = int(kaihuang_day_ent.get())
        month = kaihuang_month_ent.get()
        year = int(kaihuang_year_ent.get())
        jday = kaihuang.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def daye_converter():
        day = int(daye_day_ent.get())
        month = daye_month_ent.get()
        year = int(daye_year_ent.get())
        jday = daye.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def wuyin_converter():
        day = int(wuyin_day_ent.get())
        month = wuyin_month_ent.get()
        year = int(wuyin_year_ent.get())
        jday = wuyin.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def xuanming_converter():
        day = int(xuanming_day_ent.get())
        month = xuanming_month_ent.get()
        year = int(xuanming_year_ent.get())
        jday = xuanming.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def vietnamese_converter():
        day = int(vietnamese_day_ent.get())
        month = vietnamese_month_ent.get()
        year = int(vietnamese_year_ent.get())
        jday = vietnamese.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def korean_converter():
        day = int(korean_day_ent.get())
        month = korean_month_ent.get()
        year = int(korean_year_ent.get())
        jday = korean.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def dangun_converter():
        day = int(dangun_day_ent.get())
        month = dangun_month_ent.get()
        year = int(dangun_year_ent.get())
        jday = dangun.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def japanese_lunisolar_converter():
        day = int(japanese_lunisolar_day_ent.get())
        month = japanese_lunisolar_month_ent.get()
        year = int(japanese_lunisolar_year_ent.get())
        jday = japanese_lunisolar.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def japanese_converter():
        day = int(japanese_day_ent.get())
        month = japanese_month_ent.get()
        year = int(japanese_year_ent.get())
        jday = japanese.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def mongolian_converter():
        day = int(mongolian_day_ent.get())
        month = mongolian_month_ent.get()
        year = int(mongolian_year_ent.get())
        jday = mongolian.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def qadimi_yz_converter():
        day = int(qadimi_yz_day_ent.get())
        month = qadimi_yz_month_ent.get()
        year = int(qadimi_yz_year_ent.get())
        jday = qadimi_yz.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def qadimi_az_converter():
        day = int(qadimi_az_day_ent.get())
        month = qadimi_az_month_ent.get()
        year = int(qadimi_az_year_ent.get())
        jday = qadimi_az.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def qadimi_zre_converter():
        day = int(qadimi_zre_day_ent.get())
        month = qadimi_zre_month_ent.get()
        year = int(qadimi_zre_year_ent.get())
        jday = qadimi_zre.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def shenshai_yz_converter():
        day = int(shenshai_yz_day_ent.get())
        month = shenshai_yz_month_ent.get()
        year = int(shenshai_yz_year_ent.get())
        jday = shenshai_yz.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def shenshai_az_converter():
        day = int(shenshai_az_day_ent.get())
        month = shenshai_az_month_ent.get()
        year = int(shenshai_az_year_ent.get())
        jday = shenshai_az.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def shenshai_zre_converter():
        day = int(shenshai_zre_day_ent.get())
        month = shenshai_zre_month_ent.get()
        year = int(shenshai_zre_year_ent.get())
        jday = shenshai_zre.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def young_avestan_iran_yz_converter():
        day = int(young_avestan_iran_yz_day_ent.get())
        month = young_avestan_iran_yz_month_ent.get()
        year = int(young_avestan_iran_yz_year_ent.get())
        jday = young_avestan_iran_yz.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def young_avestan_iran_az_converter():
        day = int(young_avestan_iran_az_day_ent.get())
        month = young_avestan_iran_az_month_ent.get()
        year = int(young_avestan_iran_az_year_ent.get())
        jday = young_avestan_iran_az.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def young_avestan_iran_zre_converter():
        day = int(young_avestan_iran_zre_day_ent.get())
        month = young_avestan_iran_zre_month_ent.get()
        year = int(young_avestan_iran_zre_year_ent.get())
        jday = young_avestan_iran_zre.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def young_avestan_india_yz_converter():
        day = int(young_avestan_india_yz_day_ent.get())
        month = young_avestan_india_yz_month_ent.get()
        year = int(young_avestan_india_yz_year_ent.get())
        jday = young_avestan_india_yz.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def young_avestan_india_az_converter():
        day = int(young_avestan_india_az_day_ent.get())
        month = young_avestan_india_az_month_ent.get()
        year = int(young_avestan_india_az_year_ent.get())
        jday = young_avestan_india_az.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def young_avestan_india_zre_converter():
        day = int(young_avestan_india_zre_day_ent.get())
        month = young_avestan_india_zre_month_ent.get()
        year = int(young_avestan_india_zre_year_ent.get())
        jday = young_avestan_india_zre.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def shahanshahi_yz_converter():
        day = int(shahanshahi_yz_day_ent.get())
        month = shahanshahi_yz_month_ent.get()
        year = int(shahanshahi_yz_year_ent.get())
        jday = shahanshahi_yz.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def shahanshahi_az_converter():
        day = int(shahanshahi_az_day_ent.get())
        month = shahanshahi_az_month_ent.get()
        year = int(shahanshahi_az_year_ent.get())
        jday = shahanshahi_az.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def shahanshahi_zre_converter():
        day = int(shahanshahi_zre_day_ent.get())
        month = shahanshahi_zre_month_ent.get()
        year = int(shahanshahi_zre_year_ent.get())
        jday = shahanshahi_zre.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def old_avestan_yz_converter():
        day = int(old_avestan_yz_day_ent.get())
        month = old_avestan_yz_month_ent.get()
        year = int(old_avestan_yz_year_ent.get())
        jday = old_avestan_yz.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def old_avestan_az_converter():
        day = int(old_avestan_az_day_ent.get())
        month = old_avestan_az_month_ent.get()
        year = int(old_avestan_az_year_ent.get())
        jday = old_avestan_az.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def old_avestan_zre_converter():
        day = int(old_avestan_zre_day_ent.get())
        month = old_avestan_zre_month_ent.get()
        year = int(old_avestan_zre_year_ent.get())
        jday = old_avestan_zre.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def fasli_yz_converter():
        day = int(fasli_yz_day_ent.get())
        month = fasli_yz_month_ent.get()
        year = int(fasli_yz_year_ent.get())
        jday = fasli_yz.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def fasli_az_converter():
        day = int(fasli_az_day_ent.get())
        month = fasli_az_month_ent.get()
        year = int(fasli_az_year_ent.get())
        jday = fasli_az.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def fasli_zre_converter():
        day = int(fasli_zre_day_ent.get())
        month = fasli_zre_month_ent.get()
        year = int(fasli_zre_year_ent.get())
        jday = fasli_zre.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def sogdian_converter():
        day = int(sogdian_day_ent.get())
        month = sogdian_month_ent.get()
        year = int(sogdian_year_ent.get())
        jday = sogdian.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def indian_converter():
        day = int(indian_day_ent.get())
        month = indian_month_ent.get()
        year = int(indian_year_ent.get())
        jday = indian.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def mandaean_converter():
        day = int(mandaean_day_ent.get())
        month = mandaean_month_ent.get()
        year = int(mandaean_year_ent.get())
        jday = mandaean.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def bahai_sid_converter():
        day = int(bahai_sid_day_ent.get())
        month = bahai_sid_month_ent.get()
        year = int(bahai_sid_year_ent.get())
        jday = bahai_sid.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def sothic_converter():
        day = int(sothic_day_ent.get())
        month = sothic_month_ent.get()
        year = int(sothic_year_ent.get())
        jday = sothic.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def madhyama_solar_ky_converter():
        day = int(madhyama_solar_ky_day_ent.get())
        month = madhyama_solar_ky_month_ent.get()
        year = int(madhyama_solar_ky_year_ent.get())
        jday = madhyama_solar_ky.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def madhyama_solar_vs_converter():
        day = int(madhyama_solar_vs_day_ent.get())
        month = madhyama_solar_vs_month_ent.get()
        year = int(madhyama_solar_vs_year_ent.get())
        jday = madhyama_solar_vs.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def madhyama_solar_se_converter():
        day = int(madhyama_solar_se_day_ent.get())
        month = madhyama_solar_se_month_ent.get()
        year = int(madhyama_solar_se_year_ent.get())
        jday = madhyama_solar_se.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def tamil_converter():
        day = int(tamil_day_ent.get())
        month = tamil_month_ent.get()
        year = int(tamil_year_ent.get())
        jday = tamil.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def madhyama_lunar_ky_converter():
        day = int(madhyama_lunar_ky_day_ent.get())
        month = madhyama_lunar_ky_month_ent.get()
        year = int(madhyama_lunar_ky_year_ent.get())
        jday = madhyama_lunar_ky.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def madhyama_lunar_vs_converter():
        day = int(madhyama_lunar_vs_day_ent.get())
        month = madhyama_lunar_vs_month_ent.get()
        year = int(madhyama_lunar_vs_year_ent.get())
        jday = madhyama_lunar_vs.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def madhyama_lunar_se_converter():
        day = int(madhyama_lunar_se_day_ent.get())
        month = madhyama_lunar_se_month_ent.get()
        year = int(madhyama_lunar_se_year_ent.get())
        jday = madhyama_lunar_se.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def sid_bengali_converter():
        day = int(sid_bengali_day_ent.get())
        month = sid_bengali_month_ent.get()
        year = int(sid_bengali_year_ent.get())
        jday = sid_bengali.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def obs_bengali_converter():
        day = int(obs_bengali_day_ent.get())
        month = obs_bengali_month_ent.get()
        year = int(obs_bengali_year_ent.get())
        jday = obs_bengali.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def siddhantic_solar_ky_converter():
        day = int(siddhantic_solar_ky_day_ent.get())
        month = siddhantic_solar_ky_month_ent.get()
        year = int(siddhantic_solar_ky_year_ent.get())
        jday = siddhantic_solar_ky.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def siddhantic_solar_se_converter():
        day = int(siddhantic_solar_se_day_ent.get())
        month = siddhantic_solar_se_month_ent.get()
        year = int(siddhantic_solar_se_year_ent.get())
        jday = siddhantic_solar_se.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def siddhantic_solar_vs_converter():
        day = int(siddhantic_solar_vs_day_ent.get())
        month = siddhantic_solar_vs_month_ent.get()
        year = int(siddhantic_solar_vs_year_ent.get())
        jday = siddhantic_solar_vs.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def sid_tripuri_converter():
        day = int(sid_tripuri_day_ent.get())
        month = sid_tripuri_month_ent.get()
        year = int(sid_tripuri_year_ent.get())
        jday = sid_tripuri.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def trop_tripuri_converter():
        day = int(trop_tripuri_day_ent.get())
        month = trop_tripuri_month_ent.get()
        year = int(trop_tripuri_year_ent.get())
        jday = trop_tripuri.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def siddhantic_lunisolar_ky_converter():
        day = int(siddhantic_lunisolar_ky_day_ent.get())
        month = siddhantic_lunisolar_ky_month_ent.get()
        year = int(siddhantic_lunisolar_ky_year_ent.get())
        jday = siddhantic_lunisolar_ky.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def siddhantic_lunisolar_se_converter():
        day = int(siddhantic_lunisolar_se_day_ent.get())
        month = siddhantic_lunisolar_se_month_ent.get()
        year = int(siddhantic_lunisolar_se_year_ent.get())
        jday = siddhantic_lunisolar_se.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def siddhantic_lunisolar_vs_converter():
        day = int(siddhantic_lunisolar_vs_day_ent.get())
        month = siddhantic_lunisolar_vs_month_ent.get()
        year = int(siddhantic_lunisolar_vs_year_ent.get())
        jday = siddhantic_lunisolar_vs.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def obs_indian_solar_ky_converter():
        day = int(obs_indian_solar_ky_day_ent.get())
        month = obs_indian_solar_ky_month_ent.get()
        year = int(obs_indian_solar_ky_year_ent.get())
        jday = obs_indian_solar_ky.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def obs_indian_solar_se_converter():
        day = int(obs_indian_solar_se_day_ent.get())
        month = obs_indian_solar_se_month_ent.get()
        year = int(obs_indian_solar_se_year_ent.get())
        jday = obs_indian_solar_se.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def obs_indian_solar_vs_converter():
        day = int(obs_indian_solar_vs_day_ent.get())
        month = obs_indian_solar_vs_month_ent.get()
        year = int(obs_indian_solar_vs_year_ent.get())
        jday = obs_indian_solar_vs.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def obs_indian_lunisolar_ky_converter():
        day = int(obs_indian_lunisolar_ky_day_ent.get())
        month = obs_indian_lunisolar_ky_month_ent.get()
        year = int(obs_indian_lunisolar_ky_year_ent.get())
        jday = obs_indian_lunisolar_ky.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def obs_indian_lunisolar_se_converter():
        day = int(obs_indian_lunisolar_se_day_ent.get())
        month = obs_indian_lunisolar_se_month_ent.get()
        year = int(obs_indian_lunisolar_se_year_ent.get())
        jday = obs_indian_lunisolar_se.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def obs_indian_lunisolar_vs_converter():
        day = int(obs_indian_lunisolar_vs_day_ent.get())
        month = obs_indian_lunisolar_vs_month_ent.get()
        year = int(obs_indian_lunisolar_vs_year_ent.get())
        jday = obs_indian_lunisolar_vs.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def mughal_converter():
        day = int(mughal_day_ent.get())
        month = mughal_month_ent.get()
        year = int(mughal_year_ent.get())
        jday = mughal.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def sid_malayam_converter():
        day = int(sid_malayam_day_ent.get())
        month = sid_malayam_month_ent.get()
        year = int(sid_malayam_year_ent.get())
        jday = sid_malayam.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def obs_malayam_converter():
        day = int(obs_malayam_day_ent.get())
        month = obs_malayam_month_ent.get()
        year = int(obs_malayam_year_ent.get())
        jday = obs_malayam.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def alt_malayam_converter():
        day = int(alt_malayam_day_ent.get())
        month = alt_malayam_month_ent.get()
        year = int(alt_malayam_year_ent.get())
        jday = alt_malayam.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def bangladeshi1373_converter():
        day = int(bangladeshi1373_day_ent.get())
        month = bangladeshi1373_month_ent.get()
        year = int(bangladeshi1373_year_ent.get())
        jday = bangladeshi1373.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def bangladeshi1426_converter():
        day = int(bangladeshi1426_day_ent.get())
        month = bangladeshi1426_month_ent.get()
        year = int(bangladeshi1426_year_ent.get())
        jday = bangladeshi1426.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def odia_converter():
        day = int(odia_day_ent.get())
        month = odia_month_ent.get()
        year = int(odia_year_ent.get())
        jday = odia.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def trop_indian_solar_converter():
        day = int(trop_indian_solar_day_ent.get())
        month = trop_indian_solar_month_ent.get()
        year = int(trop_indian_solar_year_ent.get())
        jday = trop_indian_solar.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def trop_indian_lunisolar_converter():
        day = int(trop_indian_lunisolar_day_ent.get())
        month = trop_indian_lunisolar_month_ent.get()
        year = int(trop_indian_lunisolar_year_ent.get())
        jday = trop_indian_lunisolar.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def jalgaon_converter():
        day = int(jalgaon_day_ent.get())
        month = jalgaon_month_ent.get()
        year = int(jalgaon_year_ent.get())
        jday = jalgaon.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def manipuri_converter():
        day = int(manipuri_day_ent.get())
        month = manipuri_month_ent.get()
        year = int(manipuri_year_ent.get())
        jday = manipuri.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def gujarat_converter():
        day = int(gujarat_day_ent.get())
        month = gujarat_month_ent.get()
        year = int(gujarat_year_ent.get())
        jday = gujarat.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def kutch_converter():
        day = int(kutch_day_ent.get())
        month = kutch_month_ent.get()
        year = int(kutch_year_ent.get())
        jday = kutch.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def sid_purnimanta_converter():
        day = int(sid_purnimanta_day_ent.get())
        month = sid_purnimanta_month_ent.get()
        year = int(sid_purnimanta_year_ent.get())
        jday = sid_purnimanta.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def obs_purnimanta_converter():
        day = int(obs_purnimanta_day_ent.get())
        month = obs_purnimanta_month_ent.get()
        year = int(obs_purnimanta_year_ent.get())
        jday = obs_purnimanta.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def mool_nanakshahi_converter():
        day = int(mool_nanakshahi_day_ent.get())
        month = mool_nanakshahi_month_ent.get()
        year = int(mool_nanakshahi_year_ent.get())
        jday = mool_nanakshahi.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def sid_nanakshahi_converter():
        day = int(sid_nanakshahi_day_ent.get())
        month = sid_nanakshahi_month_ent.get()
        year = int(sid_nanakshahi_year_ent.get())
        jday = sid_nanakshahi.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def jain_shvetambara_converter():
        day = int(jain_shvetambara_day_ent.get())
        month = jain_shvetambara_month_ent.get()
        year = int(jain_shvetambara_year_ent.get())
        jday = jain_shvetambara.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def jain_digambaras_converter():
        day = int(jain_digambaras_day_ent.get())
        month = jain_digambaras_month_ent.get()
        year = int(jain_digambaras_year_ent.get())
        jday = jain_digambaras.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def vj_converter():
        day = int(vj_day_ent.get())
        month = vj_month_ent.get()
        year = int(vj_year_ent.get())
        jday = vj.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def newar_converter():
        day = int(newar_day_ent.get())
        month = newar_month_ent.get()
        year = int(newar_year_ent.get())
        jday = newar.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def nepali_solar_converter():
        day = int(nepali_solar_day_ent.get())
        month = nepali_solar_month_ent.get()
        year = int(nepali_solar_year_ent.get())
        jday = nepali_solar.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def karana_converter():
        day = int(karana_day_ent.get())
        month = karana_month_ent.get()
        year = int(karana_year_ent.get())
        jday = karana.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def phugpa_converter():
        day = int(phugpa_day_ent.get())
        month = phugpa_month_ent.get()
        year = int(phugpa_year_ent.get())
        jday = phugpa.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def tsurphu_converter():
        day = int(tsurphu_day_ent.get())
        month = tsurphu_month_ent.get()
        year = int(tsurphu_year_ent.get())
        jday = tsurphu.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def mongolian_converter():
        day = int(mongolian_day_ent.get())
        month = mongolian_month_ent.get()
        year = int(mongolian_year_ent.get())
        jday = mongolian.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def bhutanese_converter():
        day = int(bhutanese_day_ent.get())
        month = bhutanese_month_ent.get()
        year = int(bhutanese_year_ent.get())
        jday = bhutanese.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def yellow_converter():
        day = int(yellow_day_ent.get())
        month = yellow_month_ent.get()
        year = int(yellow_year_ent.get())
        jday = yellow.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def sherab_ling_converter():
        day = int(sherab_ling_day_ent.get())
        month = sherab_ling_month_ent.get()
        year = int(sherab_ling_year_ent.get())
        jday = sherab_ling.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def sarnath_converter():
        day = int(sarnath_day_ent.get())
        month = sarnath_month_ent.get()
        year = int(sarnath_year_ent.get())
        jday = sarnath.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()


root = Tk()

container = Frame(root, width = 1920, height = 1080)
container.pack(expand = True, fill = BOTH)
canvas = Canvas(container, width = 1900, height = 1080)
scrollbar = Scrollbar(container)                      

canvas.pack(side = LEFT, expand = True, fill = BOTH)
scrollbar.pack(side = RIGHT, fill = Y)
scrollbar.configure(command = canvas.yview)
frame = Frame(canvas)
frame.grid()
frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
                scrollregion = canvas.bbox("all")
        )
)

canvas.create_window((0,0), window = frame, anchor = "nw")
canvas.configure(yscrollcommand = scrollbar.set)



# Consecutive Julian day widget
cons_day_julian_lbl = Label(frame, text = "Chronological Julian day").grid(row = 0, column = 0, columnspan = 1, sticky = W)
#cons_day_julian_desc_lbl = Label(frame, text = "Day").grid(row = 2, column = 0, columnspan = 3, sticky = W)
cons_day_julian_ent = Entry(frame)
cons_day_julian_ent.grid(row = 1, column = 0, sticky = W)
cons_day_julian_bttn = Button(frame, text = "Calculate", command = cons_day_julian_todate).grid(row = 2, column = 0, columnspan = 1, sticky = W)

# Plus and Minus buttons
#cons_day_julian_plus_bttn = Button(frame, text = "+", command = cons_day_julian_plus).grid(row = 2, column = 1, sticky = W)
#cons_day_julian_minus_bttn = Button(frame, text = "-", command = cons_day_julian_minus).grid(row = 3, column = 1, sticky = W)

# True Julian Day
day_julian_lbl = Label(frame, text = "True Julian Day").grid(row = 0, column = 1, sticky = W)
day_julian_ent = Entry(frame)
day_julian_ent.grid(row = 1, column = 1, sticky = W)
day_julian_bttn = Button(frame, text = "Calculate", command = true_day_julian_converter).grid(row = 2, column = 1, sticky = W)

# Reduced Julian Day
red_day_julian_lbl = Label(frame, text = "Reduced Julian Day").grid(row = 0, column = 2, sticky = W)
red_day_julian_ent = Entry(frame)
red_day_julian_ent.grid(row = 1, column = 2, sticky = W)
red_day_julian_bttn = Button(frame, text = "Calculate", command = red_day_julian_converter).grid(row = 2, column = 2, sticky = W)

# Modified Julian Day
mod_day_julian_lbl = Label(frame, text = "Modified Julian Day").grid(row = 0, column = 3, sticky = W)
mod_day_julian_ent = Entry(frame)
mod_day_julian_ent.grid(row = 1, column = 3, sticky = W)
mod_day_julian_bttn = Button(frame, text = "Calculate", command = mod_day_julian_converter).grid(row = 2, column = 3, sticky = W)

# Truncated Julian Day                                                                                      
trun_day_julian_lbl = Label(frame, text = "Truncated Julian Day").grid(row = 0, column = 4, sticky = W)
trun_day_julian_ent = Entry(frame)
trun_day_julian_ent.grid(row = 1, column = 4, sticky = W)
trun_day_julian_bttn = Button(frame, text = "Calculate", command = trun_day_julian_converter).grid(row = 2, column = 4, sticky = W)

# Dublin Julian Day                                                                                         
dub_day_julian_lbl = Label(frame, text = "Dublin Julian Day").grid(row = 0, column = 5, sticky = W)
dub_day_julian_ent = Entry(frame)
dub_day_julian_ent.grid(row = 1, column = 5, sticky = W)
dub_day_julian_bttn = Button(frame, text = "Calculate", command = dub_day_julian_converter).grid(row = 2, column = 5, sticky = W)

# CNES Julian Day                                                                                           
cnes_lbl = Label(frame, text = "CNES Julian Day").grid(row = 0, column = 6, sticky = W)
cnes_ent = Entry(frame)
cnes_ent.grid(row = 1, column = 6, sticky = W)
cnes_bttn = Button(frame, text = "Calculate", command = cnes_converter).grid(row = 2, column = 6, sticky = W)

# CCSDS Julian Day                                                                                       
ccsds_lbl = Label(frame, text = "CCSDS Julian Day").grid(row = 0, column = 7, sticky = W)
ccsds_ent = Entry(frame)
ccsds_ent.grid(row = 1, column = 7, sticky = W)
ccsds_bttn = Button(frame, text = "Calculate", command = ccsds_converter).grid(row = 2, column = 7, sticky = W)

# Lilian Day                                                                                           
day_lilian_lbl = Label(frame, text = "Lilian Day").grid(row = 0, column = 8, sticky = W)
day_lilian_ent = Entry(frame)
day_lilian_ent.grid(row = 1, column = 8, sticky = W)
day_lilian_bttn = Button(frame, text = "Calculate", command = day_lilian_converter).grid(row = 2, column = 8, sticky = W)

# Rata Die
rata_die_lbl = Label(frame, text = "Rata Die").grid(row = 0, column = 9, sticky = W)
rata_die_ent = Entry(frame)
rata_die_ent.grid(row = 1, column = 9, sticky = W)
rata_die_bttn = Button(frame, text = "Calculate", command = rata_die_converter).grid(row = 2, column = 9, sticky = W)

# LOP day
lop_lbl = Label(frame, text = "LOP Julian day").grid(row = 0, column = 10, sticky = W)
lop_ent = Entry(frame)
lop_ent.grid(row = 1, column = 10, sticky = W)
lop_bttn = Button(frame, text = "Calculate", command = lop_converter).grid(row = 2, column = 10, sticky = W)

# Unix time
unix_time_lbl = Label(frame, text = "Unix time").grid(row = 0, column = 11, sticky = W)
unix_time_ent = Entry(frame)
unix_time_ent.grid(row = 1, column = 11, sticky = W)
unix_time_bttn = Button(frame, text = "Calculate", command = unix_time_converter).grid(row = 2, column = 11, sticky = W)

# VMS time
vms_time_lbl = Label(frame, text = "VMS time").grid(row = 0, column = 12, sticky = W)
vms_time_ent = Entry(frame)
vms_time_ent.grid(row = 1, column = 12, sticky = W)
vms_time_bttn = Button(frame, text = "Calculate", command = vms_time_converter).grid(row = 2, column = 12, sticky = W)

# Julian Calendar
julian_lbl = Label(frame, text = "Julian Calendar").grid(row = 4, column = 0, columnspan = 3, sticky = W)
julian_day_lbl = Label(frame, text = "Day").grid(row = 5, column = 0, columnspan = 3, sticky = W)
julian_day_ent = Entry(frame)
julian_day_ent.grid(row = 6, column = 0, sticky = W)
julian_month_lbl = Label(frame, text = "Month").grid(row = 5, column = 1, sticky = W)
julian_month_ent = Entry(frame)
julian_month_ent.grid(row = 6, column = 1, sticky = W)
julian_year_lbl = Label(frame, text = "Year").grid(row = 5, column = 2, sticky = W)
julian_year_ent = Entry(frame)
julian_year_ent.grid(row = 6, column = 2, sticky = W)
julian_bttn = Button(frame, text = "Calculate", command = julian_converter).grid(row = 7, column = 0, columnspan = 3, sticky = W)

# Amazigh calendar
amazigh_lbl = Label(frame, text = "Amazigh calendar").grid(row = 4, column = 3, columnspan = 3, sticky = W)
amazigh_day_lbl = Label(frame, text = "Day").grid(row = 5, column = 3, sticky = W)
amazigh_day_ent = Entry(frame)
amazigh_day_ent.grid(row = 6, column = 3, sticky = W)
amazigh_month_lbl = Label(frame, text = "Month").grid(row = 5, column = 4, sticky = W)
amazigh_month_ent = Entry(frame)
amazigh_month_ent.grid(row = 6, column = 4, sticky = W)
amazigh_year_lbl = Label(frame, text = "Year").grid(row = 5, column = 5, sticky = W)
amazigh_year_ent = Entry(frame)
amazigh_year_ent.grid(row = 6, column = 5, sticky = W)
amazigh_bttn = Button(frame, text = "Calculate", command = amazigh_converter).grid(row = 7, column = 3, sticky = W)

# Rumi calendar                                                                                            
rumi_lbl = Label(frame, text = "Ottoman fiscal calendar").grid(row = 4, column = 6, columnspan = 3, sticky = W)
rumi_day_lbl = Label(frame, text = "Day").grid(row = 5, column = 6, sticky = W)
rumi_day_ent = Entry(frame)
rumi_day_ent.grid(row = 6, column = 6, sticky = W)
rumi_month_lbl = Label(frame, text = "Month").grid(row = 5, column = 7, sticky = W)
rumi_month_ent = Entry(frame)
rumi_month_ent.grid(row = 6, column = 7, sticky = W)
rumi_year_lbl = Label(frame, text = "Year").grid(row = 5, column = 8, sticky = W)
rumi_year_ent = Entry(frame)
rumi_year_ent.grid(row = 6, column = 8, sticky = W)
rumi_bttn = Button(frame, text = "Calculate", command = rumi_converter).grid(row = 7, column = 6, columnspan = 3, sticky = W)

# Gregorian Calendar
gregorian_lbl = Label(frame, text = "Gregorian Calendar").grid(row = 8, column = 0, columnspan = 3, sticky = W)
gregorian_day_lbl = Label(frame, text = "Day").grid(row = 9, column = 0, sticky = W)
gregorian_day_ent = Entry(frame)
gregorian_day_ent.grid(row = 10, column = 0, sticky = W)
gregorian_month_lbl = Label(frame, text = "Month").grid(row = 9, column = 1, sticky = W)
gregorian_month_ent = Entry(frame)
gregorian_month_ent.grid(row = 10, column = 1, sticky = W)
gregorian_year_lbl= Label(frame, text = "Year").grid(row = 9, column = 2, sticky = W)
gregorian_year_ent = Entry(frame)
gregorian_year_ent.grid(row = 10, column = 2, sticky = W)
gregorian_bttn = Button(frame, text = "Calculate", command = gregorian_converter).grid(row = 11, column = 0, columnspan = 3, sticky = W)

# Astronomical Gregorian calendar
ast_gregorian_lbl = Label(frame, text = "Astronomical Gregorian calendar").grid(row = 8, column = 3, columnspan = 3, sticky = W)
ast_gregorian_day_lbl = Label(frame, text = "Day").grid(row = 9, column = 3, sticky = W)
ast_gregorian_day_ent = Entry(frame)
ast_gregorian_day_ent.grid(row = 10, column = 3, sticky = W)
ast_gregorian_month_lbl = Label(frame, text = "Month").grid(row = 9, column = 4, sticky = W)
ast_gregorian_month_ent = Entry(frame)
ast_gregorian_month_ent.grid(row = 10, column = 4, sticky = W)
ast_gregorian_year_lbl = Label(frame, text = "Year").grid(row = 9, column = 5, sticky = W)
ast_gregorian_year_ent = Entry(frame)
ast_gregorian_year_ent.grid(row = 10, column = 5, sticky = W)
ast_gregorian_bttn = Button(frame, text = "Calculate", command = ast_gregorian_converter).grid(row = 11, column = 3, columnspan = 3, sticky = W)

# Revised Gregorian calendar
rev_gregorian_lbl = Label(frame, text = "Revised Gregorian calendar").grid(row = 8, column = 6, columnspan = 3, sticky = W)
rev_gregorian_day_lbl = Label(frame, text = "Day").grid(row = 9, column = 6, sticky = W)
rev_gregorian_day_ent = Entry(frame)
rev_gregorian_day_ent.grid(row = 10, column = 6, sticky = W)
rev_gregorian_month_lbl = Label(frame, text = "Months").grid(row = 9, column = 7, sticky = W)
rev_gregorian_month_ent = Entry(frame)
rev_gregorian_month_ent.grid(row = 10, column = 7, sticky = W)
rev_gregorian_year_lbl = Label(frame, text = "Year").grid(row = 9, column = 8, sticky = W)
rev_gregorian_year_ent = Entry(frame)
rev_gregorian_year_ent.grid(row = 10, column = 8, sticky = W)
rev_gregorian_bttn = Button(frame, text = "Calculate", command = rev_gregorian_converter).grid(row = 11, column = 6, columnspan = 3, sticky = W)

# Juche calendar
juche_lbl = Label(frame, text = "Juche calendar").grid(row = 8, column = 9, columnspan = 3, sticky = W)
juche_day_lbl = Label(frame, text = "Day").grid(row = 9, column = 9, sticky = W)
juche_day_ent = Entry(frame)
juche_day_ent.grid(row = 10, column = 9, sticky = W)
juche_month_lbl = Label(frame, text = "Month").grid(row = 9, column = 10, sticky = W)
juche_month_ent = Entry(frame)
juche_month_ent.grid(row = 10, column = 10, sticky = W)
juche_year_lbl = Label(frame, text = "Year").grid(row = 9, column = 11, sticky = W)
juche_year_ent = Entry(frame)
juche_year_ent.grid(row = 10, column = 11, sticky = W)
juche_bttn = Button(frame, text = "Calculate", command = juche_converter).grid(row = 11, column = 9, columnspan = 3, sticky = W)

# Serbian church calendar
serbian_church_lbl = Label(frame, text = "Serbian church calendar").grid(row = 12, column = 0, columnspan = 3, sticky = W)
serbian_church_day_lbl = Label(frame, text = "Day").grid(row = 13, column = 0, sticky = W)
serbian_church_day_ent = Entry(frame)
serbian_church_day_ent.grid(row = 14, column = 0, sticky = W)
serbian_church_month_lbl = Label(frame, text = "Month").grid(row = 13, column = 1, sticky = W)
serbian_church_month_ent = Entry(frame)
serbian_church_month_ent.grid(row = 14, column = 1, sticky = W)
serbian_church_year_lbl = Label(frame, text = "Year").grid(row = 13, column = 2, sticky = W)
serbian_church_year_ent = Entry(frame)
serbian_church_year_ent.grid(row = 14, column = 2, sticky = W)
serbian_church_bttn = Button(frame, text = "Calculate", command = serbian_church_converter).grid(row = 15, column = 0, columnspan = 3, sticky = W)

# Revised Julian calendar
rev_julian_lbl = Label(frame, text = "Revised Julian calendar").grid(row = 12, column = 3, columnspan = 3, sticky = W)
rev_julian_day_lbl = Label(frame, text = "Day").grid(row = 13, column = 3, sticky = W)
rev_julian_day_ent = Entry(frame)
rev_julian_day_ent.grid(row = 14, column = 3, sticky = W)
rev_julian_month_lbl = Label(frame, text = "Month").grid(row = 13, column = 4, sticky = W)
rev_julian_month_ent = Entry(frame)
rev_julian_month_ent.grid(row = 14, column = 4, sticky = W)
rev_julian_year_lbl = Label(frame, text = "Year").grid(row = 13, column = 5, sticky = W)
rev_julian_year_ent = Entry(frame)
rev_julian_year_ent.grid(row = 14, column = 5, sticky = W)
rev_julian_bttn = Button(frame, text = "Calculate", command = rev_julian_converter).grid(row = 15, column = 3, sticky = W)

# Parker calendar
parker_lbl = Label(frame, text = "Parker calendar").grid(row = 12, column = 6, columnspan = 3, sticky = W)
parker_day_lbl = Label(frame, text = "Day").grid(row = 13, column = 6, sticky = W)
parker_day_ent = Entry(frame)
parker_day_ent.grid(row = 14, column = 6, sticky = W)
parker_month_lbl = Label(frame, text = "Month").grid(row = 13, column = 7, sticky = W)
parker_month_ent = Entry(frame)
parker_month_ent.grid(row = 14, column = 7, sticky = W)
parker_year_lbl = Label(frame, text = "Year").grid(row = 13, column = 8, sticky = W)
parker_year_ent = Entry(frame)
parker_year_ent.grid(row = 14, column = 8, sticky = W)
parker_bttn = Button(frame, text = "Calculate", command = parker_converter).grid(row = 15, column = 6, columnspan = 3, sticky = W)

# Goucher-Parker calendar
goucher_lbl = Label(frame, text = "Goucher-Parker calendar").grid(row = 12, column = 9, columnspan = 3, sticky = W)
goucher_day_lbl = Label(frame, text = "Day").grid(row = 13, column = 9, sticky = W)
goucher_day_ent = Entry(frame)
goucher_day_ent.grid(row = 14, column = 9, sticky = W)
goucher_month_lbl = Label(frame, text = "Month").grid(row = 13, column = 10, sticky = W)
goucher_month_ent = Entry(frame)
goucher_month_ent.grid(row = 14, column = 10, sticky = W)
goucher_year_lbl = Label(frame, text = "Year").grid(row = 13, column = 11, sticky = W)
goucher_year_ent = Entry(frame)
goucher_year_ent.grid(row = 14, column = 11, sticky = W)
goucher_bttn = Button(frame, text = "Calculate", command = goucher_converter).grid(row = 15, column = 9, columnspan = 3, sticky = W)

# Masonic calendar
lucis_lbl = Label(frame, text = "Anno Lucis (Craft Freemasonry)").grid(row = 16, column = 0, columnspan = 3, sticky = W)
lucis_day_lbl = Label(frame, text = "Day").grid(row = 17, column = 0, sticky = W)
lucis_day_ent = Entry(frame)
lucis_day_ent.grid(row = 18, column = 0, sticky = W)
lucis_month_lbl = Label(frame, text = "Month").grid(row = 17, column = 1, sticky = W)
lucis_month_ent = Entry(frame)
lucis_month_ent.grid(row = 18, column = 1, sticky = W)
lucis_year_lbl = Label(frame, text = "Year").grid(row = 17, column = 2, sticky = W)
lucis_year_ent = Entry(frame)
lucis_year_ent.grid(row = 18, column = 2, sticky = W)
lucis_bttn = Button(frame, text = "Calculate", command = lucis_converter).grid(row = 19, column = 0, columnspan = 3, sticky = W)

# Archmasonic calendar                                                                                            
inventionis_lbl = Label(frame, text = "Anno Inventionis (Royal Archmasons)").grid(row = 16, column = 3, columnspan = 3, sticky = W)
inventionis_day_lbl = Label(frame, text = "Day").grid(row = 17, column = 3, sticky = W)
inventionis_day_ent = Entry(frame)
inventionis_day_ent.grid(row = 18, column = 3, sticky = W)
inventionis_month_lbl = Label(frame, text = "Month").grid(row = 17, column = 4, sticky = W)
inventionis_month_ent = Entry(frame)
inventionis_month_ent.grid(row = 18, column = 4, sticky = W)
inventionis_year_lbl = Label(frame, text = "Year").grid(row = 17, column = 5, sticky = W)
inventionis_year_ent = Entry(frame)
inventionis_year_ent.grid(row = 18, column = 5, sticky = W)
inventionis_bttn = Button(frame, text = "Calculate", command = inventionis_converter).grid(row = 19, column = 3, columnspan = 3, sticky = W)

# Holocene era                                                                                             
holocene_lbl = Label(frame, text = "Holocene era").grid(row = 16, column = 6, columnspan = 3, sticky = W)
holocene_day_lbl = Label(frame, text = "Day").grid(row = 17, column = 6, sticky = W)
holocene_day_ent = Entry(frame)
holocene_day_ent.grid(row = 18, column = 6, sticky = W)
holocene_month_lbl = Label(frame, text = "Month").grid(row = 17, column = 7, sticky = W)
holocene_month_ent = Entry(frame)
holocene_month_ent.grid(row = 18, column = 7, sticky = W)
holocene_year_lbl = Label(frame, text = "Year").grid(row = 17, column = 8, sticky = W)
holocene_year_ent = Entry(frame)
holocene_year_ent.grid(row = 18, column = 8, sticky = W)
holocene_bttn = Button(frame, text = "Calculate", command = holocene_converter).grid(row = 19, column = 6, columnspan = 3, sticky = W)

# After Development of Agriculture
ada_lbl = Label(frame, text = "After Development of Agriculture").grid(row = 16, column = 9, columnspan = 3, sticky = W)
ada_day_lbl = Label(frame, text = "Day").grid(row = 17, column = 9, sticky = W)
ada_day_ent = Entry(frame)
ada_day_ent.grid(row = 18, column = 9, sticky = W)
ada_month_lbl = Label(frame, text = "Month").grid(row = 17, column = 10, sticky = W)
ada_month_ent = Entry(frame)
ada_month_ent.grid(row = 18, column = 10, sticky = W)
ada_year_lbl = Label(frame, text = "Year").grid(row = 17, column = 11, sticky = W)
ada_year_ent = Entry(frame)
ada_year_ent.grid(row = 18, column = 11, sticky = W)
ada_bttn = Button(frame, text = "Calculate", command = ada_converter).grid(row = 19, column = 9, columnspan = 3, sticky = W)

# Egyptian Calendar
egyptian_lbl = Label(frame, text = "Ancient Egyptian civil calendar").grid(row = 20, column = 0, columnspan = 3, sticky = W)
egyptian_day_lbl = Label(frame, text = "Day").grid(row = 21, column = 0, sticky = W)
egyptian_day_ent = Entry(frame)
egyptian_day_ent.grid(row = 22, column = 0, sticky = W)
egyptian_month_lbl = Label(frame, text = "Month").grid(row = 21, column = 1, sticky = W)
egyptian_month_ent = Entry(frame)
egyptian_month_ent.grid(row = 22, column = 1, sticky = W)
egyptian_year_lbl = Label(frame, text = "Year").grid(row = 21, column = 2, sticky = W)
egyptian_year_ent = Entry(frame)
egyptian_year_ent.grid(row = 22, column = 2, sticky = W)
egyptian_bttn = Button(frame, text = "Calculate", command = egyptian_converter).grid(row = 23, column = 0, columnspan = 3, sticky = W)

# Armenian Calendar
armenian_lbl = Label(frame, text = "Armenian Calendar").grid(row = 20, column = 3, columnspan = 3, sticky = W)
armenian_day_lbl = Label(frame, text = "Day").grid(row = 21, column = 3, sticky = W)
armenian_day_ent = Entry(frame)
armenian_day_ent.grid(row = 22, column = 3, sticky = W)
armenian_month_lbl = Label(frame, text = "Month").grid(row = 21, column = 4, sticky = W)
armenian_month_ent = Entry(frame)
armenian_month_ent.grid(row = 22, column = 4, sticky = W)
armenian_year_lbl = Label(frame, text = "Year").grid(row = 21, column = 5, sticky = W)
armenian_year_ent = Entry(frame)
armenian_year_ent.grid(row = 22, column = 5, sticky = W)
armenian_bttn = Button(frame, text = "Calculate", command = armenian_converter).grid(row = 23, column = 3, columnspan = 3, sticky = W)

# Coptic Calendar
coptic_lbl = Label(frame, text = "Coptic Calendar").grid(row = 20, column = 6, columnspan = 3, sticky = W)
coptic_day_lbl = Label(frame, text = "Day").grid(row = 21, column = 6, sticky = W)
coptic_day_ent = Entry(frame)
coptic_day_ent.grid(row = 22, column = 6, sticky = W)
coptic_month_lbl = Label(frame, text = "Month").grid(row = 21, column = 7, sticky = W)
coptic_month_ent = Entry(frame)
coptic_month_ent.grid(row = 22, column = 7, sticky = W)
coptic_year_lbl = Label(frame, text = "Year").grid(row = 21, column = 8, sticky = W)
coptic_year_ent = Entry(frame)
coptic_year_ent.grid(row = 22, column = 8, sticky = W)
coptic_bttn = Button(frame, text = "Calculate", command = coptic_converter).grid(row = 23, column = 6, columnspan = 3, sticky = W)

# Ethiopian Calendar
ethiopian_lbl = Label(frame, text = "Ethiopian Calendar").grid(row = 20, column = 9, columnspan = 3, sticky = W)
ethiopian_day_lbl = Label(frame, text = "Day").grid(row = 21, column = 9, sticky = W)
ethiopian_day_ent = Entry(frame)
ethiopian_day_ent.grid(row = 22, column = 9, sticky = W)
ethiopian_month_lbl = Label(frame, text = "Month").grid(row = 21, column = 10, sticky = W)
ethiopian_month_ent = Entry(frame)
ethiopian_month_ent.grid(row = 22, column = 10, sticky = W)
ethiopian_year_lbl = Label(frame, text = "Year").grid(row = 21, column = 11, sticky = W)
ethiopian_year_ent = Entry(frame)
ethiopian_year_ent.grid(row = 22, column = 11, sticky = W)
ethiopian_bttn = Button(frame, text = "Calculate", command = ethiopian_converter).grid(row = 23, column = 9, columnspan = 3, sticky = W)

# Lunar Hijri calendar                                                                                            
lunar_hijri_lbl = Label(frame, text = "Lunar Hijri (Islamic) calendar").grid(row = 24, column = 0, columnspan = 3, sticky = W)
lunar_hijri_day_lbl = Label(frame, text = "Day").grid(row = 25, column = 0, sticky = W)
lunar_hijri_day_ent = Entry(frame)
lunar_hijri_day_ent.grid(row = 26, column = 0, sticky = W)
lunar_hijri_month_lbl = Label(frame, text = "Month").grid(row = 25, column = 1, sticky = W)
lunar_hijri_month_ent = Entry(frame)
lunar_hijri_month_ent.grid(row = 26, column = 1, sticky = W)
lunar_hijri_year_lbl = Label(frame, text = "Year").grid(row = 25, column = 2, sticky = W)
lunar_hijri_year_ent = Entry(frame)
lunar_hijri_year_ent.grid(row = 26, column = 2, sticky = W)
lunar_hijri_bttn = Button(frame, text = "Calculate", command = lunar_hijri_converter).grid(row = 27, column = 0, columnspan = 3, sticky = W)

# Tabular Islamic Calendar
tab_islamic_lbl = Label(frame, text = "Tabular Islamic Calendar").grid(row = 24, column = 3, columnspan = 3, sticky = W)
tab_islamic_day_lbl = Label(frame, text = "Day").grid(row = 25, column = 3, sticky = W)
tab_islamic_day_ent = Entry(frame)
tab_islamic_day_ent.grid(row = 26, column = 3, sticky = W)
tab_islamic_month_lbl = Label(frame, text = "Month").grid(row = 25, column = 4, sticky = W)
tab_islamic_month_ent = Entry(frame)
tab_islamic_month_ent.grid(row = 26, column = 4, sticky = W)
tab_islamic_year_lbl = Label(frame, text = "Year").grid(row = 25, column = 5, sticky = W)
tab_islamic_year_ent = Entry(frame)
tab_islamic_year_ent.grid(row = 26, column = 5, sticky = W)
tab_islamic_bttn = Button(frame, text = "Calculate", command = tab_islamic_converter).grid(row = 27, column = 3, columnspan = 3, sticky = W)

# JAVANESE CALENDAR GOES HERE

# Pre-Islamic Arab calendar                                                                                            
arab_lbl = Label(frame, text = "Pre-Islamic Arab calendar").grid(row = 24, column = 9, columnspan = 3, sticky = W)
arab_day_lbl = Label(frame, text = "Day").grid(row = 25, column = 9, sticky = W)
arab_day_ent = Entry(frame)
arab_day_ent.grid(row = 26, column = 9, sticky = W)
arab_month_lbl = Label(frame, text = "Month").grid(row = 25, column = 10, sticky = W)
arab_month_ent = Entry(frame)
arab_month_ent.grid(row = 26, column = 10, sticky = W)
arab_year_lbl = Label(frame, text = "Year").grid(row = 25, column = 11, sticky = W)
arab_year_ent = Entry(frame)
arab_year_ent.grid(row = 26, column = 11, sticky = W)
arab_bttn = Button(frame, text = "Calculate", command = arab_converter).grid(row = 27, column = 9, columnspan = 3, sticky = W)





# Solar Hijri calendar                                                                                            
solar_hijri_lbl = Label(frame, text = "Solar Hijri calendar").grid(row = 36, column = 0, columnspan = 3, sticky = W)
solar_hijri_day_lbl = Label(frame, text = "Day").grid(row = 37, column = 0, sticky = W)
solar_hijri_day_ent = Entry(frame)
solar_hijri_day_ent.grid(row = 38, column = 0, sticky = W)
solar_hijri_month_lbl = Label(frame, text = "Month").grid(row = 37, column = 1, sticky = W)
solar_hijri_month_ent = Entry(frame)
solar_hijri_month_ent.grid(row = 38, column = 1, sticky = W)
solar_hijri_year_lbl = Label(frame, text = "Year").grid(row = 37, column = 2, sticky = W)
solar_hijri_year_ent = Entry(frame)
solar_hijri_year_ent.grid(row = 38, column = 2, sticky = W)
solar_hijri_bttn = Button(frame, text = "Calculate", command = solar_hijri_converter).grid(row = 39, column = 0, columnspan = 3, sticky = W)

# Jalali Calendar
jalali_lbl = Label(frame, text = "Jalali Calendar").grid(row = 36, column = 3, columnspan = 3, sticky = W)
jalali_day_lbl = Label(frame, text = "Day").grid(row = 37, column = 3, sticky = W)
jalali_day_ent = Entry(frame)
jalali_day_ent.grid(row = 38, column = 3, sticky = W)
jalali_month_lbl = Label(frame, text = "Month").grid(row = 37, column = 4, sticky = W)
jalali_month_ent = Entry(frame)
jalali_month_ent.grid(row = 38, column = 4, sticky = W)
jalali_year_lbl = Label(frame, text = "Year").grid(row = 37, column = 5, sticky = W)
jalali_year_ent = Entry(frame)
jalali_year_ent.grid(row = 38, column = 5, sticky = W)
jalali_bttn = Button(frame, text = "Calculate", command = jalali_converter).grid(row = 39, column = 3, columnspan = 3, sticky = W)

# Birashk's calendar
birashk_lbl = Label(frame, text = "Ahmad Birashk's Calendar").grid(row = 36, column = 6, columnspan = 3, sticky = W)
birashk_day_lbl = Label(frame, text = "Day").grid(row = 37, column = 6, sticky = W)
birashk_day_ent = Entry(frame)
birashk_day_ent.grid(row = 38, column = 6, sticky = W)
birashk_month_lbl = Label(frame, text = "Month").grid(row = 37, column = 7, sticky = W)
birashk_month_ent = Entry(frame)
birashk_month_ent.grid(row = 38, column = 7, sticky = W)
birashk_year_lbl = Label(frame, text = "Year").grid(row = 37, column = 8, sticky = W)
birashk_year_ent = Entry(frame)
birashk_year_ent.grid(row = 38, column = 8, sticky = W)
birashk_bttn = Button(frame, text = "Calculate", command = birashk_converter).grid(row = 39, column = 6, columnspan = 3, sticky = W)

# Kurdish Calendar
kurdish_lbl = Label(frame, text = "Kurdish Calendar").grid(row = 36, column = 9, columnspan = 3, sticky = W)
kurdish_day_lbl = Label(frame, text = "Day").grid(row = 37, column = 9, sticky = W)
kurdish_day_ent = Entry(frame)
kurdish_day_ent.grid(row = 38, column = 9, sticky = W)
kurdish_month_lbl = Label(frame, text = "Month").grid(row = 37, column = 10, sticky = W)
kurdish_month_ent = Entry(frame)
kurdish_month_ent.grid(row = 38, column = 10, sticky = W)
kurdish_year_lbl = Label(frame, text = "Year").grid(row = 37, column = 11, sticky = W)
kurdish_year_ent = Entry(frame)
kurdish_year_ent.grid(row = 38, column = 11, sticky = W)
kurdish_bttn = Button(frame, text = "Calculate", command = kurdish_converter).grid(row = 39, column = 9, columnspan = 3, sticky = W)

# Iranian national calendar                                                                                            
cyrus_lbl = Label(frame, text = "Iranian national calendar").grid(row = 40, column = 0, columnspan = 3, sticky = W)
cyrus_day_lbl = Label(frame, text = "Day").grid(row = 41, column = 0, sticky = W)
cyrus_day_ent = Entry(frame)
cyrus_day_ent.grid(row = 42, column = 0, sticky = W)
cyrus_month_lbl = Label(frame, text = "Month").grid(row = 41, column = 1, sticky = W)
cyrus_month_ent = Entry(frame)
cyrus_month_ent.grid(row = 42, column = 1, sticky = W)
cyrus_year_lbl = Label(frame, text = "Year").grid(row = 41, column = 2, sticky = W)
cyrus_year_ent = Entry(frame)
cyrus_year_ent.grid(row = 42, column = 2, sticky = W)
cyrus_bttn = Button(frame, text = "Calculate", command = cyrus_converter).grid(row = 43, column = 0, columnspan = 3, sticky = W)

# Assyrian calendar
assyrian_lbl = Label(frame, text = "Modern Assyrian Calendar").grid(row = 40, column = 3, columnspan = 3, sticky = W)
assyrian_day_lbl = Label(frame, text = "Day").grid(row = 41, column = 3, sticky = W)
assyrian_day_ent = Entry(frame)
assyrian_day_ent.grid(row = 42, column = 3, sticky = W)
assyrian_month_lbl = Label(frame, text = "Month").grid(row = 41, column = 4, sticky = W)
assyrian_month_ent = Entry(frame)
assyrian_month_ent.grid(row = 42, column = 4, sticky = W)
assyrian_year_lbl = Label(frame, text = "Year").grid(row = 41, column = 5, sticky = W)
assyrian_year_ent = Entry(frame)
assyrian_year_ent.grid(row = 42, column = 5, sticky = W)
assyrian_bttn = Button(frame, text = "Calculate", command = assyrian_converter).grid(row = 43, column = 3, columnspan = 3, sticky = W)

# Hebrew (Jewish) Calendar
jewish_lbl = Label(frame, text = "Jewish Hebrew Calendar").grid(row = 40, column = 6, columnspan = 3, sticky = W)
jewish_day_lbl = Label(frame, text = "Day").grid(row = 41, column = 6, sticky = W)
jewish_day_ent = Entry(frame)
jewish_day_ent.grid(row = 42, column = 6, sticky = W)
jewish_month_lbl = Label(frame, text = "Month").grid(row = 41, column = 7, sticky = W)
jewish_month_ent = Entry(frame)
jewish_month_ent.grid(row = 42, column = 7, sticky = W)
jewish_year_lbl = Label(frame, text = "Year").grid(row = 41, column = 8, sticky = W)
jewish_year_ent = Entry(frame)
jewish_year_ent.grid(row = 42, column = 8, sticky = W)
jewish_bttn = Button(frame, text = "Calculate", command = jewish_converter).grid(row = 43, column = 6, columnspan = 3, sticky = W)

# Samaritan Calendar
samaritan_lbl = Label(frame, text = "Samaritan Hebrew Calendar (estimated)").grid(row = 40, column = 9, columnspan = 3, sticky = W)
samaritan_day_lbl = Label(frame, text = "Day").grid(row = 41, column = 9, sticky = W)
samaritan_day_ent = Entry(frame)
samaritan_day_ent.grid(row = 42, column = 9, sticky = W)
samaritan_month_lbl = Label(frame, text = "Month").grid(row = 41, column = 10, sticky = W)
samaritan_month_ent = Entry(frame)
samaritan_month_ent.grid(row = 42, column = 10, sticky = W)
samaritan_year_lbl = Label(frame, text = "Year").grid(row = 41, column = 11, sticky = W)
samaritan_year_ent = Entry(frame)
samaritan_year_ent.grid(row = 42, column = 11, sticky = W)
samaritan_bttn = Button(frame, text = "Calculate", command = samaritan_converter).grid(row = 43, column = 9, columnspan = 3, sticky = W)

# Long Count
maya_lbl = Label(frame, text = "Mesoamerican Long Count").grid(row = 44, column = 0, columnspan = 5, sticky = W)
maya_piktun_lbl = Label(frame, text = "Piktun").grid(row = 45, column = 0, sticky = W)
maya_piktun_ent = Entry(frame)
maya_piktun_ent.grid(row = 46, column = 0, sticky = W)

maya_baktun_lbl = Label(frame, text = "B'ak'tun").grid(row = 45, column = 1, sticky = W)
maya_baktun_ent = Entry(frame)
maya_baktun_ent.grid(row = 46, column = 1, sticky =W)

maya_katun_lbl = Label(frame, text = "K'atun").grid(row = 45, column = 2, sticky = W)
maya_katun_ent = Entry(frame)
maya_katun_ent.grid(row = 46, column = 2, sticky = W)

maya_tun_lbl = Label(frame, text = "Tun").grid(row = 45, column = 3, sticky = W)
maya_tun_ent = Entry(frame)
maya_tun_ent.grid(row = 46, column = 3, sticky = W)

maya_uinal_lbl = Label(frame, text = "Uinal").grid(row = 45, column = 4, sticky = W)
maya_uinal_ent = Entry(frame)
maya_uinal_ent.grid(row = 46, column = 4, sticky = W)

maya_kin_lbl = Label(frame, text = "Kin").grid(row = 45, column = 5, sticky = W)
maya_kin_ent = Entry(frame)
maya_kin_ent.grid(row = 46, column = 5, sticky = W)

maya_bttn = Button(frame, text = "Calculate", command = maya_converter).grid(row = 47, column = 0, columnspan = 5, sticky = W)

# Roman calendar                                                                                            
roman_lbl = Label(frame, text = "Roman calendar").grid(row = 44, column = 6, columnspan = 3, sticky = W)
roman_day_lbl = Label(frame, text = "Day").grid(row = 45, column = 6, sticky = W)
roman_day_ent = Entry(frame)
roman_day_ent.grid(row = 46, column = 6, sticky = W)
roman_month_lbl = Label(frame, text = "Month").grid(row = 45, column = 7, sticky = W)
roman_month_ent = Entry(frame)
roman_month_ent.grid(row = 46, column = 7, sticky = W)
roman_year_lbl = Label(frame, text = "Year").grid(row = 45, column = 8, sticky = W)
roman_year_ent = Entry(frame)
roman_year_ent.grid(row = 46, column = 8, sticky = W)
roman_bttn = Button(frame, text = "Calculate", command = roman_converter).grid(row = 47, column = 6, columnspan = 3, sticky = W)

# Gangale sol
sol_gangale_lbl = Label(frame, text = "Consecutive Martian sol").grid(row = 44, column = 9, sticky = W)
sol_gangale_ent = Entry(frame)
sol_gangale_ent.grid(row = 46, column = 9, sticky = W)
sol_gangale_bttn = Button(frame, text = "Calculate", command = sol_gangale_converter).grid(row = 47, column = 9, sticky = W)

# Revised Georgian calendar
georgian_c_lbl = Label(frame, text = "Georgian calendar (Georgian era)").grid(row = 48, column = 0, columnspan = 3, sticky = W)
georgian_c_day_lbl = Label(frame, text = "Day").grid(row = 49, column = 0, sticky = W)
georgian_c_day_ent = Entry(frame)
georgian_c_day_ent.grid(row = 50, column = 0, sticky = W)
georgian_c_month_lbl = Label(frame, text = "Month").grid(row = 49, column = 1, sticky = W)
georgian_c_month_ent = Entry(frame)
georgian_c_month_ent.grid(row = 50, column = 1, sticky = W)
georgian_c_year_lbl = Label(frame, text = "Year").grid(row = 49, column = 2, sticky = W)
georgian_c_year_ent = Entry(frame)
georgian_c_year_ent.grid(row = 50, column = 2, sticky = W)
georgian_c_bttn = Button(frame, text = "Calculate", command = georgian_c_converter).grid(row = 51, column = 0, columnspan = 3, sticky = W)

# Original Georgian calendar
georgian_g_lbl = Label(frame, text = "Georgian calendar (Christian era)").grid(row = 48, column = 3, columnspan = 3, sticky = W)
georgian_g_day_lbl = Label(frame, text = "Day").grid(row = 49, column = 3, sticky = W)
georgian_g_day_ent = Entry(frame)
georgian_g_day_ent.grid(row = 50, column = 3, sticky = W)
georgian_g_month_lbl = Label(frame, text = "Month").grid(row = 49, column = 4, sticky = W)
georgian_g_month_ent = Entry(frame)
georgian_g_month_ent.grid(row = 50, column = 4, sticky = W)
georgian_g_year_lbl = Label(frame, text = "Year").grid(row = 49, column = 5, sticky = W)
georgian_g_year_ent = Entry(frame)
georgian_g_year_ent.grid(row = 50, column = 5, sticky = W)
georgian_g_bttn = Button(frame, text = "Calculate", command = georgian_g_converter).grid(row = 51, column = 3, columnspan = 3, sticky = W)

# World calendar
world_lbl = Label(frame, text = "World Calendar").grid(row = 48, column = 6, columnspan = 3, sticky = W)
world_day_lbl = Label(frame, text = "Day").grid(row = 49, column = 6, sticky = W)
world_day_ent = Entry(frame)
world_day_ent.grid(row = 50, column = 6, sticky = W)
world_month_lbl = Label(frame, text = "Month").grid(row = 49, column = 7, sticky = W)
world_month_ent = Entry(frame)
world_month_ent.grid(row = 50, column = 7, sticky = W)
world_year_lbl = Label(frame, text = "Year").grid(row = 49, column = 8, sticky = W)
world_year_ent = Entry(frame)
world_year_ent.grid(row = 50, column = 8, sticky = W)
world_bttn = Button(frame, text = "Calculate", command = world_converter).grid(row = 51, column = 6, columnspan = 3, sticky = W)

# International Fixed Calendar
ifc_lbl = Label(frame, text = "International Fixed Calendar").grid(row = 48, column = 9, columnspan = 3, sticky = W)
ifc_day_lbl = Label(frame, text = "Day").grid(row = 49, column = 9, sticky = W)
ifc_day_ent = Entry(frame)
ifc_day_ent.grid(row = 50, column = 9, sticky = W)
ifc_month_lbl = Label(frame, text = "Month").grid(row = 49, column = 10, sticky = W)
ifc_month_ent = Entry(frame)
ifc_month_ent.grid(row = 50, column = 10, sticky = W)
ifc_year_lbl = Label(frame, text = "Year").grid(row = 49, column = 11, sticky = W)
ifc_year_ent = Entry(frame)
ifc_year_ent.grid(row = 50, column = 11, sticky = W)
ifc_bttn = Button(frame, text = "Calculate", command = ifc_converter).grid(row = 51, column = 9, columnspan = 3, sticky = W)

# Gorman calendar
gorman_lbl = Label(frame, text = "Gorman calendar").grid(row = 52, column = 0, columnspan = 3, sticky = W)
gorman_day_lbl = Label(frame, text = "Day").grid(row = 53, column = 0, sticky = W)
gorman_day_ent = Entry(frame)
gorman_day_ent.grid(row = 54, column = 0, sticky = W)
gorman_month_lbl = Label(frame, text = "Month").grid(row = 53, column = 1, sticky = W)
gorman_month_ent = Entry(frame)
gorman_month_ent.grid(row = 54, column = 1, sticky = W)
gorman_year_lbl = Label(frame, text = "Year").grid(row = 53, column = 2, sticky = W)
gorman_year_ent = Entry(frame)
gorman_year_ent.grid(row = 54, column = 2, sticky = W)
gorman_bttn = Button(frame, text = "Calculate", command = gorman_converter).grid(row = 55, column = 0, columnspan = 3, sticky = W)

# Pax calendar
pax_lbl = Label(frame, text = "Pax calendar").grid(row = 52, column = 3, columnspan = 3, sticky = W)
pax_day_lbl = Label(frame, text = "Day").grid(row = 53, column = 3, sticky = W)
pax_day_ent = Entry(frame)
pax_day_ent.grid(row = 54, column = 3, sticky = W)
pax_month_lbl = Label(frame, text = "Month").grid(row = 53, column = 4, sticky = W)
pax_month_ent = Entry(frame)
pax_month_ent.grid(row = 54, column = 4, sticky = W)
pax_year_lbl = Label(frame, text = "Year").grid(row = 53, column = 5, sticky = W)
pax_year_ent = Entry(frame)
pax_year_ent.grid(row = 54, column = 5, sticky = W)
pax_bttn = Button(frame, text = "Calculate", command = pax_converter).grid(row = 55, column = 3, columnspan = 3, sticky = W)

# Pax 2020 calendar
pax2_lbl = Label(frame, text = "Pax 2020 calendar").grid(row = 52, column = 6, columnspan = 3, sticky = W)
pax2_day_lbl = Label(frame, text = "Day").grid(row = 53, column = 6, sticky = W)
pax2_day_ent = Entry(frame)
pax2_day_ent.grid(row = 54, column = 6, sticky = W)
pax2_month_lbl = Label(frame, text = "Month").grid(row = 53, column = 7, sticky = W)
pax2_month_ent = Entry(frame)
pax2_month_ent.grid(row = 54, column = 7, sticky = W)
pax2_year_lbl = Label(frame, text = "Year").grid(row = 53, column = 8, sticky = W)
pax2_year_ent = Entry(frame)
pax2_year_ent.grid(row = 54, column = 8, sticky = W)
pax2_bttn = Button(frame, text = "Calculate", command = pax2_converter).grid(row = 55, column = 6, columnspan = 3, sticky = W)

# Positivist calendar
positivist_lbl = Label(frame, text = "Positivist calendar").grid(row = 52, column = 9, columnspan = 3, sticky = W)
positivist_day_lbl = Label(frame, text = "Day").grid(row = 53, column = 9, sticky = W)
positivist_day_ent = Entry(frame)
positivist_day_ent.grid(row = 54, column = 9, sticky = W)
positivist_month_lbl = Label(frame, text = "Month").grid(row = 53, column = 10, sticky = W)
positivist_month_ent = Entry(frame)
positivist_month_ent.grid(row = 54, column = 10, sticky = W)
positivist_year_lbl = Label(frame, text = "Year").grid(row = 53, column = 11, sticky = W)
positivist_year_ent = Entry(frame)
positivist_year_ent.grid(row = 54, column = 11, sticky = W)
positivist_bttn = Button(frame, text = "Calculate", command = positivist_converter).grid(row = 55, column = 9, columnspan = 3, sticky = W)

# Nex calendar
nex_lbl = Label(frame, text = "Nex calendar").grid(row = 56, column = 0, columnspan = 3, sticky = W)
nex_day_lbl = Label(frame, text = "Day").grid(row = 57, column = 0, sticky = W)
nex_day_ent = Entry(frame)
nex_day_ent.grid(row = 58, column = 0, sticky = W)
nex_month_lbl = Label(frame, text = "Month").grid(row = 57, column = 1, sticky = W)
nex_month_ent = Entry(frame)
nex_month_ent.grid(row = 58, column = 1, sticky = W)
nex_year_lbl = Label(frame, text = "Year").grid(row = 57, column = 2, sticky = W)
nex_year_ent = Entry(frame)
nex_year_ent.grid(row = 58, column = 2, sticky = W)
nex_bttn = Button(frame, text = "Calculate", command = nex_converter).grid(row = 59, column = 0, columnspan = 3, sticky = W)

# Thellid calendar                                                                                            
thellid_lbl = Label(frame, text = "Thellid calendar").grid(row = 56, column = 3, columnspan = 3, sticky = W)
thellid_day_lbl = Label(frame, text = "Day").grid(row = 57, column = 3, sticky = W)
thellid_day_ent = Entry(frame)
thellid_day_ent.grid(row = 58, column = 3, sticky = W)
thellid_month_lbl = Label(frame, text = "Month").grid(row = 57, column = 4, sticky = W)
thellid_month_ent = Entry(frame)
thellid_month_ent.grid(row = 58, column = 4, sticky = W)
thellid_year_lbl = Label(frame, text = "Year").grid(row = 57, column = 5, sticky = W)
thellid_year_ent = Entry(frame)
thellid_year_ent.grid(row = 58, column = 5, sticky = W)
thellid_bttn = Button(frame, text = "Calculate", command = thellid_converter).grid(row = 59, column = 3, columnspan = 3, sticky = W)

# Astronomical French Republican calendar                                                                                            
obs_french_lbl = Label(frame, text = "Astronomical French Republican calendar").grid(row = 56, column = 6, columnspan = 3, sticky = W)
obs_french_day_lbl = Label(frame, text = "Day").grid(row = 57, column = 6, sticky = W)
obs_french_day_ent = Entry(frame)
obs_french_day_ent.grid(row = 58, column = 6, sticky = W)
obs_french_month_lbl = Label(frame, text = "Month").grid(row = 57, column = 7, sticky = W)
obs_french_month_ent = Entry(frame)
obs_french_month_ent.grid(row = 58, column = 7, sticky = W)
obs_french_year_lbl = Label(frame, text = "Year").grid(row = 57, column = 8, sticky = W)
obs_french_year_ent = Entry(frame)
obs_french_year_ent.grid(row = 58, column = 8, sticky = W)
obs_french_bttn = Button(frame, text = "Calculate", command = obs_french_converter).grid(row = 59, column = 6, columnspan = 3, sticky = W)

# Algorithmic French Republican calendar                                                                                            
alg_french_lbl = Label(frame, text = "Algorithmic French Republican calendar").grid(row = 56, column = 9, columnspan = 3, sticky = W)
alg_french_day_lbl = Label(frame, text = "Day").grid(row = 57, column = 9, sticky = W)
alg_french_day_ent = Entry(frame)
alg_french_day_ent.grid(row = 58, column = 9, sticky = W)
alg_french_month_lbl = Label(frame, text = "Month").grid(row = 57, column = 10, sticky = W)
alg_french_month_ent = Entry(frame)
alg_french_month_ent.grid(row = 58, column = 10, sticky = W)
alg_french_year_lbl = Label(frame, text = "Year").grid(row = 57, column = 11, sticky = W)
alg_french_year_ent = Entry(frame)
alg_french_year_ent.grid(row = 58, column = 11, sticky = W)
alg_french_bttn = Button(frame, text = "Calculate", command = alg_french_converter).grid(row = 59, column = 9, columnspan = 3, sticky = W)

# Old Babylonian Calendar
babylonian_lbl = Label(frame, text = "Old Babylonian Calendar").grid(row = 60, column = 0, columnspan = 3, sticky = W)
babylonian_day_lbl = Label(frame, text = "Day").grid(row = 61, column = 0, sticky = W)
babylonian_day_ent = Entry(frame)
babylonian_day_ent.grid(row = 62, column = 0, sticky = W)
babylonian_month_lbl = Label(frame, text = "Month").grid(row = 61, column = 1, sticky = W)
babylonian_month_ent = Entry(frame)
babylonian_month_ent.grid(row = 62, column = 1, sticky = W)
babylonian_year_lbl = Label(frame, text = "Year").grid(row = 61, column = 2, sticky = W)
babylonian_year_ent = Entry(frame)
babylonian_year_ent.grid(row = 62, column = 2, sticky = W)
babylonian_bttn = Button(frame, text = "Calculate", command = babylonian_converter).grid(row = 63, column = 3, columnspan = 3, sticky = W)

# Fixed Babylonian calendar                                                                                            
fixed_babylonian_lbl = Label(frame, text = "Fixed Babylonian calendar").grid(row = 60, column = 3, columnspan = 3, sticky = W)
fixed_babylonian_day_lbl = Label(frame, text = "Day").grid(row = 61, column = 3, sticky = W)
fixed_babylonian_day_ent = Entry(frame)
fixed_babylonian_day_ent.grid(row = 62, column = 3, sticky = W)
fixed_babylonian_month_lbl = Label(frame, text = "Month").grid(row = 61, column = 4, sticky = W)
fixed_babylonian_month_ent = Entry(frame)
fixed_babylonian_month_ent.grid(row = 62, column = 4, sticky = W)
fixed_babylonian_year_lbl = Label(frame, text = "Year").grid(row = 61, column = 5, sticky = W)
fixed_babylonian_year_ent = Entry(frame)
fixed_babylonian_year_ent.grid(row = 62, column = 5, sticky = W)
fixed_babylonian_bttn = Button(frame, text = "Calculate", command = fixed_babylonian_converter).grid(row = 63, column = 3, columnspan = 3, sticky = W)

# Macedonian calendar                                                                                            
macedonian_lbl = Label(frame, text = "Macedonian calendar").grid(row = 60, column = 6, columnspan = 3, sticky = W)
macedonian_day_lbl = Label(frame, text = "Day").grid(row = 61, column = 6, sticky = W)
macedonian_day_ent = Entry(frame)
macedonian_day_ent.grid(row = 62, column = 6, sticky = W)
macedonian_month_lbl = Label(frame, text = "Month").grid(row = 61, column = 7, sticky = W)
macedonian_month_ent = Entry(frame)
macedonian_month_ent.grid(row = 62, column = 7, sticky = W)
macedonian_year_lbl = Label(frame, text = "Year").grid(row = 61, column = 8, sticky = W)
macedonian_year_ent = Entry(frame)
macedonian_year_ent.grid(row = 62, column = 8, sticky = W)
macedonian_bttn = Button(frame, text = "Calculate", command = macedonian_converter).grid(row = 63, column = 6, columnspan = 3, sticky = W)

# Seleucid calendar                                                                                            
seleucid_lbl = Label(frame, text = "Seleucid calendar").grid(row = 60, column = 9, columnspan = 3, sticky = W)
seleucid_day_lbl = Label(frame, text = "Day").grid(row = 61, column = 9, sticky = W)
seleucid_day_ent = Entry(frame)
seleucid_day_ent.grid(row = 62, column = 9, sticky = W)
seleucid_month_lbl = Label(frame, text = "Month").grid(row = 61, column = 10, sticky = W)
seleucid_month_ent = Entry(frame)
seleucid_month_ent.grid(row = 62, column = 10, sticky = W)
seleucid_year_lbl = Label(frame, text = "Year").grid(row = 61, column = 11, sticky = W)
seleucid_year_ent = Entry(frame)
seleucid_year_ent.grid(row = 62, column = 11, sticky = W)
seleucid_bttn = Button(frame, text = "Calculate", command = seleucid_converter).grid(row = 63, column = 9, columnspan = 3, sticky = W)

# Inca civil calendar                                                                                            
inca_lunar_lbl = Label(frame, text = "Inca civil calendar (tentative)").grid(row = 64, column = 0, columnspan = 3, sticky = W)
inca_lunar_day_lbl = Label(frame, text = "Day").grid(row = 65, column = 0, sticky = W)
inca_lunar_day_ent = Entry(frame)
inca_lunar_day_ent.grid(row = 66, column = 0, sticky = W)
inca_lunar_month_lbl = Label(frame, text = "Month").grid(row = 65, column = 1, sticky = W)
inca_lunar_month_ent = Entry(frame)
inca_lunar_month_ent.grid(row = 66, column = 1, sticky = W)
inca_lunar_year_lbl = Label(frame, text = "Year").grid(row = 65, column = 2, sticky = W)
inca_lunar_year_ent = Entry(frame)
inca_lunar_year_ent.grid(row = 66, column = 2, sticky = W)
inca_lunar_bttn = Button(frame, text = "Calculate", command = inca_lunar_converter).grid(row = 67, column = 0, columnspan = 3, sticky = W)

# Inca_solar calendar
inca_solar_lbl = Label(frame, text = "Inca agricultural calendar (tentative)").grid(row = 64, column = 3, columnspan = 3, sticky = W)
inca_solar_day_lbl = Label(frame, text = "Day").grid(row = 65, column = 3, sticky = W)
inca_solar_day_ent = Entry(frame)
inca_solar_day_ent.grid(row = 66, column = 3, sticky = W)
inca_solar_month_lbl = Label(frame, text = "Month").grid(row = 65, column = 4, sticky = W)
inca_solar_month_ent = Entry(frame)
inca_solar_month_ent.grid(row = 66, column = 4, sticky = W)
inca_solar_year_lbl = Label(frame, text = "Year").grid(row = 65, column = 5, sticky = W)
inca_solar_year_ent = Entry(frame)
inca_solar_year_ent.grid(row = 66, column = 5, sticky = W)
inca_solar_bttn = Button(frame, text = "Calculate", command = inca_solar_converter).grid(row = 67, column = 3, columnspan = 3, sticky = W)

# Old Bahá'í calendar                                                                                            
bahai_alg_lbl = Label(frame, text = "Old Bahá'í calendar").grid(row = 64, column = 6, columnspan = 3, sticky = W)
bahai_alg_day_lbl = Label(frame, text = "Day").grid(row = 65, column = 6, sticky = W)
bahai_alg_day_ent = Entry(frame)
bahai_alg_day_ent.grid(row = 66, column = 6, sticky = W)
bahai_alg_month_lbl = Label(frame, text = "Month").grid(row = 65, column = 7, sticky = W)
bahai_alg_month_ent = Entry(frame)
bahai_alg_month_ent.grid(row = 66, column = 7, sticky = W)
bahai_alg_year_lbl = Label(frame, text = "Year").grid(row = 65, column = 8, sticky = W)
bahai_alg_year_ent = Entry(frame)
bahai_alg_year_ent.grid(row = 66, column = 8, sticky = W)
bahai_alg_bttn = Button(frame, text = "Calculate", command = bahai_alg_converter).grid(row = 67, column = 6, columnspan = 3, sticky = W)

# New Bahí'í calendar                                                                                            
bahai_obs_lbl = Label(frame, text = "New Bahí'í calendar").grid(row = 64, column = 9, columnspan = 3, sticky = W)
bahai_obs_day_lbl = Label(frame, text = "Day").grid(row = 65, column = 9, sticky = W)
bahai_obs_day_ent = Entry(frame)
bahai_obs_day_ent.grid(row = 66, column = 9, sticky = W)
bahai_obs_month_lbl = Label(frame, text = "Month").grid(row = 65, column = 10, sticky = W)
bahai_obs_month_ent = Entry(frame)
bahai_obs_month_ent.grid(row = 66, column = 10, sticky = W)
bahai_obs_year_lbl = Label(frame, text = "Year").grid(row = 65, column = 11, sticky = W)
bahai_obs_year_ent = Entry(frame)
bahai_obs_year_ent.grid(row = 66, column = 11, sticky = W)
bahai_obs_bttn = Button(frame, text = "Calculate", command = bahai_obs_converter).grid(row = 67, column = 9, columnspan = 3, sticky = W)

# Chinese lunisolar calendar (Huangdi era)
chinese_lunisolar_huangdi_lbl = Label(frame, text = "Chinese lunisolar calendar (Yellow Emperor era)").grid(row = 68, column = 0, columnspan = 3, sticky = W)
chinese_lunisolar_huangdi_day_lbl = Label(frame, text = "Day").grid(row = 69, column = 0, sticky = W)
chinese_lunisolar_huangdi_day_ent = Entry(frame)
chinese_lunisolar_huangdi_day_ent.grid(row = 70, column = 0, sticky = W)
chinese_lunisolar_huangdi_month_lbl = Label(frame, text = "Month").grid(row = 69, column = 1, sticky = W)
chinese_lunisolar_huangdi_month_ent = Entry(frame)
chinese_lunisolar_huangdi_month_ent.grid(row = 70, column = 1, sticky = W)
chinese_lunisolar_huangdi_year_lbl = Label(frame, text = "Year").grid(row = 69, column = 2, sticky = W)
chinese_lunisolar_huangdi_year_ent = Entry(frame)
chinese_lunisolar_huangdi_year_ent.grid(row = 70, column = 2, sticky = W)
chinese_lunisolar_huangdi_bttn = Button(frame, text = "Calculate", command = chinese_lunisolar_huangdi_converter).grid(row = 71, column = 0, columnspan = 3, sticky = W)

# Chinese lunisolar calendar (Yao era)                                                                                         
chinese_lunisolar_yao_lbl = Label(frame, text = "Chinese lunisolar calendar (Yao era) calendar").grid(row = 68, column = 3, columnspan = 3, sticky = W)
chinese_lunisolar_yao_day_lbl = Label(frame, text = "Day").grid(row = 69, column = 3, sticky = W)
chinese_lunisolar_yao_day_ent = Entry(frame)
chinese_lunisolar_yao_day_ent.grid(row = 70, column = 3, sticky = W)
chinese_lunisolar_yao_month_lbl = Label(frame, text = "Month").grid(row = 69, column = 4, sticky = W)
chinese_lunisolar_yao_month_ent = Entry(frame)
chinese_lunisolar_yao_month_ent.grid(row = 70, column = 4, sticky = W)
chinese_lunisolar_yao_year_lbl = Label(frame, text = "Year").grid(row = 69, column = 5, sticky = W)
chinese_lunisolar_yao_year_ent = Entry(frame)
chinese_lunisolar_yao_year_ent.grid(row = 70, column = 5, sticky = W)
chinese_lunisolar_yao_bttn = Button(frame, text = "Calculate", command = chinese_lunisolar_yao_converter).grid(row = 71, column = 3, columnspan = 3, sticky = W)

# Chinese lunisolar calendar (Confucian era)                                                                                            
chinese_lunisolar_confucius_lbl = Label(frame, text = "Chinese lunisolar calendar (Confucian era)").grid(row = 68, column = 6, columnspan = 3, sticky = W)
chinese_lunisolar_confucius_day_lbl = Label(frame, text = "Day").grid(row = 69, column = 6, sticky = W)
chinese_lunisolar_confucius_day_ent = Entry(frame)
chinese_lunisolar_confucius_day_ent.grid(row = 70, column = 6, sticky = W)
chinese_lunisolar_confucius_month_lbl = Label(frame, text = "Month").grid(row = 69, column = 7, sticky = W)
chinese_lunisolar_confucius_month_ent = Entry(frame)
chinese_lunisolar_confucius_month_ent.grid(row = 70, column = 7, sticky = W)
chinese_lunisolar_confucius_year_lbl = Label(frame, text = "Year").grid(row = 69, column = 8, sticky = W)
chinese_lunisolar_confucius_year_ent = Entry(frame)
chinese_lunisolar_confucius_year_ent.grid(row = 70, column = 8, sticky = W)
chinese_lunisolar_confucius_bttn = Button(frame, text = "Calculate", command = chinese_lunisolar_confucius_converter).grid(row = 71, column = 6, columnspan = 3, sticky = W)

# Chinese lunisolar calendar (Gonghe era)                                                                                            
chinese_lunisolar_gonghe_lbl = Label(frame, text = "Chinese lunisolar calendar (Gonghe era)").grid(row = 68, column = 9, columnspan = 3, sticky = W)
chinese_lunisolar_gonghe_day_lbl = Label(frame, text = "Day").grid(row = 69, column = 9, sticky = W)
chinese_lunisolar_gonghe_day_ent = Entry(frame)
chinese_lunisolar_gonghe_day_ent.grid(row = 70, column = 9, sticky = W)
chinese_lunisolar_gonghe_month_lbl = Label(frame, text = "Month").grid(row = 69, column = 10, sticky = W)
chinese_lunisolar_gonghe_month_ent = Entry(frame)
chinese_lunisolar_gonghe_month_ent.grid(row = 70, column = 10, sticky = W)
chinese_lunisolar_gonghe_year_lbl = Label(frame, text = "Year").grid(row = 69, column = 11, sticky = W)
chinese_lunisolar_gonghe_year_ent = Entry(frame)
chinese_lunisolar_gonghe_year_ent.grid(row = 70, column = 11, sticky = W)
chinese_lunisolar_gonghe_bttn = Button(frame, text = "Calculate", command = chinese_lunisolar_gonghe_converter).grid(row = 71, column = 9, columnspan = 3, sticky = W)

# Chinese lunisolar calendar (Qin era)                                                                                            
chinese_lunisolar_qin_lbl = Label(frame, text = "Chinese lunisolar calendar (Qin era)").grid(row = 72, column = 0, columnspan = 3, sticky = W)
chinese_lunisolar_qin_day_lbl = Label(frame, text = "Day").grid(row = 73, column = 0, sticky = W)
chinese_lunisolar_qin_day_ent = Entry(frame)
chinese_lunisolar_qin_day_ent.grid(row = 74, column = 0, sticky = W)
chinese_lunisolar_qin_month_lbl = Label(frame, text = "Month").grid(row = 73, column = 1, sticky = W)
chinese_lunisolar_qin_month_ent = Entry(frame)
chinese_lunisolar_qin_month_ent.grid(row = 74, column = 1, sticky = W)
chinese_lunisolar_qin_year_lbl = Label(frame, text = "Year").grid(row = 73, column = 2, sticky = W)
chinese_lunisolar_qin_year_ent = Entry(frame)
chinese_lunisolar_qin_year_ent.grid(row = 74, column = 2, sticky = W)
chinese_lunisolar_qin_bttn = Button(frame, text = "Calculate", command = chinese_lunisolar_qin_converter).grid(row = 75, column = 0, columnspan = 3, sticky = W)

# Chinese solar calendar (Yellow Emperor era)                                                                                           
chinese_solar_huangdi_lbl = Label(frame, text = "Chinese solar calendar (Yellow Emperor era)").grid(row = 72, column = 3, columnspan = 3, sticky = W)
chinese_solar_huangdi_day_lbl = Label(frame, text = "Day").grid(row = 73, column = 3, sticky = W)
chinese_solar_huangdi_day_ent = Entry(frame)
chinese_solar_huangdi_day_ent.grid(row = 74, column = 3, sticky = W)
chinese_solar_huangdi_month_lbl = Label(frame, text = "Month").grid(row = 73, column = 4, sticky = W)
chinese_solar_huangdi_month_ent = Entry(frame)
chinese_solar_huangdi_month_ent.grid(row = 74, column = 4, sticky = W)
chinese_solar_huangdi_year_lbl = Label(frame, text = "Year").grid(row = 73, column = 5, sticky = W)
chinese_solar_huangdi_year_ent = Entry(frame)
chinese_solar_huangdi_year_ent.grid(row = 74, column = 5, sticky = W)
chinese_solar_huangdi_bttn = Button(frame, text = "Calculate", command = chinese_solar_huangdi_converter).grid(row = 75, column = 3, columnspan = 3, sticky = W)

# Chinese solar calendar (Yao era)                                                                                            
chinese_solar_yao_lbl = Label(frame, text = "Chinese solar calendar (Yao era)").grid(row = 72, column = 6, columnspan = 3, sticky = W)
chinese_solar_yao_day_lbl = Label(frame, text = "Day").grid(row = 73, column = 6, sticky = W)
chinese_solar_yao_day_ent = Entry(frame)
chinese_solar_yao_day_ent.grid(row = 74, column = 6, sticky = W)
chinese_solar_yao_month_lbl = Label(frame, text = "Month").grid(row = 73, column = 7, sticky = W)
chinese_solar_yao_month_ent = Entry(frame)
chinese_solar_yao_month_ent.grid(row = 74, column = 7, sticky = W)
chinese_solar_yao_year_lbl = Label(frame, text = "Year").grid(row = 73, column = 8, sticky = W)
chinese_solar_yao_year_ent = Entry(frame)
chinese_solar_yao_year_ent.grid(row = 74, column = 8, sticky = W)
chinese_solar_yao_bttn = Button(frame, text = "Calculate", command = chinese_solar_yao_converter).grid(row = 75, column = 6, columnspan = 3, sticky = W)

# Chinese solar calendar (Confucius era)                                                                                            
chinese_solar_confucius_lbl = Label(frame, text = "Chinese solar calendar (Confucius era)").grid(row = 72, column = 9, columnspan = 3, sticky = W)
chinese_solar_confucius_day_lbl = Label(frame, text = "Day").grid(row = 73, column = 9, sticky = W)
chinese_solar_confucius_day_ent = Entry(frame)
chinese_solar_confucius_day_ent.grid(row = 74, column = 9, sticky = W)
chinese_solar_confucius_month_lbl = Label(frame, text = "Month").grid(row = 73, column = 10, sticky = W)
chinese_solar_confucius_month_ent = Entry(frame)
chinese_solar_confucius_month_ent.grid(row = 74, column = 10, sticky = W)
chinese_solar_confucius_year_lbl = Label(frame, text = "Year").grid(row = 73, column = 11, sticky = W)
chinese_solar_confucius_year_ent = Entry(frame)
chinese_solar_confucius_year_ent.grid(row = 74, column = 11, sticky = W)
chinese_solar_confucius_bttn = Button(frame, text = "Calculate", command = chinese_solar_confucius_converter).grid(row = 75, column = 9, columnspan = 3, sticky = W)

# Chinese solar calendar (Gonghe era)                                                                                            
chinese_solar_gonghe_lbl = Label(frame, text = "Chinese solar calendar (Gonghe era)").grid(row = 76, column = 0, columnspan = 3, sticky = W)
chinese_solar_gonghe_day_lbl = Label(frame, text = "Day").grid(row = 77, column = 0, sticky = W)
chinese_solar_gonghe_day_ent = Entry(frame)
chinese_solar_gonghe_day_ent.grid(row = 78, column = 0, sticky = W)
chinese_solar_gonghe_month_lbl = Label(frame, text = "Month").grid(row = 77, column = 1, sticky = W)
chinese_solar_gonghe_month_ent = Entry(frame)
chinese_solar_gonghe_month_ent.grid(row = 78, column = 1, sticky = W)
chinese_solar_gonghe_year_lbl = Label(frame, text = "Year").grid(row = 77, column = 2, sticky = W)
chinese_solar_gonghe_year_ent = Entry(frame)
chinese_solar_gonghe_year_ent.grid(row = 78, column = 2, sticky = W)
chinese_solar_gonghe_bttn = Button(frame, text = "Calculate", command = chinese_solar_gonghe_converter).grid(row = 79, column = 0, columnspan = 3, sticky = W)

# Chinese solar calendar (Qin era)                                                                                            
chinese_solar_qin_lbl = Label(frame, text = "Chinese solar calendar (Qin era)").grid(row = 76, column = 3, columnspan = 3, sticky = W)
chinese_solar_qin_day_lbl = Label(frame, text = "Day").grid(row = 77, column = 3, sticky = W)
chinese_solar_qin_day_ent = Entry(frame)
chinese_solar_qin_day_ent.grid(row = 78, column = 3, sticky = W)
chinese_solar_qin_month_lbl = Label(frame, text = "Month").grid(row = 77, column = 4, sticky = W)
chinese_solar_qin_month_ent = Entry(frame)
chinese_solar_qin_month_ent.grid(row = 78, column = 4, sticky = W)
chinese_solar_qin_year_lbl = Label(frame, text = "Year").grid(row = 77, column = 5, sticky = W)
chinese_solar_qin_year_ent = Entry(frame)
chinese_solar_qin_year_ent.grid(row = 78, column = 5, sticky = W)
chinese_solar_qin_bttn = Button(frame, text = "Calculate", command = chinese_solar_qin_converter).grid(row = 79, column = 3, columnspan = 3, sticky = W)

# Zhou calendar
zhou_lbl = Label(frame, text = "Zhou calendar").grid(row = 76, column = 6, columnspan = 3, sticky = W)
zhou_day_lbl = Label(frame, text = "Day").grid(row = 77, column = 6, sticky = W)
zhou_day_ent = Entry(frame)
zhou_day_ent.grid(row = 78, column = 6, sticky = W)
zhou_month_lbl = Label(frame, text = "Month").grid(row = 77, column = 7, sticky = W)
zhou_month_ent = Entry(frame)
zhou_month_ent.grid(row = 78, column = 7, sticky = W)
zhou_year_lbl = Label(frame, text = "Year").grid(row = 77, column = 8, sticky = W)
zhou_year_ent = Entry(frame)
zhou_year_ent.grid(row = 78, column = 8, sticky = W)
zhou_bttn = Button(frame, text = "Calculate", command = zhou_converter).grid(row = 79, column = 6, columnspan = 3, sticky = W)

# Zhuanxu calendar                                                                                            
zhuanxu_lbl = Label(frame, text = "Zhuanxu calendar").grid(row = 76, column = 9, columnspan = 3, sticky = W)
zhuanxu_day_lbl = Label(frame, text = "Day").grid(row = 77, column = 9, sticky = W)
zhuanxu_day_ent = Entry(frame)
zhuanxu_day_ent.grid(row = 78, column = 9, sticky = W)
zhuanxu_month_lbl = Label(frame, text = "Month").grid(row = 77, column = 10, sticky = W)
zhuanxu_month_ent = Entry(frame)
zhuanxu_month_ent.grid(row = 78, column = 10, sticky = W)
zhuanxu_year_lbl = Label(frame, text = "Year").grid(row = 77, column = 11, sticky = W)
zhuanxu_year_ent = Entry(frame)
zhuanxu_year_ent.grid(row = 78, column = 11, sticky = W)
zhuanxu_bttn = Button(frame, text = "Calculate", command = zhuanxu_converter).grid(row = 79, column = 9, columnspan = 3, sticky = W)

# Xia calendar                                                                                            
xia_lbl = Label(frame, text = "Xia calendar").grid(row = 80, column = 0, columnspan = 3, sticky = W)
xia_day_lbl = Label(frame, text = "Day").grid(row = 81, column = 0, sticky = W)
xia_day_ent = Entry(frame)
xia_day_ent.grid(row = 82, column = 0, sticky = W)
xia_month_lbl = Label(frame, text = "Month").grid(row = 81, column = 1, sticky = W)
xia_month_ent = Entry(frame)
xia_month_ent.grid(row = 82, column = 1, sticky = W)
xia_year_lbl = Label(frame, text = "Year").grid(row = 81, column = 2, sticky = W)
xia_year_ent = Entry(frame)
xia_year_ent.grid(row = 82, column = 2, sticky = W)
xia_bttn = Button(frame, text = "Calculate", command = xia_converter).grid(row = 83, column = 0, columnspan = 3, sticky = W)

# Shang calendar                                                                                            
shang_lbl = Label(frame, text = "Shang calendar").grid(row = 80, column = 3, columnspan = 3, sticky = W)
shang_day_lbl = Label(frame, text = "Day").grid(row = 81, column = 3, sticky = W)
shang_day_ent = Entry(frame)
shang_day_ent.grid(row = 82, column = 3, sticky = W)
shang_month_lbl = Label(frame, text = "Month").grid(row = 81, column = 4, sticky = W)
shang_month_ent = Entry(frame)
shang_month_ent.grid(row = 82, column = 4, sticky = W)
shang_year_lbl = Label(frame, text = "Year").grid(row = 81, column = 5, sticky = W)
shang_year_ent = Entry(frame)
shang_year_ent.grid(row = 82, column = 5, sticky = W)
shang_bttn = Button(frame, text = "Calculate", command = shang_converter).grid(row = 83, column = 3, columnspan = 3, sticky = W)

# Lu calendar                                                                                            
lu_lbl = Label(frame, text = "Lu calendar").grid(row = 80, column = 6, columnspan = 3, sticky = W)
lu_day_lbl = Label(frame, text = "Day").grid(row = 81, column = 6, sticky = W)
lu_day_ent = Entry(frame)
lu_day_ent.grid(row = 82, column = 6, sticky = W)
lu_month_lbl = Label(frame, text = "Month").grid(row = 81, column = 7, sticky = W)
lu_month_ent = Entry(frame)
lu_month_ent.grid(row = 82, column = 7, sticky = W)
lu_year_lbl = Label(frame, text = "Year").grid(row = 81, column = 8, sticky = W)
lu_year_ent = Entry(frame)
lu_year_ent.grid(row = 82, column = 8, sticky = W)
lu_bttn = Button(frame, text = "Calculate", command = lu_converter).grid(row = 83, column = 6, columnspan = 3, sticky = W)

# Yin calendar                                                                                            
yin_lbl = Label(frame, text = "Yin calendar").grid(row = 80, column = 9, columnspan = 3, sticky = W)
yin_day_lbl = Label(frame, text = "Day").grid(row = 81, column = 9, sticky = W)
yin_day_ent = Entry(frame)
yin_day_ent.grid(row = 82, column = 9, sticky = W)
yin_month_lbl = Label(frame, text = "Month").grid(row = 81, column = 10, sticky = W)
yin_month_ent = Entry(frame)
yin_month_ent.grid(row = 82, column = 10, sticky = W)
yin_year_lbl = Label(frame, text = "Year").grid(row = 81, column = 11, sticky = W)
yin_year_ent = Entry(frame)
yin_year_ent.grid(row = 82, column = 11, sticky = W)
yin_bttn = Button(frame, text = "Calculate", command = yin_converter).grid(row = 83, column = 9, columnspan = 3, sticky = W)

# Taichu calendar                                                                                            
taichu_lbl = Label(frame, text = "Taichu calendar").grid(row = 84, column = 0, columnspan = 3, sticky = W)
taichu_day_lbl = Label(frame, text = "Day").grid(row = 85, column = 0, sticky = W)
taichu_day_ent = Entry(frame)
taichu_day_ent.grid(row = 86, column = 0, sticky = W)
taichu_month_lbl = Label(frame, text = "Month").grid(row = 85, column = 1, sticky = W)
taichu_month_ent = Entry(frame)
taichu_month_ent.grid(row = 86, column = 1, sticky = W)
taichu_year_lbl = Label(frame, text = "Year").grid(row = 85, column = 2, sticky = W)
taichu_year_ent = Entry(frame)
taichu_year_ent.grid(row = 86, column = 2, sticky = W)
taichu_bttn = Button(frame, text = "Calculate", command = taichu_converter).grid(row = 87, column = 0, columnspan = 3, sticky = W)

# Santong calendar                                                                                            
santong_lbl = Label(frame, text = "Santong calendar").grid(row = 84, column = 3, columnspan = 3, sticky = W)
santong_day_lbl = Label(frame, text = "Day").grid(row = 85, column = 3, sticky = W)
santong_day_ent = Entry(frame)
santong_day_ent.grid(row = 86, column = 3, sticky = W)
santong_month_lbl = Label(frame, text = "Month").grid(row = 85, column = 4, sticky = W)
santong_month_ent = Entry(frame)
santong_month_ent.grid(row = 86, column = 4, sticky = W)
santong_year_lbl = Label(frame, text = "Year").grid(row = 85, column = 5, sticky = W)
santong_year_ent = Entry(frame)
santong_year_ent.grid(row = 86, column = 5, sticky = W)
santong_bttn = Button(frame, text = "Calculate", command = santong_converter).grid(row = 87, column = 3, columnspan = 3, sticky = W)

# Han Quarter Remainder calendar                                                                                            
sifen_lbl = Label(frame, text = "Han Quarter Remainder calendar").grid(row = 84, column = 6, columnspan = 3, sticky = W)
sifen_day_lbl = Label(frame, text = "Day").grid(row = 85, column = 6, sticky = W)
sifen_day_ent = Entry(frame)
sifen_day_ent.grid(row = 86, column = 6, sticky = W)
sifen_month_lbl = Label(frame, text = "Month").grid(row = 85, column = 7, sticky = W)
sifen_month_ent = Entry(frame)
sifen_month_ent.grid(row = 86, column = 7, sticky = W)
sifen_year_lbl = Label(frame, text = "Year").grid(row = 85, column = 8, sticky = W)
sifen_year_ent = Entry(frame)
sifen_year_ent.grid(row = 86, column = 8, sticky = W)
sifen_bttn = Button(frame, text = "Calculate", command = sifen_converter).grid(row = 87, column = 6, columnspan = 3, sticky = W)

# Qianxiang calendar                                                                                            
qianxiang_lbl = Label(frame, text = "Qianxiang calendar").grid(row = 84, column = 9, columnspan = 12, sticky = W)
qianxiang_day_lbl = Label(frame, text = "Day").grid(row = 85, column = 9, sticky = W)
qianxiang_day_ent = Entry(frame)
qianxiang_day_ent.grid(row = 86, column = 9, sticky = W)
qianxiang_month_lbl = Label(frame, text = "Month").grid(row = 85, column = 10, sticky = W)
qianxiang_month_ent = Entry(frame)
qianxiang_month_ent.grid(row = 86, column = 10, sticky = W)
qianxiang_year_lbl = Label(frame, text = "Year").grid(row = 85, column = 11, sticky = W)
qianxiang_year_ent = Entry(frame)
qianxiang_year_ent.grid(row = 86, column = 11, sticky = W)
qianxiang_bttn = Button(frame, text = "Calculate", command = qianxiang_converter).grid(row = 87, column = 9, columnspan = 3, sticky = W)

# Jingchu calendar                                                                                            
jingchu_lbl = Label(frame, text = "Jingchu calendar").grid(row = 88, column = 0, columnspan = 3, sticky = W)
jingchu_day_lbl = Label(frame, text = "Day").grid(row = 89, column = 0, sticky = W)
jingchu_day_ent = Entry(frame)
jingchu_day_ent.grid(row = 90, column = 0, sticky = W)
jingchu_month_lbl = Label(frame, text = "Month").grid(row = 89, column = 1, sticky = W)
jingchu_month_ent = Entry(frame)
jingchu_month_ent.grid(row = 90, column = 1, sticky = W)
jingchu_year_lbl = Label(frame, text = "Year").grid(row = 89, column = 2, sticky = W)
jingchu_year_ent = Entry(frame)
jingchu_year_ent.grid(row = 90, column = 2, sticky = W)
jingchu_bttn = Button(frame, text = "Calculate", command = jingchu_converter).grid(row = 91, column = 0, columnspan = 3, sticky = W)

# Sanji calendar                                                                                            
sanji_lbl = Label(frame, text = "Sanji calendar").grid(row = 88, column = 3, columnspan = 3, sticky = W)
sanji_day_lbl = Label(frame, text = "Day").grid(row = 89, column = 3, sticky = W)
sanji_day_ent = Entry(frame)
sanji_day_ent.grid(row = 90, column = 3, sticky = W)
sanji_month_lbl = Label(frame, text = "Month").grid(row = 89, column = 4, sticky = W)
sanji_month_ent = Entry(frame)
sanji_month_ent.grid(row = 90, column = 4, sticky = W)
sanji_year_lbl = Label(frame, text = "Year").grid(row = 89, column = 5, sticky = W)
sanji_year_ent = Entry(frame)
sanji_year_ent.grid(row = 90, column = 5, sticky = W)
sanji_bttn = Button(frame, text = "Calculate", command = sanji_converter).grid(row = 91, column = 3, columnspan = 3, sticky = W)

# Yuanjia calendar                                                                                            
yuanjia_lbl = Label(frame, text = "Yuanjia calendar").grid(row = 88, column = 6, columnspan = 3, sticky = W)
yuanjia_day_lbl = Label(frame, text = "Day").grid(row = 89, column = 6, sticky = W)
yuanjia_day_ent = Entry(frame)
yuanjia_day_ent.grid(row = 90, column = 6, sticky = W)
yuanjia_month_lbl = Label(frame, text = "Month").grid(row = 89, column = 7, sticky = W)
yuanjia_month_ent = Entry(frame)
yuanjia_month_ent.grid(row = 90, column = 7, sticky = W)
yuanjia_year_lbl = Label(frame, text = "Year").grid(row = 89, column = 8, sticky = W)
yuanjia_year_ent = Entry(frame)
yuanjia_year_ent.grid(row = 90, column = 8, sticky = W)
yuanjia_bttn = Button(frame, text = "Calculate", command = yuanjia_converter).grid(row = 91, column = 6, columnspan = 3, sticky = W)

# Xuanshi calendar                                                                                            
xuanshi_lbl = Label(frame, text = "Xuanshi calendar").grid(row = 88, column = 9, columnspan = 3, sticky = W)
xuanshi_day_lbl = Label(frame, text = "Day").grid(row = 89, column = 9, sticky = W)
xuanshi_day_ent = Entry(frame)
xuanshi_day_ent.grid(row = 90, column = 9, sticky = W)
xuanshi_month_lbl = Label(frame, text = "Month").grid(row = 89, column = 10, sticky = W)
xuanshi_month_ent = Entry(frame)
xuanshi_month_ent.grid(row = 90, column = 10, sticky = W)
xuanshi_year_lbl = Label(frame, text = "Year").grid(row = 89, column = 11, sticky = W)
xuanshi_year_ent = Entry(frame)
xuanshi_year_ent.grid(row = 90, column = 11, sticky = W)
xuanshi_bttn = Button(frame, text = "Calculate", command = xuanshi_converter).grid(row = 91, column = 9, columnspan = 3, sticky = W)

# Daming calendar                                                                                            
daming_lbl = Label(frame, text = "Daming calendar").grid(row = 92, column = 0, columnspan = 3, sticky = W)
daming_day_lbl = Label(frame, text = "Day").grid(row = 93, column = 0, sticky = W)
daming_day_ent = Entry(frame)
daming_day_ent.grid(row = 94, column = 0, sticky = W)
daming_month_lbl = Label(frame, text = "Month").grid(row = 93, column = 1, sticky = W)
daming_month_ent = Entry(frame)
daming_month_ent.grid(row = 94, column = 1, sticky = W)
daming_year_lbl = Label(frame, text = "Year").grid(row = 93, column = 2, sticky = W)
daming_year_ent = Entry(frame)
daming_year_ent.grid(row = 94, column = 2, sticky = W)
daming_bttn = Button(frame, text = "Calculate", command = daming_converter).grid(row = 95, column = 0, columnspan = 3, sticky = W)

# Zhengguang calendar                                                                                            
zhengguang_lbl = Label(frame, text = "Zhengguang calendar").grid(row = 92, column = 3, columnspan = 3, sticky = W)
zhengguang_day_lbl = Label(frame, text = "Day").grid(row = 93, column = 3, sticky = W)
zhengguang_day_ent = Entry(frame)
zhengguang_day_ent.grid(row = 94, column = 3, sticky = W)
zhengguang_month_lbl = Label(frame, text = "Month").grid(row = 93, column = 4, sticky = W)
zhengguang_month_ent = Entry(frame)
zhengguang_month_ent.grid(row = 94, column = 4, sticky = W)
zhengguang_year_lbl = Label(frame, text = "Year").grid(row = 93, column = 5, sticky = W)
zhengguang_year_ent = Entry(frame)
zhengguang_year_ent.grid(row = 94, column = 5, sticky = W)
zhengguang_bttn = Button(frame, text = "Calculate", command = zhengguang_converter).grid(row = 95, column = 3, columnspan = 3, sticky = W)

# Xinghe calendar                                                                                            
xinghe_lbl = Label(frame, text = "Xinghe calendar").grid(row = 92, column = 6, columnspan = 3, sticky = W)
xinghe_day_lbl = Label(frame, text = "Day").grid(row = 93, column = 6, sticky = W)
xinghe_day_ent = Entry(frame)
xinghe_day_ent.grid(row = 94, column = 6, sticky = W)
xinghe_month_lbl = Label(frame, text = "Month").grid(row = 93, column = 7, sticky = W)
xinghe_month_ent = Entry(frame)
xinghe_month_ent.grid(row = 94, column = 7, sticky = W)
xinghe_year_lbl = Label(frame, text = "Year").grid(row = 93, column = 8, sticky = W)
xinghe_year_ent = Entry(frame)
xinghe_year_ent.grid(row = 94, column = 8, sticky = W)
xinghe_bttn = Button(frame, text = "Calculate", command = xinghe_converter).grid(row = 95, column = 6, columnspan = 3, sticky = W)

# Tianbao calendar                                                                                            
tianbao_lbl = Label(frame, text = "Tianbao calendar").grid(row = 92, column = 9, columnspan = 3, sticky = W)
tianbao_day_lbl = Label(frame, text = "Day").grid(row = 93, column = 9, sticky = W)
tianbao_day_ent = Entry(frame)
tianbao_day_ent.grid(row = 94, column = 9, sticky = W)
tianbao_month_lbl = Label(frame, text = "Month").grid(row = 93, column = 10, sticky = W)
tianbao_month_ent = Entry(frame)
tianbao_month_ent.grid(row = 94, column = 10, sticky = W)
tianbao_year_lbl = Label(frame, text = "Year").grid(row = 93, column = 11, sticky = W)
tianbao_year_ent = Entry(frame)
tianbao_year_ent.grid(row = 94, column = 11, sticky = W)
tianbao_bttn = Button(frame, text = "Calculate", command = tianbao_converter).grid(row = 95, column = 9, columnspan = 3, sticky = W)

# Tianhe calendar                                                                                            
tianhe_lbl = Label(frame, text = "Tianhe calendar").grid(row = 96, column = 0, columnspan = 3, sticky = W)
tianhe_day_lbl = Label(frame, text = "Day").grid(row = 97, column = 0, sticky = W)
tianhe_day_ent = Entry(frame)
tianhe_day_ent.grid(row = 98, column = 0, sticky = W)
tianhe_month_lbl = Label(frame, text = "Month").grid(row = 97, column = 1, sticky = W)
tianhe_month_ent = Entry(frame)
tianhe_month_ent.grid(row = 98, column = 1, sticky = W)
tianhe_year_lbl = Label(frame, text = "Year").grid(row = 97, column = 2, sticky = W)
tianhe_year_ent = Entry(frame)
tianhe_year_ent.grid(row = 98, column = 2, sticky = W)
tianhe_bttn = Button(frame, text = "Calculate", command = tianhe_converter).grid(row = 99, column = 0, columnspan = 3, sticky = W)

# Daxiang calendar                                                                                            
daxiang_lbl = Label(frame, text = "Daxiang calendar").grid(row = 96, column = 3, columnspan = 3, sticky = W)
daxiang_day_lbl = Label(frame, text = "Day").grid(row = 97, column = 3, sticky = W)
daxiang_day_ent = Entry(frame)
daxiang_day_ent.grid(row = 98, column = 3, sticky = W)
daxiang_month_lbl = Label(frame, text = "Month").grid(row = 97, column = 4, sticky = W)
daxiang_month_ent = Entry(frame)
daxiang_month_ent.grid(row = 98, column = 4, sticky = W)
daxiang_year_lbl = Label(frame, text = "Year").grid(row = 97, column = 5, sticky = W)
daxiang_year_ent = Entry(frame)
daxiang_year_ent.grid(row = 98, column = 5, sticky = W)
daxiang_bttn = Button(frame, text = "Calculate", command = daxiang_converter).grid(row = 99, column = 3, columnspan = 3, sticky = W)

# Kaihuang calendar                                                                                            
kaihuang_lbl = Label(frame, text = "Kaihuang calendar").grid(row = 96, column = 6, columnspan = 3, sticky = W)
kaihuang_day_lbl = Label(frame, text = "Day").grid(row = 97, column = 6, sticky = W)
kaihuang_day_ent = Entry(frame)
kaihuang_day_ent.grid(row = 98, column = 6, sticky = W)
kaihuang_month_lbl = Label(frame, text = "Month").grid(row = 97, column = 7, sticky = W)
kaihuang_month_ent = Entry(frame)
kaihuang_month_ent.grid(row = 98, column = 7, sticky = W)
kaihuang_year_lbl = Label(frame, text = "Year").grid(row = 97, column = 8, sticky = W)
kaihuang_year_ent = Entry(frame)
kaihuang_year_ent.grid(row = 98, column = 8, sticky = W)
kaihuang_bttn = Button(frame, text = "Calculate", command = kaihuang_converter).grid(row = 99, column = 6, columnspan = 3, sticky = W)

# Daye calendar                                                                                            
daye_lbl = Label(frame, text = "Daye calendar").grid(row = 96, column = 9, columnspan = 3, sticky = W)
daye_day_lbl = Label(frame, text = "Day").grid(row = 97, column = 9, sticky = W)
daye_day_ent = Entry(frame)
daye_day_ent.grid(row = 98, column = 9, sticky = W)
daye_month_lbl = Label(frame, text = "Month").grid(row = 97, column = 10, sticky = W)
daye_month_ent = Entry(frame)
daye_month_ent.grid(row = 98, column = 10, sticky = W)
daye_year_lbl = Label(frame, text = "Year").grid(row = 97, column = 11, sticky = W)
daye_year_ent = Entry(frame)
daye_year_ent.grid(row = 98, column = 11, sticky = W)
daye_bttn = Button(frame, text = "Calculate", command = daye_converter).grid(row = 99, column = 9, columnspan = 3, sticky = W)

# Wuyin calendar                                                                                            
wuyin_lbl = Label(frame, text = "Wuyin calendar").grid(row = 100, column = 0, columnspan = 3, sticky = W)
wuyin_day_lbl = Label(frame, text = "Day").grid(row = 101, column = 0, sticky = W)
wuyin_day_ent = Entry(frame)
wuyin_day_ent.grid(row = 102, column = 0, sticky = W)
wuyin_month_lbl = Label(frame, text = "Month").grid(row = 101, column = 1, sticky = W)
wuyin_month_ent = Entry(frame)
wuyin_month_ent.grid(row = 102, column = 1, sticky = W)
wuyin_year_lbl = Label(frame, text = "Year").grid(row = 101, column = 2, sticky = W)
wuyin_year_ent = Entry(frame)
wuyin_year_ent.grid(row = 102, column = 2, sticky = W)
wuyin_bttn = Button(frame, text = "Calculate", command = wuyin_converter).grid(row = 103, column = 0, columnspan = 3, sticky = W)

# Xuanming calendar                                                                                            
xuanming_lbl = Label(frame, text = "Xuanming calendar").grid(row = 100, column = 3, columnspan = 3, sticky = W)
xuanming_day_lbl = Label(frame, text = "Day").grid(row = 101, column = 3, sticky = W)
xuanming_day_ent = Entry(frame)
xuanming_day_ent.grid(row = 102, column = 3, sticky = W)
xuanming_month_lbl = Label(frame, text = "Month").grid(row = 101, column = 4, sticky = W)
xuanming_month_ent = Entry(frame)
xuanming_month_ent.grid(row = 102, column = 4, sticky = W)
xuanming_year_lbl = Label(frame, text = "Year").grid(row = 101, column = 5, sticky = W)
xuanming_year_ent = Entry(frame)
xuanming_year_ent.grid(row = 102, column = 5, sticky = W)
xuanming_bttn = Button(frame, text = "Calculate", command = xuanming_converter).grid(row = 103, column = 3, columnspan = 3, sticky = W)

# Vietnamese lunisolar calendar                                                                                            
vietnamese_lbl = Label(frame, text = "Vietnamese lunisolar calendar").grid(row = 100, column = 6, columnspan = 3, sticky = W)
vietnamese_day_lbl = Label(frame, text = "Day").grid(row = 101, column = 6, sticky = W)
vietnamese_day_ent = Entry(frame)
vietnamese_day_ent.grid(row = 102, column = 6, sticky = W)
vietnamese_month_lbl = Label(frame, text = "Month").grid(row = 101, column = 7, sticky = W)
vietnamese_month_ent = Entry(frame)
vietnamese_month_ent.grid(row = 102, column = 7, sticky = W)
vietnamese_year_lbl = Label(frame, text = "Year").grid(row = 101, column = 8, sticky = W)
vietnamese_year_ent = Entry(frame)
vietnamese_year_ent.grid(row = 102, column = 8, sticky = W)
vietnamese_bttn = Button(frame, text = "Calculate", command = vietnamese_converter).grid(row = 103, column = 6, columnspan = 3, sticky = W)

# Royal Korean calendar                                                                                            
korean_lbl = Label(frame, text = "Royal Korean calendar").grid(row = 100, column = 9, columnspan = 3, sticky = W)
korean_day_lbl = Label(frame, text = "Day").grid(row = 101, column = 9, sticky = W)
korean_day_ent = Entry(frame)
korean_day_ent.grid(row = 102, column = 9, sticky = W)
korean_month_lbl = Label(frame, text = "Month").grid(row = 101, column = 10, sticky = W)
korean_month_ent = Entry(frame)
korean_month_ent.grid(row = 102, column = 10, sticky = W)
korean_year_lbl = Label(frame, text = "Year").grid(row = 101, column = 11, sticky = W)
korean_year_ent = Entry(frame)
korean_year_ent.grid(row = 102, column = 11, sticky = W)
korean_bttn = Button(frame, text = "Calculate", command = korean_converter).grid(row = 103, column = 9, columnspan = 3, sticky = W)

# Dangun (Korean lunisolar) calendar                                                                                            
dangun_lbl = Label(frame, text = "Dangun (Korean lunisolar) calendar").grid(row = 104, column = 0, columnspan = 3, sticky = W)
dangun_day_lbl = Label(frame, text = "Day").grid(row = 105, column = 0, sticky = W)
dangun_day_ent = Entry(frame)
dangun_day_ent.grid(row = 106, column = 0, sticky = W)
dangun_month_lbl = Label(frame, text = "Month").grid(row = 105, column = 1, sticky = W)
dangun_month_ent = Entry(frame)
dangun_month_ent.grid(row = 106, column = 1, sticky = W)
dangun_year_lbl = Label(frame, text = "Year").grid(row = 105, column = 2, sticky = W)
dangun_year_ent = Entry(frame)
dangun_year_ent.grid(row = 106, column = 2, sticky = W)
dangun_bttn = Button(frame, text = "Calculate", command = dangun_converter).grid(row = 107, column = 0, columnspan = 3, sticky = W)

# Japanese lunisolar calendar                                                                                            
japanese_lunisolar_lbl = Label(frame, text = "Japanese lunisolar calendar").grid(row = 104, column = 3, columnspan = 3, sticky = W)
japanese_lunisolar_day_lbl = Label(frame, text = "Day").grid(row = 105, column = 3, sticky = W)
japanese_lunisolar_day_ent = Entry(frame)
japanese_lunisolar_day_ent.grid(row = 106, column = 3, sticky = W)
japanese_lunisolar_month_lbl = Label(frame, text = "Month").grid(row = 105, column = 4, sticky = W)
japanese_lunisolar_month_ent = Entry(frame)
japanese_lunisolar_month_ent.grid(row = 106, column = 4, sticky = W)
japanese_lunisolar_year_lbl = Label(frame, text = "Year").grid(row = 105, column = 5, sticky = W)
japanese_lunisolar_year_ent = Entry(frame)
japanese_lunisolar_year_ent.grid(row = 106, column = 5, sticky = W)
japanese_lunisolar_bttn = Button(frame, text = "Calculate", command = japanese_lunisolar_converter).grid(row = 107, column = 3, columnspan = 3, sticky = W)

# Imperial Japanese calendar                                                                                            
japanese_lbl = Label(frame, text = "Imperial Japanese calendar").grid(row = 104, column = 6, columnspan = 3, sticky = W)
japanese_day_lbl = Label(frame, text = "Day").grid(row = 105, column = 6, sticky = W)
japanese_day_ent = Entry(frame)
japanese_day_ent.grid(row = 106, column = 6, sticky = W)
japanese_month_lbl = Label(frame, text = "Month").grid(row = 105, column = 7, sticky = W)
japanese_month_ent = Entry(frame)
japanese_month_ent.grid(row = 106, column = 7, sticky = W)
japanese_year_lbl = Label(frame, text = "Year").grid(row = 105, column = 8, sticky = W)
japanese_year_ent = Entry(frame)
japanese_year_ent.grid(row = 106, column = 8, sticky = W)
japanese_bttn = Button(frame, text = "Calculate", command = japanese_converter).grid(row = 107, column = 6, columnspan = 3, sticky = W)

# Qadimi calendar (Yazdegerdi era) calendar                                                                                            
qadimi_yz_lbl = Label(frame, text = "Qadimi calendar (Yazdegerdi era)").grid(row = 104, column = 9, columnspan = 3, sticky = W)
qadimi_yz_day_lbl = Label(frame, text = "Day").grid(row = 105, column = 9, sticky = W)
qadimi_yz_day_ent = Entry(frame)
qadimi_yz_day_ent.grid(row = 106, column = 9, sticky = W)
qadimi_yz_month_lbl = Label(frame, text = "Month").grid(row = 105, column = 10, sticky = W)
qadimi_yz_month_ent = Entry(frame)
qadimi_yz_month_ent.grid(row = 106, column = 10, sticky = W)
qadimi_yz_year_lbl = Label(frame, text = "Year").grid(row = 105, column = 11, sticky = W)
qadimi_yz_year_ent = Entry(frame)
qadimi_yz_year_ent.grid(row = 106, column = 11, sticky = W)
qadimi_yz_bttn = Button(frame, text = "Calculate", command = qadimi_yz_converter).grid(row = 107, column = 9, columnspan = 3, sticky = W)

# Qadimi calendar (Anno Zoroastres) calendar                                                                                            
qadimi_az_lbl = Label(frame, text = "Qadimi calendar (Anno Zoroastres)r").grid(row = 108, column = 0, columnspan = 3, sticky = W)
qadimi_az_day_lbl = Label(frame, text = "Day").grid(row = 109, column = 0, sticky = W)
qadimi_az_day_ent = Entry(frame)
qadimi_az_day_ent.grid(row = 110, column = 0, sticky = W)
qadimi_az_month_lbl = Label(frame, text = "Month").grid(row = 109, column = 1, sticky = W)
qadimi_az_month_ent = Entry(frame)
qadimi_az_month_ent.grid(row = 110, column = 1, sticky = W)
qadimi_az_year_lbl = Label(frame, text = "Year").grid(row = 109, column = 2, sticky = W)
qadimi_az_year_ent = Entry(frame)
qadimi_az_year_ent.grid(row = 110, column = 2, sticky = W)
qadimi_az_bttn = Button(frame, text = "Calculate", command = qadimi_az_converter).grid(row = 111, column = 0, columnspan = 3, sticky = W)

# Qadimi calendar (Zoroastrian Religious Era)                                                                                            
qadimi_zre_lbl = Label(frame, text = "Qadimi calendar (Zoroastrian Religious Era)").grid(row = 108, column = 3, columnspan = 3, sticky = W)
qadimi_zre_day_lbl = Label(frame, text = "Day").grid(row = 109, column = 3, sticky = W)
qadimi_zre_day_ent = Entry(frame)
qadimi_zre_day_ent.grid(row = 110, column = 3, sticky = W)
qadimi_zre_month_lbl = Label(frame, text = "Month").grid(row = 109, column = 4, sticky = W)
qadimi_zre_month_ent = Entry(frame)
qadimi_zre_month_ent.grid(row = 110, column = 4, sticky = W)
qadimi_zre_year_lbl = Label(frame, text = "Year").grid(row = 109, column = 5, sticky = W)
qadimi_zre_year_ent = Entry(frame)
qadimi_zre_year_ent.grid(row = 110, column = 5, sticky = W)
qadimi_zre_bttn = Button(frame, text = "Calculate", command = qadimi_zre_converter).grid(row = 111, column = 3, columnspan = 3, sticky = W)

# Shenshai calendar (Yazdegerdi era)                                                                                            
shenshai_yz_lbl = Label(frame, text = "Shenshai calendar (Yazdegerdi era)").grid(row = 108, column = 6, columnspan = 3, sticky = W)
shenshai_yz_day_lbl = Label(frame, text = "Day").grid(row = 109, column = 6, sticky = W)
shenshai_yz_day_ent = Entry(frame)
shenshai_yz_day_ent.grid(row = 110, column = 6, sticky = W)
shenshai_yz_month_lbl = Label(frame, text = "Month").grid(row = 109, column = 7, sticky = W)
shenshai_yz_month_ent = Entry(frame)
shenshai_yz_month_ent.grid(row = 110, column = 7, sticky = W)
shenshai_yz_year_lbl = Label(frame, text = "Year").grid(row = 109, column = 8, sticky = W)
shenshai_yz_year_ent = Entry(frame)
shenshai_yz_year_ent.grid(row = 110, column = 8, sticky = W)
shenshai_yz_bttn = Button(frame, text = "Calculate", command = shenshai_yz_converter).grid(row = 111, column = 6, columnspan = 3, sticky = W)

# Shenshai calendar (Anno Zoroastres)                                                                                            
shenshai_az_lbl = Label(frame, text = "Shenshai calendar (Anno Zoroastres)").grid(row = 108, column = 9, columnspan = 3, sticky = W)
shenshai_az_day_lbl = Label(frame, text = "Day").grid(row = 109, column = 9, sticky = W)
shenshai_az_day_ent = Entry(frame)
shenshai_az_day_ent.grid(row = 110, column = 9, sticky = W)
shenshai_az_month_lbl = Label(frame, text = "Month").grid(row = 109, column = 10, sticky = W)
shenshai_az_month_ent = Entry(frame)
shenshai_az_month_ent.grid(row = 110, column = 10, sticky = W)
shenshai_az_year_lbl = Label(frame, text = "Year").grid(row = 109, column = 11, sticky = W)
shenshai_az_year_ent = Entry(frame)
shenshai_az_year_ent.grid(row = 110, column = 11, sticky = W)
shenshai_az_bttn = Button(frame, text = "Calculate", command = shenshai_az_converter).grid(row = 111, column = 9, columnspan = 3, sticky = W)

# Shenshai calendar (Zoroastrian religious era)                                                                                            
shenshai_zre_lbl = Label(frame, text = "Shenshai calendar (Zoroastrian religious era)").grid(row = 112, column = 0, columnspan = 3, sticky = W)
shenshai_zre_day_lbl = Label(frame, text = "Day").grid(row = 113, column = 0, sticky = W)
shenshai_zre_day_ent = Entry(frame)
shenshai_zre_day_ent.grid(row = 114, column = 0, sticky = W)
shenshai_zre_month_lbl = Label(frame, text = "Month").grid(row = 113, column = 1, sticky = W)
shenshai_zre_month_ent = Entry(frame)
shenshai_zre_month_ent.grid(row = 114, column = 1, sticky = W)
shenshai_zre_year_lbl = Label(frame, text = "Year").grid(row = 113, column = 2, sticky = W)
shenshai_zre_year_ent = Entry(frame)
shenshai_zre_year_ent.grid(row = 114, column = 2, sticky = W)
shenshai_zre_bttn = Button(frame, text = "Calculate", command = shenshai_zre_converter).grid(row = 115, column = 0, columnspan = 3, sticky = W)

# Young Avestan calendar (Iran, Yazdegerdi era)                                                                                            
young_avestan_iran_yz_lbl = Label(frame, text = "Young Avestan calendar (Iran, Yazdegerdi era)").grid(row = 112, column = 3, columnspan = 3, sticky = W)
young_avestan_iran_yz_day_lbl = Label(frame, text = "Day").grid(row = 113, column = 3, sticky = W)
young_avestan_iran_yz_day_ent = Entry(frame)
young_avestan_iran_yz_day_ent.grid(row = 114, column = 3, sticky = W)
young_avestan_iran_yz_month_lbl = Label(frame, text = "Month").grid(row = 113, column = 4, sticky = W)
young_avestan_iran_yz_month_ent = Entry(frame)
young_avestan_iran_yz_month_ent.grid(row = 114, column = 4, sticky = W)
young_avestan_iran_yz_year_lbl = Label(frame, text = "Year").grid(row = 113, column = 5, sticky = W)
young_avestan_iran_yz_year_ent = Entry(frame)
young_avestan_iran_yz_year_ent.grid(row = 114, column = 5, sticky = W)
young_avestan_iran_yz_bttn = Button(frame, text = "Calculate", command = young_avestan_iran_yz_converter).grid(row = 115, column = 3, columnspan = 3, sticky = W)

# Young Avestan calendar (Iran, Anno Zoroastres)                                                                                            
young_avestan_iran_az_lbl = Label(frame, text = "Young Avestan calendar (Iran, Anno Zoroastres)").grid(row = 112, column = 6, columnspan = 3, sticky = W)
young_avestan_iran_az_day_lbl = Label(frame, text = "Day").grid(row = 113, column = 6, sticky = W)
young_avestan_iran_az_day_ent = Entry(frame)
young_avestan_iran_az_day_ent.grid(row = 114, column = 6, sticky = W)
young_avestan_iran_az_month_lbl = Label(frame, text = "Month").grid(row = 113, column = 7, sticky = W)
young_avestan_iran_az_month_ent = Entry(frame)
young_avestan_iran_az_month_ent.grid(row = 114, column = 7, sticky = W)
young_avestan_iran_az_year_lbl = Label(frame, text = "Year").grid(row = 113, column = 8, sticky = W)
young_avestan_iran_az_year_ent = Entry(frame)
young_avestan_iran_az_year_ent.grid(row = 114, column = 8, sticky = W)
young_avestan_iran_az_bttn = Button(frame, text = "Calculate", command = young_avestan_iran_az_converter).grid(row = 115, column = 6, columnspan = 3, sticky = W)

# Young Avestan calendar (Iran, Zoroastrian Religious Era)                                                                                            
young_avestan_iran_zre_lbl = Label(frame, text = "Young Avestan calendar (Iran, Zoroastrian Religious Era)").grid(row = 112, column = 9, columnspan = 3, sticky = W)
young_avestan_iran_zre_day_lbl = Label(frame, text = "Day").grid(row = 113, column = 9, sticky = W)
young_avestan_iran_zre_day_ent = Entry(frame)
young_avestan_iran_zre_day_ent.grid(row = 114, column = 9, sticky = W)
young_avestan_iran_zre_month_lbl = Label(frame, text = "Month").grid(row = 113, column = 10, sticky = W)
young_avestan_iran_zre_month_ent = Entry(frame)
young_avestan_iran_zre_month_ent.grid(row = 114, column = 10, sticky = W)
young_avestan_iran_zre_year_lbl = Label(frame, text = "Year").grid(row = 113, column = 11, sticky = W)
young_avestan_iran_zre_year_ent = Entry(frame)
young_avestan_iran_zre_year_ent.grid(row = 114, column = 11, sticky = W)
young_avestan_iran_zre_bttn = Button(frame, text = "Calculate", command = young_avestan_iran_zre_converter).grid(row = 115, column = 9, columnspan = 3, sticky = W)

# Young Avestan Calendar (India, Yazdegerdi era)                                                                                            
young_avestan_india_yz_lbl = Label(frame, text = "Young Avestan Calendar (India, Yazdegerdi era)").grid(row = 116, column = 0, columnspan = 3, sticky = W)
young_avestan_india_yz_day_lbl = Label(frame, text = "Day").grid(row = 117, column = 0, sticky = W)
young_avestan_india_yz_day_ent = Entry(frame)
young_avestan_india_yz_day_ent.grid(row = 118, column = 0, sticky = W)
young_avestan_india_yz_month_lbl = Label(frame, text = "Month").grid(row = 117, column = 1, sticky = W)
young_avestan_india_yz_month_ent = Entry(frame)
young_avestan_india_yz_month_ent.grid(row = 118, column = 1, sticky = W)
young_avestan_india_yz_year_lbl = Label(frame, text = "Year").grid(row = 117, column = 2, sticky = W)
young_avestan_india_yz_year_ent = Entry(frame)
young_avestan_india_yz_year_ent.grid(row = 118, column = 2, sticky = W)
young_avestan_india_yz_bttn = Button(frame, text = "Calculate", command = young_avestan_india_yz_converter).grid(row = 119, column = 0, columnspan = 3, sticky = W)

# Young Avestan calendar (India, Anno Zoroastres)                                                                                            
young_avestan_india_az_lbl = Label(frame, text = "Young Avestan calendar (India, Anno Zoroastres)").grid(row = 116, column = 3, columnspan = 3, sticky = W)
young_avestan_india_az_day_lbl = Label(frame, text = "Day").grid(row = 117, column = 3, sticky = W)
young_avestan_india_az_day_ent = Entry(frame)
young_avestan_india_az_day_ent.grid(row = 118, column = 3, sticky = W)
young_avestan_india_az_month_lbl = Label(frame, text = "Month").grid(row = 117, column = 4, sticky = W)
young_avestan_india_az_month_ent = Entry(frame)
young_avestan_india_az_month_ent.grid(row = 118, column = 4, sticky = W)
young_avestan_india_az_year_lbl = Label(frame, text = "Year").grid(row = 117, column = 5, sticky = W)
young_avestan_india_az_year_ent = Entry(frame)
young_avestan_india_az_year_ent.grid(row = 118, column = 5, sticky = W)
young_avestan_india_az_bttn = Button(frame, text = "Calculate", command = young_avestan_india_az_converter).grid(row = 119, column = 3, columnspan = 3, sticky = W)

# Young Avestan calendar (India, Zoroastrian Religious Era)                                                                                            
young_avestan_india_zre_lbl = Label(frame, text = "Young Avestan calendar (India, Zoroastrian Religious Era)").grid(row = 116, column = 6, columnspan = 3, sticky = W)
young_avestan_india_zre_day_lbl = Label(frame, text = "Day").grid(row = 117, column = 6, sticky = W)
young_avestan_india_zre_day_ent = Entry(frame)
young_avestan_india_zre_day_ent.grid(row = 118, column = 6, sticky = W)
young_avestan_india_zre_month_lbl = Label(frame, text = "Month").grid(row = 117, column = 7, sticky = W)
young_avestan_india_zre_month_ent = Entry(frame)
young_avestan_india_zre_month_ent.grid(row = 118, column = 7, sticky = W)
young_avestan_india_zre_year_lbl = Label(frame, text = "Year").grid(row = 117, column = 8, sticky = W)
young_avestan_india_zre_year_ent = Entry(frame)
young_avestan_india_zre_year_ent.grid(row = 118, column = 8, sticky = W)
young_avestan_india_zre_bttn = Button(frame, text = "Calculate", command = young_avestan_india_zre_converter).grid(row = 119, column = 6, columnspan = 3, sticky = W)

# Shahanshahi calendar (Yazdegerdi era)                                                                                            
shahanshahi_yz_lbl = Label(frame, text = "Shahanshahi calendar (Yazdegerdi era)").grid(row = 116, column = 9, columnspan = 9, sticky = W)
shahanshahi_yz_day_lbl = Label(frame, text = "Day").grid(row = 117, column = 9, sticky = W)
shahanshahi_yz_day_ent = Entry(frame)
shahanshahi_yz_day_ent.grid(row = 118, column = 9, sticky = W)
shahanshahi_yz_month_lbl = Label(frame, text = "Month").grid(row = 117, column = 10, sticky = W)
shahanshahi_yz_month_ent = Entry(frame)
shahanshahi_yz_month_ent.grid(row = 118, column = 10, sticky = W)
shahanshahi_yz_year_lbl = Label(frame, text = "Year").grid(row = 117, column = 11, sticky = W)
shahanshahi_yz_year_ent = Entry(frame)
shahanshahi_yz_year_ent.grid(row = 118, column = 11, sticky = W)
shahanshahi_yz_bttn = Button(frame, text = "Calculate", command = shahanshahi_yz_converter).grid(row = 119, column = 9, columnspan = 3, sticky = W)

# Shahanshahi calendar (Anno Zoroastres)                                                                                            
shahanshahi_az_lbl = Label(frame, text = "Shahanshahi calendar (Anno Zoroastres)").grid(row = 120, column = 0, columnspan = 3, sticky = W)
shahanshahi_az_day_lbl = Label(frame, text = "Day").grid(row = 121, column = 0, sticky = W)
shahanshahi_az_day_ent = Entry(frame)
shahanshahi_az_day_ent.grid(row = 122, column = 0, sticky = W)
shahanshahi_az_month_lbl = Label(frame, text = "Month").grid(row = 121, column = 1, sticky = W)
shahanshahi_az_month_ent = Entry(frame)
shahanshahi_az_month_ent.grid(row = 122, column = 1, sticky = W)
shahanshahi_az_year_lbl = Label(frame, text = "Year").grid(row = 121, column = 2, sticky = W)
shahanshahi_az_year_ent = Entry(frame)
shahanshahi_az_year_ent.grid(row = 122, column = 2, sticky = W)
shahanshahi_az_bttn = Button(frame, text = "Calculate", command = shahanshahi_az_converter).grid(row = 123, column = 0, columnspan = 3, sticky = W)

# Shahanshahi calendar (Zoroastrian Religous Era)                                                                                            
shahanshahi_zre_lbl = Label(frame, text = "Shahanshahi calendar (Zoroastrian Religous Era)").grid(row = 120, column = 3, columnspan = 3, sticky = W)
shahanshahi_zre_day_lbl = Label(frame, text = "Day").grid(row = 121, column = 3, sticky = W)
shahanshahi_zre_day_ent = Entry(frame)
shahanshahi_zre_day_ent.grid(row = 122, column = 3, sticky = W)
shahanshahi_zre_month_lbl = Label(frame, text = "Month").grid(row = 121, column = 4, sticky = W)
shahanshahi_zre_month_ent = Entry(frame)
shahanshahi_zre_month_ent.grid(row = 122, column = 4, sticky = W)
shahanshahi_zre_year_lbl = Label(frame, text = "Year").grid(row = 123, column = 5, sticky = W)
shahanshahi_zre_year_ent = Entry(frame)
shahanshahi_zre_year_ent.grid(row = 122, column = 5, sticky = W)
shahanshahi_zre_bttn = Button(frame, text = "Calculate", command = shahanshahi_zre_converter).grid(row = 123, column = 3, columnspan = 3, sticky = W)

# Old Avestan calendar (Yazdegerdi era)                                                                                            
old_avestan_yz_lbl = Label(frame, text = "Old Avestan calendar (Yazdegerdi era)").grid(row = 120, column = 6, columnspan = 3, sticky = W)
old_avestan_yz_day_lbl = Label(frame, text = "Day").grid(row = 121, column = 6, sticky = W)
old_avestan_yz_day_ent = Entry(frame)
old_avestan_yz_day_ent.grid(row = 122, column = 6, sticky = W)
old_avestan_yz_month_lbl = Label(frame, text = "Month").grid(row = 121, column = 7, sticky = W)
old_avestan_yz_month_ent = Entry(frame)
old_avestan_yz_month_ent.grid(row = 122, column = 7, sticky = W)
old_avestan_yz_year_lbl = Label(frame, text = "Year").grid(row = 121, column = 8, sticky = W)
old_avestan_yz_year_ent = Entry(frame)
old_avestan_yz_year_ent.grid(row = 122, column = 8, sticky = W)
old_avestan_yz_bttn = Button(frame, text = "Calculate", command = old_avestan_yz_converter).grid(row = 123, column = 6, columnspan = 3, sticky = W)

# Old Avestan calendar (Anno Zoroastres)                                                                                            
old_avestan_az_lbl = Label(frame, text = "Old Avestan calendar (Anno Zoroastres)").grid(row = 120, column = 9, columnspan = 3, sticky = W)
old_avestan_az_day_lbl = Label(frame, text = "Day").grid(row = 121, column = 9, sticky = W)
old_avestan_az_day_ent = Entry(frame)
old_avestan_az_day_ent.grid(row = 122, column = 9, sticky = W)
old_avestan_az_month_lbl = Label(frame, text = "Month").grid(row = 121, column = 10, sticky = W)
old_avestan_az_month_ent = Entry(frame)
old_avestan_az_month_ent.grid(row = 122, column = 10, sticky = W)
old_avestan_az_year_lbl = Label(frame, text = "Year").grid(row = 121, column = 11, sticky = W)
old_avestan_az_year_ent = Entry(frame)
old_avestan_az_year_ent.grid(row = 122, column = 11, sticky = W)
old_avestan_az_bttn = Button(frame, text = "Calculate", command = old_avestan_az_converter).grid(row = 123, column = 9, columnspan = 3, sticky = W)

# Old Avestan calendar (Zarathushtrian Religious Era)                                                                                            
old_avestan_zre_lbl = Label(frame, text = "Old Avestan calendar (Zarathushtrian Religious Era)").grid(row = 124, column = 0, columnspan = 3, sticky = W)
old_avestan_zre_day_lbl = Label(frame, text = "Day").grid(row = 125, column = 0, sticky = W)
old_avestan_zre_day_ent = Entry(frame)
old_avestan_zre_day_ent.grid(row = 126, column = 0, sticky = W)
old_avestan_zre_month_lbl = Label(frame, text = "Month").grid(row = 125, column = 1, sticky = W)
old_avestan_zre_month_ent = Entry(frame)
old_avestan_zre_month_ent.grid(row = 126, column = 1, sticky = W)
old_avestan_zre_year_lbl = Label(frame, text = "Year").grid(row = 125, column = 2, sticky = W)
old_avestan_zre_year_ent = Entry(frame)
old_avestan_zre_year_ent.grid(row = 126, column = 2, sticky = W)
old_avestan_zre_bttn = Button(frame, text = "Calculate", command = old_avestan_zre_converter).grid(row = 127, column = 0, columnspan = 3, sticky = W)

# Fasli calendar (Yazdegerdi era)                                                                                            
fasli_yz_lbl = Label(frame, text = "Fasli calendar (Yazdegerdi era)").grid(row = 124, column = 3, columnspan = 3, sticky = W)
fasli_yz_day_lbl = Label(frame, text = "Day").grid(row = 125, column = 3, sticky = W)
fasli_yz_day_ent = Entry(frame)
fasli_yz_day_ent.grid(row = 126, column = 3, sticky = W)
fasli_yz_month_lbl = Label(frame, text = "Month").grid(row = 125, column = 4, sticky = W)
fasli_yz_month_ent = Entry(frame)
fasli_yz_month_ent.grid(row = 126, column = 4, sticky = W)
fasli_yz_year_lbl = Label(frame, text = "Year").grid(row = 125, column = 5, sticky = W)
fasli_yz_year_ent = Entry(frame)
fasli_yz_year_ent.grid(row = 126, column = 5, sticky = W)
fasli_yz_bttn = Button(frame, text = "Calculate", command = fasli_yz_converter).grid(row = 127, column = 3, columnspan = 3, sticky = W)

# Fasli calendar (Anno Zoroastres)                                                                                            
fasli_az_lbl = Label(frame, text = "Fasli calendar (Anno Zoroastres)").grid(row = 124, column = 6, columnspan = 3, sticky = W)
fasli_az_day_lbl = Label(frame, text = "Day").grid(row = 125, column = 6, sticky = W)
fasli_az_day_ent = Entry(frame)
fasli_az_day_ent.grid(row = 126, column = 6, sticky = W)
fasli_az_month_lbl = Label(frame, text = "Month").grid(row = 125, column = 7, sticky = W)
fasli_az_month_ent = Entry(frame)
fasli_az_month_ent.grid(row = 126, column = 7, sticky = W)
fasli_az_year_lbl = Label(frame, text = "Year").grid(row = 125, column = 8, sticky = W)
fasli_az_year_ent = Entry(frame)
fasli_az_year_ent.grid(row = 126, column = 8, sticky = W)
fasli_az_bttn = Button(frame, text = "Calculate", command = fasli_az_converter).grid(row = 127, column = 6, columnspan = 3, sticky = W)

# Fasli calendar (Zarathushtrian Religious Era)                                                                                           
fasli_zre_lbl = Label(frame, text = "Fasli calendar (ZRE)").grid(row = 124, column = 9, columnspan = 3, sticky = W)
fasli_zre_day_lbl = Label(frame, text = "Day").grid(row = 125, column = 9, sticky = W)
fasli_zre_day_ent = Entry(frame)
fasli_zre_day_ent.grid(row = 126, column = 9, sticky = W)
fasli_zre_month_lbl = Label(frame, text = "Month").grid(row = 125, column = 10, sticky = W)
fasli_zre_month_ent = Entry(frame)
fasli_zre_month_ent.grid(row = 126, column = 10, sticky = W)
fasli_zre_year_lbl = Label(frame, text = "Year").grid(row = 125, column = 11, sticky = W)
fasli_zre_year_ent = Entry(frame)
fasli_zre_year_ent.grid(row = 126, column = 11, sticky = W)
fasli_zre_bttn = Button(frame, text = "Calculate", command = fasli_zre_converter).grid(row = 127, column = 9, columnspan = 3, sticky = W)

# Sogdian calendar                                                                                            
sogdian_lbl = Label(frame, text = "Sogdian calendar").grid(row = 128, column = 0, columnspan = 3, sticky = W)
sogdian_day_lbl = Label(frame, text = "Day").grid(row = 129, column = 0, sticky = W)
sogdian_day_ent = Entry(frame)
sogdian_day_ent.grid(row = 130, column = 0, sticky = W)
sogdian_month_lbl = Label(frame, text = "Month").grid(row = 129, column = 1, sticky = W)
sogdian_month_ent = Entry(frame)
sogdian_month_ent.grid(row = 130, column = 1, sticky = W)
sogdian_year_lbl = Label(frame, text = "Year").grid(row = 129, column = 2, sticky = W)
sogdian_year_ent = Entry(frame)
sogdian_year_ent.grid(row = 130, column = 2, sticky = W)
sogdian_bttn = Button(frame, text = "Calculate", command = sogdian_converter).grid(row = 131, column = 0, columnspan = 3, sticky = W)

# Indian national calendar                                                                                            
indian_lbl = Label(frame, text = "Indian national calendar").grid(row = 128, column = 3, columnspan = 3, sticky = W)
indian_day_lbl = Label(frame, text = "Day").grid(row = 129, column = 3, sticky = W)
indian_day_ent = Entry(frame)
indian_day_ent.grid(row = 130, column = 3, sticky = W)
indian_month_lbl = Label(frame, text = "Month").grid(row = 129, column = 4, sticky = W)
indian_month_ent = Entry(frame)
indian_month_ent.grid(row = 130, column = 4, sticky = W)
indian_year_lbl = Label(frame, text = "Year").grid(row = 129, column = 5, sticky = W)
indian_year_ent = Entry(frame)
indian_year_ent.grid(row = 130, column = 5, sticky = W)
indian_bttn = Button(frame, text = "Calculate", command = indian_converter).grid(row = 131, column = 3, columnspan = 3, sticky = W)

# Mandaean calendar                                                                                            
mandaean_lbl = Label(frame, text = "Mandaean calendar").grid(row = 128, column = 6, columnspan = 3, sticky = W)
mandaean_day_lbl = Label(frame, text = "Day").grid(row = 129, column = 6, sticky = W)
mandaean_day_ent = Entry(frame)
mandaean_day_ent.grid(row = 130, column = 6, sticky = W)
mandaean_month_lbl = Label(frame, text = "Month").grid(row = 129, column = 7, sticky = W)
mandaean_month_ent = Entry(frame)
mandaean_month_ent.grid(row = 130, column = 7, sticky = W)
mandaean_year_lbl = Label(frame, text = "Year").grid(row = 129, column = 8, sticky = W)
mandaean_year_ent = Entry(frame)
mandaean_year_ent.grid(row = 130, column = 8, sticky = W)
mandaean_bttn = Button(frame, text = "Calculate", command = mandaean_converter).grid(row = 131, column = 6, columnspan = 3, sticky = W)

# Sidereal Bahá'í calendar                                                                                            
bahai_sid_lbl = Label(frame, text = "Sidereal Bahá'í calendar").grid(row = 128, column = 9, columnspan = 3, sticky = W)
bahai_sid_day_lbl = Label(frame, text = "Day").grid(row = 129, column = 9, sticky = W)
bahai_sid_day_ent = Entry(frame)
bahai_sid_day_ent.grid(row = 130, column = 9, sticky = W)
bahai_sid_month_lbl = Label(frame, text = "Month").grid(row = 129, column = 10, sticky = W)
bahai_sid_month_ent = Entry(frame)
bahai_sid_month_ent.grid(row = 130, column = 10, sticky = W)
bahai_sid_year_lbl = Label(frame, text = "Year").grid(row = 129, column = 11, sticky = W)
bahai_sid_year_ent = Entry(frame)
bahai_sid_year_ent.grid(row = 130, column = 11, sticky = W)
bahai_sid_bttn = Button(frame, text = "Calculate", command = bahai_sid_converter).grid(row = 131, column = 9, columnspan = 3, sticky = W)

# Sothic calendar                                                                                            
sothic_lbl = Label(frame, text = "Sothic calendar").grid(row = 132, column = 0, columnspan = 3, sticky = W)
sothic_day_lbl = Label(frame, text = "Day").grid(row = 133, column = 0, sticky = W)
sothic_day_ent = Entry(frame)
sothic_day_ent.grid(row = 134, column = 0, sticky = W)
sothic_month_lbl = Label(frame, text = "Month").grid(row = 133, column = 1, sticky = W)
sothic_month_ent = Entry(frame)
sothic_month_ent.grid(row = 134, column = 1, sticky = W)
sothic_year_lbl = Label(frame, text = "Year").grid(row = 133, column = 2, sticky = W)
sothic_year_ent = Entry(frame)
sothic_year_ent.grid(row = 134, column = 2, sticky = W)
sothic_bttn = Button(frame, text = "Calculate", command = sothic_converter).grid(row = 135, column = 0, columnspan = 3, sticky = W)

# Madhyama solar calendar (Kali Yuga)                                                                                            
madhyama_solar_ky_lbl = Label(frame, text = "Madhyama solar calendar (Kali Yuga)").grid(row = 132, column = 3, columnspan = 3, sticky = W)
madhyama_solar_ky_day_lbl = Label(frame, text = "Day").grid(row = 133, column = 3, sticky = W)
madhyama_solar_ky_day_ent = Entry(frame)
madhyama_solar_ky_day_ent.grid(row = 134, column = 3, sticky = W)
madhyama_solar_ky_month_lbl = Label(frame, text = "Month").grid(row = 133, column = 4, sticky = W)
madhyama_solar_ky_month_ent = Entry(frame)
madhyama_solar_ky_month_ent.grid(row = 134, column = 4, sticky = W)
madhyama_solar_ky_year_lbl = Label(frame, text = "Year").grid(row = 133, column = 5, sticky = W)
madhyama_solar_ky_year_ent = Entry(frame)
madhyama_solar_ky_year_ent.grid(row = 134, column = 5, sticky = W)
madhyama_solar_ky_bttn = Button(frame, text = "Calculate", command = madhyama_solar_ky_converter).grid(row = 135, column = 3, columnspan = 3, sticky = W)

# Madhyama solar calendar (Vikram Samvat)                                                                                            
madhyama_solar_vs_lbl = Label(frame, text = "Madhyama solar calendar (Vikram Samvat)").grid(row = 132, column = 6, columnspan = 3, sticky = W)
madhyama_solar_vs_day_lbl = Label(frame, text = "Day").grid(row = 133, column = 6, sticky = W)
madhyama_solar_vs_day_ent = Entry(frame)
madhyama_solar_vs_day_ent.grid(row = 134, column = 6, sticky = W)
madhyama_solar_vs_month_lbl = Label(frame, text = "Month").grid(row = 133, column = 7, sticky = W)
madhyama_solar_vs_month_ent = Entry(frame)
madhyama_solar_vs_month_ent.grid(row = 134, column = 7, sticky = W)
madhyama_solar_vs_year_lbl = Label(frame, text = "Year").grid(row = 133, column = 8, sticky = W)
madhyama_solar_vs_year_ent = Entry(frame)
madhyama_solar_vs_year_ent.grid(row = 134, column = 8, sticky = W)
madhyama_solar_vs_bttn = Button(frame, text = "Calculate", command = madhyama_solar_vs_converter).grid(row = 135, column = 6, columnspan = 3, sticky = W)

# Madhyama solar calendar (Shaka Era)                                                                                            
madhyama_solar_se_lbl = Label(frame, text = "Madhyama solar calendar (Shaka Era)").grid(row = 132, column = 9, columnspan = 3, sticky = W)
madhyama_solar_se_day_lbl = Label(frame, text = "Day").grid(row = 133, column = 9, sticky = W)
madhyama_solar_se_day_ent = Entry(frame)
madhyama_solar_se_day_ent.grid(row = 134, column = 9, sticky = W)
madhyama_solar_se_month_lbl = Label(frame, text = "Month").grid(row = 133, column = 10, sticky = W)
madhyama_solar_se_month_ent = Entry(frame)
madhyama_solar_se_month_ent.grid(row = 134, column = 10, sticky = W)
madhyama_solar_se_year_lbl = Label(frame, text = "Year").grid(row = 133, column = 11, sticky = W)
madhyama_solar_se_year_ent = Entry(frame)
madhyama_solar_se_year_ent.grid(row = 134, column = 11, sticky = W)
madhyama_solar_se_bttn = Button(frame, text = "Calculate", command = madhyama_solar_se_converter).grid(row = 135, column = 9, columnspan = 3, sticky = W)

# Tamil calendar                                                                                            
tamil_lbl = Label(frame, text = "Tamil calendar").grid(row = 136, column = 0, columnspan = 3, sticky = W)
tamil_day_lbl = Label(frame, text = "Day").grid(row = 137, column = 0, sticky = W)
tamil_day_ent = Entry(frame)
tamil_day_ent.grid(row = 138, column = 0, sticky = W)
tamil_month_lbl = Label(frame, text = "Month").grid(row = 137, column = 1, sticky = W)
tamil_month_ent = Entry(frame)
tamil_month_ent.grid(row = 138, column = 1, sticky = W)
tamil_year_lbl = Label(frame, text = "Year").grid(row = 137, column = 2, sticky = W)
tamil_year_ent = Entry(frame)
tamil_year_ent.grid(row = 138, column = 2, sticky = W)
tamil_bttn = Button(frame, text = "Calculate", command = tamil_converter).grid(row = 139, column = 0, columnspan = 3, sticky = W)

# Madhyama lunisolar calendar (Kali Yuga)                                                                                            
madhyama_lunar_ky_lbl = Label(frame, text = "Madhyama lunisolar calendar (Kali Yuga)").grid(row = 136, column = 3, columnspan = 3, sticky = W)
madhyama_lunar_ky_day_lbl = Label(frame, text = "Tithi").grid(row = 137, column = 3, sticky = W)
madhyama_lunar_ky_day_ent = Entry(frame)
madhyama_lunar_ky_day_ent.grid(row = 138, column = 3, sticky = W)
madhyama_lunar_ky_month_lbl = Label(frame, text = "Month").grid(row = 137, column = 4, sticky = W)
madhyama_lunar_ky_month_ent = Entry(frame)
madhyama_lunar_ky_month_ent.grid(row = 138, column = 4, sticky = W)
madhyama_lunar_ky_year_lbl = Label(frame, text = "Year").grid(row = 137, column = 5, sticky = W)
madhyama_lunar_ky_year_ent = Entry(frame)
madhyama_lunar_ky_year_ent.grid(row = 138, column = 5, sticky = W)
madhyama_lunar_ky_bttn = Button(frame, text = "Calculate", command = madhyama_lunar_ky_converter).grid(row = 139, column = 3, columnspan = 3, sticky = W)

# Madhyama lunisolar calendar (Vikram Samvat)                                                                                            
madhyama_lunar_vs_lbl = Label(frame, text = "Madhyama lunisolar calendar (Vikram Samvat)").grid(row = 136, column = 6, columnspan = 3, sticky = W)
madhyama_lunar_vs_day_lbl = Label(frame, text = "Tithi").grid(row = 137, column = 6, sticky = W)
madhyama_lunar_vs_day_ent = Entry(frame)
madhyama_lunar_vs_day_ent.grid(row = 138, column = 6, sticky = W)
madhyama_lunar_vs_month_lbl = Label(frame, text = "Month").grid(row = 137, column = 7, sticky = W)
madhyama_lunar_vs_month_ent = Entry(frame)
madhyama_lunar_vs_month_ent.grid(row = 138, column = 7, sticky = W)
madhyama_lunar_vs_year_lbl = Label(frame, text = "Year").grid(row = 137, column = 8, sticky = W)
madhyama_lunar_vs_year_ent = Entry(frame)
madhyama_lunar_vs_year_ent.grid(row = 138, column = 8, sticky = W)
madhyama_lunar_vs_bttn = Button(frame, text = "Calculate", command = madhyama_lunar_vs_converter).grid(row = 139, column = 6, columnspan = 3, sticky = W)

# Madhyama lunisolar calendar (Shaka Era)                                                                                            
madhyama_lunar_se_lbl = Label(frame, text = "Madhyama lunisolar calendar (Shaka Era)").grid(row = 136, column = 9, columnspan = 3, sticky = W)
madhyama_lunar_se_day_lbl = Label(frame, text = "Tithi").grid(row = 137, column = 9, sticky = W)
madhyama_lunar_se_day_ent = Entry(frame)
madhyama_lunar_se_day_ent.grid(row = 138, column = 9, sticky = W)
madhyama_lunar_se_month_lbl = Label(frame, text = "Month").grid(row = 137, column = 10, sticky = W)
madhyama_lunar_se_month_ent = Entry(frame)
madhyama_lunar_se_month_ent.grid(row = 138, column = 10, sticky = W)
madhyama_lunar_se_year_lbl = Label(frame, text = "Year").grid(row = 137, column = 11, sticky = W)
madhyama_lunar_se_year_ent = Entry(frame)
madhyama_lunar_se_year_ent.grid(row = 138, column = 11, sticky = W)
madhyama_lunar_se_bttn = Button(frame, text = "Calculate", command = madhyama_lunar_se_converter).grid(row = 139, column = 9, columnspan = 3, sticky = W)

# Traditional Bengali calendar                                                                                            
sid_bengali_lbl = Label(frame, text = "Traditional Bengali calendar").grid(row = 140, column = 0, columnspan = 3, sticky = W)
sid_bengali_day_lbl = Label(frame, text = "Day").grid(row = 141, column = 0, sticky = W)
sid_bengali_day_ent = Entry(frame)
sid_bengali_day_ent.grid(row = 142, column = 0, sticky = W)
sid_bengali_month_lbl = Label(frame, text = "Month").grid(row = 141, column = 1, sticky = W)
sid_bengali_month_ent = Entry(frame)
sid_bengali_month_ent.grid(row = 142, column = 1, sticky = W)
sid_bengali_year_lbl = Label(frame, text = "Year").grid(row = 141, column = 2, sticky = W)
sid_bengali_year_ent = Entry(frame)
sid_bengali_year_ent.grid(row = 142, column = 2, sticky = W)
sid_bengali_bttn = Button(frame, text = "Calculate", command = sid_bengali_converter).grid(row = 143, column = 0, columnspan = 3, sticky = W)

# Modern Bengali calendar                                                                                            
obs_bengali_lbl = Label(frame, text = "Modern Bengali calendar").grid(row = 140, column = 3, columnspan = 3, sticky = W)
obs_bengali_day_lbl = Label(frame, text = "Day").grid(row = 141, column = 3, sticky = W)
obs_bengali_day_ent = Entry(frame)
obs_bengali_day_ent.grid(row = 142, column = 3, sticky = W)
obs_bengali_month_lbl = Label(frame, text = "Month").grid(row = 141, column = 4, sticky = W)
obs_bengali_month_ent = Entry(frame)
obs_bengali_month_ent.grid(row = 142, column = 4, sticky = W)
obs_bengali_year_lbl = Label(frame, text = "Year").grid(row = 141, column = 5, sticky = W)
obs_bengali_year_ent = Entry(frame)
obs_bengali_year_ent.grid(row = 142, column = 5, sticky = W)
obs_bengali_bttn = Button(frame, text = "Calculate", command = obs_bengali_converter).grid(row = 143, column = 3, columnspan = 3, sticky = W)

# Traditional Indian solar calendar (Kali Yuga)                                                                                        
siddhantic_solar_ky_lbl = Label(frame, text = "Traditional Indian solar calendar (Kali Yuga)").grid(row = 140, column = 6, columnspan = 3, sticky = W)
siddhantic_solar_ky_day_lbl = Label(frame, text = "Day").grid(row = 141, column = 6, sticky = W)
siddhantic_solar_ky_day_ent = Entry(frame)
siddhantic_solar_ky_day_ent.grid(row = 142, column = 6, sticky = W)
siddhantic_solar_ky_month_lbl = Label(frame, text = "Month").grid(row = 141, column = 7, sticky = W)
siddhantic_solar_ky_month_ent = Entry(frame)
siddhantic_solar_ky_month_ent.grid(row = 142, column = 7, sticky = W)
siddhantic_solar_ky_year_lbl = Label(frame, text = "Year").grid(row = 141, column = 8, sticky = W)
siddhantic_solar_ky_year_ent = Entry(frame)
siddhantic_solar_ky_year_ent.grid(row = 142, column = 8, sticky = W)
siddhantic_solar_ky_bttn = Button(frame, text = "Calculate", command = siddhantic_solar_ky_converter).grid(row = 143, column = 6, columnspan = 3, sticky = W)

# Traditional Indian solar calendar (Saka Era)                                                                                       
siddhantic_solar_se_lbl = Label(frame, text = "Traditional Indian solar calendar (Śaka Era)").grid(row = 140, column = 9, columnspan = 3, sticky = W)
siddhantic_solar_se_day_lbl = Label(frame, text = "Day").grid(row = 141, column = 9, sticky = W)
siddhantic_solar_se_day_ent = Entry(frame)
siddhantic_solar_se_day_ent.grid(row = 142, column = 9, sticky = W)
siddhantic_solar_se_month_lbl = Label(frame, text = "Month").grid(row = 141, column = 10, sticky = W)
siddhantic_solar_se_month_ent = Entry(frame)
siddhantic_solar_se_month_ent.grid(row = 142, column = 10, sticky = W)
siddhantic_solar_se_year_lbl = Label(frame, text = "Year").grid(row = 141, column = 11, sticky = W)
siddhantic_solar_se_year_ent = Entry(frame)
siddhantic_solar_se_year_ent.grid(row = 142, column = 11, sticky = W)
siddhantic_solar_se_bttn = Button(frame, text = "Calculate", command = siddhantic_solar_se_converter).grid(row = 143, column = 9, columnspan = 3, sticky = W)

# Traditional Indian solar calendar (Vikram Samvat)                                                                                        
siddhantic_solar_vs_lbl = Label(frame, text = "Traditional Indian solar calendar (Vikram Samvat)").grid(row = 148, column = 0, columnspan = 3, sticky = W)
siddhantic_solar_vs_day_lbl = Label(frame, text = "Day").grid(row = 149, column = 0, sticky = W)
siddhantic_solar_vs_day_ent = Entry(frame)
siddhantic_solar_vs_day_ent.grid(row = 150, column = 0, sticky = W)
siddhantic_solar_vs_month_lbl = Label(frame, text = "Month").grid(row = 149, column = 1, sticky = W)
siddhantic_solar_vs_month_ent = Entry(frame)
siddhantic_solar_vs_month_ent.grid(row = 150, column = 1, sticky = W)
siddhantic_solar_vs_year_lbl = Label(frame, text = "Year").grid(row = 149, column = 2, sticky = W)
siddhantic_solar_vs_year_ent = Entry(frame)
siddhantic_solar_vs_year_ent.grid(row = 150, column = 2, sticky = W)
siddhantic_solar_vs_bttn = Button(frame, text = "Calculate", command = siddhantic_solar_vs_converter).grid(row = 151, column = 0, columnspan = 3, sticky = W)

# Bangladeshi calendar (1373)
bangladeshi1373_lbl = Label(frame, text = "Bangladeshi calendar (1373) calendar").grid(row = 148, column = 3, columnspan = 3, sticky = W)
bangladeshi1373_day_lbl = Label(frame, text = "Day").grid(row = 149, column = 3, sticky = W)
bangladeshi1373_day_ent = Entry(frame)
bangladeshi1373_day_ent.grid(row = 150, column = 3, sticky = W)
bangladeshi1373_month_lbl = Label(frame, text = "Month").grid(row = 149, column = 4, sticky = W)
bangladeshi1373_month_ent = Entry(frame)
bangladeshi1373_month_ent.grid(row = 150, column = 4, sticky = W)
bangladeshi1373_year_lbl = Label(frame, text = "Year").grid(row = 149, column = 5, sticky = W)
bangladeshi1373_year_ent = Entry(frame)
bangladeshi1373_year_ent.grid(row = 150, column = 5, sticky = W)
bangladeshi1373_bttn = Button(frame, text = "Calculate", command = bangladeshi1373_converter).grid(row = 151, column = 3, columnspan = 3, sticky = W)

# Bangladeshi calendar (1426)
bangladeshi1426_lbl = Label(frame, text = "Bangladeshi calendar (1426) calendar").grid(row = 148, column = 6, columnspan = 3, sticky = W)
bangladeshi1426_day_lbl = Label(frame, text = "Day").grid(row = 149, column = 6, sticky = W)
bangladeshi1426_day_ent = Entry(frame)
bangladeshi1426_day_ent.grid(row = 150, column = 6, sticky = W)
bangladeshi1426_month_lbl = Label(frame, text = "Month").grid(row = 149, column = 7, sticky = W)
bangladeshi1426_month_ent = Entry(frame)
bangladeshi1426_month_ent.grid(row = 150, column = 7, sticky = W)
bangladeshi1426_year_lbl = Label(frame, text = "Year").grid(row = 149, column = 8, sticky = W)
bangladeshi1426_year_ent = Entry(frame)
bangladeshi1426_year_ent.grid(row = 150, column = 8, sticky = W)
bangladeshi1426_bttn = Button(frame, text = "Calculate", command = bangladeshi1426_converter).grid(row = 151, column = 6, columnspan = 3, sticky = W)

# Traditional Indian lunisolar calendar (Kali Yuga)                                                                                            
siddhantic_lunisolar_ky_lbl = Label(frame, text = "Traditional Indian lunisolar calendar (Kali Yuga)").grid(row = 148, column = 9, columnspan = 3, sticky = W)
siddhantic_lunisolar_ky_day_lbl = Label(frame, text = "Tithi").grid(row = 149, column = 9, sticky = W)
siddhantic_lunisolar_ky_day_ent = Entry(frame)
siddhantic_lunisolar_ky_day_ent.grid(row = 150, column = 9, sticky = W)
siddhantic_lunisolar_ky_month_lbl = Label(frame, text = "Month").grid(row = 149, column = 10, sticky = W)
siddhantic_lunisolar_ky_month_ent = Entry(frame)
siddhantic_lunisolar_ky_month_ent.grid(row = 150, column = 10, sticky = W)
siddhantic_lunisolar_ky_year_lbl = Label(frame, text = "Year").grid(row = 149, column = 11, sticky = W)
siddhantic_lunisolar_ky_year_ent = Entry(frame)
siddhantic_lunisolar_ky_year_ent.grid(row = 150, column = 11, sticky = W)
siddhantic_lunisolar_ky_bttn = Button(frame, text = "Calculate", command = siddhantic_lunisolar_ky_converter).grid(row = 151, column = 9, columnspan = 3, sticky = W)

# Traditional Indian lunisolar calendar (Ṡaka Era)                                                                                            
siddhantic_lunisolar_se_lbl = Label(frame, text = "Traditional Indian lunisolar calendar (Ṡaka Era)").grid(row = 152, column = 0, columnspan = 3, sticky = W)
siddhantic_lunisolar_se_day_lbl = Label(frame, text = "Tithi").grid(row = 153, column = 0, sticky = W)
siddhantic_lunisolar_se_day_ent = Entry(frame)
siddhantic_lunisolar_se_day_ent.grid(row = 154, column = 0, sticky = W)
siddhantic_lunisolar_se_month_lbl = Label(frame, text = "Month").grid(row = 153, column = 1, sticky = W)
siddhantic_lunisolar_se_month_ent = Entry(frame)
siddhantic_lunisolar_se_month_ent.grid(row = 154, column = 1, sticky = W)
siddhantic_lunisolar_se_year_lbl = Label(frame, text = "Year").grid(row = 153, column = 2, sticky = W)
siddhantic_lunisolar_se_year_ent = Entry(frame)
siddhantic_lunisolar_se_year_ent.grid(row = 154, column = 2, sticky = W)
siddhantic_lunisolar_se_bttn = Button(frame, text = "Calculate", command = siddhantic_lunisolar_se_converter).grid(row = 155, column = 0, columnspan = 3, sticky = W)

# Traditional Indian lunisolar calendar (Vikram Samvat)                                                                                            
siddhantic_lunisolar_vs_lbl = Label(frame, text = "Traditional Indian lunisolar calendar (Vikram Samvat)").grid(row = 152, column = 3, columnspan = 3, sticky = W)
siddhantic_lunisolar_vs_day_lbl = Label(frame, text = "Tithi").grid(row = 153, column = 3, sticky = W)
siddhantic_lunisolar_vs_day_ent = Entry(frame)
siddhantic_lunisolar_vs_day_ent.grid(row = 154, column = 3, sticky = W)
siddhantic_lunisolar_vs_month_lbl = Label(frame, text = "Month").grid(row = 153, column = 4, sticky = W)
siddhantic_lunisolar_vs_month_ent = Entry(frame)
siddhantic_lunisolar_vs_month_ent.grid(row = 154, column = 4, sticky = W)
siddhantic_lunisolar_vs_year_lbl = Label(frame, text = "Year").grid(row = 153, column = 5, sticky = W)
siddhantic_lunisolar_vs_year_ent = Entry(frame)
siddhantic_lunisolar_vs_year_ent.grid(row = 154, column = 5, sticky = W)
siddhantic_lunisolar_vs_bttn = Button(frame, text = "Calculate", command = siddhantic_lunisolar_vs_converter).grid(row = 155, column = 3, columnspan = 3, sticky = W)

# Sidereal Tripuri calendar                                                                                            
sid_tripuri_lbl = Label(frame, text = "Sidereal Tripuri calendar").grid(row = 152, column = 6, columnspan = 3, sticky = W)
sid_tripuri_day_lbl = Label(frame, text = "Day").grid(row = 153, column = 6, sticky = W)
sid_tripuri_day_ent = Entry(frame)
sid_tripuri_day_ent.grid(row = 154, column = 6, sticky = W)
sid_tripuri_month_lbl = Label(frame, text = "Month").grid(row = 153, column = 7, sticky = W)
sid_tripuri_month_ent = Entry(frame)
sid_tripuri_month_ent.grid(row = 154, column = 7, sticky = W)
sid_tripuri_year_lbl = Label(frame, text = "Year").grid(row = 153, column = 8, sticky = W)
sid_tripuri_year_ent = Entry(frame)
sid_tripuri_year_ent.grid(row = 154, column = 8, sticky = W)
sid_tripuri_bttn = Button(frame, text = "Calculate", command = sid_tripuri_converter).grid(row = 155, column = 6, columnspan = 3, sticky = W)

# Tropical Tripuri calendar                                                                                            
trop_tripuri_lbl = Label(frame, text = "Tropical Tripuri calendar").grid(row = 152, column = 9, columnspan = 3, sticky = W)
trop_tripuri_day_lbl = Label(frame, text = "Day").grid(row = 153, column = 9, sticky = W)
trop_tripuri_day_ent = Entry(frame)
trop_tripuri_day_ent.grid(row = 154, column = 9, sticky = W)
trop_tripuri_month_lbl = Label(frame, text = "Month").grid(row = 153, column = 10, sticky = W)
trop_tripuri_month_ent = Entry(frame)
trop_tripuri_month_ent.grid(row = 154, column = 10, sticky = W)
trop_tripuri_year_lbl = Label(frame, text = "Year").grid(row = 153, column = 11, sticky = W)
trop_tripuri_year_ent = Entry(frame)
trop_tripuri_year_ent.grid(row = 154, column = 11, sticky = W)
trop_tripuri_bttn = Button(frame, text = "Calculate", command = trop_tripuri_converter).grid(row = 155, column = 9, columnspan = 3, sticky = W)

# Observational Indian solar calendar (Kali Yuga)                                                                                            
obs_indian_solar_ky_lbl = Label(frame, text = "Observational Indian solar calendar (Kali Yuga)").grid(row = 161, column = 0, columnspan = 3, sticky = W)
obs_indian_solar_ky_day_lbl = Label(frame, text = "Day").grid(row = 162, column = 0, sticky = W)
obs_indian_solar_ky_day_ent = Entry(frame)
obs_indian_solar_ky_day_ent.grid(row = 163, column = 0, sticky = W)
obs_indian_solar_ky_month_lbl = Label(frame, text = "Month").grid(row = 162, column = 1, sticky = W)
obs_indian_solar_ky_month_ent = Entry(frame)
obs_indian_solar_ky_month_ent.grid(row = 163, column = 1, sticky = W)
obs_indian_solar_ky_year_lbl = Label(frame, text = "Year").grid(row = 162, column = 2, sticky = W)
obs_indian_solar_ky_year_ent = Entry(frame)
obs_indian_solar_ky_year_ent.grid(row = 163, column = 2, sticky = W)
obs_indian_solar_ky_bttn = Button(frame, text = "Calculate", command = obs_indian_solar_ky_converter).grid(row = 164, column = 0, columnspan = 3, sticky = W)

# Observational Indian solar calendar (Śaka Era)                                                                                            
obs_indian_solar_se_lbl = Label(frame, text = "Observational Indian solar calendar (Śaka Era)").grid(row = 161, column = 3, columnspan = 3, sticky = W)
obs_indian_solar_se_day_lbl = Label(frame, text = "Day").grid(row = 162, column = 3, sticky = W)
obs_indian_solar_se_day_ent = Entry(frame)
obs_indian_solar_se_day_ent.grid(row = 163, column = 3, sticky = W)
obs_indian_solar_se_month_lbl = Label(frame, text = "Month").grid(row = 162, column = 4, sticky = W)
obs_indian_solar_se_month_ent = Entry(frame)
obs_indian_solar_se_month_ent.grid(row = 163, column = 4, sticky = W)
obs_indian_solar_se_year_lbl = Label(frame, text = "Year").grid(row = 162, column = 5, sticky = W)
obs_indian_solar_se_year_ent = Entry(frame)
obs_indian_solar_se_year_ent.grid(row = 163, column = 5, sticky = W)
obs_indian_solar_se_bttn = Button(frame, text = "Calculate", command = obs_indian_solar_se_converter).grid(row = 164, column = 3, columnspan = 3, sticky = W)

# Observational Indian solar calendar (Vikram Samvat)                                                                                            
obs_indian_solar_vs_lbl = Label(frame, text = "Observational Indian solar calendar (Vikram Samvat)").grid(row = 161, column = 6, columnspan = 3, sticky = W)
obs_indian_solar_vs_day_lbl = Label(frame, text = "Day").grid(row = 162, column = 6, sticky = W)
obs_indian_solar_vs_day_ent = Entry(frame)
obs_indian_solar_vs_day_ent.grid(row = 163, column = 6, sticky = W)
obs_indian_solar_vs_month_lbl = Label(frame, text = "Month").grid(row = 162, column = 7, sticky = W)
obs_indian_solar_vs_month_ent = Entry(frame)
obs_indian_solar_vs_month_ent.grid(row = 163, column = 7, sticky = W)
obs_indian_solar_vs_year_lbl = Label(frame, text = "Year").grid(row = 162, column = 8, sticky = W)
obs_indian_solar_vs_year_ent = Entry(frame)
obs_indian_solar_vs_year_ent.grid(row = 163, column = 8, sticky = W)
obs_indian_solar_vs_bttn = Button(frame, text = "Calculate", command = obs_indian_solar_vs_converter).grid(row = 164, column = 6, columnspan = 3, sticky = W)

# Mughal Faṣlī calendar                                                                                            
mughal_lbl = Label(frame, text = "Mughal Faṣlī calendar").grid(row = 161, column = 9, columnspan = 3, sticky = W)
mughal_day_lbl = Label(frame, text = "Day").grid(row = 162, column = 9, sticky = W)
mughal_day_ent = Entry(frame)
mughal_day_ent.grid(row = 163, column = 9, sticky = W)
mughal_month_lbl = Label(frame, text = "Month").grid(row = 162, column = 10, sticky = W)
mughal_month_ent = Entry(frame)
mughal_month_ent.grid(row = 163, column = 10, sticky = W)
mughal_year_lbl = Label(frame, text = "Year").grid(row = 162, column = 11, sticky = W)
mughal_year_ent = Entry(frame)
mughal_year_ent.grid(row = 163, column = 11, sticky = W)
mughal_bttn = Button(frame, text = "Calculate", command = mughal_converter).grid(row = 164, column = 9, columnspan = 3, sticky = W)

# Odia calendar                                                                                            
odia_lbl = Label(frame, text = "Odia calendar").grid(row = 165, column = 0, columnspan = 3, sticky = W)
odia_day_lbl = Label(frame, text = "Day").grid(row = 166, column = 0, sticky = W)
odia_day_ent = Entry(frame)
odia_day_ent.grid(row = 167, column = 0, sticky = W)
odia_month_lbl = Label(frame, text = "Month").grid(row = 166, column = 1, sticky = W)
odia_month_ent = Entry(frame)
odia_month_ent.grid(row = 167, column = 1, sticky = W)
odia_year_lbl = Label(frame, text = "Year").grid(row = 166, column = 2, sticky = W)
odia_year_ent = Entry(frame)
odia_year_ent.grid(row = 167, column = 2, sticky = W)
odia_bttn = Button(frame, text = "Calculate", command = odia_converter).grid(row = 168, column = 0, columnspan = 3, sticky = W)

# Observational Indian lunisolar calendar (Kali Yuga)                                                                                            
obs_indian_lunisolar_ky_lbl = Label(frame, text = "Observational Indian lunisolar calendar (Kali Yuga)").grid(row = 165, column = 3, columnspan = 3, sticky = W)
obs_indian_lunisolar_ky_day_lbl = Label(frame, text = "Tithi").grid(row = 166, column = 3, sticky = W)
obs_indian_lunisolar_ky_day_ent = Entry(frame)
obs_indian_lunisolar_ky_day_ent.grid(row = 167, column = 3, sticky = W)
obs_indian_lunisolar_ky_month_lbl = Label(frame, text = "Month").grid(row = 166, column = 4, sticky = W)
obs_indian_lunisolar_ky_month_ent = Entry(frame)
obs_indian_lunisolar_ky_month_ent.grid(row = 167, column = 4, sticky = W)
obs_indian_lunisolar_ky_year_lbl = Label(frame, text = "Year").grid(row = 166, column = 5, sticky = W)
obs_indian_lunisolar_ky_year_ent = Entry(frame)
obs_indian_lunisolar_ky_year_ent.grid(row = 167, column = 5, sticky = W)
obs_indian_lunisolar_ky_bttn = Button(frame, text = "Calculate", command = obs_indian_lunisolar_ky_converter).grid(row = 168, column = 3, columnspan = 3, sticky = W)

# Observational Indian lunisolar calendar (Śaka Era)                                                                         
obs_indian_lunisolar_se_lbl = Label(frame, text = "Observational Indian lunisolar calendar (Śaka Era)").grid(row = 165, column = 6, columnspan = 3, sticky = W)
obs_indian_lunisolar_se_day_lbl = Label(frame, text = "Tithi").grid(row = 166, column = 6, sticky = W)
obs_indian_lunisolar_se_day_ent = Entry(frame)
obs_indian_lunisolar_se_day_ent.grid(row = 167, column = 6, sticky = W)
obs_indian_lunisolar_se_month_lbl = Label(frame, text = "Month").grid(row = 166, column = 7, sticky = W)
obs_indian_lunisolar_se_month_ent = Entry(frame)
obs_indian_lunisolar_se_month_ent.grid(row = 167, column = 7, sticky = W)
obs_indian_lunisolar_se_year_lbl = Label(frame, text = "Year").grid(row = 166, column = 8, sticky = W)
obs_indian_lunisolar_se_year_ent = Entry(frame)
obs_indian_lunisolar_se_year_ent.grid(row = 167, column = 8, sticky = W)
obs_indian_lunisolar_se_bttn = Button(frame, text = "Calculate", command = obs_indian_lunisolar_se_converter).grid(row = 168, column = 6, columnspan = 3, sticky = W)

# Observational Indian lunisolar calendar (Vikram Samvat)                                                                                            
obs_indian_lunisolar_vs_lbl = Label(frame, text = "Observational Indian lunisolar calendar (Vikram Samvat)").grid(row = 165, column = 9, columnspan = 3, sticky = W)
obs_indian_lunisolar_vs_day_lbl = Label(frame, text = "Tithi").grid(row = 166, column = 9, sticky = W)
obs_indian_lunisolar_vs_day_ent = Entry(frame)
obs_indian_lunisolar_vs_day_ent.grid(row = 167, column = 9, sticky = W)
obs_indian_lunisolar_vs_month_lbl = Label(frame, text = "Month").grid(row = 166, column = 10, sticky = W)
obs_indian_lunisolar_vs_month_ent = Entry(frame)
obs_indian_lunisolar_vs_month_ent.grid(row = 167, column = 10, sticky = W)
obs_indian_lunisolar_vs_year_lbl = Label(frame, text = "Year").grid(row = 166, column = 11, sticky = W)
obs_indian_lunisolar_vs_year_ent = Entry(frame)
obs_indian_lunisolar_vs_year_ent.grid(row = 167, column = 11, sticky = W)
obs_indian_lunisolar_vs_bttn = Button(frame, text = "Calculate", command = obs_indian_lunisolar_vs_converter).grid(row = 168, column = 9, columnspan = 3, sticky = W)

# Tropical Indian solar calendar                                                                                            
trop_indian_solar_lbl = Label(frame, text = "Tropical Indian solar calendar").grid(row = 170, column = 0, columnspan = 3, sticky = W)
trop_indian_solar_day_lbl = Label(frame, text = "Day").grid(row = 171, column = 0, sticky = W)
trop_indian_solar_day_ent = Entry(frame)
trop_indian_solar_day_ent.grid(row = 172, column = 0, sticky = W)
trop_indian_solar_month_lbl = Label(frame, text = "Month").grid(row = 171, column = 1, sticky = W)
trop_indian_solar_month_ent = Entry(frame)
trop_indian_solar_month_ent.grid(row = 172, column = 1, sticky = W)
trop_indian_solar_year_lbl = Label(frame, text = "Year").grid(row = 171, column = 2, sticky = W)
trop_indian_solar_year_ent = Entry(frame)
trop_indian_solar_year_ent.grid(row = 172, column = 2, sticky = W)
trop_indian_solar_bttn = Button(frame, text = "Calculate", command = trop_indian_solar_converter).grid(row = 173, column = 0, columnspan = 3, sticky = W)

# Tropical Indian lunisolar calendar                                                                                            
trop_indian_lunisolar_lbl = Label(frame, text = "Tropical Indian lunisolar calendar").grid(row = 170, column = 3, columnspan = 3, sticky = W)
trop_indian_lunisolar_day_lbl = Label(frame, text = "Tithi").grid(row = 171, column = 3, sticky = W)
trop_indian_lunisolar_day_ent = Entry(frame)
trop_indian_lunisolar_day_ent.grid(row = 172, column = 3, sticky = W)
trop_indian_lunisolar_month_lbl = Label(frame, text = "Month").grid(row = 171, column = 4, sticky = W)
trop_indian_lunisolar_month_ent = Entry(frame)
trop_indian_lunisolar_month_ent.grid(row = 172, column = 4, sticky = W)
trop_indian_lunisolar_year_lbl = Label(frame, text = "Year").grid(row = 171, column = 5, sticky = W)
trop_indian_lunisolar_year_ent = Entry(frame)
trop_indian_lunisolar_year_ent.grid(row = 172, column = 5, sticky = W)
trop_indian_lunisolar_bttn = Button(frame, text = "Calculate", command = trop_indian_lunisolar_converter).grid(row = 173, column = 3, columnspan = 3, sticky = W)

# Traditional Malayam calendar
sid_malayam_lbl = Label(frame, text = "Traditional Malayam calendar").grid(row = 170, column = 6, columnspan = 3, sticky = W)
sid_malayam_day_lbl = Label(frame, text = "Day").grid(row = 171, column = 6, sticky = W)
sid_malayam_day_ent = Entry(frame)
sid_malayam_day_ent.grid(row = 172, column = 6, sticky = W)
sid_malayam_month_lbl = Label(frame, text = "Month").grid(row = 171, column = 7, sticky = W)
sid_malayam_month_ent = Entry(frame)
sid_malayam_month_ent.grid(row = 172, column = 7, sticky = W)
sid_malayam_year_lbl = Label(frame, text = "Year").grid(row = 171, column = 8, sticky = W)
sid_malayam_year_ent = Entry(frame)
sid_malayam_year_ent.grid(row = 172, column = 8, sticky = W)
sid_malayam_bttn = Button(frame, text = "Calculate", command = sid_malayam_converter).grid(row = 173, column = 6, columnspan = 3, sticky = W)

# Modern Malayam calendar (Jyothir Deepika)
obs_malayam_lbl = Label(frame, text = "Modern Malayam calendar (Jyothir Deepika)").grid(row = 170, column = 9, columnspan = 3, sticky = W)
obs_malayam_day_lbl = Label(frame, text = "Day").grid(row = 171, column = 9, sticky = W)
obs_malayam_day_ent = Entry(frame)
obs_malayam_day_ent.grid(row = 172, column = 9, sticky = W)
obs_malayam_month_lbl = Label(frame, text = "Month").grid(row = 171, column = 10, sticky = W)
obs_malayam_month_ent = Entry(frame)
obs_malayam_month_ent.grid(row = 172, column = 10, sticky = W)
obs_malayam_year_lbl = Label(frame, text = "Year").grid(row = 171, column = 11, sticky = W)
obs_malayam_year_ent = Entry(frame)
obs_malayam_year_ent.grid(row = 172, column = 11, sticky = W)
obs_malayam_bttn = Button(frame, text = "Calculate", command = obs_malayam_converter).grid(row = 173, column = 9, columnspan = 3, sticky = W)

# Jalgaon calendar                                                                                            
jalgaon_lbl = Label(frame, text = "Jalgaon calendar").grid(row = 174, column = 0, columnspan = 3, sticky = W)
jalgaon_day_lbl = Label(frame, text = "Tithi").grid(row = 175, column = 0, sticky = W)
jalgaon_day_ent = Entry(frame)
jalgaon_day_ent.grid(row = 176, column = 0, sticky = W)
jalgaon_month_lbl = Label(frame, text = "Month").grid(row = 175, column = 1, sticky = W)
jalgaon_month_ent = Entry(frame)
jalgaon_month_ent.grid(row = 176, column = 1, sticky = W)
jalgaon_year_lbl = Label(frame, text = "Year").grid(row = 175, column = 2, sticky = W)
jalgaon_year_ent = Entry(frame)
jalgaon_year_ent.grid(row = 176, column = 2, sticky = W)
jalgaon_bttn = Button(frame, text = "Calculate", command = jalgaon_converter).grid(row = 177, column = 0, columnspan = 3, sticky = W)

# Manipuri calendar                                                                                            
manipuri_lbl = Label(frame, text = "Manipuri calendar").grid(row = 174, column = 3, columnspan = 3, sticky = W)
manipuri_day_lbl = Label(frame, text = "Tithi").grid(row = 175, column = 3, sticky = W)
manipuri_day_ent = Entry(frame)
manipuri_day_ent.grid(row = 176, column = 3, sticky = W)
manipuri_month_lbl = Label(frame, text = "Month").grid(row = 175, column = 4, sticky = W)
manipuri_month_ent = Entry(frame)
manipuri_month_ent.grid(row = 176, column = 4, sticky = W)
manipuri_year_lbl = Label(frame, text = "Year").grid(row = 175, column = 5, sticky = W)
manipuri_year_ent = Entry(frame)
manipuri_year_ent.grid(row = 176, column = 5, sticky = W)
manipuri_bttn = Button(frame, text = "Calculate", command = manipuri_converter).grid(row = 177, column = 3, columnspan = 3, sticky = W)

# Gujarat calendar                                                                                            
gujarat_lbl = Label(frame, text = "Gujarat calendar").grid(row = 174, column = 6, columnspan = 3, sticky = W)
gujarat_day_lbl = Label(frame, text = "Tithi").grid(row = 175, column = 6, sticky = W)
gujarat_day_ent = Entry(frame)
gujarat_day_ent.grid(row = 176, column = 6, sticky = W)
gujarat_month_lbl = Label(frame, text = "Month").grid(row = 175, column = 7, sticky = W)
gujarat_month_ent = Entry(frame)
gujarat_month_ent.grid(row = 176, column = 7, sticky = W)
gujarat_year_lbl = Label(frame, text = "Year").grid(row = 175, column = 8, sticky = W)
gujarat_year_ent = Entry(frame)
gujarat_year_ent.grid(row = 176, column = 8, sticky = W)
gujarat_bttn = Button(frame, text = "Calculate", command = gujarat_converter).grid(row = 177, column = 6, columnspan = 3, sticky = W)

# Modern Malayam calendar (Uthara Malayala)
alt_malayam_lbl = Label(frame, text = "Modern Malayam calendar (Uthara Malayala)").grid(row = 174, column = 9, columnspan = 3, sticky = W)
alt_malayam_day_lbl = Label(frame, text = "Day").grid(row = 175, column = 9, sticky = W)
alt_malayam_day_ent = Entry(frame)
alt_malayam_day_ent.grid(row = 176, column = 9, sticky = W)
alt_malayam_month_lbl = Label(frame, text = "Month").grid(row = 175, column = 10, sticky = W)
alt_malayam_month_ent = Entry(frame)
alt_malayam_month_ent.grid(row = 176, column = 10, sticky = W)
alt_malayam_year_lbl = Label(frame, text = "Year").grid(row = 175, column = 11, sticky = W)
alt_malayam_year_ent = Entry(frame)
alt_malayam_year_ent.grid(row = 176, column = 11, sticky = W)
alt_malayam_bttn = Button(frame, text = "Calculate", command = alt_malayam_converter).grid(row = 177, column = 9, columnspan = 3, sticky = W)

# Kutch calendar                                                                                            
kutch_lbl = Label(frame, text = "Kutch calendar").grid(row = 178, column = 9, columnspan = 3, sticky = W)
kutch_day_lbl = Label(frame, text = "Tithi").grid(row = 179, column = 9, sticky = W)
kutch_day_ent = Entry(frame)
kutch_day_ent.grid(row = 180, column = 9, sticky = W)
kutch_month_lbl = Label(frame, text = "Month").grid(row = 179, column = 10, sticky = W)
kutch_month_ent = Entry(frame)
kutch_month_ent.grid(row = 180, column = 10, sticky = W)
kutch_year_lbl = Label(frame, text = "Year").grid(row = 179, column = 11, sticky = W)
kutch_year_ent = Entry(frame)
kutch_year_ent.grid(row = 180, column = 11, sticky = W)
kutch_bttn = Button(frame, text = "Calculate", command = kutch_converter).grid(row = 181, column = 9, columnspan = 3, sticky = W)

# Traditional Indian lunisolar calendar (purnimanta)                                                                                            
sid_purnimanta_lbl = Label(frame, text = "Traditional Indian lunisolar calendar (purnimanta)").grid(row = 178, column = 0, columnspan = 3, sticky = W)
sid_purnimanta_day_lbl = Label(frame, text = "Tithi").grid(row = 179, column = 0, sticky = W)
sid_purnimanta_day_ent = Entry(frame)
sid_purnimanta_day_ent.grid(row = 180, column = 0, sticky = W)
sid_purnimanta_month_lbl = Label(frame, text = "Month").grid(row = 179, column = 1, sticky = W)
sid_purnimanta_month_ent = Entry(frame)
sid_purnimanta_month_ent.grid(row = 180, column = 1, sticky = W)
sid_purnimanta_year_lbl = Label(frame, text = "Year").grid(row = 179, column = 2, sticky = W)
sid_purnimanta_year_ent = Entry(frame)
sid_purnimanta_year_ent.grid(row = 180, column = 2, sticky = W)
sid_purnimanta_bttn = Button(frame, text = "Calculate", command = sid_purnimanta_converter).grid(row = 181, column = 0, columnspan = 3, sticky = W)

# Indian lunisolar calendar (purnimanta)                                                                                            
obs_purnimanta_lbl = Label(frame, text = "Indian lunisolar calendar (purnimanta)").grid(row = 178, column = 3, columnspan = 3, sticky = W)
obs_purnimanta_day_lbl = Label(frame, text = "Tithi").grid(row = 179, column = 3, sticky = W)
obs_purnimanta_day_ent = Entry(frame)
obs_purnimanta_day_ent.grid(row = 180, column = 3, sticky = W)
obs_purnimanta_month_lbl = Label(frame, text = "Month").grid(row = 179, column = 4, sticky = W)
obs_purnimanta_month_ent = Entry(frame)
obs_purnimanta_month_ent.grid(row = 180, column = 4, sticky = W)
obs_purnimanta_year_lbl = Label(frame, text = "Year").grid(row = 179, column = 5, sticky = W)
obs_purnimanta_year_ent = Entry(frame)
obs_purnimanta_year_ent.grid(row = 180, column = 5, sticky = W)
obs_purnimanta_bttn = Button(frame, text = "Calculate", command = obs_purnimanta_converter).grid(row = 181, column = 3, columnspan = 3, sticky = W)

# Vedāṅga Jyotiṣa calendar                                                                                            
vj_lbl = Label(frame, text = "Vedāṅga Jyotiṣa calendar").grid(row = 178, column = 6, columnspan = 3, sticky = W)
vj_day_lbl = Label(frame, text = "Day").grid(row = 179, column = 6, sticky = W)
vj_day_ent = Entry(frame)
vj_day_ent.grid(row = 180, column = 6, sticky = W)
vj_month_lbl = Label(frame, text = "Month").grid(row = 179, column = 7, sticky = W)
vj_month_ent = Entry(frame)
vj_month_ent.grid(row = 180, column = 7, sticky = W)
vj_year_lbl = Label(frame, text = "Year").grid(row = 179, column = 8, sticky = W)
vj_year_ent = Entry(frame)
vj_year_ent.grid(row = 180, column = 8, sticky = W)
vj_bttn = Button(frame, text = "Calculate", command = vj_converter).grid(row = 181, column = 6, columnspan = 3, sticky = W)

# Original Nnanakshahi calendar                                                                                            
mool_nanakshahi_lbl = Label(frame, text = "Original Nnanakshahi calendar").grid(row = 182, column = 0, columnspan = 3, sticky = W)
mool_nanakshahi_day_lbl = Label(frame, text = "Day").grid(row = 183, column = 0, sticky = W)
mool_nanakshahi_day_ent = Entry(frame)
mool_nanakshahi_day_ent.grid(row = 184, column = 0, sticky = W)
mool_nanakshahi_month_lbl = Label(frame, text = "Month").grid(row = 183, column = 1, sticky = W)
mool_nanakshahi_month_ent = Entry(frame)
mool_nanakshahi_month_ent.grid(row = 184, column = 1, sticky = W)
mool_nanakshahi_year_lbl = Label(frame, text = "Year").grid(row = 183, column = 2, sticky = W)
mool_nanakshahi_year_ent = Entry(frame)
mool_nanakshahi_year_ent.grid(row = 184, column = 2, sticky = W)
mool_nanakshahi_bttn = Button(frame, text = "Calculate", command = mool_nanakshahi_converter).grid(row = 185, column = 0, columnspan = 3, sticky = W)

# Sidereal Nnanakshahi calendar                                                                                            
sid_nanakshahi_lbl = Label(frame, text = "Sidereal Nnanakshahi calendar").grid(row = 182, column = 3, columnspan = 3, sticky = W)
sid_nanakshahi_day_lbl = Label(frame, text = "Tithi").grid(row = 183, column = 3, sticky = W)
sid_nanakshahi_day_ent = Entry(frame)
sid_nanakshahi_day_ent.grid(row = 184, column = 3, sticky = W)
sid_nanakshahi_month_lbl = Label(frame, text = "Month").grid(row = 183, column = 4, sticky = W)
sid_nanakshahi_month_ent = Entry(frame)
sid_nanakshahi_month_ent.grid(row = 184, column = 4, sticky = W)
sid_nanakshahi_year_lbl = Label(frame, text = "Year").grid(row = 183, column = 5, sticky = W)
sid_nanakshahi_year_ent = Entry(frame)
sid_nanakshahi_year_ent.grid(row = 184, column = 5, sticky = W)
sid_nanakshahi_bttn = Button(frame, text = "Calculate", command = sid_nanakshahi_converter).grid(row = 185, column = 3, columnspan = 3, sticky = W)

# Śvetāmbara Jain calendar                                                                                            
jain_shvetambara_lbl = Label(frame, text = "Śvetāmbara Jain calendar").grid(row = 182, column = 6, columnspan = 3, sticky = W)
jain_shvetambara_day_lbl = Label(frame, text = "Day").grid(row = 183, column = 6, sticky = W)
jain_shvetambara_day_ent = Entry(frame)
jain_shvetambara_day_ent.grid(row = 184, column = 6, sticky = W)
jain_shvetambara_month_lbl = Label(frame, text = "Month").grid(row = 183, column = 7, sticky = W)
jain_shvetambara_month_ent = Entry(frame)
jain_shvetambara_month_ent.grid(row = 184, column = 7, sticky = W)
jain_shvetambara_year_lbl = Label(frame, text = "Year").grid(row = 183, column = 8, sticky = W)
jain_shvetambara_year_ent = Entry(frame)
jain_shvetambara_year_ent.grid(row = 184, column = 8, sticky = W)
jain_shvetambara_bttn = Button(frame, text = "Calculate", command = jain_shvetambara_converter).grid(row = 185, column = 6, columnspan = 3, sticky = W)

# Digambaras Jain calendar                                                                                            
jain_digambaras_lbl = Label(frame, text = "Digambaras Jain calendar").grid(row = 182, column = 9, columnspan = 3, sticky = W)
jain_digambaras_day_lbl = Label(frame, text = "Day").grid(row = 183, column = 9, sticky = W)
jain_digambaras_day_ent = Entry(frame)
jain_digambaras_day_ent.grid(row = 184, column = 9, sticky = W)
jain_digambaras_month_lbl = Label(frame, text = "Month").grid(row = 183, column = 10, sticky = W)
jain_digambaras_month_ent = Entry(frame)
jain_digambaras_month_ent.grid(row = 184, column = 10, sticky = W)
jain_digambaras_year_lbl = Label(frame, text = "Year").grid(row = 183, column = 11, sticky = W)
jain_digambaras_year_ent = Entry(frame)
jain_digambaras_year_ent.grid(row = 184, column = 11, sticky = W)
jain_digambaras_bttn = Button(frame, text = "Calculate", command = jain_digambaras_converter).grid(row = 185, column = 9, columnspan = 3, sticky = W)

# Nepali lunisolar calendar                                                                                            
newar_lbl = Label(frame, text = "Nepali lunisolar calendar").grid(row = 186, column = 0, columnspan = 3, sticky = W)
newar_day_lbl = Label(frame, text = "Day").grid(row = 187, column = 0, sticky = W)
newar_day_ent = Entry(frame)
newar_day_ent.grid(row = 188, column = 0, sticky = W)
newar_month_lbl = Label(frame, text = "Month").grid(row = 187, column = 1, sticky = W)
newar_month_ent = Entry(frame)
newar_month_ent.grid(row = 188, column = 1, sticky = W)
newar_year_lbl = Label(frame, text = "Year").grid(row = 187, column = 2, sticky = W)
newar_year_ent = Entry(frame)
newar_year_ent.grid(row = 188, column = 2, sticky = W)
newar_bttn = Button(frame, text = "Calculate", command = newar_converter).grid(row = 189, column = 0, columnspan = 3, sticky = W)

# Nepali solar calendar                                                                                            
nepali_solar_lbl = Label(frame, text = "Nepali solar calendar").grid(row = 186, column = 3, columnspan = 3, sticky = W)
nepali_solar_day_lbl = Label(frame, text = "Day").grid(row = 187, column = 3, sticky = W)
nepali_solar_day_ent = Entry(frame)
nepali_solar_day_ent.grid(row = 188, column = 3, sticky = W)
nepali_solar_month_lbl = Label(frame, text = "Month").grid(row = 187, column = 4, sticky = W)
nepali_solar_month_ent = Entry(frame)
nepali_solar_month_ent.grid(row = 188, column = 4, sticky = W)
nepali_solar_year_lbl = Label(frame, text = "Year").grid(row = 187, column = 5, sticky = W)
nepali_solar_year_ent = Entry(frame)
nepali_solar_year_ent.grid(row = 188, column = 5, sticky = W)
nepali_solar_bttn = Button(frame, text = "Calculate", command = nepali_solar_converter).grid(row = 189, column = 3, columnspan = 3, sticky = W)

# Karana calendar                                                                                            
karana_lbl = Label(frame, text = "Karana system").grid(row = 186, column = 6, columnspan = 3, sticky = W)
karana_day_lbl = Label(frame, text = "Day").grid(row = 187, column = 6, sticky = W)
karana_day_ent = Entry(frame)
karana_day_ent.grid(row = 188, column = 6, sticky = W)
karana_month_lbl = Label(frame, text = "Month").grid(row = 187, column = 7, sticky = W)
karana_month_ent = Entry(frame)
karana_month_ent.grid(row = 188, column = 7, sticky = W)
karana_year_lbl = Label(frame, text = "Year").grid(row = 187, column = 8, sticky = W)
karana_year_ent = Entry(frame)
karana_year_ent.grid(row = 188, column = 8, sticky = W)
karana_bttn = Button(frame, text = "Calculate", command = karana_converter).grid(row = 189, column = 6, columnspan = 3, sticky = W)

# Tibetan calendar (Phugpa tradition)                                                                                           
phugpa_lbl = Label(frame, text = "Tibetan calendar (Phugpa tradition)").grid(row = 186, column = 9, columnspan = 3, sticky = W)
phugpa_day_lbl = Label(frame, text = "Day").grid(row = 187, column = 9, sticky = W)
phugpa_day_ent = Entry(frame)
phugpa_day_ent.grid(row = 188, column = 9, sticky = W)
phugpa_month_lbl = Label(frame, text = "Month").grid(row = 187, column = 10, sticky = W)
phugpa_month_ent = Entry(frame)
phugpa_month_ent.grid(row = 188, column = 10, sticky = W)
phugpa_year_lbl = Label(frame, text = "Year").grid(row = 187, column = 11, sticky = W)
phugpa_year_ent = Entry(frame)
phugpa_year_ent.grid(row = 188, column = 11, sticky = W)
phugpa_bttn = Button(frame, text = "Calculate", command = phugpa_converter).grid(row = 189, column = 9, columnspan = 3, sticky = W)

# Tibetan calendar (Tsurphu tradition)                                                                                            
tsurphu_lbl = Label(frame, text = "Tibetan calendar (Tsurphu tradition)").grid(row = 190, column = 0, columnspan = 3, sticky = W)
tsurphu_day_lbl = Label(frame, text = "Day").grid(row = 191, column = 0, sticky = W)
tsurphu_day_ent = Entry(frame)
tsurphu_day_ent.grid(row = 192, column = 0, sticky = W)
tsurphu_month_lbl = Label(frame, text = "Month").grid(row = 191, column = 1, sticky = W)
tsurphu_month_ent = Entry(frame)
tsurphu_month_ent.grid(row = 192, column = 1, sticky = W)
tsurphu_year_lbl = Label(frame, text = "Year").grid(row = 191, column = 2, sticky = W)
tsurphu_year_ent = Entry(frame)
tsurphu_year_ent.grid(row = 192, column = 2, sticky = W)
tsurphu_bttn = Button(frame, text = "Calculate", command = tsurphu_converter).grid(row = 193, column = 0, columnspan = 3, sticky = W)

# Mongolian traditional calendar                                                                                            
mongolian_lbl = Label(frame, text = "Mongolian traditional calendar").grid(row = 190, column = 3, columnspan = 3, sticky = W)
mongolian_day_lbl = Label(frame, text = "Day").grid(row = 191, column = 3, sticky = W)
mongolian_day_ent = Entry(frame)
mongolian_day_ent.grid(row = 192, column = 3, sticky = W)
mongolian_month_lbl = Label(frame, text = "Month").grid(row = 191, column = 4, sticky = W)
mongolian_month_ent = Entry(frame)
mongolian_month_ent.grid(row = 192, column = 4, sticky = W)
mongolian_year_lbl = Label(frame, text = "Year").grid(row = 191, column = 5, sticky = W)
mongolian_year_ent = Entry(frame)
mongolian_year_ent.grid(row = 192, column = 5, sticky = W)
mongolian_bttn = Button(frame, text = "Calculate", command = mongolian_converter).grid(row = 193, column = 3, columnspan = 3, sticky = W)

# Bhutanese calendar                                                                                            
bhutanese_lbl = Label(frame, text = "Bhutanese calendar").grid(row = 190, column = 6, columnspan = 3, sticky = W)
bhutanese_day_lbl = Label(frame, text = "Day").grid(row = 191, column = 6, sticky = W)
bhutanese_day_ent = Entry(frame)
bhutanese_day_ent.grid(row = 192, column = 6, sticky = W)
bhutanese_month_lbl = Label(frame, text = "Month").grid(row = 191, column = 7, sticky = W)
bhutanese_month_ent = Entry(frame)
bhutanese_month_ent.grid(row = 192, column = 7, sticky = W)
bhutanese_year_lbl = Label(frame, text = "Year").grid(row = 191, column = 8, sticky = W)
bhutanese_year_ent = Entry(frame)
bhutanese_year_ent.grid(row = 192, column = 8, sticky = W)
bhutanese_bttn = Button(frame, text = "Calculate", command = bhutanese_converter).grid(row = 193, column = 6, columnspan = 3, sticky = W)

# Yellow Tibetan calendar                                                                                            
yellow_lbl = Label(frame, text = "Yellow Tibetan calendar").grid(row = 190, column = 9, columnspan = 3, sticky = W)
yellow_day_lbl = Label(frame, text = "Day").grid(row = 191, column = 9, sticky = W)
yellow_day_ent = Entry(frame)
yellow_day_ent.grid(row = 192, column = 9, sticky = W)
yellow_month_lbl = Label(frame, text = "Month").grid(row = 191, column = 10, sticky = W)
yellow_month_ent = Entry(frame)
yellow_month_ent.grid(row = 192, column = 10, sticky = W)
yellow_year_lbl = Label(frame, text = "Year").grid(row = 191, column = 11, sticky = W)
yellow_year_ent = Entry(frame)
yellow_year_ent.grid(row = 192, column = 11, sticky = W)
yellow_bttn = Button(frame, text = "Calculate", command = yellow_converter).grid(row = 193, column = 9, columnspan = 3, sticky = W)

# Sherab Ling calendar                                                                                            
sherab_ling_lbl = Label(frame, text = "Sherab Ling calendar").grid(row = 194, column = 0, columnspan = 3, sticky = W)
sherab_ling_day_lbl = Label(frame, text = "Day").grid(row = 195, column = 0, sticky = W)
sherab_ling_day_ent = Entry(frame)
sherab_ling_day_ent.grid(row = 196, column = 0, sticky = W)
sherab_ling_month_lbl = Label(frame, text = "Month").grid(row = 195, column = 1, sticky = W)
sherab_ling_month_ent = Entry(frame)
sherab_ling_month_ent.grid(row = 196, column = 1, sticky = W)
sherab_ling_year_lbl = Label(frame, text = "Year").grid(row = 195, column = 2, sticky = W)
sherab_ling_year_ent = Entry(frame)
sherab_ling_year_ent.grid(row = 196, column = 2, sticky = W)
sherab_ling_bttn = Button(frame, text = "Calculate", command = sherab_ling_converter).grid(row = 197, column = 0, columnspan = 3, sticky = W)

# Sarnath calendar                                                                                            
sarnath_lbl = Label(frame, text = "Sarnath calendar").grid(row = 194, column = 3, columnspan = 3, sticky = W)
sarnath_day_lbl = Label(frame, text = "Day").grid(row = 195, column = 3, sticky = W)
sarnath_day_ent = Entry(frame)
sarnath_day_ent.grid(row = 196, column = 3, sticky = W)
sarnath_month_lbl = Label(frame, text = "Month").grid(row = 195, column = 4, sticky = W)
sarnath_month_ent = Entry(frame)
sarnath_month_ent.grid(row = 196, column = 4, sticky = W)
sarnath_year_lbl = Label(frame, text = "Year").grid(row = 195, column = 5, sticky = W)
sarnath_year_ent = Entry(frame)
sarnath_year_ent.grid(row = 196, column = 5, sticky = W)
sarnath_bttn = Button(frame, text = "Calculate", command = sarnath_converter).grid(row = 197, column = 3, columnspan = 3, sticky = W)


root.title("Calendar Converter 0.63.0")
root.mainloop()
