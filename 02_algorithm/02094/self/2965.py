import sys
sys.stdin = open('input.txt')

num = list(map(int, input().split()))

move = 0
while True:
    if num[2] - num[1] + num[1] - num[0] < 3:
        break
    else:
        if num[1] - num[0] > num[2] - num[1]:
            num[2] = num[1] - 1
            num = sorted(num)
            move +=1
        elif num[1] - num[0] < num[2] - num[1]:
            num[1] = num[1] + 1
            num = sorted(num)
            move += 1

print(move)