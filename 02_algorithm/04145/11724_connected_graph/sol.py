# 1. 전체 길 2차원 배열에 저장
# 2. 이차원 배열을 탐색하며 1을 만나면 DFS 함수 실행, count += 1
# 3. 카운트 수 출력

import sys
sys.stdin = open('input.txt')

# 간선 삭제 함수
def DFS(arr, num):
    visited = [0] * n
    connect = [num]
    stack = [num]
    while stack:
        i = stack.pop()
        for j in range(n):
            if arr[i][j] == 1 and visited[j] == 0:
                connect.append(j)
                stack.append(j)
                visited[j] = 1
    # 모든 연결 노드 간선 삭제
    for x in range(len(connect)):
        for y in range(len(connect)):
            arr[connect[x]][connect[y]] = arr[connect[y]][connect[x]] = 0

    return


n, m = list(map(int, sys.stdin.readline().split()))
load = [[0] * n for _ in range(n)]
for _ in range(m):    # 양방향 간선정보 저장
    u, v = list(map(int, sys.stdin.readline().split()))
    load[u-1][v-1] = load[v-1][u-1] = 1

for w in range(n):    # 간선 없는 노드 파악을 위한 작업
    load[w][w] = 1

count = 0

# 2차원 배열 순회하며 간선 발견 시 함수 실행
# 함수 실행 시, 연결 요소 개수 +1
for a in range(n):
    for b in range(n):
        if load[a][b] == 1:
            DFS(load, a)
            count += 1

print(count)