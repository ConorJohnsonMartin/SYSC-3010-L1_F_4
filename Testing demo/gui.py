# L1-F-4 Water plEase
# @description For the GUI implementation of Water plEase
# @author Kevin Belanger 101121709
# @version Version 1, 24 November 2020

# Import statements
from tkinter import *
from tkinter import ttk
from data_transmission import giveWater, givepHSuppliment, id, plantName, moisture, pHmin, pHmax, pH

# Sets our pH value to a string which is read from the data_transmission class
pH = str(pH)

# Creates the window with title "Water plEase"
window = Tk()
window.geometry("250x110")
window.title("Water plEase")

# Creates 3 tabs for window
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)

# Adds titles for each of the 3 tabs
tab_control.add(tab1, text='Plant 1')
tab_control.add(tab2, text='Plant 2')
tab_control.add(tab3, text='Plant 3')
tab_control.add(tab4, text='Plant 4')
tab_control.add(tab5, text='Plant 5')

# On tab 1, creates text attribute and lists it with the corresponding variable for readability
lbl1 = Label(tab1, text='Plant type: ')
lbl1.grid(column=0, row=0)
lbl1 = Label(tab1, text=plantName[0])
lbl1.grid(column=1, row=0)
lbl1 = Label(tab1, text='Water status: ')
lbl1.grid(column=0, row=1)
lbl1 = Label(tab1, text=giveWater(0))
lbl1.grid(column=1, row=1)
lbl1 = Label(tab1, text='pH Status: ')
lbl1.grid(column=0, row=2)
lbl1 = Label(tab1, text=givepHSuppliment(0))
lbl1.grid(column=1, row=2)
lbl1 = Label(tab1, text='pH: ')
lbl1.grid(column=0, row=3)
lbl1 = Label(tab1, text=pH)
lbl1.grid(column=1, row=3)

# On tab 2, creates text attribute and lists it with the corresponding variable for readability
lbl2 = Label(tab2, text='Plant type: ')
lbl2.grid(column=0, row=0)
lbl2 = Label(tab2, text=plantName[1])
lbl2.grid(column=1, row=0)
lbl2 = Label(tab2, text='Water status: ')
lbl2.grid(column=0, row=1)
lbl2 = Label(tab2, text=giveWater(1))
lbl2.grid(column=1, row=1)
lbl2 = Label(tab2, text='pH Status: ')
lbl2.grid(column=0, row=2)
lbl2 = Label(tab2, text=givepHSuppliment(1))
lbl2.grid(column=1, row=2)
lbl2 = Label(tab2, text='pH: ')
lbl2.grid(column=0, row=3)
lbl2 = Label(tab2, text=pH)
lbl2.grid(column=1, row=3)

# On tab 3, creates text attribute and lists it with the corresponding variable for readability
lbl3 = Label(tab3, text='Plant type: ')
lbl3.grid(column=0, row=0)
lbl3 = Label(tab3, text=plantName[2])
lbl3.grid(column=1, row=0)
lbl3 = Label(tab3, text='Water status: ')
lbl3.grid(column=0, row=1)
lbl3 = Label(tab3, text=giveWater(2))
lbl3.grid(column=1, row=1)
lbl3 = Label(tab3, text='pH Status: ')
lbl3.grid(column=0, row=2)
lbl3 = Label(tab3, text=givepHSuppliment(2))
lbl3.grid(column=1, row=2)
lbl3 = Label(tab3, text='pH: ')
lbl3.grid(column=0, row=3)
lbl3 = Label(tab3, text=pH)
lbl3.grid(column=1, row=3)

# On tab 4, creates text attribute and lists it with the corresponding variable for readability
lbl4 = Label(tab4, text='Plant type: ')
lbl4.grid(column=0, row=0)
lbl4 = Label(tab4, text=plantName[3])
lbl4.grid(column=1, row=0)
lbl4 = Label(tab4, text='Water status: ')
lbl4.grid(column=0, row=1)
lbl4 = Label(tab4, text=giveWater(3))
lbl4.grid(column=1, row=1)
lbl4 = Label(tab4, text='pH Status: ')
lbl4.grid(column=0, row=2)
lbl4 = Label(tab4, text=givepHSuppliment(3))
lbl4.grid(column=1, row=2)
lbl4 = Label(tab4, text='pH: ')
lbl4.grid(column=0, row=3)
lbl4 = Label(tab4, text=pH)
lbl4.grid(column=1, row=3)

# On tab 5, creates text attribute and lists it with the corresponding variable for readability
lbl5 = Label(tab5, text='Plant type: ')
lbl5.grid(column=0, row=0)
lbl5 = Label(tab5, text=plantName[4])
lbl5.grid(column=1, row=0)
lbl5 = Label(tab5, text='Water status: ')
lbl5.grid(column=0, row=1)
lbl5 = Label(tab5, text=giveWater(4))
lbl5.grid(column=1, row=1)
lbl5 = Label(tab5, text='pH Status: ')
lbl5.grid(column=0, row=2)
lbl5 = Label(tab5, text=givepHSuppliment(4))
lbl5.grid(column=1, row=2)
lbl5 = Label(tab5, text='pH: ')
lbl5.grid(column=0, row=3)
lbl5 = Label(tab5, text=pH)
lbl5.grid(column=1, row=3)

# Executes pop up of window
tab_control.pack(expand=1, fill='both')
window.mainloop()
