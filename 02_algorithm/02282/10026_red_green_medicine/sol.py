import sys
sys.stdin = open('input.txt')

def color(arr, i, j, visited):
    queue = [i, j]
    target = arr[i][j]

    while queue:
        i = queue.pop(0)
        j = queue.pop(0)
        visited[i][j] = 1

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == target and visited[ni][nj] == 0:
                queue.append(ni)
                queue.append(nj)
                visited[ni][nj] = 1
    return

def blind(arr, i, j, visited):
    queue = [i, j]
    target = arr[i][j]
    visited[i][j] = 1

    while queue:
        i = queue.pop(0)
        j = queue.pop(0)

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == target and visited[ni][nj] == 0:
                queue.append(ni)
                queue.append(nj)
                visited[ni][nj] = 1
    return


n = int(input())
arr = [list(map(str, input())) for _ in range(n)]
arr_1 = [a[:] for a in arr]
for x in range(n):
    for y in range(n):
        if arr_1[x][y] == 'G':
            arr_1[x][y] = 'R'

count_color = 0
count_blind = 0

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

visited_color = [[0] * n for _ in range(n)]
visited_blind = [[0] * n for _ in range(n)]

for x in range(n):
    for y in range(n):
        if visited_color[x][y] == 0:
            color(arr, x, y, visited_color)
            count_color += 1

for x in range(n):
    for y in range(n):
        if visited_blind[x][y] == 0:
            blind(arr_1, x, y, visited_blind)
            count_blind += 1

print(count_color, end= ' ')
print(count_blind)