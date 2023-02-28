import sys
sys.stdin = open('input.txt')

n, m = list(map(int, input().split()))
arr = [[0] * (n+1) for _ in range(n+1)]
for i in range(m):
    a, b = list(map(int, input().split()))
    arr[a][b] = arr[b][a] = 1

road = []
for i in range(1, n+1):
    temp = []
    stack = [i]
    visit = [0] * (n+1)
    visit[i] = 1
    while stack:
        now = stack.pop()
        temp.append(now)
        for j in range(n):
            if arr[now][j] == 1 and visit[j] == 0:
                stack.append(j)
                visit[j] = 1
    temp = sorted(temp)
    word = ''
    for k in temp:
        word += str(k)
    road.append(word)

for i in road:
    for j in road:
        if i in j:
            road.remove(i)

print(len(road))