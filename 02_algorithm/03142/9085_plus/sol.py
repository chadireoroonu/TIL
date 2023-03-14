import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(sum(arr))