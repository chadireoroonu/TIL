import sys
sys.stdin = open('input.txt')

n, m = list(map(int, sys.stdin.readline().split()))
arr = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    arr[a][b] = arr[b][a] = 1

person = 0
mini = n*m
for i in range(1, n+1):
    temp = 0
    queue = [i]
    visited = [0] * (n+1)
    visited[i] = 1
    while queue:
        x = queue.pop(0)
        for j in range(1, n+1):
            if arr[x][j] == 1 and visited[j] == 0:
                visited[j] = visited[x] + 1
                queue.append(j)

    temp = sum(visited)-n
    if mini > temp:
        mini = temp
        person = i

print(person)