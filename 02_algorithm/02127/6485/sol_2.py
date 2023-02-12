import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    stop = [list(map(int, input().split())) for w in range(n)]

    p = int(input())

    print(f'#{tc}', end= ' ')
    for j in range(p):
        key = int(input())
        count = 0
        for i in range(len(stop)):
            if stop[i][0] <= key and stop[i][1] >= key:
                count += 1
        print(count, end= ' ')
    print()