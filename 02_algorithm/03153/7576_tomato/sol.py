import sys
sys.stdin = open('input.txt')

# 시간초과 오답
m, n = list(map(int, sys.stdin.readline().split()))
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 토마토들이 익는 날짜를 저장
def sol(arr, queue):
    q = queue
    while q:
        i = q.pop(0)
        j = q.pop(0)
        di, dj = [1, -1, 0, 0], [0, 0, -1, 1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            # 이미 날짜가 기록되어 있을 경우 제외
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0:
                arr[ni][nj] = arr[i][j] + 1
                q.append(ni)
                q.append(nj)
    return

# 익은 토마토 좌표를 저장
queue = []
for a in range(n):
    for b in range(m):
        if arr[a][b] == 1:
            queue.append(a)
            queue.append(b)

sol(arr, queue)

# 최종 결과를 확인
def result(arr):
    maxi = 0
    for a in range(n):
        for b in range(m):
            if arr[a][b] > maxi:
                maxi = arr[a][b]
            # 익지 않은 토마토가 있다면 '-1' 출력
            if arr[a][b] == 0:
                return print(-1)
    # 익은 토마토가 1로 주어지므로, '날짜 -1' 출력
    return print(maxi-1)

result(arr)