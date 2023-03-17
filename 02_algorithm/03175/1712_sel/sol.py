import sys
sys.stdin = open('input.txt')

a, b, c = list(map(int, sys.stdin.readline().split()))

if b >= c:
    print(-1)
else:
    if a / (c-b):
        print(a//(c-b)+1)
    else:
        print(a//(c-b))