# 높이가 더 낮은 지점으로만 이동 가능 -> visited 필요 없음
# DFS로 진행, 도착 지점 도착 시마다 +1
# 시간 효율을 위해 -1 사용 -> 종료 조건 모호

# 1차 시도 16% 시간초과
# visited 만들고 0 이면 포인터 적용, 아니면 포인터 -1 이동
# i, j 정할 때 while 사용

# 2차 시도 런타임 에러


import sys
sys.stdin = open('input.txt')

def downhill(x, y):
    load = 0
    stack = [[x, y]]
    p = 0
    visited = []
    while p < len(stack):
        pointer = -1
        while True:
            if [[stack[pointer][0]], [stack[pointer][1]]] not in visited:
                i, j = stack[pointer][0], stack[pointer][1]
                visited.append([i, j])
                break
            pointer -= 1
        p += 1
        if i == n-1 and j == m-1:
            load += 1

        di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < n and 0 <= nj < m:
                if land[ni][nj] < land[i][j]:
                    stack.append([ni, nj])

    return print(load)


n, m = list(map(int, sys.stdin.readline().split()))
land = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

downhill(0, 0)