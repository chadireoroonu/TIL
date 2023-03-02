import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = list(map(int, input().split()))
    arr = [list(map(str, input())) for _ in range(n)]

    for i in range(n):
        for j in range(n-m+1):
            temp = ''
            for k in range(m):
                temp += arr[i][j+k]
            if temp == temp[::-1]:
                print(f'#{tc} {temp}')
                break

    for j in range(n):
        for i in range(n-m+1):
            temp = ''
            for k in range(m):
                temp += arr[i+k][j]
            if temp == temp[::-1]:
                print(f'#{tc} {temp}')
                break