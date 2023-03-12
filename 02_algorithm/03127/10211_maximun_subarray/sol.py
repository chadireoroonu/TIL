import sys
sys.stdin = open('input.txt')

t = int(sys.stdin.readline())
for tc in range(1, t+1):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    num = [0] * (n+1)
    for q in range(n):
        num[q+1] = arr[q] + num[q]
    num.pop(0)
    print(max(num))
    print(num)