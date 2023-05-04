# 내 앞에 서야 하는 사람 정보 리스트에 저장, mini 배열 해당 인덱스 += 1
# 내 앞에 서야 하는 사람이 없다면, queue, order 추가
# queue 요소 popleft 후 people 해당 인덱스 리스트 속 요소들 앞 사람 -1
# 앞에 서야 하는 사람이 없어졌다면, 해당 인덱스 queue, order 추가
# order : 처음부터 끝까지 queue 추가된 순서 출력 (출력 형식 주의)

# 메모리 : 37796KB, 시간 : 224ms, 코드길이 : 579B

import sys
from collections import deque
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
people = [[] for _ in range(N+1)]
mini = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    people[a].append(b)
    mini[b] += 1

order = deque()
queue = deque()
for x in range(1, N+1):
    if not mini[x]:
        queue.append(x)
        order.append(x)

while queue:
    i = queue.popleft()
    for j in people[i]:
        mini[j] -= 1
        if not mini[j]:
            queue.append(j)
            order.append(j)

for x in order:
    print(x, end=' ')