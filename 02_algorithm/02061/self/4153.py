import sys
sys.stdin = open('input.txt')

while True:
    num = list(map(int, input().split()))
    if num == [0, 0, 0]:
        break
    else:
        num.sort()
        if num[-1]**2 == num[0]**2 + num[1]**2:
            print('right')
        else:
            print('wrong')

