import sys
from collections import deque
sys.stdin = open('input.txt')

N = int(sys.stdin.readline().strip())
miro = list(map(int, sys.stdin.readline().split()))

queue = deque([0])
visited = [0] * N
visited[0] = 1
while queue:
    i = queue.popleft()
    for j in range(miro[i], 0, -1):
        ni = i + j
        if ni < N and not visited[ni]:
            visited[ni] = visited[i] + 1
            queue.append(ni)

print(visited[-1] - 1 if visited[-1] else -1)