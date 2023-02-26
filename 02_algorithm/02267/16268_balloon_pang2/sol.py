import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]

    maxi = 0
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for i in range(n):
        for j in range(m):
            temp = 0
            temp += arr[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < m:
                    temp += arr[ni][nj]
            if temp > maxi:
                maxi = temp
    print(f'#{tc} {maxi}')
