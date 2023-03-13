import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline().strip())
arr = list(enumerate(map(int, sys.stdin.readline().split())))

stack = [arr[0]]
tower = [0] * n

for i in range(1, n):
    while stack:
        if stack[-1][1] >= arr[i][1]:
            tower[i] = stack[-1][0]+1
            break
        else:
            stack.pop()
    stack.append(arr[i])

print(*tower)