# deque 활용으로 시간초과 방지
# 방문 여부 확인 배열 생성
# 각 숫자를 인덱스로 활용
# 3,2로 나누어 떨어지는 수, 몫 기록
# 숫자 방문 시, 현재까지의 변환 횟수 기록
# 처음 1부터 시작 -> 출력시 -1

import sys
from collections import deque
sys.stdin = open('input.txt')

N = int(sys.stdin.readline().strip())
visited = [0] * (N + 1)

queue = deque([N])
visited[N] = 1
while queue:
    x = queue.popleft()
    # 1 도착 시 visited[1]-1 출력
    if x == 1:
        print(visited[1]-1)
        break
    # 3으로 나누어 떨어지고, 3으로 나눈 몫 미방문 시 처리
    if not x % 3 and not visited[x//3]:
        queue.append(x//3)
        visited[x//3] = visited[x] + 1
    # 2로 나누어 떨어지고, 2로 나눈 몫 미방문 시 처리
    if not x % 2 and not visited[x//2]:
        queue.append(x//2)
        visited[x//2] = visited[x] + 1
    # 1을 뺀 숫자 미방문 시 처리
    if not visited[x-1]:
        queue.append(x-1)
        visited[x-1] = visited[x] + 1