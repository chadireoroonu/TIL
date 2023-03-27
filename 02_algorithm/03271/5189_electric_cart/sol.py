import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    queue = []
    visited = [0] * N
    elect = [[0] * N for _ in range(N)]
    for x in range(1, N):
        queue.append(x)
        visited[x] = 1
        elect[0][x] = arr[0][x]
    print(queue)
    print(visited)

    while queue:
        i = queue.pop(0)
        j = 0
        for k in range(1, N):
            if arr[i][k] and visited[k] == 0:
                queue.append(k)
                visited[k] = 1
                elect[k][i] = elect[j][1] + arr[i][k]
                elect[j][i] = 0
        j = i

    print(visited)
    print(elect)
