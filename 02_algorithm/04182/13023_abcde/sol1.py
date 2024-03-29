# 2차원 배열에 친구 관계 저장
# 모든 숫자에 대해 DFS 함수 실행
# 스택에서 연결 친구가 없으면 지우는 과정 필요

import sys
sys.stdin = open('input.txt')

def find(arr):
    for x in range(n):
        stack = [x]
        visited = 'x'
        while stack:
            i = stack.pop()
            for j in range(n):
                if arr[i][j] and str(j) not in visited:
                    stack.append(j)
                    visited += str(j)
                    if len(visited) >= 5:
                        return print(1)
    return print(0)


n, m = map(int, sys.stdin.readline().split())
friend = [[0] * n for _ in range(n)]

for _ in range(m):
    v, u = map(int, sys.stdin.readline().split())
    friend[v][u] = friend[u][v] = 1

find(friend)