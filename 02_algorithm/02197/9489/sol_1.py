import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(arr)

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    maxi = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                temp = 0
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1:
                        temp += 1
                        i = ni
                        j = nj

                    if temp > maxi:
                        maxi = temp

    print(maxi)
