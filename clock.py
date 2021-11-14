# chuỗi input: frame
# s = [1, 2, 3, 6, 7, 1, 4, 3, 4, 5, 7,
#     4, 1, 2, 3, 1, 3, 1, 4, 5, 6, 7, 1]
s = [1, 2, 3, 6, 7, 1, 4, 3, 4, 5, 7, 4, 1, 2, 3, 1, 3, 1, 4, 5, 6, 7, 1]
# input: số trang
capacity = 4
# output: thay đổi của trang
pf = ''
fault, top, f, status = 0, 0, [], [0]*capacity

print("\nString|Frame →\t", end='')
for i in range(capacity):
    print(i, end='  ')
stt=''
for x in range(capacity):
    stt= stt+ str(0)+ '  '
print("    Fault "+ stt+"Pointer\n   ↓\n")
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

    output = ' '+str(i)+' '*14
#    print("   %d\t\t" % i, end='')
    for x in f:
        if x== i:
            output = output + str(x)+'*  '
        else:
            output = output+str(x)+'  '
    for x in range(capacity-len(f)):
        output = output+' '*3
    output = output + " "*3+pf + ' '
    for y in range(capacity):
        if y == top:
            output = output + str(status[y]) + '* '
        else:
            output = output + str(status[y]) + '  '
    output = output + '|' + str(top)
    print(output)
print(fault)
