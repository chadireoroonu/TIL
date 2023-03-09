import sys
sys.stdin = open('input.txt')

n, k = list(map(int, sys.stdin.readline().split()))
number = list(map(int, sys.stdin.readline().split()))

num = [0] * (n+1)

for i in range(n):
    num[i+1] = number[i] + num[i]

maxi = -100 * n+1
for i in range(n, k-1, -1):
    if num[i] - num[i-k] >= maxi:
        maxi = num[i] - num[i-k]

print(maxi)