# Optimal page replacement algorithm (OPT or OPR) implementation in python
# Created By: Suman Adhikari

#print("Enter the number of frames: ", end="")
#capacity = int(input())

capacity = 4
f, fault, pf = [], 0, 'No'
# s = [1, 2, 3, 6, 7, 1, 4, 3, 4, 5, 7, 4, 1, 2, 3, 1, 3, 1, 4, 5, 6, 7, 1]
s = [1, 2, 3, 4, 7, 4, 2, 3, 4, 5, 7, 1, 2, 3, 7, 1, 3, 4, 1, 5, 6, 7, 1]

print("\nString|Frame →\t", end='')
for i in range(capacity):
    print(i, end='  ')
print("Fault\n   ↓\n")
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
            # f[st.index(max(st))] = s[i]
        fault += 1
        pf = 'Yes'
    else:
        pf = 'No'
    print("   %d\t\t" % s[i], end='')
    if(pf == 'No'):
        for x in f:
            print(x, end='  ')
    else:
        for y in f:
            if(y != s[i]):
                print(str(y)+'*', end=' ')
            else:
                print(y, end='  ')
    for x in range(capacity-len(f)):
        print('  ', end=' ')
    print(" %s" % pf)
print('Total Page Faults:', fault)
