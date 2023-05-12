# visited 배열 3차원 구성
# 위치정보와 함께 말처럼 이동한 횟수 세기
# 말처럼 이동한 횟수 K 도달 시, 이동가능 범위 조정
# 가장 오른쪽 아래 칸 도달 시, 이동 횟수 move 리스트 저장

# 1차 시도 -> 런타임 에러 visited 숫자가 커서 방문할 수 없지만, 벽으로 가로 막혀 나중에 말처럼 이동해야 하는 경우

import sys
from collections import deque
sys.stdin = open('input.txt')

K = int(sys.stdin.readline().strip())
W, H = map(int, sys.stdin.readline().split())
world = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]
move = []    # 도착지까지의 이동 수

di = [-1, -2, -2, -1, 1, 2, 2, 1, -1, 1, 0, 0]    # 원숭이 이동가능 좌표
dj = [-2, -1, 1, 2, 2, 1, -1, -2, 0, 0, -1, 1]

queue = deque()
queue.append((0, 0, 0))
visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]
visited[0][0][0] = 1

while queue:
    i, j, z = queue.popleft()
    if i == H-1 and j == W-1:
        move.append(visited[i][j][z]-1)
    if z < K:    # 말처럼 이동할 기회가 있을 경우
        for k in range(12):
            ni, nj, nz = i + di[k], j + dj[k], z
            if k < 8:    # 말처럼 이동했을 경우 nz 조정
                nz = z + 1
            if 0 <= ni < H and 0 <= nj < W and not visited[ni][nj][nz] and not world[ni][nj]:
                queue.append((ni, nj, nz))
                visited[ni][nj][nz] = visited[i][j][z] + 1

    else:    # 말처럼 이동할 기회가 없을 경우
        for k in range(8, 12):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < H and 0 <= nj < W and not visited[ni][nj][z] and not world[ni][nj]:
                queue.append((ni, nj, z))
                visited[ni][nj][z] = visited[i][j][z] + 1

print(min(move) if move else -1)    # 도착 가능 시 최소값 출력