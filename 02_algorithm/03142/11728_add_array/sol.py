import sys
sys.stdin = open('input.txt')

n, m = list(map(int, sys.stdin.readline().split()))
arr = []
temp = list(map(int, sys.stdin.readline().split()))
for i in temp:
    arr.append(i)

temp = list(map(int, sys.stdin.readline().split()))
for j in temp:
    arr.append(j)

arr.sort()
print(*arr)