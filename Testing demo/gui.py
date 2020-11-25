# L1-F-4 Water plEase
# @description For the GUI implementation of Water plEase
# @author Kevin Belanger 101121709
# @version Version 1, 24 November 2020

# Import statements
from tkinter import *
from tkinter import ttk
from data_transmission import giveWater, givepHSuppliment, plant1, plant2, plant3, pH

# Sets our pH value to a string which is read from the data_transmission class
pH = str(pH)

# Creates the window with title "Water plEase"
window = Tk()
window.title("Water plEase")

# Creates 6 tabs for window
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

# Adds titles for each of the 6 tabs
tab_control.add(tab1, text='Plant 1')
tab_control.add(tab2, text='Plant 2')
tab_control.add(tab3, text='Plant 3')

# On tab 1, creates text attribute and lists it with the corresponding variable for readability
# x is a placeholder for the tab creation
lbl1 = Label(tab1, text='Plant type: ')
lbl1.grid(column=0, row=0)
lbl1 = Label(tab1, text=plant1)
lbl1.grid(column=1, row=0)
lbl1 = Label(tab1, text='Water status: ')
lbl1.grid(column=0, row=1)
lbl1 = Label(tab1, text=giveWater())
lbl1.grid(column=1, row=1)
lbl1 = Label(tab1, text='pH Status: ')
lbl1.grid(column=0, row=2)
lbl1 = Label(tab1, text=givepHSuppliment())
lbl1.grid(column=1, row=2)
lbl1 = Label(tab1, text='pH: ')
lbl1.grid(column=0, row=3)
lbl1 = Label(tab1, text=pH)
lbl1.grid(column=1, row=3)

# On tab 2, creates text attribute and lists it with the corresponding variable for readability
lbl2 = Label(tab2, text='Plant type: ')
lbl2.grid(column=0, row=0)
lbl2 = Label(tab2, text=plant2)
lbl2.grid(column=1, row=0)
lbl2 = Label(tab2, text='Water status: ')
lbl2.grid(column=0, row=1)
lbl2 = Label(tab2, text=giveWater())
lbl2.grid(column=1, row=1)
lbl2 = Label(tab2, text='pH Status: ')
lbl2.grid(column=0, row=2)
lbl2 = Label(tab2, text=givepHSuppliment())
lbl2.grid(column=1, row=2)
lbl2 = Label(tab2, text='pH: ')
lbl2.grid(column=0, row=3)
lbl2 = Label(tab2, text=pH)
lbl2.grid(column=1, row=3)

# On tab 3, creates text attribute and lists it with the corresponding variable for readability
lbl3 = Label(tab3, text='Plant type: ')
lbl3.grid(column=0, row=0)
lbl3 = Label(tab3, text=plant3)
lbl3.grid(column=1, row=0)
lbl3 = Label(tab3, text='Water status: ')
lbl3.grid(column=0, row=1)
lbl3 = Label(tab3, text=giveWater())
lbl3.grid(column=1, row=1)
lbl3 = Label(tab3, text='pH Status: ')
lbl3.grid(column=0, row=2)
lbl3 = Label(tab3, text=givepHSuppliment())
lbl3.grid(column=1, row=2)
lbl3 = Label(tab3, text='pH: ')
lbl3.grid(column=0, row=3)
lbl3 = Label(tab3, text=pH)
lbl3.grid(column=1, row=3)

# Executes pop up of window
tab_control.pack(expand=1, fill='both')
window.mainloop()
