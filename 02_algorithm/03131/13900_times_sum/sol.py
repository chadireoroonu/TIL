import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

front = 0
rear = 1
count = 0
while rear <= n and front <= n:
    if front != rear:
        count += arr[front] * arr[rear]
        print(arr[front] * arr[rear])
        print(f'front {front}, rear {rear}')
        rear += 1
    if rear + 1 == n:
        front += 1
        rear = front + 1

print(count)