import sys
sys.stdin = open('input.txt')

def white(arr, i, j):
    queue = [i, j]
    num = 1
    arr[i][j] = 1
    while queue:
        x = queue.pop(0)
        y = queue.pop(0)
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 0:
                queue.append(nx)
                queue.append(ny)
                num += 1
                arr[nx][ny] = num
    sel.append(num)
    return

m, n, k = list(map(int, input().split()))
arr = [[0]*n for _ in range(m)]
for kc in range(k):
    a, b, x, y = list(map(int, input().split()))

    for i in range(b, y):
        for j in range(a, x):
            arr[i][j] = 1

count = 0
sel = []
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            count += 1
            white(arr, i, j)

print(count)
sel = sorted(sel)
for number in sel:
    print(number, end= ' ')