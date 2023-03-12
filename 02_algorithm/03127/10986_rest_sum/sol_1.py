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

print(total)
total.sort()
# 개수가 겹치는 연산을 줄여볼까

count = 0
for i in range(m):
    temp = num.count(i)
    while temp-1 > 0:
        count += temp - 1
        temp -= 1

print(count)