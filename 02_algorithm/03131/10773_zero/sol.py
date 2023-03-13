import sys
sys.stdin = open('input.txt')

k = int(sys.stdin.readline().strip())
stack = []
for i in range(k):
    temp = int(sys.stdin.readline().strip())
    if temp == 0:
        stack.pop()
    else:
        stack.append(temp)

print(sum(stack))