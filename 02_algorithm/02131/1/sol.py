import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    bracket = input()
    stack = []
    result = 1
    for char in bracket:
        if char == '(':
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                result = -1
                break
    else:
        if stack:
            result = -1

    print(f'#{tc} {result}')