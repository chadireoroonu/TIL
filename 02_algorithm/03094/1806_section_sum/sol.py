import sys
sys.stdin = open('input.txt')

n, s = list(map(int, sys.stdin.readline().split()))
number = list(map(int, sys.stdin.readline().split()))

num = [0] * (n+1)
for i in range(n):
    num[i+1] = number[i] + num[i]

def sol(arr, n):
    for j in range(n):
        for k in range(n, j, -1):
            if arr[k] - arr[k-j] >= s:
                return print(j)

    return print(0)

sol(num, n)