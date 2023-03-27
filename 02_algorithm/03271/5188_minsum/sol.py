import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 시작점을 담은 queue 생성
    # 방문 여부 확인 및 합산을 위한 visited 배열 생성
    queue = [0, 0]
    visited = [[0]*N for _ in range(N)]
    visited[0][0] = arr[0][0]
    while queue:
        i = queue.pop(0)
        j = queue.pop(0)
        # 아래, 오른쪽 두 방향 탐색
        di = [1, 0]
        dj = [0, 1]
        for k in range(2):
            ni = i + di[k]
            nj = j + dj[k]
            # ni, nj 범위 내에 있다 다음 작업 수행
            if 0 <= ni < N and 0 <= nj < N:
                # queue.append 여기에 넣으면 제한시간 초과 오답
                # visited[ni][nj] 0이면 합 넣어주고 queue 추가
                if visited[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + arr[ni][nj]
                    queue.append(ni)
                    queue.append(nj)
                # 0 이외 값 위치하면 현재 경로 합과 크기 비교 후 작은 값 기록
                elif visited[ni][nj] > visited[i][j] + arr[ni][nj]:
                    visited[ni][nj] = visited[i][j] + arr[ni][nj]
                    queue.append(ni)
                    queue.append(nj)

    print(f'#{tc} {visited[N-1][N-1]}')