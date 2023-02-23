import sys
sys.stdin = open('input.txt')

def cal(i):
    if i:
        cal(left[i])
        if tree[i] in '+-*/':
            if tree[i] == '+':
                stack.append(y + x)
            elif tree[i] == '-':
                stack.append(y - x)
            elif tree[i] == '*':
                stack.append(y * x)
            elif tree[i] == '//':
                stack.append(y // x)
        else:
            stack.append(int(tree[i]))
        cal(right[i])

for tc in range(1, 11):
    n = int(input())
    tree = [0] * (n + 1)
    left = [0] * (n + 1)
    right = [0] * (n + 1)

    for nc in range(n):
        temp = list(map(str, input().split()))
        tree[int(temp[0])] = temp[1]
        try:
            left[int(temp[0])] = int(temp[2])
        except:
            pass
        try:
            right[int(temp[0])] = int(temp[3])
        except:
            pass

    cal(1)
    print()

