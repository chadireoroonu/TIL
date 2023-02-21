import sys

def sol(w):
    count = 1
    for i in w:
        if i in stack and i == stack[-1]:
            pass
        elif i in stack and i != stack[-1]:
            count = 0
            return count
        elif i not in stack:
            stack.append(i)

    return count

total = 0
t = int(sys.stdin.readline())
for tc in range(t):
    stack = []
    w = sys.stdin.readline()
    total += sol(w)

print(total)