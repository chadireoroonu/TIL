import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline().strip())
for tc in range(T):
    N, K = map(int, sys.stdin.readline().split())
    time = list(map(int, sys.stdin.readline().split()))
    total = [0] * N
    for _ in range(K):
        a, b = map(int, sys.stdin.readline().split())
        if total[a-1]:
            total[b-1] = max(total[b-1], total[a-1] + time[b-1])
        else:
            total[b-1] = max(total[b-1], time[a-1] + time[b-1])
    w = int(sys.stdin.readline().strip())

    if total[w-1]:
        print(total[w-1])
    else:
        print(time[w-1])

    print(total)