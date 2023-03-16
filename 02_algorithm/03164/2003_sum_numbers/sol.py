import sys
sys.stdin = open('input.txt')

N, M = list(map(int, sys.stdin.readline().split()))
num = [0] * (N+1)    # 누적합 배열 생성
arr = list(map(int, sys.stdin.readline().split()))
for i in range(N):    # 누적합 배열 채우기
    num[i+1] = arr[i] + num[i]

count = 0    # 조건에 맞는 경우의 수
front = 0
rear = 0
while rear < N+1:    # 누적합 배열 전체 조사
    if num[rear] - num[front] < M:
        rear += 1
    elif num[rear] - num[front] > M:
        front += 1
    elif num[rear] - num[front] == M:
        count += 1
        rear += 1

print(count)