import sys
sys.stdin = open('input.txt')

n, s = list(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))

# 누적합 배열 생성
num = [0] * (n+1)
for q in range(n):
    num[q+1] = arr[q] + num[q]

# 투포인터 탐색
front = 0
rear = 0
mini = len(num) + 1
while rear < len(num):
    if num[rear] - num[front] < s:
        rear += 1
    elif num[rear] - num[front] >= s:
        if rear - front < mini:
            mini = rear - front
        front += 1

if mini == len(num) + 1:
    print(0)
else:
    print(mini)