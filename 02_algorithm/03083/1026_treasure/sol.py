import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a.sort()
b.sort(reverse=True)

temp = 0
for i in range(n):
    temp += a[i] * b[i]

print(temp)