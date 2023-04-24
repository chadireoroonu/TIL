# 정점별 연결관계 2차원 배열 기록
# K 정점에 대한 모든 visited 출력

# 1차 시도 -> 2% 메모리 초과
# 인접행렬 말고 인접 리스트 구현
# 다익스트라 공부해보기
# 우선순위큐도 공부해보기

import sys
sys.stdin = open('input.txt')


def sol(n):
    queue = [n]
    p = 0
    while p < len(queue):
        i = queue[p]
        p += 1
        for j in range(V):
            if arr[i][j] and visited[j] == 'INF':
                visited[j] = arr[i][j] + visited[i]
                queue.append(j)

    return


V, E = map(int, sys.stdin.readline().split())
arr = [[0] * (V + 1) for _ in range(V + 1)]
K = int(sys.stdin.readline().strip())
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    arr[u][v] = arr[v][u] = w

visited = ['INF'] * (V + 1)
visited[K] = 0
sol(K)

for t in range(1, V+1):
    print(visited[t])