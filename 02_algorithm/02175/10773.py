import sys
sys.stdin = open('input.txt')

t = int(input())
stack = []
for tc in range(t):
    temp = int(input())
    if temp != 0:
        stack.append(temp)
    else:
        stack.remove(stack[-1])

print(sum(stack))
