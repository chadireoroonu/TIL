import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = list(map(int, input().split()))
    arr = [[0]*n for _ in range(n)]

    arr[n//2-1][n//2-1] = 2
    arr[n//2][n//2] = 2
    arr[n//2][n//2-1] = 1
    arr[n//2-1][n//2] = 1

    for play in range(m):
        i, j, s = list(map(int, input().split()))
        i = i - 1
        j = j - 1
        arr[i][j] = s

        di = [-1, -1, -1, 0, 0, 1, 1, 1]
        dj = [-1, 0, 1, -1, 1, -1, 0, 1]

        for k in range(8):
            ni = i + di[k]*2
            nj = j + dj[k]*2
            ti = i + di[k]
            tj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == s:
                if arr[ti][tj] != s:
                    arr[ti][tj] = s

    black = 0
    white = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                black += 1
            elif arr[i][j] == 2:
                white += 1

    print(f'#{tc} {black} {white}')
