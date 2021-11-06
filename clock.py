# chuỗi input: frame
# s = [1, 2, 3, 6, 7, 1, 4, 3, 4, 5, 7,
#     4, 1, 2, 3, 1, 3, 1, 4, 5, 6, 7, 1]
s = [1, 2, 3, 4, 7, 4, 2, 3, 4, 5, 7, 1, 2, 3, 7, 1, 3, 4, 1, 5, 6, 7, 1]
# input: số trang
capacity = 4
# output: thay đổi của trang
pf = ''
fault, top, f, status = 0, 0, [], [0]*capacity
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

    output = ' '+str(i)+' '*2
#    print("   %d\t\t" % i, end='')
    for x in f:
        output = output+str(x)+' '
    for x in range(capacity-len(f)):
        output = output+' '*2
    output = output + pf + ' '
    for y in status:
        output = output + str(y) + ' '
    output = output + '|' + str(top)

    print(output)

    '''
    print("   %d\t\t" % i, end='')
    for x in f:
        print(x, end=' ')
    for x in range(capacity-len(f)):
        print(' ', end=' ')
    print(" %s" % pf, end=' ')
    for y in status:
        print(y, end=' ')
    print("|", top)
    print("")
    '''
print(fault)
