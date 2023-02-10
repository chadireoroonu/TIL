import sys
sys.stdin = open('input.txt')

q = int(input())
for tc in range(1, q+1):
    n = int(input())
    stop = []
    for w in range(n):
        t, a, b = list(map(int, input().split()))
        if t == 1:
            for i in range(a, b+1):
                stop.append(i)
        elif t == 2:
            if a % 2:
                for i in range(a, b+1):
                    if i % 2:
                        stop.append(i)
            else:
                for i in range(a, b+1):
                    if i % 2 == 0:
                        stop.append(i)
        else:
            if a % 2:
                for i in range(a, b+1):
                    if i % 3 == 0 and i % 10:
                        stop.append(i)
            else:
                for i in range(a, b+1):
                    if i % 4 == 0:
                        stop.append(i)
    # maxi = 0
    # for i in stop:
    #     count = 0
    #     for j in stop:
    #         if i == j:
    #             count += 1
    #     if count > maxi:
    #         maxi = count

    

    print(f'#{tc} {maxi}')