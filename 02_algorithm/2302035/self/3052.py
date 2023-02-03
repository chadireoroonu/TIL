import sys
sys.stdin = open('input.txt')

num = []
for i in range(10):
    n = int(input())
    if n % 42 not in num:
        num.append(n % 42)

counting = 0
for i in num:
    counting += 1

print(counting)