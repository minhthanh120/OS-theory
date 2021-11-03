from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter

window = Tk()
window.title("Mì AI Form")
window.geometry("400x600")
scrollbar = Scrollbar(window)
scrollbar.pack( side = RIGHT, fill = Y )
for i in range(100):
    Label(text =str(i)).pack()
window.mainloop()