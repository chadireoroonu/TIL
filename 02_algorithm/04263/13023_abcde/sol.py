import sys
from collections import deque
sys.stdin = open('input.txt')

def DFS(arr):
    maxi = 0
    for i in range(n):
        visited = [0] * n
        temp = deque([i])
        visited[i] = 1
        while temp:
            x = temp.pop()
            for y in range(n):
                if arr[x][y] and visited[y] == 0:
                    visited[y] = visited[x] + 1
                    temp.append(y)
                    if visited[y] > maxi:
                        maxi = visited[y]
    print(visited)
    if maxi >= 5:
        return print(1)
    else:
        return print(0)

n, m = map(int, sys.stdin.readline().split())
person = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    person[a][b] = person[b][a] = 1

DFS(person)