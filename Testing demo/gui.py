from tkinter import *
from tkinter import ttk
from data_transmission import giveWater
from data_transmission import givepHSuppliment
from data_transmission import plant

window = Tk()
window.title("Water plEase")

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)
tab6 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Plant 1')
tab_control.add(tab2, text='Plant 2')
tab_control.add(tab3, text='Plant 3')
tab_control.add(tab4, text='Plant 4')
tab_control.add(tab5, text='Plant 5')
tab_control.add(tab6, text='Plant 6')

lbl1 = Label(tab1, text= 'Plant type: ' + plant)
lbl1.grid(column=0, row=0)
lbl1 = Label(tab1, text= 'Water status: ' + giveWater())
lbl1.grid(column=0, row=1)
lbl1 = Label(tab1, text= 'pH Status: ' + givepHSuppliment())
lbl1.grid(column=0, row=2)

lbl2 = Label(tab2, text= 'Plant type: ' + plant)
lbl2.grid(column=0, row=0)
lbl2 = Label(tab2, text= 'Water status: ' + giveWater())
lbl2.grid(column=0, row=1)
lbl2 = Label(tab2, text= 'pH Status: ' + givepHSuppliment())
lbl2.grid(column=0, row=2)

lbl3 = Label(tab3, text= 'Plant type: ' + plant)
lbl3.grid(column=0, row=0)
lbl3 = Label(tab3, text= 'Water status: ' + giveWater())
lbl3.grid(column=0, row=1)
lbl3 = Label(tab3, text= 'pH Status: ' + givepHSuppliment())
lbl3.grid(column=0, row=2)

lbl4 = Label(tab4, text= 'Plant type: ' + plant)
lbl4.grid(column=0, row=0)
lbl4 = Label(tab4, text= 'Water status: ' + giveWater())
lbl4.grid(column=0, row=1)
lbl4 = Label(tab4, text= 'pH Status: ' + givepHSuppliment())
lbl4.grid(column=0, row=2)

lbl5 = Label(tab5, text= 'Plant type: ' + plant)
lbl5.grid(column=0, row=0)
lbl5 = Label(tab5, text= 'Water status: ' + giveWater())
lbl5.grid(column=0, row=1)
lbl5 = Label(tab5, text= 'pH Status: ' + givepHSuppliment())
lbl5.grid(column=0, row=2)

lbl6 = Label(tab6, text= 'Plant type: ' + plant)
lbl6.grid(column=0, row=0)
lbl6 = Label(tab6, text= 'Water status: ' + giveWater())
lbl6.grid(column=0, row=1)
lbl6 = Label(tab6, text= 'pH Status: ' + givepHSuppliment())
lbl6.grid(column=0, row=2)

tab_control.pack(expand=1, fill='both')

window.mainloop()
