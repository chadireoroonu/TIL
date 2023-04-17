# 1차 시도 런타임 에러

# k-1 번째 까지만 선택 정렬 -> 1% 시간초과

import sys
sys.stdin = open('input.txt')

n, k = list(map(int, sys.stdin.readline().split()))
num = list(map(int, sys.stdin.readline().split()))


for i in range(k):
    mini = 10 ** 9
    idx = 0
    for j in range(i+1, n):
        if num[j] < mini:
            mini = num[j]
            idx = j
    num[i], num[idx] = mini, num[i]

print(num[k-1])