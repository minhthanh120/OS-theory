# FIFO page replacement algorithm implementation in python
# Created By: Suman Adhikari

# print("Enter the number of frames: ", end="")
# capacity = int(input())
capacity = 4
f, fault, top, pf = [], 0, 0, 'No'
s = [1, 2, 3, 4, 7, 4, 2, 3, 4, 5, 7, 1, 2, 3, 7, 1, 3, 4, 1, 5, 6, 7, 1]

print("\nString|Frame →\t", end='')
for i in range(capacity):
    print(i, end=' ')
print("Fault Pointer\n   ↓\n")
for i in s:
    if i not in f:
        if len(f) < capacity:
            f.append(i)
        else:
            f[top] = i
            top = (top+1) % capacity
        fault += 1
        pf = 'T'
    else:
        pf = 'F'
    print("   %d\t\t" % i, end='')
    for x in f:
        print(x, end=' ')
    for x in range(capacity-len(f)):
        print(' ', end=' ')
    print(pf, end=' '*6)
    print(top)
print("\nTotal requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%" %
      (len(s), fault, (fault/len(s))*100))
# Viết chương trình mô phỏng các giải thuật thay thế trang: OPT, FIFO, LRU (LFU, NUR,...) Second Chance (Clock). Thực hiện theo từng bước và thực hiện toàn bộ. Input: số khung trang, chuỗi tham khảo trang, yêu cầu thay thế trang…được sinh ngẫu nhiên. Output: sơ đồ các bước thay thế trang, số PAGE FAULTS. Sử dụng Gridbox hoặc đồ họa. Đánh giá độ hiệu quả (so sánh số page fault) của từng giải thuật
