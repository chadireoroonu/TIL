import sys
sys.stdin = open('input.txt')

n, m = list(map(int, input().split()))
arr = [list(map(int, input().split())) for q in range(n)]

k = int(input())
for w in range(k):
    i, j, x, y = list(map(int, input().split()))
    total = 0
    for a in range(i-1, x):
        for b in range(j-1, y):
            total += arr[a][b]
    print(total)
