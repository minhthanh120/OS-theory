from tkinter import *
import tkinter
from tkinter.ttk import *


window = Tk()
window.geometry("800x150")
var = IntVar()
# start = IntVar()
# end=IntVar()


def sel():
    selection = "You selected the option " + str(var.get())
    label.config(text=selection)
    if var.get() == 2:
        s.config(state=DISABLED)
        end.config(state=NORMAL)
        start.config(state=NORMAL)
    else:
        s.config(state=NORMAL)
        end.config(state=DISABLED)
        start.config(state=DISABLED)


R1 = Radiobutton(window, text="Danh sách trang", variable=var, value=1,
                 command=sel)
R1.grid(column=0, row=0, sticky=W)

s = Entry(window, width=60)
s.grid(column=0, row=1)

R2 = Radiobutton(window, text="Tự động tạo danh sách trang", variable=var, value=2,
                 command=sel)
R2.grid(column=0, row=2, sticky=W)

# b = Entry(window, width=90, state=DISABLED)
# b.grid(column=0, row=4)

start = Combobox(window, state=DISABLED)
start['values'] = list(range(1, 10))
start.grid(column=0, row=5, sticky=W)

end = Combobox(window, state=DISABLED)
end['values'] = list(range(1, 10))
end.grid(column=1, row=5, sticky=W)

ls = Label(window, text="Bắt đầu")
ls.grid(column=0, row=4, sticky=W)

le = Label(window, text="Kết thúc")
le.grid(column=1, row=4, sticky=W)

label = Label(window)
label.grid(column=0, row=6, sticky=W)

window.mainloop()
