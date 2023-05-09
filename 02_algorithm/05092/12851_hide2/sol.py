import sys
from collections import deque
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())
visited = [100001] * 100001    # 작거나 같은 경우 이동가능 하도록 최대치에서 시작
count = 0    # 최소 시간으로 도달 가능한 수
mini = 100001

if N == K:    # 수빈이와 동생 좌표가 같을 때
    print(0)
    print(1)
else:    # 수빈이와 동생 좌표가 다를 때
    queue = deque([N])
    visited[N] = 1
    while queue:
        i = queue.popleft()
        di = [i, -1, 1]
        if visited[i] > mini:    # 유망성 검사
            continue
        for j in range(3):
            ni = i + di[j]
            if 0 <= ni < 100001 and visited[ni] >= visited[i] + 1:
                visited[ni] = visited[i] + 1
                queue.append(ni)
                if ni == K:    # 동생을 찾았을 때
                    count += 1
                    mini = visited[ni]

    print(mini-1)
    print(count)