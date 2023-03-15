import sys
sys.stdin = open('input.txt')

def sol(x, y):
    queue = [x, y]
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1
    while queue:
        i = queue.pop(0)
        j = queue.pop(0)
        di = [-2, -1, 1, 2, 2, 1, -1, -2]    # 나이트의 이동 방향
        dj = [1, 2, 2, 1, -1, -2, -2, -1]
        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0:
                queue.append(ni)
                queue.append(nj)
                visited[ni][nj] = visited[i][j] + 1
                # 목표지점 도달 시 이동횟수 출력 반환
                if ni == goal_x and nj == goal_y:
                    return print(visited[ni][nj]-1)

t = int(sys.stdin.readline())
for tc in range(t):
    n = int(sys.stdin.readline())
    chess = [[0]*n for _ in range(n)]

    # 나이트의 위치와 목표지점 저장
    knight_x, knight_y = list(map(int, sys.stdin.readline().split()))
    goal_x, goal_y = list(map(int, sys.stdin.readline().split()))

    # 나이트 위치와 목표 지점이 같으면 이동 불필요
    # pop 이후 목표지점 비교 로직을 사용하면 반복문 삭제 가능
    if knight_x == goal_x and knight_y == goal_y:
        print(0)
    else:
        sol(knight_x, knight_y)
