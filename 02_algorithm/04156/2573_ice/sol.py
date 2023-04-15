# 1. 빙산을 줄어들게 하는 함수 -> 인접 바다 개수를 세어 높이 차감
# -> 주의! 방금 녹아 바다가 된 지점은 세지 않음
# -> 녹일 빙산이 없을 때 문제 해결
# 2. 빙산의 개수를 세는 함수 -> DFS로 빙산이 두 개 이상인지 파악
# 3. 두 개 이상이라면 -> 지금까지의 일 수 출력 반환

import sys
sys.stdin = open('input.txt')

def melt(arr):
    global year
    temp = [[0] * m for _ in range(n)]    # 녹을 높이 저장

    flag = False    # 빙산 존재 여부
    # 녹을 높이 구하기
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                flag = True    # 빙산 존재 여부
                # 네 방향 탐사로 바다 수, 녹을 높이 저장
                di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
                for k in range(4):
                    ni, nj = i + di[k], j + dj[k]
                    if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0:
                        temp[i][j] += 1
    if flag:    # 실제 녹이기
        year += 1
        for i in range(n):
            for j in range(m):
                if arr[i][j] >= temp[i][j]:
                    arr[i][j] -= temp[i][j]
                else:
                    arr[i][j] = 0
        ice(arr)    # 빙산 개수 세기
        return
    else:    # 빙산 없을 시 0 출력
        return print(0)

# 빙산 개수 세기
def ice(arr):
    visited = [[0] * m for _ in range(n)]
    queue = []
    count = 0
    p = 0    # 시간 효율을 위해 포인터 사용
    for a in range(n):
        for b in range(m):
            if arr[a][b] and visited[a][b] == 0:
                count += 1
                queue.append(a)
                queue.append(b)
                visited[a][b] = 1
                while p < len(queue):    # 네 방향 탐사로 붙어 있는 빙산 방문
                    i = queue[p]
                    j = queue[p+1]
                    p += 2
                    di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
                    for k in range(4):
                        ni, nj = i + di[k], j + dj[k]
                        if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 0 and arr[ni][nj]:
                            queue.append(ni)
                            queue.append(nj)
                            visited[ni][nj] = 1
    if count > 1:    # 빙산이 여러 조각이면 시간 출력 반환
        return print(year)

    return melt(arr)    # 빙산이 한 조각이면 melt 함수 실행


n, m = list(map(int, sys.stdin.readline().split()))
sea = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
year = 0

# 처음 주어지는 빙산의 개수 세기
ice(sea)