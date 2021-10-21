# FIFO page replacement algorithm implementation in python
# Created By: Suman Adhikari

#print("Enter the number of frames: ", end="")
#capacity = int(input())
capacity = 4
f, fault, top, pf = [], 0, 0, 'No'
s = [1, 2, 3, 4, 7, 4, 2, 3, 4, 5, 7, 1, 2, 3, 7, 1, 3, 4, 1, 5, 6, 7, 1]

print("\nString|Frame →\t", end='')
for i in range(capacity):
    print(i, end=' ')
print("Fault\n   ↓\n")
for i in s:
    if i not in f:
        if len(f) < capacity:
            f.append(i)
        else:
            f[top] = i
            top = (top+1) % capacity
        fault += 1
        pf = 'Yes'
    else:
        pf = 'No'
    print("   %d\t\t" % i, end='')
    for x in f:
        print(x, end=' ')
    for x in range(capacity-len(f)):
        print(' ', end=' ')
    print(" %s" % pf)
print("\nTotal requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%" %
      (len(s), fault, (fault/len(s))*100))
