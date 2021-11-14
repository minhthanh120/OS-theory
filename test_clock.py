from tkinter import *
from tkinter.ttk import *
import tkinter
import tkinter.font as font
from tkinter import messagebox

s = [1, 2, 3, 6, 7, 1, 4, 3, 4, 5, 7, 4, 1, 2, 3, 1, 3, 1, 4, 5, 6, 7, 1]
# input: số trang
capacity = 4
def f_clock(s, capacity):
    new = Tk()
    new.title('Giải thuật thay thế trang clock')
    new.geometry("400x300")
    scrollbar = Scrollbar(new)
    scrollbar.pack( side = RIGHT, fill = Y )
    myfont = font.Font(size=30)

    mylist= Listbox(new,width= 400, height = 600, yscrollcommand = scrollbar.set)

    # output: thay đổi của trang
    pf = ''
    fault, top, f, status = 0, 0, [], [0]*capacity
    ptr = 'String|Frame →'
    for b in range(capacity):
        ptr = ptr + str(b) + ' '*4

    stt=''
    for x in range(capacity):
        stt= stt+ str(0)+ '  '
    ptr=ptr+'    Fault'+"  "+stt+ "Pointer"
    mylist.insert(END, ptr)
    for i in s:
        if i not in f:
            if len(f) < capacity:
                f.append(i)
                top = (top+1) % capacity
            else:
                while status[top] == 1:
                    status[top] = 0
                    top = (top+1) % capacity
                f[top] = i
                top = (top+1) % capacity
            pf = '|Yes|'
            fault += 1
        else:
            status[f.index(i)] = 1
            pf = '| No|'

        output = ' '+str(i)+' '*24
    #    print("   %d\t\t" % i, end='')
        for x in f:
            if x== i:
                if fault>capacity and pf=='|Yes|':
                    output = output + str(x)+'*   '
                else:
                    output = output + str(x)+'    '
            else:
                output = output+str(x)+'    '
        for x in range(capacity-len(f)):
                output = output+' '*6
        output = output + " "*5+pf + ' '
        for y in range(capacity):
            if y == top:
                output = output + str(status[y]) + '* '
            else:
                output = output + str(status[y]) + '  '
        output = output + '|' + str(top)
        mylist.insert(END, output)
    mylist.insert(END, "Số page-fault là: "+ str(fault))
    mylist.pack()
    scrollbar.config( command = mylist.yview )

    new.mainloop()

if __name__ == "__main__":
    
    f_clock(s, capacity)