import sys
sys.stdin = open('input.txt')

n, m = list(map(int, sys.stdin.readline().split()))
number = list(map(int, sys.stdin.readline().split()))

num = [0] * (n+1)

for i in range(n):
    num[i+1] = number[i] + num[i]

for k in range(m):
    i, j = list(map(int, sys.stdin.readline().split()))
    print(num[j] - num[i-1])