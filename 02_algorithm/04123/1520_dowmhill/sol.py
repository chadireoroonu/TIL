# 이동할 곳의 숫자가 작으면 이동
# 중복 길 제거 -> 이동 시 arr[x][y] * count
# visited 불필요 -> 높이 차이때문에 못돌아옴 X
# visited -> 지금까지 지나온 길 정보 기록 -> 숫자 배열로 변환

import sys
sys.stdin = open('input.txt')

n, m = list(map(int, sys.stdin.readline().split()))
land = [list(map(int, sys.stdin.readline().split()))for _ in range(n)]
load = set()

def downhill(arr, x, y):
    global load
    count = 1
    visited = [[0] * n for _ in range(n)]
    queue = [x, y]
    # visited[x][y] = arr[x][y] * count
    visited[x][y] = str(arr[x][y])
    while queue:
        i = queue.pop(0)
        j = queue.pop(0)
        count += 1
        di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] < arr[i][j]:
                queue.append(ni)
                queue.append(nj)
                if ni == n-1 and nj == n-1:
                    load.add(visited[n-1][n-1])
                # visited[ni][nj] = visited[i][j] + arr[ni][nj] * count
                visited[ni][nj] = visited[i][j] + str(arr[ni][nj])
    print(visited)
    print(visited[n-1][n-1])
    return

downhill(land, 0, 0)
print(load)