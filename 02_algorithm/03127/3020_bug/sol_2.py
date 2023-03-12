import sys
sys.stdin = open('input.txt')

n, h = list(map(int, sys.stdin.readline().split()))
cave = [0] * h

for i in range(n):
    temp = int(sys.stdin.readline().strip())
    if i % 2:
        cave[h - temp] += 1
    else:
        cave[0] += 1
        cave[temp] -= 1

print(cave)

for i in range(1, h):
    cave[i] += cave[i-1]

print(cave)

count = 0
mini = min(cave)
for i in cave:
    if i == mini:
        count += 1

print(mini, count)