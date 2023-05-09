import sys
from collections import deque
sys.stdin = open('input.txt')

N, M, X = map(int, sys.stdin.readline().split())
load = deque([] for _ in range(N))
for _ in range(M):
    a, b, t = map(int, sys.stdin.readline().split())
    load[a-1].append([b-1, t])
maxi = 0    # 최대 이동시간

def shift(x, y):    # 이동함수
    time = 10000000
    queue = deque([x])
    visited = [10000000] * M
    visited[x] = 1
    while queue:
        i = queue.popleft()
        if i == y and visited[i] < time:
            time = visited[i]    # 최소 이동시간 재할당
        if visited[i] > time:    # 유망성 조사
            continue
        for j in load[i]:    # visited 비교로 진입 조건 설정
            if visited[i] + j[1] <= visited[j[0]]:
                visited[j[0]] = visited[i] + j[1]
                queue.append(j[0])
    return time - 1    # 최초 1에서 시작

for k in range(N):    # 각 학생들의 이동시간 확인, 최대값 재할당
    time = shift(k, X-1) + shift(X-1, k)
    if time > maxi:
        maxi = time

print(maxi)