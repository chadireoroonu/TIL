import sys
sys.stdin = open('input.txt')

t = int(input())
for i in range(t):
    num = list(map(int, input().split()))
    mini = 100
    total = 0
    for j in num:
        if j % 2 == 0:
            total += j
            if j < mini:
                mini = j
    print(total, end= ' ')
    print(mini)