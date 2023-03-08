import sys

sys.stdin = open('input.txt')

n, s = list(map(int, sys.stdin.readline().split()))
number = list(map(int, sys.stdin.readline().split()))
num = [0] * (n + 1)

for i in range(1, n + 1):
    num[i] = number[i - 1] + num[i - 1]  # 부분합 배열

def sol(arr, n):
    for j in range(n):
        for k in range(n-j):
            if arr[-j-1] - arr[-j-2-k] >= s:
                return k+1
    return 0

print(sol(num, n))