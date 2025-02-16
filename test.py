#!/usr/bin/python3

from tkinter import *
from tkinter import ttk
from decimal import *

import months

import julian
import gregorian
import archetypes
import obs_muisca
import chinese_lunisolar_qin
import iso_week
import iso_day

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

        # Convert a Julian day to a date in the Solar Hijri calendar
        chinese_lunisolar_qin_date = chinese_lunisolar_qin.fromjd(day)
        chinese_lunisolar_qin_day_ent.delete(0, END)
        chinese_lunisolar_qin_month_ent.delete(0, END)
        chinese_lunisolar_qin_year_ent.delete(0, END)
        chinese_lunisolar_qin_day_ent.insert(0, chinese_lunisolar_qin_date[0])
        chinese_lunisolar_qin_month_ent.insert(0, chinese_lunisolar_qin_date[1])
        chinese_lunisolar_qin_year_ent.insert(0, chinese_lunisolar_qin_date[2])

        # Convert a Julian Day to a date in the archetypes calendar
        archetypes_date = archetypes.fromjd(day)
        archetypes_day_ent.delete(0, END)
        archetypes_month_ent.delete(0, END)
        archetypes_year_ent.delete(0, END)
        archetypes_day_ent.insert(0, archetypes_date[0])
        archetypes_month_ent.insert(0, archetypes_date[1])
        archetypes_year_ent.insert(0, archetypes_date[2])
	
        # Convert a Julian Day to a date in the obs_muisca calendar
        obs_muisca_date = obs_muisca.fromjd(day)
        obs_muisca_day_ent.delete(0, END)
        obs_muisca_month_ent.delete(0, END)
        obs_muisca_year_ent.delete(0, END)
        obs_muisca_day_ent.insert(0, obs_muisca_date[0])
        obs_muisca_month_ent.insert(0, obs_muisca_date[1])
        obs_muisca_year_ent.insert(0, obs_muisca_date[2])

        # Convert a Julian day to a date in the ISO-week calendar
        iso_week_date = iso_week.fromjd(day)
        iso_week_day_ent.delete(0, END)
        iso_week_month_ent.delete(0, END)
        iso_week_year_ent.delete(0, END)
        iso_week_day_ent.insert(0, iso_week_date[0])
        iso_week_month_ent.insert(0, iso_week_date[1])
        iso_week_year_ent.insert(0, iso_week_date[2])

        # Convert a Julian day to a date in the ISO-day calendar
        iso_day_date = iso_day.fromjd(day)
        iso_day_day_ent.delete(0, END)
        
        iso_day_year_ent.delete(0, END)
        iso_day_day_ent.insert(0, iso_day_date[0])
        
        iso_day_year_ent.insert(0, iso_day_date[1])

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

def chinese_lunisolar_qin_converter():
        day = int(chinese_lunisolar_qin_day_ent.get())
        month = chinese_lunisolar_qin_month_ent.get()
        year = int(chinese_lunisolar_qin_year_ent.get())
        jday = chinese_lunisolar_qin.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def archetypes_converter():
        day = int(archetypes_day_ent.get())
        month = archetypes_month_ent.get()
        year = str(archetypes_year_ent.get())
        #if(year[len(year) - 1:] == '*'):
        #        year = int(year[:len(year) - 1])
        #else:
        #        year = int(year)
        jday = archetypes.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()
        
def obs_muisca_converter():
        day = int(obs_muisca_day_ent.get())
        month = obs_muisca_month_ent.get()
        year = int(obs_muisca_year_ent.get())
        jday = obs_muisca.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def iso_week_converter():
        day = str(iso_week_day_ent.get())
        month = int(iso_week_month_ent.get())
        year = int(iso_week_year_ent.get())
        jday = iso_week.tojd(day, month, year)
        cons_day_julian_ent.delete(0, END)
        cons_day_julian_ent.insert(0, jday)
        cons_day_julian_todate()

