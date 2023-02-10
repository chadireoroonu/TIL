import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for q in range(n)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    maxi = 0
    for i in range(n):
        for j in range(m):
            ballon = 0
            ballon += arr[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < m:
                    ballon += arr[ni][nj]
            if ballon > maxi:
                maxi = ballon

    print(f'#{tc} {maxi}')