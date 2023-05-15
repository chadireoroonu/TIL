# 외부 공간 숫자 2로 변경
# 치즈 존재 여부 확인, 연결되지 않는 치즈 덩어리 세서 deque 추가
# 치즈 녹이기 -> 시간 증가
# 내부 공간 외부와 연결 여부 확인 -> 연결 시 2로 변경

# 1차 시도 런타임 에러 -> arr[ni][nj]가 0인 경우만 찾아서 2인 경우 종료 됨

import sys
from collections import deque
sys.stdin = open('input.txt')

def air(x, y):    # 외부 공간 숫자 변경
    space = deque()
    space.append((x, y))
    visited = [[0] * M for _ in range(N)]
    visited[x][y] = 1
    while space:    # 다시 visited 추가하고 재방문 방지
        i, j = space.popleft()
        for k in range(4):    # 상하좌우 방향 연결된 공간 확인
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                if not arr[ni][nj] or arr[ni][nj] == 2:
                    arr[ni][nj] = 2
                    space.append((ni, nj))
                    visited[ni][nj] = 1
    melt(arr)
    return

def melt(arr):
    global hour
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

    if not cheese:    # cheese 다 녹으면 시간 출력 반환
        return print(hour)
    else:    # 치즈 녹이기
        hour += 1
        while cheese:
            a, b = cheese.popleft()
            if temp[a][b] >= 2:    # 두 면 이상 외부 노출 시
                arr[a][b] = 2
        air(0, 0)    # 내부 공간 외부 연결 확인

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
hour = 0

arr[0][0] = 2
air(0, 0)