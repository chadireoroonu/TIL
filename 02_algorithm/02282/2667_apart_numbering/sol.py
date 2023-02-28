import sys
sys.stdin = open('input.txt')

def apart(arr, i, j):
    global count
    count += 1
    queue = [i, j]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    temp = 0
    while queue:
        i = queue.pop(0)
        j = queue.pop(0)
        arr[i][j] = 0
        temp += 1

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 1:
                queue.append(ni)
                queue.append(nj)
                arr[ni][nj] = 0

    home.append(temp)

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
count = 0
home = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            apart(arr, i, j)

print(count)
home = sorted(home)
for i in home:
    print(i)