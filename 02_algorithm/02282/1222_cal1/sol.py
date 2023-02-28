import sys
sys.stdin = open('input.txt')

def sol(num):
    result = 0
    stack_1 = []
    for i in range(len(num)):
        if num[i] == '+':
            stack_1.append(int(stack_1.pop()) + int(stack_1.pop()))
        else:
            stack_1.append(num[i])

    return stack_1[0]

for tc in range(1, 11):
    n = int(input())
    number = input()
    stack = []
    word = ''

    for num in number:
        if num == '+' and stack == []:
            stack.append(num)
        elif num == '+':
            word += stack.pop()
            stack.append(num)
        else:
            word += num
    while stack:
        word += stack.pop()

    print(f'#{tc} {sol(word)}')