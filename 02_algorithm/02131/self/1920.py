import sys
sys.stdin = open('input.txt')

n = int(input())
num = list(map(int, input().split()))

m = int(input())
key = list(map(int, input().split()))

for i in range(m):
    if key[i] in num:
        print(1)
    else:
        print(0)