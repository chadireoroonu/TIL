# 8 범위 조사하며 BFS 탐사
# deque 사용으로 시간초과 방지
# 큰 숫자부터 앞쪽에 배치

import sys
from collections import deque
sys.stdin = open('input.txt')

def sol(a):
    dq = deque([a])
    stone[a] = 1
    while dq:
        x = dq.popleft()
        dx = [(a-1)*x, (b-1)*x, a, b, -a, -b, 1, -1]
        for k in range(8):
            nx = x + dx[k]
            if 0 <= nx < 100001 and stone[nx] == 0:
                stone[nx] = stone[x] + 1
                dq.append(nx)
                if nx == m:
                    return print(stone[x])

a, b, n, m = map(int, sys.stdin.readline().split())

stone = [0] * 100001
sol(n)