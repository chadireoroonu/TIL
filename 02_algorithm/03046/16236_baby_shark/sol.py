import sys
sys.stdin = open('input.txt')

# 자기보다 큰 물고기가 있는 칸은 지나가지 못함 -> 같으면 지나감
# 자기보다 작은 물고기만 먹을 수 있음 -> 같으면 못먹음
# 자기의 크기만큼 물고기를 먹으면 덩치가 커짐 -> 처음크기 2
# 물고기를 먹으면 그 칸은 빈칸

# 가까운 물고기부터 먹는데, 같은 거리라면 위쪽 물고기를 먹음
# 같은 거리의 위쪽 물고기가 많으면 왼쪽 물고기를 먹
# 1. 탐색 : 왼쪽 위부터 행우선 조회를 해서 먹을 수 있는 것들을 후보군에 넣음
# 2. 거리 : 후보군들의 거리를 조사

def distance(arr, food):
    global total
    global count
    global shark
    second = []    # 먹이 좌표, 이동 시간(거리) 담을 리스트
    for w in range(len(food)//2):
        queue = [food[w*2], food[w*2+1]]    # 먹이들의 i, j 좌표
        visited = [[0] * n for _ in range(n)]    # 방문 여부 및 이동 시간 계산
        while queue:
            i = queue.pop(0)
            j = queue.pop(0)
            di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0:
                    if arr[ni][nj] == 9:    # 상어 위치 도달 시 좌표와 시간 기록
                        second.append([food[w*2], food[w*2+1], visited[i][j]+1])
                        continue
                    elif arr[ni][nj] <= shark:    # 상어보다 큰 물고기칸 이동 불가
                        visited[ni][nj] = visited[i][j] + 1
                        queue.append(ni)
                        queue.append(nj)
    if second:    # 가장 가까운 먹이 판별
        final = []
        mini = n*n
        for r in range(len(second)):
            if second[r][2] < mini:
                mini = second[r][2]
                final = second[r]
        for x in range(n):
            for y in range(n):
                if arr[x][y] == 9:     # 상어의 원래 위치 0 설정
                    arr[x][y] = 0

        arr[final[0]][final[1]] = 9    # 상어 이동
        total += final[2]              # 이동 시간 추가
        count += 1                     # 먹은 횟수 기록
        if count == shark:             # 상어 크기만큼 먹이를 먹으면 상어 성장
            shark += 1
            count = 0
    else:
        arr[food[w*2]][food[w*2+1]] = 0    # 길 없는 먹이는 0으로 바꿈
    return

n = int(sys.stdin.readline())
sea = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

shark = 2
total = 0
count = 0

while True:    # 먹이가 있다면 함수 실행
    food = []
    for a in range(n):
        for b in range(n):
            if 0 < sea[a][b] < shark:
                food.append(a)
                food.append(b)
    if food:
        distance(sea, food)
    else:
        break

print(total)