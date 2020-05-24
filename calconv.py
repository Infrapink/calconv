#!/usr/bin/python

from tkinter import *
import julian_day_conversions
import julian_convert
import gregorian_convert
import coptic_convert
import ethiopian_convert
import egyptian_convert
import armenian_convert
import months

class Application(Frame):
    """A GUI application with various widgets"""
    def __init__(self, master):
        """Initialise the Frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def day_julian_convert(self):
        """Take the input into the Julian Day box and convert it into the other date formats"""
        day = self.day_julian_ent.get()

        # Convert a Julian Day to a date in the Julian Calendar
        julian_date = julian_day_conversions.julian_day_to_julian(day)
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
        gregorian_date = julian_day_conversions.julian_day_to_gregorian(day)
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
        coptic_date = julian_day_conversions.julian_day_to_coptic(day)
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
        ethiopian_date = julian_day_conversions.julian_day_to_ethiopian(day)
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
        egyptian_date = julian_day_conversions.julian_day_to_egyptian(day)
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
        armenian_date = julian_day_conversions.julian_day_to_armenian(day)
        armenian_day_value = armenian_date[0]
        armenian_month_value = armenian_date[1]
        armenian_year_value = armenian_date[2]
        self.armenian_day_ent.delete(0, END)
        self.armenian_month_ent.delete(0, END)
        self.armenian_year_ent.delete(0, END)
        self.armenian_day_ent.insert(0, armenian_day_value)
        self.armenian_month_ent.insert(0, armenian_month_value)
        self.armenian_year_ent.insert(0, armenian_year_value)
        


    def julian_converter(self):
        """Convert a date in the Julian Calendar to a Julian Day."""
        day = self.julian_day_ent.get()
        month = self.julian_month_ent.get()
        year = self.julian_year_ent.get()
        jday = julian_convert.convert(day, month, year)
        self.day_julian_ent.delete(0, END)
        self.day_julian_ent.insert(0, jday)
        self.day_julian_convert()

    def gregorian_converter(self):
        """Convert a date in the Gregorian Calendar to a Julian  Day."""
        day = self.gregorian_day_ent.get()
        month = self.gregorian_month_ent.get()
        year = self.gregorian_year_ent.get()
        jday = gregorian_convert.convert(day, month, year)
        self.day_julian_ent.delete(0, END)
        self.day_julian_ent.insert(0, jday)
        self.day_julian_convert()

    def coptic_converter(self):
        """Convert a date in the Coptic Calendar to a Julian Day."""
        day = self.coptic_day_ent.get()
        month = self.coptic_month_ent.get()
        year = self.coptic_year_ent.get()
        jday = coptic_convert.convert(day, month, year)
        self.day_julian_ent.delete(0, END)
        self.day_julian_ent.insert(0, jday)
        self.day_julian_convert()

    def ethiopian_converter(self):
        """Convert a date in the Ethiopian Calendar to a Julian day."""
        day = self.ethiopian_day_ent.get()
        month = self.ethiopian_month_ent.get()
        year = self.ethiopian_year_ent.get()
        jday = ethiopian_convert.convert(day,month,year)
        self.day_julian_ent.delete(0, END)
        self.day_julian_ent.insert(0, jday)
        self.day_julian_convert()

    def egyptian_converter(self):
        """Convert a date in the Egyptian Calendar to a Julian Day."""
        day = self.egyptian_day_ent.get()
        month = self.egyptian_month_ent.get()
        year = self.egyptian_year_ent.get()
        jday = egyptian_convert.convert(day, month, year)
        self.day_julian_ent.delete(0, END)
        self.day_julian_ent.insert(0, jday)
        self.day_julian_convert()

    def armenian_converter(self):
        """Convert a date in the Armenian Calendar to a Julian Day."""
        day = self.armenian_day_ent.get()
        month = self.armenian_month_ent.get()
        year = self.armenian_year_ent.get()
        jday = armenian_convert.convert(day, month, year)
        self.day_julian_ent.delete(0, END)
        self.day_julian_ent.insert(0, jday)
        self.day_julian_convert()


        
    def create_widgets(self):
        """Generate various widgets."""
        # For now, months will just have to be typed manually until I can figure out how to use dropdown menus.
        
        # Julian Day
        self.day_julian_lbl = Label(self, text = "Julian Day").grid(row = 0, column = 0, columnspan = 3, sticky = W)
        self.day_julian_desc_lbl = Label(self, text = "Day").grid (row = 1, column = 0, columnspan = 3, sticky = W)
        self.day_julian_ent = Entry(self)
        self.day_julian_ent.grid(row = 2, column = 0, columnspan = 3, sticky = W)
        self.day_julian_bttn = Button(self, text = "Calculate", command = self.day_julian_convert)
        self.day_julian_bttn.grid(row = 3, column = 0, columnspan = 3, sticky = W)

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

# create the root window
root = Tk()
app = Application(root)
root.title("Calendar Converter 0.6.0")

root.mainloop()
