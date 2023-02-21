import sys
sys.stdin = open('input.txt')

# 복습 중 런타임에러 발생
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    stop = {}
    for q in range(n):
        a, b = list(map(int, input().split()))
        for i in range(a, b+1):
            if i in stop:
                stop[i] += 1
            else:
                stop[i] = 1
    p = int(input())
    print(f'#{tc}', end= ' ')
    for w in range(p):
        key = int(input())
        print(stop[key], end= ' ')
    print()