import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
result = [-1] * N
num = 0

for i in range(N):
    for j in range(i+1, N):
        if arr.count(arr[i]) < arr.count(arr[j]):
            result[i] = arr[j]
            break

print(*result)