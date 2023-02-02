num = []
for i in range(0, 9):
    n = int(input())
    num.append(n)
max_num = num[0]
for j in num:
    if j > max_num:
        max_num = j
print(max_num)
print(num.index(max_num)+1)
