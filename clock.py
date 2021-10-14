import numpy as np
# chuỗi input: frame
frame = np.array([1, 2, 3, 6, 7, 1, 4, 3, 4, 5, 7,
                 4, 1, 2, 3, 1, 3, 1, 4, 5, 6, 7, 1])
# input: số trang
paging = 4
# output: thay đổi của trang
schedule = np.array([])
status = np.zeros((paging, len(frame)+1))
sp = np.array([])  # vị trí con trỏ status
pf = np.array([])  # chuỗi page fault
for i in range(len(frame)):
    
    if (len(now) < paging-1):
        now = np.append(now, frame[i])
        pf=np.append(pf, 1)
    np.hstack((schedule,now.T))
    schedule = np.append(schedule, 1)
print(schedule)
print(pf)