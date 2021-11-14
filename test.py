from tkinter import *
import tkinter
from tkinter.ttk import *
from tkinter import messagebox
import cal_clock, cal_fifo, cal_lru, cal_opt

capacity = 4

s = [1, 2, 3, 6, 7, 1, 4, 3, 4, 5, 7, 4, 1, 2, 3, 1, 3, 1, 4, 5, 6, 7, 1]
# 1 2 3 6 7 1 4 3 4 5 7 4 1 2 3 1 3 1 4 5 6 7 1
new = Tk()
new.title("Đánh giá thuật toán thay thế trang")
new.geometry("400x100")
Label(new, text= "Page-fault thuật toán OPT: "+ str(cal_opt.opt(s, capacity))).pack()
Label(new, text= "Page-fault thuật toán LRU: "+ str(cal_lru.lru(s, capacity))).pack()
Label(new, text= "Page-fault thuật toán FIFO: "+ str(cal_fifo.fifo(s, capacity))).pack()
Label(new, text= "Page-fault thuật toán CLOCK: "+ str(cal_clock.clock(s, capacity))).pack()
new.mainloop()