import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

num = [0] * (n+1)
for q in range(n):
    num[q+1] = arr[q] + num[q]

t = int(sys.stdin.readline())
for tc in range(t):
    a, b = list(map(int, sys.stdin.readline().split()))
    print(num[b] - num[a-1])