import sys
sys.stdin = open('input.txt')

t = int(sys.stdin.readline())
for tc in range(1, t+1):
    a, b = list(map(int, sys.stdin.readline().split()))
    print(f'Case #{tc}: {a} + {b} = {a+b}')

