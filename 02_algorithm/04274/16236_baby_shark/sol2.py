# https://www.acmicpc.net/problem/16236

# 1. 아기 상어보다 작은 물고기만 먹음
# 2. 상어 크기 수의 물고기 먹으면 성장
# 3. 상어와 크기 같은 물고기 칸 통과 가능, 섭취 불가능
# 4. 먹을 수 있는 물고기가 많다면 거리가 가까운 물고기 섭취
#    거리가 가까운 물고기가 많다면 위, 왼쪽 우선순위
# 5. 아기상어 최초 크기 2, 좌표 9, 물고기 크기 1~6

# BFS 사용, 이전에는 시간초과가 났으니 deque 사용
# 먹을 수 있는 물고기를 찾으면, 동일거리까지만 탐색
# 동일 거리 물고기 deque 삽입 시, i좌표, j좌표 순으로 비교
# 작은 값은 왼쪽, 큰 값은 오른쪽에 넣기
# 먹는 물고기 수 temp 기록, temp == shark => shark + 1


# 최초 상어 좌표 찾은 후 find 함수 실행

# find 함수
# BFS 탐색으로 거리 기록
# 먹을 수 있는 물고기 발견 시 시간 기록, deque 삽입
# 같은 시간까지만 물고기 조사, 물고기 i, j 좌표 우선 정렬
# 물고기 먹고 상어 위치 재할당
# 먹은 물고기 수, 상어 크기 등 고려 후 반복


import sys
from collections import deque
sys.stdin = open('input.txt')


def find(x, y):
    global shark
    sec = 0
    while True:
        visited = [[0] * n for _ in range(n)]
        fish = deque([])
        sea = deque([x, y])
        visited[x][y] = 1
        mini = n*n
        while sea:
            i = sea.popleft()
            j = sea.popleft()
            if visited[i][j] >= mini: # 거리가 찾은 최소 거리보다 많으면 조사 그만
                continue
            di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0:
                    if arr[ni][nj] <= shark:  # 상어와 같으면 이동 가능
                        visited[ni][nj] = visited[i][j] + 1
                        sea.append(ni)
                        sea.append(nj)
                        if arr[ni][nj] and arr[ni][nj] < shark: # 먹이 발견 시 시간, 좌표 기록
                            fish.append([visited[i][j], ni, nj])
                            if mini > visited[i][j]:
                                mini = visited[i][j]
        print(fish)


        return print(sec)


n = int(sys.stdin.readline().strip())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
shark = 2
iidx = jidx = 0

for a in range(n):
    for b in range(n):
        if arr[a][b]:
            iidx, jidx = a, b

find(iidx, jidx)