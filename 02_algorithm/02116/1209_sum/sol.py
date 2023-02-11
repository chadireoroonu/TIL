import sys
sys.stdin = open('input.txt')

for q in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for w in range(100)]

    maxi = 0

    temp = 0
    for i in range(100):
        for j in range(100):
            temp += arr[i][j]
        if temp > maxi:
            maxi = temp
        temp = 0

    for i in range(100):
        for j in range(100):
            temp += arr[j][i]
        if temp > maxi:
            maxi = temp
        temp = 0

    for i in range(100):
        for j in range(100):
            if i == j:
                temp += arr[i][j]

    if temp > maxi:
        maxi = temp
    temp = 0

    for i in range(100):
        for j in range(100):
            if i + j == 99:
                temp += arr[i][j]

    if temp > maxi:
        maxi = temp
    temp = 0

    print(f'#{tc} {maxi}')
