import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    num = {2:0, 3:0, 5:0, 7:0, 11:0}
    for i in num:
        while True:
            if n % i == 0:
                num[i] += 1
                n = n // i
            else:
                break

    print(f'#{tc}', end= ' ')
    for i in num:
        print(num[i], end= ' ')
    print()
