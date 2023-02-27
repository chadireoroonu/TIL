import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]

    di = []
    dj = []

    for i in range(n):
        for j in range(m):
