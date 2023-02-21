import sys
sys.stdin = open('input.txt')

# 복습 풀이에서 제한 시간 초과
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    stop = []
    for i in range(n):
        bus, a, b = list(map(int, input().split()))
        if bus == 1:
            for j in range(a, b+1):
                stop.append(j)
        elif bus == 2:
            for j in range(a, b+1):
                if a % 2:
                    if j % 2:
                        stop.append(j)
                else:
                    if j % 2 == 0:
                        stop.append(j)
        elif bus == 3:
            for j in range(a, b+1):
                if a % 2:
                    if j % 3 == 0 and j % 10:
                        stop.append(j)
                else:
                    if j % 4 == 0:
                        stop.append(j)

    maxi = 0
    for i in stop:
        num = 0
        for j in stop:
            if i == j:
                num += 1
                if num > maxi:
                    maxi = num

    print(f'#{tc} {maxi}')