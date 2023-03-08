import sys
sys.stdin = open('input.txt')

n, m = list(map(int, sys.stdin.readline().split()))
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

num = [[0] * (m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        num[i][j] = arr[i-1][j-1] + num[i-1][j] + num[i][j-1] - num[i-1][j-1]

k = int(sys.stdin.readline())
for kc in range(k):
    a, b, x, y = list(map(int, sys.stdin.readline().split()))

    print(num[x][y] - num[x][b-1] - num[a-1][y] + num[a-1][b-1])
