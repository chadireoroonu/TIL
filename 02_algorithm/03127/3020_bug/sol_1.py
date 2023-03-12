import sys
sys.stdin = open('input.txt')

n, h = list(map(int, sys.stdin.readline().split()))
cave = [0] * h

# 종유석은 거꾸로 -> h - temp
# 석순은 총 석순, 감소 저장
for i in range(n):
    temp = int(sys.stdin.readline().strip())
    if i % 2:
        cave[h - temp] += 1
    else:
        cave[0] += 1
        cave[temp] -= 1

# 누적합
for i in range(1, h):
    cave[i] += cave[i-1]

# 최소 장애물
mini = min(cave)

print(mini, cave.count(mini))