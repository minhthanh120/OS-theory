from tkinter import *
import tkinter
from tkinter.ttk import *
from tkinter import messagebox
import random
allfont=("Arial", 12)

window = Tk()
window.title("Mô phỏng thuật toán thay thế trang")
window.geometry("410x350")
var = IntVar(window, 1)
ath = IntVar(window, 1)

# start = IntVar()
# end=IntVar()



def sel():
    # selection = "You selected the option " + \
    #     str(var.get())+"  " + str(ath.get())
    # label.config(text=selection)
    if var.get() == 2:
        s.config(state=DISABLED)
        end.config(state=NORMAL)
        start.config(state=NORMAL)
        rbt.config(state=NORMAL)
        nump.config(state=NORMAL)
        nump.delete(0, END)
        nump.insert(0, '21')
        lst.config(state= NORMAL)
    else:
        s.config(state=NORMAL)
        lst.delete(0, END)
        end.config(state=DISABLED)
        start.config(state=DISABLED)
        nump.config(state=DISABLED)
        rbt.config(state=DISABLED)
        lst.config(state= DISABLED)

listpage= []
capacity=0

def rnd():
    listpage = [random.randrange(int(start.get()), int(end.get())+1, 1) for i in range(int(nump.get()))]
    lst.delete(0, END)
    lst.insert(0, listpage)
    messagebox.showinfo("Chuỗi random",listpage)
    return 

def run():
    messagebox.showinfo("test run", str(len(listpage)))

R1 = Radiobutton(window, text="Danh sách trang", variable=var, value=1,
                 command=sel)
R1.place(x=10, y=15)

s = Entry(window, width=64)
s.place(x=10, y=40)

R2 = Radiobutton(window, text="Tự động tạo danh sách trang", variable=var, value=2,
                 command=sel)
R2.place(x=10, y=70)

# b = Entry(window, width=90, state=DISABLED)
# b.grid(column=0, row=4)

ls = Label(window, text="Bắt đầu:")
ls.place(x=10, y=100)

le = Label(window, text="Kết thúc:")
le.place(x=120, y=100)

rbt = Button(window, text="Random", state=DISABLED, command= rnd)
rbt.place(x=335, y=95, height=30, width=65)

start = Combobox(window, state=DISABLED, width=3)
start['values'] = list(range(1, 10))
start.current(0)
start.place(x=60, y=100)

end = Combobox(window, state=DISABLED, width=3)
end['values'] = list(range(1, 10))
end.current(8)
end.place(x=172, y=100)

ln = Label(window, text="Số trang:")
ln.place(x=230, y=100)

nump = Entry(window, state=DISABLED, width=5)
nump.place(x=281, y=100)

lc = Label(window, text="Số khung trang:")
lc.place(x=100, y=170)


lst = Entry(window, state=DISABLED, width=64)
lst.place(x=10, y=130)

ccb = Combobox(window, width=3)
ccb['values'] = list(range(1, 11))
ccb.current(3)
ccb.place(x=195, y=170)

la = Label(window, text="Loại giải thuật:")
la.place(x=10, y=200)

opt = Radiobutton(window, text="OPT", variable=ath, value=1)
opt.place(x=100, y=200)

lru = Radiobutton(window, text="LRU", variable=ath, value=2)
lru.place(x=160, y=200)

fifo = Radiobutton(window, text="FIFO", variable=ath, value=3)
fifo.place(x=220, y=200)

clock = Radiobutton(window, text="clock", variable=ath, value=4)
clock.place(x=280, y=200)

btn = Button(window, text="Run", command= run)
btn.place(x=140, y=230)

label = Label(window, text="here", font=allfont)
label.place(x=70, y=270)

window.eval('tk::PlaceWindow . center')

window.mainloop()
