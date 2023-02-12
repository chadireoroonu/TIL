import sys
sys. stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    d, a, b, f = list(map(int, input().split()))
    t = d / (a + b)

    print(f'#{tc} {f*t}')