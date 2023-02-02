n = int(input())
num = list(map(int, input().split()))
max_num = -1000001
min_num = 1000001
for i in range(0, n):
    if num[i] > max_num:
        max_num = num[i]
    if num[i] < min_num:
        min_num = num[i]
print(f'{min_num} {max_num}')