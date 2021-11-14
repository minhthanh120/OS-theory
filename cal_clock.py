# chuỗi input: frame
# s = [1, 2, 3, 6, 7, 1, 4, 3, 4, 5, 7,
#     4, 1, 2, 3, 1, 3, 1, 4, 5, 6, 7, 1]
s = [1, 2, 3, 6, 7, 1, 4, 3, 4, 5, 7, 4, 1, 2, 3, 1, 3, 1, 4, 5, 6, 7, 1]
# input: số trang
capacity = 4
# output: thay đổi của trang
def clock(s, capacity):
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

    return fault
if __name__ == "__main__":
    
    print(clock(s, capacity))