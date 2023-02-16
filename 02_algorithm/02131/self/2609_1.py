import sys
sys.stdin = open('input.txt')

a, b = list(map(int, input().split()))

if a > b:
    a, b = b, a

num = []
for i in range(1, a+1):
    if a % i == 0 and b % i == 0:
        num.append(i)
        a = a // i
        b = b // i

mini = 1
for i in num:
    mini *= i

print(mini)
print(mini * a * b)