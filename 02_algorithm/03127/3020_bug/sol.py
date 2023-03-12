import sys
sys.stdin = open('input.txt')

n, h = list(map(int, sys.stdin.readline().split()))
down = [0] * (n//2+1)
up = [0] * (n//2+1)
for q in range(n):
    if q % 2:
        down[q//2+1] = down[q//2] + int(sys.stdin.readline().strip())
    else:
        up[q//2+1] = up[q//2] + int(sys.stdin.readline().strip())

mini = n
count = 0
for i in range(1, h+1):
    temp = 0
    for j in range(len(up)-1):
        if up[j+1] - up[j] >= i:
            temp += 1
        if h - (down[j+1] - down[j]) < i:
            temp += 1
    if temp < mini:
        count = 1
        mini = temp
    elif temp == mini:
        count += 1

print(mini, count)
