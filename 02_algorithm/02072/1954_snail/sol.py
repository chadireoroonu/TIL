import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [[0]* n for m in range(n)]

    k = 1
    arr[0][0] = 1
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    ni = nj = 0
    p = 1

    for k in range(n**2):
        if 0 <= ni < n and 0 <= nj < n:
            ni += di[p%4]
            nj += dj[p%4]
            arr[ni][nj] = k + 1
            k += 1

    print(arr)


