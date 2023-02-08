import sys
sys.stdin = open('input.txt')

for q in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for m in range(100)]

    di = [-1, 0, 0]
    dj = [0, -1, 1]

    def labber(i, j):
        arr[i][j] = 0
        while i > 0:
            for k in range(3):
                ni = i + di[k]
                nj = j + dj[k]

                if 0 <= ni < 100 and 0 <= nj < 100:
                    if arr[ni][nj]:
                        arr[i][j] = 0
                        i = ni
                        j = nj

        return j

    for w in range(100):
        if arr[99][w] == 2:
            j = w

    print(f'#{tc}', end=' ')
    print(labber(99, j))