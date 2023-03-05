import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) + [0]*(n-_-1) for _ in range(n)]

di = [1, 1]
dj = [0, 1]
maxi = 0

def sol(x, y, num):
    global maxi
    q = [x, y, num]
    while q:
        i = q.pop(0)
        j = q.pop(0)
        num = q.pop(0)
        if num > maxi:
            maxi = num
        for k in range(2):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] != 0:
                q.append(ni)
                q.append(nj)
                q.append(num+arr[ni][nj])

sol(0, 0, arr[0][0])

print(maxi)