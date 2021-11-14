from tkinter import *
from tkinter.ttk import *
import tkinter
import tkinter.font as font
from tkinter import messagebox

# chuỗi input: frame
s = [1, 2, 3, 6, 7, 1, 4, 3, 4, 5, 7,
     4, 1, 2, 3, 1, 3, 1, 4, 5, 6, 7, 1]
#s = [1, 2, 3, 4, 7, 4, 2, 3, 4, 5, 7, 1, 2, 3, 7, 1, 3, 4, 1, 5, 6, 7, 1]
# input: số trang
capacity = 4

def f_opt(s, capacity):
    new = Tk()
    new.title('Giải thuật thay thế trang OPT')
    new.geometry("400x300")
    scrollbar = Scrollbar(new)
    scrollbar.pack( side = RIGHT, fill = Y )
    myfont = font.Font(size=30)

    mylist= Listbox(new,width= 400, height = 600, yscrollcommand = scrollbar.set)
    # output: thay đổi của trang
    f, fault, pf = [], 0, 'No'
    ptr = 'String|Frame →'
    for b in range(capacity):
        ptr = ptr + str(b) + ' '*5
    ptr=ptr+'Fault'
    mylist.insert(END, ptr)
    st = [None for i in range(capacity)]
    for i in range(len(s)):
        if s[i] not in f:
            if len(f) < capacity:
                f.append(s[i])
            else:
                for x in range(len(f)):
                    if f[x] not in s[i+1:]:
                        f[x] = s[i]
                        break
                    else:
                        st[x] = s[i+1:].index(f[x])
                else:
                    f[st.index(max(st))] = s[i]
            fault += 1
            pf = 'Yes'
        else:
            pf = 'No'
        output = '  '+str(s[i])+'  '*12
        if pf == 'No':
            for y in f:
                output= output + str(y) + ' '*5
        else:
            for y in f:
                if(fault>capacity-1 and y != s[i]):
                    output= output + str(y) + '*' + '   '
                else:
                    output = output+ str(y) + ' '*5
        for x in range(capacity-len(f)):
            output = output+ ' '*7
        output+= pf
        mylist.insert(END, output)
    mylist.insert(END, "Số page-fault là: "+ str(fault))
    mylist.pack()
    scrollbar.config( command = mylist.yview )

    new.mainloop()

if __name__ == "__main__":
    
    f_opt(s, capacity)