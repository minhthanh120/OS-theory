from tkinter import *
from tkinter.ttk import *
from tkinter.font import Font
from tkinter import messagebox
import tkinter

window = Tk()
window.title("Mì AI Form")
window.geometry("800x600")
#myFont = Font(family="Times New Roman", size=12)
# Thêm label
lbl = tkinter.Label(window, text="Hello Mì AI", fg="red", font=("Arial", 50))
lbl.grid(column=0, row=0)

# Thêm textbox
txt = Entry(window, width=20)
txt.grid(column=0, row=1)

def handleButton():
    lbl.configure(text = "Hi," + txt.get())
    return

# Thêm button
btnHello = Button(window, text="Say Hello", command=handleButton)
#btnHello.configure(font = myFont)
btnHello.grid(column=1, row=1)

# Thêm combobox

combo = Combobox(window)
combo['values'] = list(range(1,10))
combo.current(0)
combo.grid(column=0, row=2 )


def handleButton1():
    #lbl.configure(text = "Hi," + combo.get())
    messagebox.showinfo("Mì AI Test", "Hi," + str(combo.get()+100))
    return

# Thêm button
btnHello1 = Button(window, text="Say Hello Combo", command=handleButton1)
btnHello1.grid(column=1, row=2)


window.mainloop()
