import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    n, k = list(map(int, input().split()))
    arr = [list(map(int, input().split())) + [0] for q in range(n)]
    arr.append([0]*(n+1))

    count = 0
    for i in range(n+1):
        temp = 0
        for j in range(n+1):
            if arr[i][j] == 1:
                temp += 1
            else:
                if temp == k:
                    count += 1
                temp = 0

    for i in range(n+1):
        temp = 0
        for j in range(n+1):
            if arr[j][i] == 1:
                temp += 1
            else:
                if temp == k:
                    count += 1
                temp = 0

    print(f'#{tc} {count}')