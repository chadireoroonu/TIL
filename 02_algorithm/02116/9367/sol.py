import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    carrot = list(map(int, input().split()))
    big = 1
    maxi = 1
    for i in range(n-1):
        if carrot[i] < carrot[i+1]:
            big += 1
        else:
            if big > maxi:
                maxi = big
            big = 1
    if big > maxi:
        maxi = big

    print(f'#{tc} {maxi}')