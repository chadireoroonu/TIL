import sys
sys.stdin = open('input.txt')

# 미로 속에서 움직이며 길을 탐색할 함수 생성
# 이전 방문 여부를 탐색하기 위한 visit 배열 생성
# queue 이용, i,j 정보 저장
def BFS(arr, i, j):
    visit = [[0] * 100 for _ in range(100)]
    queue = [i, j]
    visit[i][j] = 1

    # queue 있는 동안 반복 진행
    # 만약, arr[i][j]가 3이면 종료
    while queue:
        i = queue.pop(0)
        j = queue.pop(0)
        if arr[i][j] == 3:
            return 1

        # 상하좌우 네 방향을 탐색할 상대좌표 저장
        # 네 방향을 탐색하며 arr[ni][nj]가 1이 아니고
        # 이전에 방문한 적이 없으면 queue에 ni, nj 추가
        # 미로는 벽으로 둘러싸여있기 때문에 범위 안쪽인지는 확인하지 않음
        di = [-1, 1, 0, 0]
        dj = [0, 0, -1, 1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if arr[ni][nj] != 1 and visit[ni][nj] == 0:
                queue.append(ni)
                queue.append(nj)
                visit[ni][nj] = 1
    # 끝까지 도착지점 도달 불가 시 0 반환
    return 0

for case in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(100)]

    print(f'#{tc} {BFS(maze, 1, 1)}')

