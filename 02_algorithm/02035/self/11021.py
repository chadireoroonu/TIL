import sys

t = int(input())

for tc in range(1, t+1):
    a, b = map(int, sys.stdin.readline().split())
    print(f'Case #{tc}: {a + b}')