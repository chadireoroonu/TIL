# 최초 시도 while 사용 -> 71% 시간초과
# 몫을 먼저 더해주고 K 재할당해야 코인 세기 가능

import sys
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())
coin = [0] * N
count = 0
for i in range(N):
    coin[-i-1] = int(sys.stdin.readline().strip())

for i in range(N):
    if K >= coin[i]:
        count += K // coin[i]
        K = K % coin[i]

print(count)