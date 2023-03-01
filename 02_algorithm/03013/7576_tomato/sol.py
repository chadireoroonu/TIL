import sys
sys.stdin = open('input.txt')

def check(arr):
    queue = []
    visited = [[0]*(m+2) for _ in range(n+2)]
    for a in range(m+2):
        for b in range(n+2):
            if arr[a][b] == 0:
                queue.append(a)
                queue.append(b)
    while queue:
        i = queue.pop(0)
        j = queue.pop(0)

        di = [-1, 1, 0, 0]
        dj = [0, 0, -1, 1]

        sub = 0
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < m+2 and 0 <= nj < n+2 and arr[ni][nj] == -1 and visited[ni][nj] == 0:
                sub += 1
                visited[ni][nj] = 1
        if sub == 4:
            return print(-1)
        else:
            return tomato(arr)

def tomato(arr):
    global day

    flag = True
    while flag:
        count = 0
        temp = []
        queue = []
        for a in range(m+2):
            for b in range(n+2):
                if box[a][b] >= 1:
                    temp.append(a)
                    temp.append(b)
                    count += 1
        for w in temp:
            queue.append(w)

        while queue:
            for q in range(count):
                i = queue.pop(0)
                j = queue.pop(0)

                di = [-1, 1, 0, 0]
                dj = [0, 0, -1, 1]

                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < m+2 and 0 <= nj < n+2 and arr[ni][nj] == 0:
                        temp.append(ni)
                        temp.append(nj)
                        arr[ni][nj] = day+1
        day += 1

        zero = 0
        for i in range(m):
            for j in range(n):
                if arr[i][j] == 0:
                    zero += 1
        if zero == 0:
            flag = False
            return print(day)


n, m = list(map(int, input().split()))
box = [[-1] + list(map(int, input().split())) + [-1] for _ in range(m)]
box.insert(0, [-1] * (n+2))
box.append([-1] * (n+2))

day = 0

start = False
for x in range(m):
    for y in range(n):
        if box[x][y] == 0:
            start = True
if start == True:
    check(box)
else:
    print(0)

