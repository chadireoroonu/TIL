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
    change(arr, red)

    day = 0
    for a in range(n):
        for b in range(m):
            if arr[a][b] == 0:
                return print(-1)
            if arr[a][b] > day:
                day = arr[a][b]

    return print(day-1)

def change(arr, q):
    queue = q
    while queue:
        i = queue.pop(0)
        j = queue.pop(0)
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