def iso_day_converter():
        day = int(iso_day_day_ent.get())
        
        year = int(iso_day_year_ent.get())
        jday = iso_day.tojd(day, year)
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
cons_day_julian_lbl = Label(frame, text = "Chronological Julian day").grid(row = 1, column = 0, columnspan = 3, sticky = W)
#cons_day_julian_desc_lbl = Label(frame, text = "Day").grid(row = 2, column = 0, columnspan = 3, sticky = W)
cons_day_julian_ent = Entry(frame)
cons_day_julian_ent.grid(row = 2, column = 0, sticky = W)
cons_day_julian_bttn = Button(frame, text = "Calculate", command = cons_day_julian_todate).grid(row = 3, column = 0, columnspan = 3, sticky = W)

# Plus and Minus buttons
cons_day_julian_plus_bttn = Button(frame, text = "+", command = cons_day_julian_plus).grid(row = 2, column = 1, sticky = W)
cons_day_julian_minus_bttn = Button(frame, text = "-", command = cons_day_julian_minus).grid(row = 3, column = 1, sticky = W)

# Julian Calendar
julian_lbl = Label(frame, text = "Julian Calendar").grid(row = 0, column = 3, columnspan = 3, sticky = W)
julian_day_lbl = Label(frame, text = "Day").grid(row = 1, column = 3, columnspan = 3, sticky = W)
julian_day_ent = Entry(frame)
julian_day_ent.grid(row = 2, column = 3, sticky = W)
julian_month_lbl = Label(frame, text = "Month").grid(row = 1, column = 4, sticky = W)
julian_month_ent = Entry(frame)
julian_month_ent.grid(row = 2, column = 4, sticky = W)
julian_year_lbl = Label(frame, text = "Year").grid(row = 1, column = 5, sticky = W)
julian_year_ent = Entry(frame)
julian_year_ent.grid(row = 2, column = 5, sticky = W)
julian_bttn = Button(frame, text = "Calculate", command = julian_converter).grid(row = 3, column = 3, columnspan = 3, sticky = W)

# Gregorian Calendar
gregorian_lbl = Label(frame, text = "Gregorian Calendar").grid(row = 0, column = 6, columnspan = 3, sticky = W)
gregorian_day_lbl = Label(frame, text = "Day").grid(row = 1, column = 6, sticky = W)
gregorian_day_ent = Entry(frame)
gregorian_day_ent.grid(row = 2, column = 6, sticky = W)
gregorian_month_lbl = Label(frame, text = "Month").grid(row = 1, column = 7, sticky = W)
gregorian_month_ent = Entry(frame)
gregorian_month_ent.grid(row = 2, column = 7, sticky = W)
gregorian_year_lbl= Label(frame, text = "Year").grid(row = 1, column = 8, sticky = W)
gregorian_year_ent = Entry(frame)
gregorian_year_ent.grid(row = 2, column = 8, sticky = W)
gregorian_bttn = Button(frame, text = "Calculate", command = gregorian_converter).grid(row = 3, column = 6, columnspan = 3, sticky = W)

# Solar Hijri calendar                                                                                            
chinese_lunisolar_qin_lbl = Label(frame, text = "Solar Hijri calendar").grid(row = 0, column = 9, columnspan = 3, sticky = W)
chinese_lunisolar_qin_day_lbl = Label(frame, text = "Day").grid(row = 1, column = 9, sticky = W)
chinese_lunisolar_qin_day_ent = Entry(frame)
chinese_lunisolar_qin_day_ent.grid(row = 2, column = 9, sticky = W)
chinese_lunisolar_qin_month_lbl = Label(frame, text = "Month").grid(row = 1, column = 10, sticky = W)
chinese_lunisolar_qin_month_ent = Entry(frame)
chinese_lunisolar_qin_month_ent.grid(row = 2, column = 10, sticky = W)
chinese_lunisolar_qin_year_lbl = Label(frame, text = "Year").grid(row = 1, column = 11, sticky = W)
chinese_lunisolar_qin_year_ent = Entry(frame)
chinese_lunisolar_qin_year_ent.grid(row = 2, column = 11, sticky = W)
chinese_lunisolar_qin_bttn = Button(frame, text = "Calculate", command = chinese_lunisolar_qin_converter).grid(row = 3, column = 9, columnspan = 3, sticky = W)

