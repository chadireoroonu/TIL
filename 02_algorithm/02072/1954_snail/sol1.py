import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [[0]* n for m in range(n)]

    k = 1
    w = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    counting = n
    for i in range(n):
        for j in range(n):
            ni = di[w % 4]
            nj = dj[w % 4]
            arr[i][j] = k
            k += 1
            counting -= 1
            if counting == 0:
                w += 1
    print(arr)

