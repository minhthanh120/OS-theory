from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter
from time import sleep
window = Tk()
for i in range(10):
    Label(window, text="Lower").grid(column=1, row=i)
    sleep(1)
    window.mainloop()
#window.mainloop()7
