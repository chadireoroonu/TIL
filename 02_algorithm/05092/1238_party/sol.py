import sys
from collections import deque
sys.stdin = open('input.txt')

N, M, X = map(int, sys.stdin.readline().split())
load = deque([] for _ in range(N))
for _ in range(M):
    a, b, t = map(int, sys.stdin.readline().split())
    load[a-1].append([b-1, t])

maxi = 0

def shift(x, y):
    time = 10000000
    queue = deque([x])
    visited = [10000000] * M
    visited[x] = 1
    while queue:
        i = queue.popleft()
        if i == y and visited[i] < time:
            time = visited[i]
        if visited[i] > time:
            continue
        for j in load[i]:
            if visited[i] + j[1] <= visited[j[0]]:
                visited[j[0]] = visited[i] + j[1]
                queue.append(j[0])
    return time - 1

for k in range(N):
    time = shift(k, X-1) + shift(X-1, k)
    if time > maxi:
        maxi = time

print(maxi)