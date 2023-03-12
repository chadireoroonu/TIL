import sys
sys.stdin = open('input.txt')

n, m = list(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))

num = [0] * (n+1)
for q in range(n):
    num[q+1] = arr[q] + num[q]

count = 0
front = 0
rear = 0
while rear < len(num):
    if front != rear and (num[rear] - num[front]) % m == 0:
        count += 1
    if rear + 1 == len(num):
        front += 1
        rear = front
    else:
        rear += 1

print(count)