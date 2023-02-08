import sys
sys.stdin = open('intput.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split()))for m in range(n)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    abs_sum = 0
    for i in range(n):
        for j in range(n):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < n:
                    abs_sum += abs(arr[i][j] - arr[ni][nj])

    print(f'#{tc} {abs_sum}')
