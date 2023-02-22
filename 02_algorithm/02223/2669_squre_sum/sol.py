import sys
sys.stdin = open('input.txt')

arr = [[0] * 100 for _ in range(100)]
for squre in range(4):
    a, b, x, y = list(map(int, sys.stdin.readline().split()))
    for i in range(a, x):
        for j in range(b, y):
            arr[i][j] += 1

count = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] != 0:
            count += 1

print(count)