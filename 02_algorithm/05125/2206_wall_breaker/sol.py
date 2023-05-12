# 공백이 없으니 분리해서 입력 받기
# 벽을 부쉈는지 확인할 수 있도록, 삼차원 배열 생성
# 위치 정보와 함께 벽 부쉈는지 여부도 함께 전달

import sys
from collections import deque
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
arr = [sys.stdin.readline().strip() for _ in range(N)]
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
shift = []    # 도착지까지의 이동 횟수

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]    # 이동 가능 좌표

queue = deque()
queue.append((0, 0, 0))
visited[0][0][0] = 1
while queue:
    x, y, z = queue.popleft()
    if x == N-1 and y == M-1:    # 도착 시 이동 수 저장
        shift.append(visited[x][y][z])
    for k in range(4):
        nx, ny, nz = x + dx[k], y + dy[k], z
        # 벽 부수기 불가능 시
        if z and 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == '0' and not visited[nx][ny][nz]:
            queue.append((nx, ny, nz))
            visited[nx][ny][nz] = visited[x][y][z] + 1
        # 벽 부수기 가능 시
        if not z and 0 <= nx < N and 0 <= ny < M and not visited[nx][ny][z]:
            if arr[nx][ny] == '1':    # 벽을 부순 경우
                nz = z + 1
            queue.append((nx, ny, nz))
            visited[nx][ny][nz] = visited[x][y][z] + 1

print(min(shift) if shift else -1)
