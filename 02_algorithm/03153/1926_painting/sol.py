import sys
sys.stdin = open('input.txt')

n, m = list(map(int, sys.stdin.readline().split()))
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def sol(arr, x, y):    # 한 번 조사 -> arr 직접 수정
    global maxi
    arr[x][y] = 0
    queue = [x, y]
    temp = 1    # 그림의 넓이 조사
    while queue:
        i = queue.pop(0)
        j = queue.pop(0)
        di = [1, -1, 0, 0]
        dj = [0, 0, -1, 1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1:
                queue.append(ni)
                queue.append(nj)
                arr[ni][nj] = 0
                temp += 1
    # 그림 넓이와 최대값 비교
    if temp > maxi:
        maxi = temp
    return

maxi = 0    # 가장 넓은 그림넓이
count = 0    # 그림 수
for a in range(n):
    for b in range(m):
        if arr[a][b] == 1:
            count += 1
            sol(arr, a, b)

print(count)
print(maxi)