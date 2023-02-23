import sys
sys.stdin = open('input.txt')

n, m = list(map(str, input().split()))

total = 0
for i in n:
    for j in m:
        total += int(i) * int(j)

print(total)