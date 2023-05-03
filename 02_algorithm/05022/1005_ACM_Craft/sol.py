# 1. 리스트로 먼저 건설되어야 하는 건물 정보 저장
# 2. BFS 탐색, total 누적 시간 저장
# 3. 먼저 건축되어야 하는 건물이 없을 경우 queue 추가, 건축 시작

# 1차 시도 -> 4% 틀렸습니다.
# 2차 시도 -> 시간 초과

import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(sys.stdin.readline().strip())
for tc in range(T):
    N, K = map(int, sys.stdin.readline().split())
    time = list(map(int, sys.stdin.readline().split()))    # 건축 시간
    count = [0] * N    # 먼저 건축되어야 하는 건물 수
    child = [[] for _ in range(N)]    # 건축 완료 후 건설될 수 있는 건물들
    for _ in range(K):
        a, b = map(int, sys.stdin.readline().split())
        child[a-1].append(b-1)    # 건축 정보 저장
        count[b-1] += 1    # 건축 조건 수 추가
    w = int(sys.stdin.readline().strip())

    total = time[::]
    queue = deque()
    for x in range(N):    # 건축 가능 시 queue 추가
        if not count[x]:
            queue.append(x)
            total[x] = time[x]    # 누적시간 저장
    while queue:
        i = queue.popleft()
        for j in child[i]:    # 건축 정보 리스트 활용
            total[j] = max(total[i] + time[j], total[j])    # 큰 값 저장
            count[j] -= 1    # 건축 조건 건물 수 조정
            if not count[j]:    # 건축 가능 시 queue 추가
                queue.append(j)

    print(total[w-1])