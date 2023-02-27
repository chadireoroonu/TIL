import sys
sys.stdin = open('input.txt')

# 시간초과
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    stop = []
    for i in range(n):
        a, b = list(map(int, input().split()))
        for j in range(a, b+1):
            stop.append(j)
    p = int(input())
    ps = [int(input()) for q in range(p)]

    print(f'#{tc}', end=' ')
    for i in ps:
        print(stop.count(i), end=' ')
    print()
