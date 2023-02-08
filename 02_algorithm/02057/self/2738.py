import sys
sys.stdin = open('input.txt')

n, m = list(map(int, input().split()))

num1 = []
for i in range(n):
    a = list(map(int, input().split()))
    num1.append(a)

num2 = []
for i in range(n):
    a = list(map(int, input().split()))
    num2.append(a)

num3 = num1
for i in range(n):
    for j in range(m):
        num3[i][j] += num2[i][j]

for i in range(n):
    for j in range(m):
        print(num3[i][j], end=' ')
    print()