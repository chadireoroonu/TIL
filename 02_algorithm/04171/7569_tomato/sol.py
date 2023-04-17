# 익은 토마토는 동, 서, 남, 북, 상, 하 6방향의 토마토에 영향
# 3차원 형식으로 리스트 구성 -> 6방향 탐색 진행
# 포인터 사용으로 pop 연산 시간초과 방지
# 익은 토마토 리스트를 구성해 토마토 숙성 함수에 넘겨주기
# 토마토가 익는 날짜는 이전 숫자 +1 기록

import sys
sys.stdin = open('input.txt')

def find(arr):
    tomato = []    # 익은 토마토 좌표 기록
    for x in range(h):
        for y in range(n):
            for z in range(m):
                if arr[x][y][z] == 1:
                    tomato.append([x, y, z])
    red(tomato)    # 토마토 숙성
    day = 0
    # 전체 숙성 여부, 날짜 확인
    for x in range(h):
        for y in range(n):
            for z in range(m):
                if arr[x][y][z] == 0:
                    return print(-1)    # 안익은 토마토 있을 경우
                if arr[x][y][z] > day:
                    day = arr[x][y][z]
    return print(day-1)    # 모든 토마토가 익었을 경우

# 토마토 익히기 함수
def red(queue):
    p = 0    # 포인터 접근
    while p < len(queue):    # 포인터가 큐 길이보다 짧은 동안 진행
        i, j, k = queue[p][0], queue[p][1], queue[p][2]
        p += 1
        di = [-1, 1, 0, 0, 0, 0]    # 여섯 방향 탐색
        dj = [0, 0, -1, 1, 0, 0]
        dk = [0, 0, 0, 0, -1, 1]
        for l in range(6):
            ni, nj, nk = i + di[l], j + dj[l], k + dk[l]
            if 0 <= ni < h and 0 <= nj < n and 0 <= nk < m:
                if box[ni][nj][nk] == 0:
                    box[ni][nj][nk] = box[i][j][k] + 1
                    queue.append([ni, nj, nk])
    return


m, n, h = list(map(int, sys.stdin.readline().split()))

box = []

for _ in range(h):
    tmp = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    box.append(tmp)

find(box)