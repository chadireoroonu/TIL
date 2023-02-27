import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    a, b = list(map(str, input().split()))

    real_a = a
    count = 0
    while True:
        if b in a:
            a = list(a)
            for i in range(len(a) - len(b) + 1):
                temp = ''
                for j in range(len(b)):
                    temp += a[i + j]
                if temp == b:
                    count += 1
                    for k in temp:
                        a.remove(k)
                    if b not in a:
                        break
        else:
            break


    key = len(real_a) - len(b) * count + count
    print(f'#{tc} {key}')