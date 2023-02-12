import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    stop = {}
    for q in range(n):
        a, b = list(map(int, input().split()))
        stop[a] = b

    p = int(input())

    print(f'#{tc}', end= ' ')
    for w in range(p):
        count = 0
        key = int(input())
        for i in stop:
            if i <= key and stop[i] >= key:
                count += 1
        print(count, end= ' ')
    print()