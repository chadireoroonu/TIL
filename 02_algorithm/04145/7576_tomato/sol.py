# 익은 토마토 발견 시, 리스트에 추가
# 리스트를 인자로 하는 함수에서 토마토 인근 4방향 탐색
# 익지 않은 토마토가 있다면, -1 출력

import sys
sys.stdin = open('input.txt')

# 익은 토마토 찾기 함수
def tomato(arr):
    red = []
    for a in range(n):
        for b in range(m):
            if arr[a][b] == 1:
                red.append(a)
                red.append(b)
    change(arr, red)    # 토마토 숙성

    # 전체 숙성 여부 및 기간 판별
    day = 0
    for a in range(n):
        for b in range(m):
            if arr[a][b] == 0:
                return print(-1)
            if arr[a][b] > day:
                day = arr[a][b]

    return print(day-1)

# 토마토 숙성 함수 시간 인덱스 활용으로 시간 초과 해결
def change(arr, q):
    queue = q
    x = 0
    while x < len(queue):
        i = queue[x]
        x += 1
        j = queue[x]
        x += 1
        di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0:
                arr[ni][nj] = arr[i][j] + 1
                queue.append(ni)
                queue.append(nj)

    return

m, n = list(map(int, sys.stdin.readline().split()))
box = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

tomato(box)