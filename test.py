#!/usr/bin/python3

from tkinter import *
from tkinter import ttk
from decimal import *

import months

import julian
import gregorian
import jewish
import chinese_lunisolar_huangdi

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

        # Convert a Julian day to a date in the jewish calendar
        jewish_date = jewish.fromjd(day)
        jewish_day_ent.delete(0, END)
        jewish_month_ent.delete(0, END)
        jewish_year_ent.delete(0, END)
        jewish_day_ent.insert(0, jewish_date[0])
        jewish_month_ent.insert(0, jewish_date[1])
        jewish_year_ent.insert(0, jewish_date[2])

         # Convert a Julian day to a date in the chinese_lunisolar_huangdi calendar
        chinese_lunisolar_huangdi_date = chinese_lunisolar_huangdi.fromjd(day)
        chinese_lunisolar_huangdi_day_ent.delete(0, END)
        chinese_lunisolar_huangdi_month_ent.delete(0, END)
        chinese_lunisolar_huangdi_year_ent.delete(0, END)
        chinese_lunisolar_huangdi_day_ent.insert(0, chinese_lunisolar_huangdi_date[0])
        chinese_lunisolar_huangdi_month_ent.insert(0, chinese_lunisolar_huangdi_date[1])
        chinese_lunisolar_huangdi_year_ent.insert(0, chinese_lunisolar_huangdi_date[2])
        
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

def jewish_converter():
        day = int(jewish_day_ent.get())
        month = jewish_month_ent.get()
        year = int(jewish_year_ent.get())
        jday = jewish.tojd(day, month, year)
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

# jewish calendar                                                                                            
jewish_lbl = Label(frame, text = "jewish calendar").grid(row = 33, column = 0, columnspan = 3, sticky = W)
jewish_day_lbl = Label(frame, text = "Day").grid(row = 34, column = 0, sticky = W)
jewish_day_ent = Entry(frame)
jewish_day_ent.grid(row = 35, column = 0, sticky = W)
jewish_month_lbl = Label(frame, text = "Month").grid(row = 34, column = 1, sticky = W)
jewish_month_ent = Entry(frame)
jewish_month_ent.grid(row = 35, column = 1, sticky = W)
jewish_year_lbl = Label(frame, text = "Year").grid(row = 34, column = 2, sticky = W)
jewish_year_ent = Entry(frame)
jewish_year_ent.grid(row = 35, column = 2, sticky = W)
jewish_bttn = Button(frame, text = "Calculate", command = jewish_converter).grid(row = 36, column = 0, columnspan = 3, sticky = W)

# chinese_lunisolar_huangdi calendar
chinese_lunisolar_huangdi_lbl = Label(frame, text = "chinese_lunisolar_huangdi calendar").grid(row = 33, column = 3, columnspan = 3, sticky = W)
chinese_lunisolar_huangdi_day_lbl = Label(frame, text = "Day").grid(row = 34, column = 3, sticky = W)
chinese_lunisolar_huangdi_day_ent = Entry(frame)
chinese_lunisolar_huangdi_day_ent.grid(row = 35, column = 3, sticky = W)
chinese_lunisolar_huangdi_month_lbl = Label(frame, text = "Month").grid(row = 34, column = 4, sticky = W)
chinese_lunisolar_huangdi_month_ent = Entry(frame)
chinese_lunisolar_huangdi_month_ent.grid(row = 35, column = 4, sticky = W)
chinese_lunisolar_huangdi_year_lbl = Label(frame, text = "Year").grid(row = 34, column = 5, sticky = W)
chinese_lunisolar_huangdi_year_ent = Entry(frame)
chinese_lunisolar_huangdi_year_ent.grid(row = 35, column = 5, sticky = W)
chinese_lunisolar_huangdi_bttn = Button(frame, text = "Calculate", command = chinese_lunisolar_huangdi_converter).grid(row = 36, column = 3, columnspan = 3, sticky = W)

root.title("Calendar Converter 0.17.0")
root.mainloop()
