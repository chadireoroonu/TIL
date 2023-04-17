import sys
sys.stdin = open('input.txt')

n, k = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num.sort()

print(num[k-1])