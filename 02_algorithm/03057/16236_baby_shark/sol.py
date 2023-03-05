import sys
sys.stdin = open('input.txt')

def distance(arr, a, b):
    global total
    global count
    global shark
    food = []
    queue = [a, b]
    visited = [[0] * n for _ in range(n)]
    visited[a][b] = 1
    while queue:
        i = queue.pop(0)
        j = queue.pop(0)
        di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0:
                if arr[ni][nj] != 0 and arr[ni][nj] < shark:
                    food.append([visited[i][j], ni, nj])
                    break
                elif arr[ni][nj] <= shark:
                    queue.append(ni)
                    queue.append(nj)
                    visited[ni][nj] = visited[i][j] + 1
    if food:
        food.sort()
        arr[a][b] = 0
        total += food[0][0]
        arr[food[0][1]][food[0][2]] = 9
        count += 1
        if count == shark:
            shark += 1
            count = 0
    else:
        for x in range(n):
            for y in range(n):
                if arr[x][y] < shark:
                    arr[x][y] = 0

    return

n = int(sys.stdin.readline())
sea = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

shark = 2
total = 0
count = 0

while True:
    idxi = idxj = 0
    fish = 0
    for a in range(n):
        for b in range(n):
            if 0 < sea[a][b] < shark:
                fish += 1
            if sea[a][b] == 9:
                idxi, idxj = a, b
                if fish:
                    distance(sea, idxi, idxj)
                    continue
    if fish:
        distance(sea, idxi, idxj)
    else:
        break

print(total)