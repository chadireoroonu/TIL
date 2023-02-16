import sys
sys.stdin = open('input.txt')

def DFS(start):
    stack = start
    visited = [0] * (v + 1)
    visited[start] = 1
    while stack:
        start = stack.pop()



T = int(input())
for tc in range(1, T+1):
    v, e = list(map(int, input().split()))
    data = [list(map(int, input().split())) for _ in range(e)]

    matrix = [[0] * (v+1) for _ in range(v+1)]
    s, g = list(map(int, input().split()))

    for i in range(e):
        matrix[data[i][0]][data[i][1]] = 1

    for i in range(v+1):
        print(matrix[i])

