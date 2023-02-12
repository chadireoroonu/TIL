import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    arr = [list(map(str, input())) for q in range(8)]

    count = 0
    temp = ''
    for i in range(8):
        for j in range(9-n):
            for k in range(n):
                temp += arr[i][j+k]
            if temp == temp[::-1]:
                count += 1
            temp = ''

    for i in range(9-n):
        for j in range(8):
            for k in range(n):
                temp += arr[i+k][j]
            if temp == temp[::-1]:
                count += 1
            temp = ''

    print(f'#{tc} {count}')
