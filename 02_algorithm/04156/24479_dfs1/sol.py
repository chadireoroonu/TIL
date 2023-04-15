# 2차원 배열 간선 정보 저장
# DFS : 방문 순서를 위해 set 길이 사용
# 간선 여러개일 경우 오름 차순 -> 내림차순 순회로 stack 추가

# 인접리스트 공부해보기

import sys
sys.setrecursionlimist(10**5)
sys.stdin = open('input.txt')

def DFS(num):
    order = set()
    stack = [num-1]
    visited = [0]*n
    while stack:
        i = stack.pop()
        order.add(i)
        visited[i] = len(order)
        for j in range(n-1, -1, -1):
            if arr[i][j] == 1 and visited[j] == 0:
                stack.append(j)

    for a in range(len(visited)):
        print(visited[a])

    return


n, m, r = list(map(int, sys.stdin.readline().split()))
arr = [[0]*n for _ in range(n)]

for _ in range(m):
    u, v = list(map(int, sys.stdin.readline().split()))
    arr[u-1][v-1] = arr[v-1][u-1] = 1

DFS(r)