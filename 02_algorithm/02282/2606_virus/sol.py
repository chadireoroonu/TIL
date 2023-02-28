import sys
sys.stdin = open('input.txt')

v = int(input())
e = int(input())

arr = [[0] * (v+1) for _ in range(v+1)]

for i in range(e):
    a, b = list(map(int, input().split()))
    arr[a][b] = arr[b][a] = 1

stack = [1]
visit = [0] * (v+1)

count = 0
while stack:
    now = stack.pop()
    for j in range(2 , v+1):
        if arr[now][j] == 1 and visit[j] == 0:
            stack.append(j)
            visit[j] = 1
            count += 1

print(count)