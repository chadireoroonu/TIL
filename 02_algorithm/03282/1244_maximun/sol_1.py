import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, c = list(input().split())
    c = int(c)

    num = []
    for i in n:
        num.append(int(i))

    change = 0
    start_idx = 0
    while change < c:
        start = num[start_idx]
        maxi_idx = start_idx
        maxi = num[start_idx]
        for j in range(start_idx+1, len(num)):
            if num[j] >= maxi:
                maxi_idx, maxi = j, num[j]
        if start_idx != maxi_idx:
            num[start_idx], num[maxi_idx] = maxi, start
            change += 1
            start_idx += 1
            if start_idx >= len(num):
                start_idx = start_idx % len(num)
        else:
            start_idx += 1
            if start_idx >= len(num):
                start_idx = start_idx % len(num)

    print(f'#{tc}', end=' ')
    for i in num:
        print(i, end='')
    print()