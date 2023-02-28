import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = [[0] * 10 for _ in range(10)]
    n = int(input())
    for nc in range(n):
        a, b, x, y, c = list(map(int, input().split()))
        for i in range(a, x+1):
            for j in range(b, y+1):
                arr[i][j] += c

    count = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                count += 1

    print(f'#{tc} {count}')