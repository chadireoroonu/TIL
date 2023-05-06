import sys
from collections import deque
sys.stdin = open('input.txt')

N = int(sys.stdin.readline().strip())
time = [0] * N    # 개별 건물 건설 시간
total = [0] * N    # 개별 건물 누적 시간
count = [0] * N    # 선행 건물 개수
building = [[] for _ in range(N)]    # 선행 건물 종류

for i in range(N):
    t, *temp = map(int, sys.stdin.readline().split())
    time[i] = t
    for j in temp:    # -1 아닌 요소에 대해 선행 건물 정보 저장
        if j > 0:
            count[i] += 1
            building[j-1].append(i)

queue = deque()    # 선행 건물이 없다면, queue 추가, 시간 저장
for i in range(N):
    if not count[i]:
        queue.append(i)
        total[i] = time[i]

while queue:    # 건설 작업, 시간은 누적 시간 중 큰 값으로 재할당
    x = queue.popleft()
    for y in building[x]:
        count[y] -= 1
        total[y] = max(total[y], total[x] + time[y])
        if not count[y]:    # 선행건물이 모두 지어진 건물은 queue 추가
            queue.append(y)

for i in total:    # 모든 건물의 누적시간 출력
    print(i)