import sys
sys.stdin = open('input.txt')

n = int(input())
for i in range(n, 0, -1):
    print('*'*i)