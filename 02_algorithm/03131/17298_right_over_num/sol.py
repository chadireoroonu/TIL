import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

stack = [arr[-1]]
num = [-1] * n
for i in range(n-2, -1, -1):
    while stack:
        if stack[-1] > arr[i]:
            num[i] = stack[-1]
            break
        else:
            stack.pop()
    stack.append(arr[i])

print(*num)