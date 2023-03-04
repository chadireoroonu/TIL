import sys
sys.stdin = open('input.txt')

# 자기보다 큰 물고기가 있는 칸은 지나가지 못함 -> 같으면 지나감
# 자기보다 작은 물고기만 먹을 수 있음 -> 같으면 못먹음
# 자기의 크기만큼 물고기를 먹으면 덩치가 커짐 -> 처음크기 2
# 물고기를 먹으면 그 칸은 빈칸

# 가까운 물고기부터 먹는데, 같은 거리라면 위쪽 물고기를 먹음
# 같은 거리의 위쪽 물고기가 많으면 왼쪽 물고기를 먹
# 1. 탐색 : 왼쪽 위부터 행우선 조회를 해서 먹을 수 있는 것들을 후보군에 넣음
# 2. 거리 : 후보군들의 거리를 조사

def distance(arr, a, b):
    global total
    global count
    global shark
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
                    arr[a][b] = 0
                    arr[ni][nj] = 9
                    count += 1
                    if count == shark:
                        shark += 1
                        count = 0
                    total += visited[i][j]
                elif arr[ni][nj] <= shark:
                    queue.append(ni)
                    queue.append(nj)
                    visited[ni][nj] = visited[i][j] + 1
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
    else:
        break

print(total)