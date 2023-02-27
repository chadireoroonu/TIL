import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    num = list(map(int, input().split()))

    mini = num[0]
    maxi = num[0]
    for i in num:
        if i > maxi:
            maxi = i
        if i < mini:
            mini = i

    print(f'#{tc} {maxi-mini}')
