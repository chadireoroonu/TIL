import sys
sys.stdin = open('input.txt')

def que(arr, queue):
    while queue:
        i = queue.pop(0)
        j = queue.pop(0)
        collect.append(arr[i][j])

        di = [-1, 1, 0, 0]
        dj = [0, 0, -1, 1]

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < r and 0 <= nj < c and visited[ni][nj] == 0:
                if arr[ni][nj] not in collect:
                    temp.append(ni)
                    temp.append(nj)
                    visited[ni][nj] = visited[i][j] + 1

r, c = list(map(int, input().split()))
arr = [list(map(str, input())) for _ in range(r)]

collect = []
visited = [[0] * c for _ in range(r)]
visited[0][0] = 1
temp = [0, 0]
queue = []

while temp:
    for q in temp:
        queue.append(q)
        print(temp)
        print(queue)
    que(arr, queue)

maxi = 0
for x in range(r):
    for y in range(c):
        if visited[x][y] > maxi:
            maxi = visited[x][y]

print(maxi)
