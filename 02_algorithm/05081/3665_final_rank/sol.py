# 작년 팀 등수 정보로, 선행조건, 선행조건 수 저장
# 등수가 바뀐 팀들 정보 수정
# result 배열에 최종 순위 추가
# result 길이가 팀 수와 다르면 impossible 출력

import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(sys.stdin.readline().strip())
for _ in range(T):
    n = int(sys.stdin.readline().strip())    # 팀 수
    last = list(map(int, sys.stdin.readline().split()))    # 작년 등수
    m = int(sys.stdin.readline().strip())    # 등수 바뀐 팀 수
    child = deque([] for _ in range(n))
    count = [0] * n

    for i in range(n):
        for j in range(i+1, n):
            child[last[i]-1].append(last[j]-1)
            count[last[j]-1] += 1    # count[j]로 해둬서 틀림

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        if a-1 in child[b-1]:
            child[a - 1].append(b - 1)
            count[a - 1] -= 1
            child[b - 1].remove(a - 1)
            count[b - 1] += 1
        else:
            child[b - 1].append(a - 1)
            count[b - 1] -= 1
            child[a - 1].remove(b - 1)
            count[a - 1] += 1

    result = []
    queue = deque()
    for x in range(n):
        if not count[x]:
            queue.append(x)
            result.append(x+1)

    while queue:
        x = queue.popleft()
        for y in child[x]:
            count[y] -= 1
            if not count[y]:
                queue.append(y)
                result.append(y+1)

    if len(result) == n:
        print(*result)
    else:
        print('IMPOSSIBLE')