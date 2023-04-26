# 루트 = 1
# 1 넣은 queue 사용
# 시간초과 방지를 위해 포인터 사용

# 1차 시도 -> 메모리 초과

import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline().strip())
arr = [[0]*(n+1) for _ in range(n+1)]
for nc in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    arr[u][v] = arr[v][u] = 1

parent = [0] * (n+1)

queue = [1]
p = 0
while p < len(queue):
    i = queue[p]
    p += 1
    for j in range(1, n+1):
        if arr[i][j] == 1:
            if not parent[j]:
                parent[j] = i
                queue.append(j)

for i in range(2, n+1):
    print(parent[i])