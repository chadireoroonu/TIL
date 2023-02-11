import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    result = ''
    for i in range(n):
        a, b = list(map(str, input().split()))
        result += a * int(b)

    print(f'#{tc}')
    while len(result) > 0:
        if len(result) >= 10:
            print(result[0:10])
            result = result[10::]
        else:
            print(result)
            break