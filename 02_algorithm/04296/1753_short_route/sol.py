# 연결 정보, 가중치 리스트에 저장
# 최단 경로 찾기 -> BFS 활용
# 시간초과 방지 deque 사용
# 각 최단 경로 저장 리스트 생성

# 1차 시도 -> 2% 시간초과

import sys
from collections import deque
sys.stdin = open('input.txt')

def shift(m):
    queue = deque([m])
    visited = [0] * (V+1)
    visited[m] = 1
    while queue:
        i = queue.popleft()
        for j in range(len(arr[i])):
            if not visited[arr[i][j][0]]:
                queue.append(arr[i][j][0])
                visited[arr[i][j][0]] = visited[i] + arr[i][j][1]
            elif visited[arr[i][j][0]] > visited[i] + arr[i][j][1]:
                queue.append(arr[i][j][0])
                visited[arr[i][j][0]] = visited[i] + arr[i][j][1]

    for i in range(1, V+1):
        if not visited[i] and i != m:
            print('INF')
        else:
            print(visited[i]-1)
    return

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline().strip())
arr = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    arr[u].append([v, w])

arr[1].sort(key=lambda x:x[1])
shift(K)