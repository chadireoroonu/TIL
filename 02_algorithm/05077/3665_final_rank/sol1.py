import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(sys.stdin.readline().strip())
for _ in range(T):
    n = int(sys.stdin.readline().strip())    # 팀 수
    last = list(map(int, sys.stdin.readline().split()))    # 작년 앞 팀 수
    m = int(sys.stdin.readline().strip())    # 등수 바뀐 팀 수
    child = deque([] for _ in range(n))

    flag = True
    for i in range(n):
        for j in range(n):
            if last[i] < last[j]:
                child[i].append(j)

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        try:
            child[a-1].append(b-1)
            last[a-1] -= 1
        except:
            flag = False
        try:
            child[b-1].remove(a-1)
            last[b-1] += 1
        except:
            flag = False

    if flag:
        queue = deque()
        for x in range(n):
            if last[x] == 1:
                queue.append(x)
                print(x+1, end=' ')
        print(queue)
        while queue:
            x = queue.popleft()
            for y in child[x]:
                last[y] -= 1
                if last[y] == 1:
                    queue.append(y)
                    print(y+1, end= ' ')
    else:
        print('IMPOSSIBLE', end=' ')

    print()