import sys
sys.stdin = open('input.txt')

def DFS(arr, s):
    stack = [s]
    visit[s] = 1

    while stack:
        now = stack.pop()
        print(now, end= ' ')
        for j in range(v+1):
            if arr[now][j] == 1 and visit[j] == 0:
                DFS(arr, j)


def BFS(arr, s, v):
    queue = [s]
    visit = [0] * (v+1)
    visit[s] = 1

    while queue:
        now = queue.pop(0)
        print(now, end= ' ')
        for j in range(1, v+1):
            if arr[now][j] == 1 and visit[j] == 0:
                queue.append(j)
                visit[j] = 1
    return

v, e, s = list(map(int, sys.stdin.readline().split()))
arr = [[0] * (v+1) for _ in range(v+1)]

for i in range(e):
    a, b = list(map(int, sys.stdin.readline().split()))
    arr[a][b] = arr[b][a] = 1

visit = [0] * (v+1)

DFS(arr, s)
print()
BFS(arr, s, v)
