import sys
sys.stdin = open('input.txt')

w = sys.stdin.readline().strip()
p = sys.stdin.readline().strip()

while p in w:
    stack = []
    result = ''
    for i in w:
        if i not in p:
            result += i
        else:
            if stack:
                if p.index(i) == len(stack) - 1:
                    stack.append(i)
                else:
                    while stack:
                        result += stack.pop(0)
            else:
                if i == p[0]:
                    stack.append(i)
                else:
                    result += i
    w = result

if w:
    print(w)
else:
    print('FRULA')
