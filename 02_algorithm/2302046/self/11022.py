import sys

t = int(input())
for i in range(1, t+1):
    a, b = map(int, sys.stdin.readline().split())
    print(f'Case #{tc}: {a} + {b} = {a + b}')

# t = int(input())
# for i in range(1, t+1):
#     a, b = list(map(int, input().split()))
#     print(f'Case #{tc}: {a} + {b} = {a + b}')