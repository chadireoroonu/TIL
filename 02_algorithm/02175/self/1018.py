import sys
sys.stdin = open('input.txt')

n, m = list(map(int, input().split()))
arr = [list(map(str, input())) for _ in range(n)]



def chess(arr):
    mini = 64
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    count = 0
    for i in range(8):
        for j in range(8):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < n:
                    if arr[i][j] == arr[ni][nj]:
                        count += 1

    count = count // 8
    if count < mini:
        mini = count
    return mini

print(chess(arr))