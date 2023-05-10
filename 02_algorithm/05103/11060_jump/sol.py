import sys
from collections import deque
sys.stdin = open('input.txt')

N = int(sys.stdin.readline().strip())
miro = list(map(int, sys.stdin.readline().split()))

queue = deque([0])
visited = [N + 1] * N
visited[0] = 0
while queue:
    i = queue.popleft()
    for j in range(1, miro[i]+1):
        ni = i + j
        if 0 <= ni < N:
            visited[ni] = min(visited[ni], visited[i] + 1)
            queue.append(ni)

if visited[N-1] != N+1:
    print(visited[N-1])
else:
    print(-1)