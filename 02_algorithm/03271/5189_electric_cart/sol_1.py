import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    queue = [0]
    # load = [[''] * N for _ in range(N)]
    load = [''] * N

    while queue:
        i = queue.pop(0)
        for j in range(N):
            if str(j) not in load[i]:
                load[j] = load[i] + str(j)
                queue.append(j)
    print(load)
