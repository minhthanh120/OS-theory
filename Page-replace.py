from tkinter import *
import tkinter
from tkinter.ttk import *


window = Tk()
window.geometry("400x350")
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
R1.place(x=0, y=0)

s = Entry(window, width=60)
s.place(x=0, y=25)

R2 = Radiobutton(window, text="Tự động tạo danh sách trang", variable=var, value=2,
                 command=sel)
R2.place(x=0, y=50)

# b = Entry(window, width=90, state=DISABLED)
# b.grid(column=0, row=4)

ls= Label(window, text="Bắt đầu")
ls.place(x=0, y=75)

le= Label(window, text="Kết thúc")
le.place(x=200, y=75)

start = Combobox(window, state = DISABLED)
start['values'] = list(range(1,10))
start.place(x=0, y=100)

end = Combobox(window, state = DISABLED)
end['values'] = list(range(1,10))
end.place(x=200, y=100)

lc = Label(window, text= "Số khung trang:")
lc.place(x= 20, y= 125)

capacity = Combobox(window, width=10)
capacity['values']= list(range(1,15))
capacity.place(x = 115, y=125)


label = Label(window, text= "here")
label.place(x=70, y=155)

window.mainloop()
