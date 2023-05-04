# 내 앞에 서야 하는 사람 정보 리스트에 저장, mini 배열 해당 인덱스 += 1
# 내 앞에 서야 하는 사람이 없다면, order 추가, 지시를 위한 포인터 사용
# order pointer 번째 요소의 people 해당 인덱스 리스트 속 요소들 앞 사람 -1
# 앞에 서야 하는 사람이 없어졌다면, 해당 인덱스 order 추가
# order : 처음부터 끝까지 리스트 추가된 순서 출력 (출력 형식 주의)
# deque 두 개 사용하는 대신 리스트와 포인터를 사용해봤음

# 메모리 : 37920KB, 시간 : 208ms, 코드길이 : 519B

import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
people = [[] for _ in range(N+1)]
mini = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    people[a].append(b)
    mini[b] += 1

order = []
pointer = 0
for x in range(1, N+1):
    if not mini[x]:
        order.append(x)

while pointer < len(order):
    i = order[pointer]
    pointer += 1
    for j in people[i]:
        mini[j] -= 1
        if not mini[j]:
            order.append(j)

for x in order:
    print(x, end=' ')