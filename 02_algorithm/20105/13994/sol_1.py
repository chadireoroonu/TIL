import sys
sys.stdin = open('input.txt')

# pass
q = int(input())
for tc in range(1, q+1):
    n = int(input())
    stop = {}
    for w in range(n):
        t, a, b = list(map(int, input().split()))
        if t == 1:
            for i in range(a, b+1):
                if i in stop:
                    stop[i] += 1
                else:
                    stop[i] = 1
        elif t == 2:
            if a % 2:
                for i in range(a, b+1):
                    if i % 2:
                        if i in stop:
                            stop[i] += 1
                        else:
                            stop[i] = 1
            else:
                for i in range(a, b+1):
                    if i % 2 == 0:
                        if i in stop:
                            stop[i] += 1
                        else:
                            stop[i] = 1
        else:
            if a % 2:
                for i in range(a, b+1):
                    if i % 3 == 0 and i % 10:
                        if i in stop:
                            stop[i] += 1
                        else:
                            stop[i] = 1
            else:
                for i in range(a, b+1):
                    if i % 4 == 0:
                        if i in stop:
                            stop[i] += 1
                        else:
                            stop[i] = 1

    maxi = 0
    for i in stop:
        if stop[i] > maxi:
            maxi = stop[i]

    print(f'#{tc} {maxi}')