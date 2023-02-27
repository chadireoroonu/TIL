import sys
sys.stdin = open('input.txt')

# pass
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    stop = [list(map(int, input().split())) for w in range(n)]

    p = int(input())
    ps = [int(input()) for q in range(p)]

    print(f'#{tc}', end= ' ')
    for i in ps:
        count = 0
        for j in range(len(stop)):
            if i >= stop[j][0] and i <= stop[j][1]:
                count += 1
        print(count, end= ' ')
    print()