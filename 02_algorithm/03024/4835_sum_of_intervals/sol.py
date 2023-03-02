import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = list(map(int, input().split()))
    num = list(map(int, input().split()))

    maxi = 0
    mini = 10000 * m
    for i in range(n-m+1):
        temp = 0
        for j in range(m):
            temp += num[i+j]
        if temp < mini:
            mini = temp
        if temp > maxi:
            maxi = temp

    print(f'#{tc} {maxi-mini}')