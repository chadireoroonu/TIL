# 트리로 부모 정보 저장
# BFS 탐색 total 저장
# 시간 제한 방지 -> 도착 노드 도착 시, 출력 조건 설정

# 1차 시도 -> 4% 틀렸습니다.

import sys
from collections import deque
sys.stdin = open('input.txt')

def sol(queue):
    while queue:
        i = queue.popleft()
        for j in child[i]:
            # print(f'i={i}, j={j}')
            total[j] = max(total[i] + time[j], total[j])
            print(total)
            queue.append(j)
            print(f'deque={queue}')
            count[j] -= 1
            print(f'count={count}')
            if not count[w-1]:
                return print(total[w-1])
    # return print(total[w-1])

T = int(sys.stdin.readline().strip())
for tc in range(T):
    N, K = map(int, sys.stdin.readline().split())
    time = list(map(int, sys.stdin.readline().split()))
    count = [0] * N
    child = [[] for _ in range(N)]
    for _ in range(K):
        a, b = map(int, sys.stdin.readline().split())
        child[a-1].append(b-1)
        count[b-1] += 1
    w = int(sys.stdin.readline().strip())
    print(child)
    print(f'count={count}')
    # print(f'w={w}')

    if count[w-1]:
        total = time[::]
        queue = deque([])
        for x in range(N):
            if not count[x]:
                queue.append(x)
                total[x] = time[x]
        # print(f'time={time}')
        print(f'first deque={queue}')
        # print(f'first total={total}')
        sol(queue)
    else:
        print(time[w-1])