import sys
sys.stdin = open('input.txt')

num = [0] * 10
for i in range(10):
    num[i] = num[i-1] + int(sys.stdin.readline())

result = 0
sub = 100
for i in range(10):
    if abs(num[i] - 100) <= sub:
        sub = abs(num[i] - 100)
        result = num[i]

print(result)