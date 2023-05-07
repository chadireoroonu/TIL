import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(sys.stdin.readline().strip())
for _ in range(T):
    K, M, P = map(int, sys.stdin.readline().split())
    node = [0] * (M + 1)
    child = [[] for _ in range(M + 1)]    # 해당 노드 다음에 오는 노드
    count = [0] * (M + 1)                 # 해당 노드 전에 오는 노드 수
    temp = deque([] for _ in range(M + 1))    # visited[i] 저장
    for _ in range(P):    # 노드 방향, 수 조정
        a, b = map(int, sys.stdin.readline().split())
        child[a].append(b)
        count[b] += 1

    queue = deque()
    visited = [0] * (M + 1)
    for i in range(1, M+1):
        if not count[i]:    # 이전에 오는 노드가 없으면 queue 추가
            visited[i] = 1    # 처음 강줄기는 문제 조건에 따라 1
            queue.append(i)

    while queue:
        i = queue.popleft()
        for j in child[i]:
            count[j] -= 1    # 호출 시 마다 앞서 오는 노드 줄이기
            temp[j].append(visited[i])    # 앞 강줄기 visited 저장
            visited[j] = max(visited[i], visited[j])    # 현재 visited 기록
            if not count[j]:    # 더이상 앞에 오는 강줄기가 없으면 queue 추가
                queue.append(j)
                if temp[j].count(max(temp[j])) > 1:    # 최대값이 두 번 이상이면 +1 저장
                    visited[j] = max(temp[j]) + 1

    print(f'{K} {max(visited)}')    # 테스트케이스 번호와 바다에 닿는 값(최대값) 출력