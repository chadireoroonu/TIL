import sys
sys.stdin = open('input.txt')

n, m = list(map(int, sys.stdin.readline().split()))
arr = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    arr[a][b] = arr[b][a] = 1

num = []
for i in range(1, n+1):
