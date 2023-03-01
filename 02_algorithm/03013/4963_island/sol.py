import sys
sys.stdin = open('input.txt')

def island(arr, i, j):
    queue = [i, j]
    arr[i][j] = 0

    while queue:
        i = queue.pop(0)
        j = queue.pop(0)
        di = [-1, -1, -1, 0, 0, 1, 1, 1]
        dj = [-1, 0, 1, -1, 1, -1, 0, 1]
        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1:
                queue.append(ni)
                queue.append(nj)
                arr[ni][nj] = 0

while True:
    m, n = list(map(int, input().split()))
    if m == 0 and n == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(n)]

    count = 0
    for x in range(n):
        for y in range(m):
            if arr[x][y] == 1:
                count += 1
                island(arr, x, y)

    print(count)
