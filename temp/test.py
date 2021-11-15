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
p_opt, t_opt = cal_opt.opt(s, capacity)
p_lru, t_lru = cal_lru.lru(s, capacity)
p_fifo, t_fifo = cal_fifo.fifo(s, capacity)
p_clock, t_clock = cal_clock.clock(s, capacity)
Label(new, text= "Page-fault thuật toán OPT: "+ str(p_opt)+" trong: "+ str(t_opt)+" giây").pack()
Label(new, text= "Page-fault thuật toán LRU: "+ str(p_lru)+" trong: "+ str(t_lru)+" giây").pack()
Label(new, text= "Page-fault thuật toán FIFO: "+ str(p_fifo)+" trong: "+ str(t_fifo)+" giây").pack()
Label(new, text= "Page-fault thuật toán CLOCK: "+ str(p_clock)+" trong: "+ str(t_clock)+" giây").pack()
new.mainloop()