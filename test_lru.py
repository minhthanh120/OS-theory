from tkinter import *
from tkinter.ttk import *
import tkinter
import tkinter.font as font
from tkinter import messagebox

# chuỗi input: frame
# s = [1, 2, 3, 6, 7, 1, 4, 3, 4, 5, 7,
#     4, 1, 2, 3, 1, 3, 1, 4, 5, 6, 7, 1]
s = [1, 2, 3, 6, 7, 1, 4, 3, 4, 5, 7, 4, 1, 2, 3, 1, 3, 1, 4, 5, 6, 7, 1]
# input: số trang
capacity = 4
def f_lru(s, capacity):
    new = Tk()
    new.title('Giải thuật thay thế trang clock')
    new.geometry("400x300")
    scrollbar = Scrollbar(new)
    scrollbar.pack( side = RIGHT, fill = Y )
    myfont = font.Font(size=30)

    mylist= Listbox(new,width= 400, height = 600, yscrollcommand = scrollbar.set)

    # output: thay đổi của trang
    f, st, fault, pf = [], [], 0, 'No'
    ptr = 'String|Frame →'
    for b in range(capacity):
        ptr = ptr + str(b) + ' '*5
    ptr=ptr+'Fault'
    mylist.insert(END, ptr)
    for i in s:
        if i not in f:
            if len(f) < capacity:
                f.append(i)
                st.append(len(f)-1)
            else:
                ind = st.pop(0)
                f[ind] = i
                st.append(ind)
            pf = 'Yes'
            fault += 1
        else:
            st.append(st.pop(st.index(f.index(i)))) 
            pf = 'No'
        output = '  '+str(i)+'  '*12
        if(pf == 'No'):
            for y in f:
                output= output + str(y) + ' '*5
        else:
            for y in f:
                if(y != i):
                    output= output + str(y) +  ' '*5
                else:
                    if fault>capacity:
                        output = output+ str(y) + '*'+' '*3    
                    else:
                        output = output+ str(y) +' '*5
        for x in range(capacity-len(f)):
            output = output+ ' '*7
        output+= pf
        mylist.insert(END, output)
    mylist.insert(END, "Số page-fault là: "+ str(fault))
    mylist.pack()
    scrollbar.config( command = mylist.yview )

    new.mainloop()
if __name__ == "__main__":
    
    f_lru(s, capacity)