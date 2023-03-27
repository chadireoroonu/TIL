import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    queue = [0, 0]
    goal = [N-1, N-1]
    visited = [[0]*N for _ in range(N)]
    visited[0][0] = arr[0][0]
    while queue:
        i = queue.pop(0)
        j = queue.pop(0)
        di = [1, 0]
        dj = [0, 1]
        for k in range(2):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                # queue.append 여기에 넣으면 제한시간 초과 오답
                if visited[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + arr[ni][nj]
                    queue.append(ni)
                    queue.append(nj)
                elif visited[ni][nj] > visited[i][j] + arr[ni][nj]:
                    visited[ni][nj] = visited[i][j] + arr[ni][nj]
                    queue.append(ni)
                    queue.append(nj)

    print(f'#{tc} {visited[N-1][N-1]}')