# O -> 1방향
# oi, oj = [1, 1, 0], [0, 1, 1]

# I -> 2방향
# ii, ij = [0, 0, 0], [1, 2, 3]
# ii, ij = [1, 2, 3], [0, 0, 0]

# S -> 2방향
# si, sj = [1, 1, 2], [0, 1, 1]
# si, sj = [0, 1, 1], [1, 0, -1]

# L -> 4방향
# li, lj = [1, 2, 2], [0, 0, 1]
# li, lj = [1, 0, 0], [0, 1, 2]
# li, lj = [0, 1, 2], [1, 1, 1]
# li, lj = [0, 0, -1], [1, 2, 2]

# T -> 4방향
# ti, tj = [0, 0, 1], [1, 2, 1]
# ti, tj = [-1, 0, 1], [1, 1, 1]
# ti, tj = [1, 1, 1], [-1, 0, 1]
# ti, tj = [1, 2, 1], [0, 0, 1]

import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

di = [[1, 1, 0], [0, 0, 0], [1, 2, 3], [1, 1, 2], [0, 1, 1], [1, 2, 2],
      [1, 0, 0], [0, 1, 2], [0, 0, -1], [0, 0, 1], [-1, 0, 1], [1, 1, 1], [1, 2, 1]]
dj = [[0, 1, 1], [1, 2, 3], [0, 0, 0], [0, 1, 1], [1, 0, -1], [0, 0, 1], [0, 1, 2],
      [0, 1, 2], [1, 1, 1], [1, 2, 2], [1, 2, 1], [1, 1, 1], [-1, 0, 1], [0, 0, 1]]

maxi = 0

for i in range(N):
    temp = 0
    for j in range(M):
        temp += arr[i][j]
        for k in range(13):
            for l in range(3):
                ni, nj = i + di[k][l], j + dj[k][l]
                if 0 <= ni < N and 0 <= nj < M:
                    temp += arr[ni][nj]
            if temp > maxi:
                maxi = temp
            temp = arr[i][j]
print(maxi-1)