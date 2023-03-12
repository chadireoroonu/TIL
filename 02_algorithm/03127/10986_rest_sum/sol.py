import sys
sys.stdin = open('input.txt')

n, m = list(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))

num = [0] * (n+1)
for q in range(n):
    num[q+1] = (arr[q] + num[q]) % m

print(num)
num.sort()
print(num)

count = 0
target = 0
while target == m:
    front = num.index(target)
    rear = front + 1
    while num[rear] == target:
        if num[rear] - num[front] == 0:
            count += 1
            rear += 1
        else:
            front += 1
    target += 1

print(count)