import sys
sys.stdin = open('input.txt')

w = sys.stdin.readline().strip()

result = ''
stack = []
for i in w:
    if i in '+-*/()':
        if i == '(':      # 우선순위 최우선 무조건 삽입
            stack.append(i)
        elif i == ')':    # 여는 괄호가 나올때까지 스택의 모든 요소 빼냄
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        elif i in '+-':   # 우선순위 최하위, 앞에 있는 사칙 연산 모두 빼냄
            while stack and stack[-1] in '+-*/':
                result += stack.pop()
            stack.append(i)
        elif i in '*/':   # 우선 순위 중간, 앞에있는 */ 빼냄
            while stack and stack[-1] in '*/':
                result += stack.pop()
            stack.append(i)
    else:
        result += i
while stack:              # 남아있는 요소는 모두 꺼냄
    result += stack.pop()

print(result)