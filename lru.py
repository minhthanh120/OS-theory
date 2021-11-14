# LRU page replacement algorithm implementation in python
# Created By: Suman Adhikari

#print("Enter the number of frames: ", end="")
#capacity = int(input())
capacity = 4
f, st, fault, pf = [], [], 0, 'No'
#print("Enter the reference string: ", end="")
s = [1, 2, 3, 6, 7, 1, 4, 3, 4, 5, 7, 4, 1, 2, 3, 1, 3, 1, 4, 5, 6, 7, 1]
print("\nString|Frame →\t", end='')
for i in range(capacity):
    print(i, end='  ')
print("Fault\n   ↓\n")
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
    print("   %d\t\t" % i, end='')
    for x in f:
        if x != i:
            print(x, end='  ')
        elif x == i:
            print(x, end='* ')
    for x in range(capacity-len(f)):
        print(' '*2, end=' ')
    print(" %s" % pf)
print("\nTotal Page Faults: %d" %
      (fault))

