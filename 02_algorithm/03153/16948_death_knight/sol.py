import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
sx, sy, gx, gy = list(map(int, sys.stdin.readline().split()))
chess = [[0]*N for _ in range(N)]

def sol(x, y):
    queue = [x, y]
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    while queue:
        i = queue.pop(0)
        j = queue.pop(0)
        di, dj = [-2, -2, 0, 0, 2, 2], [-1, 1, -2, 2, -1, 1]
        for k in range(6):
            ni, nj = i + di[k], j +dj[k]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                queue.append(ni)
                queue.append(nj)
                visited[ni][nj] = visited[i][j] + 1
                if ni == gx and nj == gy:
                    return print(visited[i][j])

    return print(-1)

sol(sx, sy)