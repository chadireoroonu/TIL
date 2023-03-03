import sys
sys.stdin = open('input.txt')

w, h = list(map(int, sys.stdin.readline().split()))
p, q = list(map(int, sys.stdin.readline().split()))
t = int(sys.stdin.readline())

k = 0
di = [1, 1, -1, 1]    # 개미가 움직일 좌표
dj = [1, -1, -1, -1]

s = 0
i, j = q, p    # 개미의 출발 지점
while s < t:   # 주어진 시간동안 개미가 움직임
    ni = i + di[k % 4]
    nj = j + dj[k % 4]
    if 0 <= ni <= h and 0 <= nj <= w:
        i, j = ni, nj
        s += 1
    else:
        k += 1

print(j, i)