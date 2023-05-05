# 입력 시, temp 리스트 활용으로 project 삽입
# 새 누적 시간과 현재 누적 시간을 비교, 큰 값 저장
# 선행 작업 완료할 때 마다 count - 1
# count 0 되면 작업 시작 -> queue 추가
# 최종 누적 시간 중 가장 큰 값 출력

import sys
from collections import deque
sys.stdin = open('input.txt')

N = int(sys.stdin.readline().strip())
time = [0] * N    # 작업 개별 수행 시간
count = [0] * N    # 선행 작업 수
project = [[] for _ in range(N)]    # 선행 작업
total = [0] * N    # 누적 시간

for i in range(N):
    t, c, *temp = map(int, sys.stdin.readline().split())
    time[i], count[i] = t, c
    for p in temp:    # project temp 요소 인덱스로 i 추가
        project[p-1].append(i)

queue = deque()
for i in range(N):    # 선행 작업 없다면 queue 추가
    if not count[i]:
        queue.append(i)
        total[i] = time[i]

while queue:
    x = queue.popleft()
    for y in project[x]:
        count[y] -= 1
        total[y] = max(total[x] + time[y], total[y])
        if not count[y]:
            queue.append(y)

print(max(total))