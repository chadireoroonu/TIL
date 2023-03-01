import sys
sys.stdin = open('input.txt')

def bug(arr, i, j):
    queue = [i, j]

    while queue:
        i = queue.pop(0)
        j = queue.pop(0)
        arr[i][j] = 0
        di = [-1, 1, 0, 0]
        dj = [0, 0, -1, 1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0<= nj < m and arr[ni][nj] == 1:
                queue.append(ni)
                queue.append(nj)
                arr[ni][nj] = 0
    return

t = int(input())
for tc in range(1, t+1):
    m, n, k = list(map(int, input().split()))
    arr = [[0]*m for _ in range(n)]
    for kc in range(k):
        b, a = list(map(int, input().split()))
        arr[a][b] = 1

    count = 0
    for x in range(n):
        for y in range(m):
            if arr[x][y] == 1:
                count += 1
                bug(arr, x, y)

    print(count)