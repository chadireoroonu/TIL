import sys
sys.stdin = open('input.txt')

t = int(input())

num = []
for i in range(t):
    n = int(input())
    num.append(n)

for j in range(len(num)):
    mini = num[0]
    for i in num:
        if i < mini:
            mini = i
    print(mini)
    num.remove(mini)
