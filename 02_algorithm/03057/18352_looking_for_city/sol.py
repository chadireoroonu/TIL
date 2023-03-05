import sys
sys.stdin = open('input.txt')

n, m, k, x = list(map(int, sys.stdin.readline().split()))
arr = [[0]*(n+1) for _ in range(n+1)]
for mc in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    arr[a][b] = 1

visited = [0] * (n+1)
queue = [x]
visited[x] = 1
while queue:
    now = queue.pop(0)
    for i in range(1, n+1):
        if arr[now][i] == 1 and visited[i] == 0:
            queue.append(i)
            visited[i] = visited[now] + 1

city = []
for j in range(1, n+1):
    if visited[j] == k+1:
        city.append(j)

if city:
    city.sort()
    for k in city:
        print(k)
else:
    print(-1)