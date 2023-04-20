# 1. 현재 칸이 청소되지 않은 경우, 현재 칸 청소
# 2. 현재 칸 주변 4칸 중 청소되지 않은 빈 칸 없는 경우
#    바라보는 방향 유지, 한 칸 후진이 가능하다면 한 칸 후진 후 1로 돌아감
#    한 칸 후진이 불가능하다면 작동 중지
# 3. 현재 칸 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
#    반시계 방향으로 90도 회전
#    바라보는 방향 기준 앞쪽 칸이 청소되지 않은 빈칸이라면 한 칸 전진 후 1로 돌아감

# 1차 시도 1% 틀렸습니다. -> 벽일때도 후진해서 문제 발생

import sys
sys.stdin = open('input.txt')

def clean(arr, i, j, h):
    sell = 0
    while True:
        if arr[i][j] == 0:
            arr[i][j] = -1
            sell += 1
        next_sell = 0
        wall = 0
        for k in range(4):
            ni = i + hi[k]
            nj = j + hj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 0:
                    next_sell += 1
                elif arr[ni][nj] == 1:
                    wall += 1
        if wall == 4:
            return print(sell)
        if next_sell:
            h -= 1
            ni, nj = i + hi[h % 4], j + hj[h % 4]
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                i, j = ni, nj
        else:
            ni, nj = i + hi[(h + 2) % 4], j + hj[(h + 2) % 4]
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 1:
                i, j = ni, nj
            else:
                return print(sell)


N, M = map(int, sys.stdin.readline().split())
r, c, h = map(int, sys.stdin.readline().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

hi = [-1, 0, 1, 0]    # 북 동 남 서
hj = [0, 1, 0, -1]

clean(room, r, c, h)