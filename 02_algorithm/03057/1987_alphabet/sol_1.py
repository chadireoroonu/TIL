import sys
sys.stdin = open('input.txt')

r, c = list(map(int, sys.stdin.readline().split()))
arr = [list(map(str, sys.stdin.readline().strip())) for _ in range(r)]

maxi = 0
visited = set()

di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]

def DFS(x, y, num):
    global maxi
    i, j = x, y
    if num > maxi:
        maxi = num
    visited.add(arr[x][y])
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < r and 0 <= nj < c and arr[ni][nj] not in visited:
            DFS(ni, nj, num + 1)
    visited.remove(arr[x][y])

DFS(0, 0, 1)

print(maxi)