# 모든 좌표에 visited 배열 생성
# 순간이동 우선으로 BFS 탐색

import sys
sys.stdin = open('input.txt')

def BFS(n):
    visited[n] = 1
    queue = [n]
    p = 0
    while p < len(queue):
        x = queue[p]
        p += 1
        dx = [x, -1, 1]
        for k in range(3):
            nx = x + dx[k]
            if 0 <= nx < 100001 and not visited[nx]:
                queue.append(nx)
                visited[nx] = visited[x] + 1
                if nx == K:
                    return print(visited[x])

N, K = map(int, sys.stdin.readline().split())
visited = [0] * 100001

if N == K:
    print(0)
else:
    BFS(N)