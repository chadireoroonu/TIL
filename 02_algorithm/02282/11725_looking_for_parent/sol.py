import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
arr = [[0] * (n+1) for _ in range(n+1)]

left = [0] * (n+1)
right = [0] * (n+1)
for m in range(n-1):
    a, b = list(map(int, sys.stdin.readline().split()))
    if left[a] == 0:
        left[a] = b
    else:
        right[a] = b
    if b == 1:
        a, b = b, a
        if left[a] == 0:
            left[a] = b
        else:
            right[a] = b

for i in range(1, n+1):
    if i in right:
        print(right.index(i))
    elif i in left:
        print(left.index(i))
