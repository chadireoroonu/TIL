import sys
sys.stdin = open('input.txt')

# 중위순회
def sol(n):
    parent = [0] * (n + 1)
    left = [0] * (n + 1)
    right = [0] * (n + 1)


T = int(input())
for tc in range(1, T+1):
    n = int(input())

    parent = [0] * (n + 1)
    left = [0] * (n + 1)
    right = [0] * (n + 1)

    if n > 3:
        parent[n//2+1] = n//2+1
    root = n // 2 + 1

    start = 1
    end = n











    print(parent)
