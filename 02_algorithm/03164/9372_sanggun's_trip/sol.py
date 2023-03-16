import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline().strip())
for tc in range(T):
    n, m = list(map(int, sys.stdin.readline().split()))
    load = [[0]*(n+1) for _ in range(n+1)]

    for i in range(m):    # 노선 저장
        a, b = list(map(int, sys.stdin.readline().split()))
        load[a][b] = load[b][a] = 1

    airplain = 0    # 총 비행기의 수
    visited = [0] * (n+1)    # 방문 여부
    for i in range(1, n+1):
        if visited[i] == 0:
            queue = [i]
            visited[i] = 1
            while queue:
                x = queue.pop(0)
                for j in range(1, n+1):
                    if load[x][j] == 1 and visited[j] == 0:
                        queue.append(j)
                        visited[j] = 1
                        airplain += 1

    print(airplain)