# 트리로 부모 정보 저장
# BFS 탐색 total 저장
# 시간 제한 방지 -> 도착 노드 도착 시, 출력 조건 설정

# 1차 시도 -> 4% 틀렸습니다.

import sys
from collections import deque
sys.stdin = open('input.txt')

def sol(queue):
    check = [0] * N
    while queue:
        i = queue.popleft()
        for j in range(len(child[i-1])):
            k = child[i-1][j]
            total[k] = max(total[i-1] + time[k], total[k])
            queue.append(k)
            check[k] += 1
            if check[w-1] == count[w-1]:
                return print(total[w-1])

T = int(sys.stdin.readline().strip())
for tc in range(T):
    N, K = map(int, sys.stdin.readline().split())
    time = list(map(int, sys.stdin.readline().split()))
    count = [0] * N
    child = []
    for _ in range(N):
        child.append([])
    for _ in range(K):
        a, b = map(int, sys.stdin.readline().split())
        child[a-1].append(b-1)
        count[b-1] += 1
    w = int(sys.stdin.readline().strip())

    if count[w-1]:
        total = [0] * N
        queue = deque([])
        for x in range(N):
            if child[x-1]:
                queue.append(x)
                total[x-1] = time[x-1]
        sol(queue)
    else:
        print(time[w-1])