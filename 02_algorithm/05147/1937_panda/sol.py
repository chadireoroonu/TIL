# BFS 탐색
# 매 칸 탐색 후 최대 이동 칸 수 갱신
# 1차 시도 -> 시간초과

# 한 번이라도 이동할 수 있는 좌표를 deque에 담아 넘기기

import sys
from collections import deque
sys.stdin = open('input.txt')

n = int(sys.stdin.readline().strip())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
eat = 0

def search(arr):
    queue = deque()
    for i in range(n):
        for j in range(n):
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < n and 0 <= nj < 0 and arr[i][j] < arr[ni][nj]:
                    queue.append((i, j))
    panda(queue)
    return

def panda(queue):
    global eat
    visited = [[0] * n for _ in range(n)]
    while queue:
        i, j = queue.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                if arr[ni][nj] > arr[i][j]:
                    visited[ni][nj] = visited[i][j] + 1
                    queue.append((ni, nj))
    for i in range(n):
        for j in range(n):
            if visited[i][j] > eat:
                eat = visited[i][j]
    return

search(arr)

print(eat)