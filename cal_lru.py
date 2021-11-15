import time
capacity = 4

#print("Enter the reference string: ", end="")
s = [1, 2, 3, 6, 7, 1, 4, 3, 4, 5, 7, 4, 1, 2, 3, 1, 3, 1, 4, 5, 6, 7, 1]
#print("\nString|Frame →\t", end='')
def lru(s, capacity):
    start = time.perf_counter()
    f, st, fault, pf = [], [], 0, 'No'
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
    end = time.perf_counter()
    return fault, end- start

if __name__ == "__main__":
    print(lru(s, capacity))