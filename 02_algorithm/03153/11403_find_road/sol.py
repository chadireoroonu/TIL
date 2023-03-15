import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def sol(x, y):
    queue = [x]
    visited = [0] * n
    while queue:
        i = queue.pop(0)
        for j in range(n):
            if arr[i][j] == 1 and visited[j] == 0:
                queue.append(j)
                visited[j] = 1
                if j == y:
                    arr[x][y] = 1

    return

for a in range(n):
    for b in range(n):
        if arr[a][b] == 0:
            sol(a, b)

for w in arr:
    print(*w)