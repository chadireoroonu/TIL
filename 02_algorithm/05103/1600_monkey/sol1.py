# visited 배열의 각 칸을 두 칸 짜리 리스트로 만들고
# 첫 칸에는 K까지 숫자 세기 작으면 이동 가능
# 지금 visited 0번째 숫자가 K와 같다면 di, dj 범위를 조절해서 이동
# visited 두 번째 칸은 이동 횟수 세기

# 1차 시도 -> 런타임 에러 visited 숫자가 커서 방문할 수 없지만, 벽으로 가로 막혀 나중에 말처럼 이동해야 하는 경우
# 시간초과 걸리지 않게 주의해서 추가하기

import sys
from collections import deque
sys.stdin = open('input.txt')

K = int(sys.stdin.readline().strip())
W, H = map(int, sys.stdin.readline().split())
world = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]
move = -1

di = [-1, -2, -2, -1, 1, 2, 2, 1, -1, 1, 0, 0]
dj = [-2, -1, 1, 2, 2, 1, -1, -2, 0, 0, -1, 1]

queue = deque()
queue.append((0, 0))
visited = [[[0, 0] for _ in range(W)] for _ in range(H)]
while queue:
    i, j = queue.popleft()
    if i == H-1 and j == W-1:
        move = visited[i][j][1]
    if move > 0 and visited[i][j][1] > move:
        continue
    if visited[i][j][0] < K:
        for k in range(12):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < H and 0 <= nj < W and not world[ni][nj]:
                if visited[ni][nj][1] and visited[ni][nj][1] >= visited[i][j][1] + 1:
                    visited[ni][nj][1] = visited[i][j][1] + 1
                    visited[ni][nj][0] = visited[i][j][0]
                    if k < 8:
                        visited[ni][nj][0] += 1
                    queue.append((ni, nj))
                elif not visited[ni][nj][1]:
                    visited[ni][nj][1] = visited[i][j][1] + 1
                    visited[ni][nj][0] = visited[i][j][0]
                    if k < 8:
                        visited[ni][nj][0] += 1
                    queue.append((ni, nj))

    else:
        for k in range(8, 12):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < H and 0 <= nj < W and not world[ni][nj]:
                if visited[ni][nj][1] and visited[ni][nj][1] >= visited[i][j][1] + 1:
                    visited[ni][nj][1] = visited[i][j][1] + 1
                    visited[ni][nj][0] = visited[i][j][0]
                    queue.append((ni, nj))
                elif not visited[ni][nj][1]:
                    visited[ni][nj][1] = visited[i][j][1] + 1
                    visited[ni][nj][0] = visited[i][j][0]
                    queue.append((ni, nj))

print(move)