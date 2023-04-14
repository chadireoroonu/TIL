import sys
sys.stdin = open('input.txt')

n, m = list(map(int, sys.stdin.readline().split()))
load = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    u, v = list(map(int, sys.stdin.readline().split()))
    load[u][v] = load[v][u] = 1
connect = []

for i in range(1, n+1):
    visited = [0] * (n+1)
    visited[i] = 1
    temp = i
    stack = [i]
    while stack:
        k = stack.pop()
        for j in range(1, n+1):
            if load[k][j] == 1 and visited[j] == 0:
                stack.append(j)
                visited[j] = 1
                load[k][j] = load[j][k] = 0
                temp += j
    if temp > i:
        connect.append(temp)

print(connect)
print(len(connect))