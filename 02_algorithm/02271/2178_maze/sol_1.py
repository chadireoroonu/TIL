import sys
sys.stdin = open('input.txt')

def sol(arr, a, b):
    count = 0
    arr[a][b] = 0

    while True:
        if a == n-1 and b == m-1:
            return count
        di = [-1, 1, 0, 0]
        dj = [0, 0, -1, 1]

        for k in range(4):
            ni = a + di[k]
            nj = b + dj[k]
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1:
                arr[ni][nj] = 0
                a, b = ni, nj
                count += 1



n, m = list(map(int, input().split()))
maze = [list(map(int, input())) for _ in range(n)]

print(sol(maze, 0, 0))
