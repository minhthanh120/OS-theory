
capacity = 4
f, fault, top, pf = [], 0, 0, 'No'
s = [1, 2, 3, 6, 7, 1, 4, 3, 4, 5, 7, 4, 1, 2, 3, 1, 3, 1, 4, 5, 6, 7, 1]

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
print("Total Page Faults: " , fault)
# Viết chương trình mô phỏng các giải thuật thay thế trang: OPT, FIFO, LRU (LFU, NUR,...) Second Chance (Clock). Thực hiện theo từng bước và thực hiện toàn bộ. Input: số khung trang, chuỗi tham khảo trang, yêu cầu thay thế trang…được sinh ngẫu nhiên. Output: sơ đồ các bước thay thế trang, số PAGE FAULTS. Sử dụng Gridbox hoặc đồ họa. Đánh giá độ hiệu quả (so sánh số page fault) của từng giải thuật