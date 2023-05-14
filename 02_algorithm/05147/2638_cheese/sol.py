# 외부 공간 숫자 2로 변경
# 치즈 존재 여부 확인, 연결되지 않는 치즈 덩어리 세서 deque 추가
# 치즈 녹이기 -> 시간 증가
# 내부 공간 외부와 연결 여부 확인 -> 연결 시 2로 변경

# 1차 시도 런타임 에러

import sys
from collections import deque
sys.stdin = open('input.txt')

def air(x, y):    # 외부 공간 숫자 변경
    space = deque()
    space.append((x, y))
    visited = [[0] * M for _ in range(N)]
    arr[x][y] = 2
    visited[x][y] = 1
    while space:
        i, j = space.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and not arr[ni][nj] and not visited[ni][nj]:
                visited[ni][nj] = 1
                arr[ni][nj] = 2
                space.append((ni, nj))
    melt(arr)
    return

def melt(arr):
    global hour
    while True:
        cheese = deque()    # 녹을 치즈 구하기
        temp = [[0] * M for _ in range(N)]    # 공기 인접 방향 수
        for x in range(N):
            for y in range(M):
                if arr[x][y] == 1:
                    cheese.append((x, y))
                    for z in range(4):
                        nx, ny = x + di[z], y + dj[z]
                        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 2:
                            temp[x][y] += 1
        if not cheese:
            break

        # 치즈 녹이기
        hour += 1
        while cheese:
            a, b = cheese.popleft()
            if temp[a][b] >= 2:
                arr[a][b] = 2

        check(arr)

def check(arr):
    # 내부 공간 연결 확인
    temp = deque()
    for x in range(N):
        for y in range(M):
            if not arr[x][y]:
                temp.append((x, y))
                visited = [[0] * M for _ in range(N)]
                visited[x][y] = 1
                while temp:
                    i, j = temp.popleft()
                    for l in range(4):
                        ni, nj = i + di[l], j + dj[l]
                        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[i][j] != 1


N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
hour = 0

air(0, 0)
print(hour)