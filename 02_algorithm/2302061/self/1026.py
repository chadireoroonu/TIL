import sys
sys.stdin = open('input.txt')

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a)
temp = [0] * n
copy_b = []
for i in b:
    copy_b.append(i)

for i in range(n):
    b_max = max(copy_b)
    idx = copy_b.index(b_max)
    temp[idx] = a[0]
    a.remove(a[0])
    copy_b[idx] = 0

total = 0
for i in range(n):
    total += temp[i] * b[i]

print(total)