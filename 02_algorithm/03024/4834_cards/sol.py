import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    num = list(map(int, input()))
    num = sorted(num)

    number = 0
    maxi = 0
    for i in num:
        temp = num.count(i)
        if temp >= maxi:
            maxi = temp
            number = i

    print(f'#{tc} {number} {maxi}')