import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
land = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 문제에서 주어진 숫자 범위
mini = 101
maxi = 0

# 배열의 최소값, 최대값 저장
for a in range(n):
    for b in range(n):
        if land[a][b] < mini:
            mini = land[a][b]
        if land[a][b] > maxi:
            maxi = land[a][b]

# 각 높이별 안전지역 수 구하기
def safe(arr, num):
    global result
    temp = 0    # 해당 높이에서의 안전지역 수
    # arr 직접 변경 시, 다음 높이 순회 때 문제 발생
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] > num and visited[i][j] == 0:
                temp += 1
                queue = [i, j]
                visited[i][j] = 1
                while queue:
                    x = queue.pop(0)
                    y = queue.pop(0)
                    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > num and visited[nx][ny] == 0:
                            queue.append(nx)
                            queue.append(ny)
                            visited[nx][ny] = 1

    if temp > result:    # 이번 높이 안전지역 수와 높이별 안전지역 수 최대값 비교
        result = temp

# 물에 잠기는 지역이 없다면 '1' 출력
if mini == maxi:
    print(1)
else:    # 높이 편차가 있다면 높이별 물에 잠기는 지역 조사
    result = 0
    for num in range(mini, maxi):
        safe(land, num)

    print(result)