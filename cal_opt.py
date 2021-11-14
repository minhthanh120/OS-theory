

capacity = 4

s = [1, 2, 3, 6, 7, 1, 4, 3, 4, 5, 7, 4, 1, 2, 3, 1, 3, 1, 4, 5, 6, 7, 1]
#s = [1, 2, 3, 4, 7, 4, 2, 3, 4, 5, 7, 1, 2, 3, 7, 1, 3, 4, 1, 5, 6, 7, 1]
def opt(s, capacity):
    f, fault, pf = [], 0, 'No'
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
    return fault
if __name__ == "__main__":
    
    print(opt(s, capacity))