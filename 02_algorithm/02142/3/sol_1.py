import sys
sys.stdin = open('input.txt')

def DFS(start):
    visited[start] = 1
    print(start, end= ' ')

    # 다음 조사 위치 찾기
    for next in range(1, v+1):
        # 인접해있고, 방문한 적 없는 곳
        if g[start][next] and not visited[next]:
            DFS(next)

v, e = map(int, input().split())
data = list(map(int, input().split()))
visited = [0] * (v+1)
# 이동가능 정보를 담기 위한 리스트
g = [[0] * (v+1) for _ in range(v+1)]

# 인접행렬 그리기
for i in range(e): # 간선의 개수만큼 그리기
    # 두개의 노드가 이어져있는 정보
    n1, n2 = data[i*2], data[i*2+1]
    g[n1][n2] = 1 # 양방향으로 이동할 수 있다.
    g[n2][n1] = 1

# for i in range(0, len(data), 2):  # 간선 정보만 있고 길이가 없다면
#     print(data[i], data[i+1])     # range를 사용해서 이렇게도 쓸 수 있다.


for mat in g:
    print(mat)

DFS(1)