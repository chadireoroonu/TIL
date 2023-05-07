import sys
from collections import deque, Counter
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
result = [-1] * N
num = deque()
count = Counter(arr)

for i in range(1, N):
    while num and count[arr[num[-1]]] < count[arr[i]]:
        result[num.pop()] = arr[i]
    num.append(i)

print(*result)