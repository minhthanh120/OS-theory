capacity = 4
f, fault, pf = [], 0, 'No'
s = [1, 2, 3, 6, 7, 1, 4, 3, 4, 5, 7, 4, 1, 2, 3, 1, 3, 1, 4, 5, 6, 7, 1]
print(len(s))
for i in range(len(s)):
    print(i)

# print("\nString|Frame →\t", end='')
# for i in range(capacity):
#     print(i, end=' ')
# print("Fault\n   ↓\n")
# st = [None for i in range(capacity)]
# for i in range(len(s)):
#     if s[i] not in f:
#         if len(f) < capacity:
#             f.append(s[i])
#         else:
#             try:
#                 index_value = s.index(44)
#             except ValueError:
#                 index_value = -1

#         fault += 1
#         pf = 'Yes'

#     else:
#         pf = 'No'
