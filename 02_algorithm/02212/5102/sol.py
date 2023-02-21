import sys
sys.stdin = open('input.txt')

# BFS 조사를 수행할 함수 생성
# 인자로는 arr, 출발지, 도착지 삽입
# 방문 여부, 이동 수 파악을 위한 visit 생성
def BFS(arr, now, goal):
    queue = [now]
    visit = [0] * (v+1)
    visit[now] = 1

    # queue 존재 하는 동안 반복
    # queue 첫 요소를 now 할당
    while queue:
        now = queue.pop(0)
        # goal 도달 시 visit을 통해 현재까지의 누적 이동 후 반환
        if now == goal:
            return visit[now] - 1
        # 아니라면 전 노드를 순회하며,
        # 현재 노드와 간선이 이어져있는 노드 queue 추가
        # visit에는 이동 정보를 담기 위해 now보다 1 큰 수를 할당
        for j in range(v+1):
            if arr[now][j] == 1 and visit[j] == 0:
                queue.append(j)
                visit[j] = visit[now] + 1
    # 함수에서 리턴되는 값이 없다면 도착 불가
    return 0

t = int(input())
for tc in range(1, t+1):
    v, e = list(map(int, input().split()))
    arr = [[0] * (v+1) for _ in range(v+1)]

    # 간선의 이동은 양방향이 가능하므로,
    # arr에서 양방향의 길을 모두 표시
    for i in range(e):
        a, b = list(map(int, input().split()))
        arr[a][b] = arr[b][a] = 1
    start, goal = list(map(int, input().split()))

    print(f'#{tc} {BFS(arr, start, goal)}')