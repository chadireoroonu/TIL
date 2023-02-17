import sys
sys.stdin = open('input.txt')

n, m = list(map(int, input().split()))
arr = [list(map(str, input())) for _ in range(n)]


for i in range(n-7):
    for j in range(n-7):
        print(arr[i])

print()
for i in range(n-7):
    for j in range(n-7):
        print(arr[j][i])
