import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    a, b = input().split()

    a = list(a)
    count = 0
    for i in range(len(a)-len(b)+1):
        temp = ''
        for j in range(len(b)):
            temp += a[i+j]
        if temp == b:
            count += 1

    key = len(a) - len(b)*count + count

    print(f'#{tc} {key}')