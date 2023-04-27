# 1. 아기 상어보다 작은 물고기만 먹음
# 2. 상어 크기 수의 물고기 먹으면 성장
# 3. 상어와 크기 같은 물고기 칸 통과 가능, 섭취 불가능
# 4. 먹을 수 있는 물고기가 많다면 거리가 가까운 물고기 섭취
#    거리가 가까운 물고기가 많다면 위, 왼쪽 우선순위
# 5. 아기상어 최초 크기 2, 좌표 9, 물고기 크기 1~6

# BFS 사용, 이전에는 시간초과가 났으니 deque 사용
# 먹을 수 있는 물고기를 찾으면, 동일거리까지만 탐색
# 동일 거리 물고기 deque 삽입 시, i좌표, j좌표 순으로 비교
# 작은 값은 왼쪽, 큰 값은 오른쪽에 넣기
# 먹는 물고기 수 temp 기록, temp == shark => shark + 1


# 최초 상어 좌표 찾은 후 find 함수 실행

# find 함수
# 먹을 수 있는 물고기 좌표 찾기

# eat 함수
# 물고기 거리 측정
# 먹기 -> 좌표 변화

# 먹을 수 없는 위치의 물고기는 어떻게 할까
# 아예 처음부터 BFS 탐색


import sys
from collections import deque
sys.stdin = open('input.txt')


def find(arr):
    while True:
        fish = deque([])
        for i in range(n):
            for j in range(n):
                if 0 < arr[i][j] <= 6 and sea[i][j] < shark:
                    fish.append([i, j])
        if fish:
            eat(fish)
        else:
            return


def eat(arr):
    global sec, shark
    visited = [[0]*n for _ in range(n)]
    while arr:


    return


n = int(sys.stdin.readline().strip())
sea = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
sec = 0
shark = 2

find(sea)