# 1차 시도 -> 메모리 초과
# 2차 시도 -> 틀렸습니다 (N==K)
# 3차 시도 -> 50%? 런타임 에러 (N==0)

import sys
from collections import deque
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())
visited = [0] * 100001
parent = [0] * 100001
sec = 0

def sol():
    global sec
    queue = deque([N])
    visited[N] = 1
    while queue:
        i = queue.popleft()
        di = [i, -1, 1]
        for j in range(3):
            ni = i + di[j]
            if 0 <= ni < 100001 and not visited[ni]:
                queue.append(ni)
                visited[ni] = visited[i] + 1
                if not parent[ni]:
                    parent[ni] = i
                if ni == K:
                    sec = visited[ni] - 1
                    print(sec)
                    load()
                    return

def load():
    result = [K]
    pointer = 0
    while pointer < sec:
        i = result[pointer]
        pointer += 1
        j = parent[i]
        result.append(j)

    print(*result[::-1])

if N == K:
    print(0)
    print(N)
else:
    sol()