import sys
sys.stdin = open('input.txt')

n, m = list(map(int, sys.stdin.readline().split()))
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

num = [[0] * (n+1) for _ in range(n+1)]

for i in range(n):
    for j in range(n):
        num[i+1][j+1] = arr[i][j] + num[i][j+1] + num[i+1][j] - num[i][j]

for i in range(m):
    a, b, x, y, = list(map(int, sys.stdin.readline().split()))
    print(num[x][y] - num[x][b-1] - num[a-1][y] + num[a-1][b-1])