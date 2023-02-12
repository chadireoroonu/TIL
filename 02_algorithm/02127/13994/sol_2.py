import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    stop = {}
    for q in range(n):
        bus, a, b = list(map(int, input().split()))
        if bus == 1:
            for i in range(a, b+1):
                if i in stop:
                    stop[i] += 1
                else:
                    stop[i] = 1
        elif bus == 2:
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
        elif bus == 3:
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
    for j in stop:
        if stop[j] > maxi:
            maxi = stop[j]

    print(f'#{tc} {maxi}')