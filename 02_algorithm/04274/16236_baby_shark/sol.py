# https://www.acmicpc.net/problem/16236

# 1. 아기 상어보다 작은 물고기만 먹음
# 2. 상어 크기 수의 물고기 먹으면 성장
# 3. 상어와 크기 같은 물고기 칸 통과 가능, 섭취 불가능
# 4. 먹을 수 있는 물고기가 많다면 거리가 가까운 물고기 섭취
#    거리가 가까운 물고기가 많다면 위, 왼쪽 우선순위
# 5. 아기상어 최초 크기 2, 좌표 9, 물고기 크기 1~6


# 최초 상어 좌표 찾은 후 find 함수 실행
# find 함수
# BFS 탐색으로 거리 기록
# 먹을 수 있는 물고기 발견 시 [시간, i, j] 리스트에 추가
# 최소거리 초과시 조사 중단, 물고기 i, j 좌표 우선 정렬
# 먹을 물고기가 있다면 먹고, 상어 위치 재할당
# 먹은 물고기 수와 상어 크기 비교후 상어 성장 확인
# 먹을 물고기가 없을 때까지 반복


import sys
from collections import deque
sys.stdin = open('input.txt')


def find(x, y, fish):
    global shark
    visited = [[0] * n for _ in range(n)]
    load = deque([x, y])
    visited[x][y] = 1
    while load:
        i = load.popleft()
        j = load.popleft()
        if fish and fish[0][0] < visited[i][j]:    # 최소 거리 초과 시 조사 중단
            continue
        di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0:
                if sea[ni][nj] <= shark:  # 상어와 같으면 이동 가능
                    visited[ni][nj] = visited[i][j] + 1
                    load.append(ni)
                    load.append(nj)
                    if 0 < sea[ni][nj] < 7 and sea[ni][nj] < shark: # 먹이 발견 시 시간, 좌표 기록
                        fish.append([visited[i][j], ni, nj])
    return fish.sort()


n = int(sys.stdin.readline().strip())
sea = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
shark = 2
sec = 0    # 총 이동 시간
eat = 0    # 먹은 물고기

x = y = 0    # 상어찾기
for a in range(n):
    for b in range(n):
        if sea[a][b] == 9:
            sea[a][b] = 0
            x, y = a, b

while True:
    food = []    # 먹이 물고기 담을 배열
    find(x, y, food)

    if food:    # 문제 조건에 따라 맨 앞 물고기 먹음
        sec += food[0][0]
        x, y = food[0][1], food[0][2]
        sea[x][y] = 0
        eat += 1
        if eat == shark:    # 상어 성장 확인
            eat = 0
            shark += 1
    else:    # 먹을 물고기가 없다면 반복 중단
        break

print(sec)