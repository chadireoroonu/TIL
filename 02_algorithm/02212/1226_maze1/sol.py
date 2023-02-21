import sys
sys.stdin = open('input.txt')

# BFS 조사를 수행하기 위한 함수 생성
# 이전 방문 여부 파악을 위한 visit 생성
# 골부터 스타트까지 거슬러 올라갈 계획
# 방문 지점은 1로 표시하고 시작
def BFS(arr, goal, start):
    visit = [[0] * 16 for _ in range(16)]
    queue = [goal]
    visit[goal[0]][goal[1]] = 1

    # queue가 있는 동안 반복 진행
    # now는 queue의 첫 요소로 설정 후 진행
    # 만약 now가 스타트라면, 1을 반환
    while queue:
        now = queue.pop()
        if now == start:
            return 1
        # 아니라면, 상하좌우 4방향 조사를 위한 리스트 생성
        # 네 범위 안에서 ni, nj에 대한 조사를 수행하는데,
        # ni, nj가 arr 안에 있고, arr[ni][nj]가 벽이 아니며
        # 이전에 방문한 적이 없다면 큐에 추가하고 visit 좌표에 1 할당
        di = [-1, 1, 0, 0]
        dj = [0, 0, -1, 1]
        for k in range(4):
            ni = now[0] + di[k]
            nj = now[1] + dj[k]
            if 0 <= ni < 16 and 0 <= nj < 16 and arr[ni][nj] != 1 and visit[ni][nj] == 0:
                queue.append([ni, nj])
                visit[ni][nj] = 1
    # 최종적으로 리턴 값이 없다면 길 존재하지 않음
    return 0

for case in range(10):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(16)]

    # 좌표값이 2인 곳은 출발지,
    # 3인 곳은 도착지로 설정 후 함수 호출
    start = []
    goal = []
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                start = [i, j]
            if arr[i][j] == 3:
                goal = [i, j]

    print(f'#{tc} {BFS(arr, goal, start)}')