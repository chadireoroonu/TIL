import sys
sys.stdin = open('input.txt')

n, m = list(map(int, input().split()))

name = []
result = []
for i in range(n):
    name.append(input())

for i in range(m):
    a = input()
    if a in name:
        result.append(a)

print(len(result))
for i in result:
    print(i)