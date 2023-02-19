import sys
sys.stdin = open('input.txt')

for i in range(3):
    temp = list(map(int, input().split()))

    one = 0
    for j in temp:
        if j == 1:
            one += 1

    if one == 0:
        print('D')
    elif one == 1:
        print('C')
    elif one == 2:
        print('B')
    elif one == 3:
        print('A')
    else:
        print('E')