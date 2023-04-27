import sys
from collections import deque
sys.stdin = open('input.txt')

def distance(arr, food):
    global total, count, shark
    idxi = 0
    idxj = 0
    second = n * n
    for w in range(len(food)//2):
        queue = deque([food[w*2], food[w*2+1]])    # 먹이들의 i, j 좌표
        visited = [[0] * n for _ in range(n)]    # 방문 여부 및 이동 시간 계산
        while queue:
            i = queue.popleft()
            j = queue.popleft()
            di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0:
                    if arr[ni][nj] == 9:    # 이동 거리가 작을 경우 시간, 좌표 재설정
                        if visited[i][j] + 1 < second:
                            second = visited[i][j] + 1
                            idxi, idxj = food[w*2], food[w*2+1]
                        continue
                    elif arr[ni][nj] <= shark:    # 상어보다 큰 물고기칸 이동 불가
                        visited[ni][nj] = visited[i][j] + 1
                        queue.append(ni)
                        queue.append(nj)
    if second != n*n:
        for x in range(n):
            for y in range(n):
                if arr[x][y] == 9:     # 상어의 원래 위치 0 설정
                    arr[x][y] = 0
        arr[idxi][idxj] = 9    # 상어 이동
        total += second        # 이동 시간 추가
        count += 1             # 먹은 횟수 기록
        if count == shark:     # 상어 크기만큼 먹이를 먹으면 상어 성장
            shark += 1
            count = 0
    else:
        arr[idxi][idxj] = 0    # 길 없는 먹이는 0으로 바꿈
    return

n = int(sys.stdin.readline())
sea = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

shark = 2
total = 0
count = 0

while True:    # 먹이가 있다면 함수 실행
    food = deque([])
    for a in range(n):
        for b in range(n):
            if 0 < sea[a][b] < 7 and sea[a][b] < shark:
                food.append(a)
                food.append(b)
    if food:
        distance(sea, food)
    else:
        break

print(total)