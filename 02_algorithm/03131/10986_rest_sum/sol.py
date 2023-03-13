import sys
sys.stdin = open('input.txt')

n, m = list(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))

num = [0] * (n+1)
for q in range(n):
    num[q+1] = (arr[q] + num[q]) % m

num.sort()
total = [0] * m
for i in range(m):
    total[i] = num.count(i)

count = 0
for i in range(m-1, -1, -1):
    if total[i]:
        count += total[i]
    if i != 0:
        total[i-2] += total[i-1] - 1

print(count)