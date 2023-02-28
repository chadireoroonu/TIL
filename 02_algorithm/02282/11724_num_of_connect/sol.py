import sys
sys.stdin = open('input.txt')

n, m = list(map(int, input().split()))
arr = [[0] * (n+1) for _ in range(n+1)]
for i in range(m):
    a, b = list(map(int, input().split()))
    arr[a][b] = arr[b][a] = 1

