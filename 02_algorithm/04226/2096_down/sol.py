# i == 1, 모든 j 넣은 내려오기 함수 실행
# visited 최소값, 최대값 함수 두 번 실행
# DFS 방향으로 세 방향 탐색
# di = [1, 1, 1]
# dj = [-1, 0, 1]
# visited 각 칸 0 -> 최소값, 1 -> 최대값 기록
# i == n-1, 모든 j visited 순회하며 maxi, mini 판별 출력

# 1차 시도 -> 3% 메모리 초과
# 한줄 입력 받고 계산하고 한 줄 입력받고 계산하고 반복

# 최대값 배열, 최소값 배열을 저장, n줄 동안 배열 한 줄 씩 입력 받기
# 최대값 찾기 함수 -> 입력 받은 배열과 최대값 배열 더해 최대값 갱신
# 비교를 위해 temp 배열 사용, 마지막에 maxi = temp
# 반복문 후 maxi 최대값, mini 최소값 출력

import sys
sys.stdin = open('input.txt')

def maxy():    # 줄 단위 최대값 찾기
    global maxi
    temp = [0, 0, 0]
    for x in range(3):
        dx = [-1, 0, 1]
        for y in range(3):
            nx = x + dx[y]
            if 0 <= nx < 3 and maxi[x] + arr[nx] > temp[nx]:
                temp[nx] = maxi[x] + arr[nx]
    maxi = temp
    return maxi

def miny():    # 줄 단위 최소값 찾기
    global mini
    temp = [10*n]*3
    for x in range(3):
        dx = [-1, 0, 1]
        for y in range(3):
            nx = x + dx[y]
            if 0 <= nx < 3 and mini[x] + arr[nx] < temp[nx]:
                temp[nx] = mini[x] + arr[nx]
    mini = temp
    return mini

n = int(sys.stdin.readline().strip())
maxi = mini = [0] * 3    # 최대, 최소 배열 선언
for t in range(n):
    arr = list(map(int, sys.stdin.readline().split()))    # 한 줄 입력
    maxy()    # 최대값 찾기 함수
    miny()    # 최소값 찾기 함수

print(f'{max(maxi)} {min(mini)}')