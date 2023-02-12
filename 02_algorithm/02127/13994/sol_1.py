import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    # 이중 for문을 이용한 풀이에서 제한시간 초과
    # 딕셔너리를 이용해서 한 번만 순회하
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
            for i in range(a, b+1):
                if bus % 2:
                    if i % 2:
                        if i in stop:
                            stop[i] += 1
                        else:
                            stop[i] = 1
                else:
                    if i % 2 == 0:
                        if i in stop:
                            stop[i] += 1
                        else:
                            stop[i] = 1
        else:
            for i in range(a, b+1):
                if bus % 2:
                    if i % 3 == 0 and i % 10:
                        if i in stop:
                            stop[i] += 1
                        else:
                            stop[i] = 1
                else:
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