# archetypes calendar                                                                                            
archetypes_lbl = Label(frame, text = "archetypes calendar").grid(row = 5, column = 0, columnspan = 3, sticky = W)
archetypes_day_lbl = Label(frame, text = "Day").grid(row = 6, column = 0, sticky = W)
archetypes_day_ent = Entry(frame)
archetypes_day_ent.grid(row = 7, column = 0, sticky = W)
archetypes_month_lbl = Label(frame, text = "Month").grid(row = 6, column = 1, sticky = W)
archetypes_month_ent = Entry(frame)
archetypes_month_ent.grid(row = 7, column = 1, sticky = W)
archetypes_year_lbl = Label(frame, text = "Year").grid(row = 6, column = 2, sticky = W)
archetypes_year_ent = Entry(frame)
archetypes_year_ent.grid(row = 7, column = 2, sticky = W)
archetypes_bttn = Button(frame, text = "Calculate", command = archetypes_converter).grid(row = 8, column = 0, columnspan = 3, sticky = W)

# obs_muisca calendar
obs_muisca_lbl = Label(frame, text = "obs_muisca calendar").grid(row = 5, column = 3, columnspan = 3, sticky = W)
obs_muisca_day_lbl = Label(frame, text = "Day").grid(row = 6, column = 3, sticky = W)
obs_muisca_day_ent = Entry(frame)
obs_muisca_day_ent.grid(row = 7, column = 3, sticky = W)
obs_muisca_month_lbl = Label(frame, text = "Month").grid(row = 6, column = 4, sticky = W)
obs_muisca_month_ent = Entry(frame)
obs_muisca_month_ent.grid(row = 7, column = 4, sticky = W)
obs_muisca_year_lbl = Label(frame, text = "Year").grid(row = 6, column = 5, sticky = W)
obs_muisca_year_ent = Entry(frame)
obs_muisca_year_ent.grid(row = 7, column = 5, sticky = W)
obs_muisca_bttn = Button(frame, text = "Calculate", command = obs_muisca_converter).grid(row = 8, column = 3, columnspan = 3, sticky = W)

# ISO-week calendar                                                                                            
iso_week_lbl = Label(frame, text = "ISO-week calendar").grid(row = 5, column = 6, columnspan = 3, sticky = W)
iso_week_day_lbl = Label(frame, text = "Day").grid(row = 6, column = 6, sticky = W)
iso_week_day_ent = Entry(frame)
iso_week_day_ent.grid(row = 7, column = 6, sticky = W)
iso_week_month_lbl = Label(frame, text = "Month").grid(row = 6, column = 7, sticky = W)
iso_week_month_ent = Entry(frame)
iso_week_month_ent.grid(row = 7, column = 7, sticky = W)
iso_week_year_lbl = Label(frame, text = "Year").grid(row = 6, column = 8, sticky = W)
iso_week_year_ent = Entry(frame)
iso_week_year_ent.grid(row = 7, column = 8, sticky = W)
iso_week_bttn = Button(frame, text = "Calculate", command = iso_week_converter).grid(row = 8, column = 6, columnspan = 3, sticky = W)

# ISO-day calendar                                                                                            
iso_day_lbl = Label(frame, text = "ISO-day calendar").grid(row = 5, column = 9, columnspan = 3, sticky = W)
iso_day_day_lbl = Label(frame, text = "Day").grid(row = 6, column = 9, sticky = W)
iso_day_day_ent = Entry(frame)
iso_day_day_ent.grid(row = 7, column = 9, sticky = W)

iso_day_year_lbl = Label(frame, text = "Year").grid(row = 6, column = 11, sticky = W)
iso_day_year_ent = Entry(frame)
iso_day_year_ent.grid(row = 7, column = 11, sticky = W)
iso_day_bttn = Button(frame, text = "Calculate", command = iso_day_converter).grid(row = 8, column = 9, columnspan = 3, sticky = W)

root.title("Calendar Converter 0.17.0")
root.mainloop()
