import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = input()
    maxi = 0
    one = 0
    for i in range(n):
        if arr[i] == '1':
            one += 1
        else:
            if one > maxi:
                maxi = one
            one = 0
    if one > maxi:
        maxi = one

    print(f'#{tc} {maxi}')