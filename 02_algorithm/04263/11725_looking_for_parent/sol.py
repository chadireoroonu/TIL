import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline().strip())
arr = [[0]*(n+1) for _ in range(n+1)]
for nc in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    arr[u][v] = arr[v][u] = 1

print(arr)