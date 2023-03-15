import sys
sys.stdin = open('input.txt')

def sol(x, y):    # 음식물의 크기 조사 
    global maxi
    queue = [x, y]
    arr[x][y] = 0
    temp = 1
    while queue:
        i = queue.pop(0)
        j = queue.pop(0)
        di, dj = [1, -1, 0, 0], [0, 0, -1, 1]
        for l in range(4):
            ni, nj = i + di[l], j + dj[l]
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1:
                queue.append(ni)
                queue.append(nj)
                arr[ni][nj] = 0
                temp += 1
    if temp > maxi:
        maxi = temp
    return

n, m, k = list(map(int, sys.stdin.readline().split()))
arr = [[0]*m for _ in range(n)]

# 음식물의 좌표 기록
for q in range(k):
    a, b = list(map(int, sys.stdin.readline().split()))
    arr[a-1][b-1] = 1

# 음식물 발견하면 크기 조사
maxi = 0
for x in range(n):
    for y in range(m):
        if arr[x][y] == 1:
            sol(x, y)

print(maxi)