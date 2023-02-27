import sys
sys.stdin = open('input.txt')

def sol(arr, a, b):
    queue = [a, b]
    visit = [[0] * (m) for _ in range(n)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    while queue:
        i = queue.pop(0)
        j = queue.pop(0)
        if i == n-1 and j == m-1:
            # 출발지를 포함하도록 하기 위해 +1
            return visit[i][j] + 1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1:
                if visit[ni][nj] == 0:
                    queue.append(ni)
                    queue.append(nj)
                    arr[ni][nj] = 0
                    # 최종적으로 도착할 때까지 이동거리를 더함
                    visit[ni][nj] = visit[i][j] + 1

n, m = list(map(int, input().split()))
maze = [list(map(int, input())) for _ in range(n)]

print(sol(maze, 0, 0))
