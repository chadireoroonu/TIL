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
            count[i] += 1

    print(count)
    print(child)

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        if a-1 in child[b-1]:
            child[a - 1].append(b - 1)
            count[a - 1] -= 1
            child[b - 1].remove(a - 1)
            count[b - 1] += 1
        else:
            child[b - 1].append(a - 1)
            count[b - 1] += 1
            child[a - 1].remove(b - 1)
            count[a - 1] -= 1

    print(count)
    print(child)
    result = []
    queue = deque()
    for x in range(n):
        if not count[x]:
            queue.append(x)
            result.append(x+1)
    print(queue)
    print(result)
    print(child)

    while queue:
        x = queue.popleft()
        print(f'child[x]={child[x]}')
        for y in child[x]:
            print(count[y])
            count[y] -= 1
            print(count[y])
            if not count[y]:
                queue.append(y)
                result.append(y+1)

    if len(result) == n:
        print(*result)
    else:
        print('IMPOSSIBLE')