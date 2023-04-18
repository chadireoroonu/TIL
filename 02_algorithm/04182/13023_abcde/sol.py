# 2차원 배열에 친구 관계 저장
# 모든 숫자에 대해 DFS 함수 실행
# DFS visited 5가 되면 1 출력

import sys
sys.stdin = open('input.txt')

def find(arr):
    for x in range(n):
        stack = [x]
        visited = [0] * n
        visited[x] = 1
        while stack:
            i = stack.pop()
            for j in range(n):
                if arr[i][j] and visited[j] == 0:
                    stack.append(j)
                    visited[j] = visited[i] + 1
                    if visited[j] == 5:
                        return print(1)
        print(visited)
    return print(0)


n, m = map(int, sys.stdin.readline().split())
friend = [[0] * n for _ in range(n)]

for _ in range(m):
    v, u = map(int, sys.stdin.readline().split())
    friend[v][u] = friend[u][v] = 1

find(friend)