import sys
sys.stdin = open('input.txt')

n, m = list(map(int, input().split()))
poketmon = []
for name in range(n):
    poketmon.append(input())

poketmon = list(enumerate(poketmon, start= 1))

print(poketmon)

for i in range(m):
    temp = input()
    if temp in poketmon[i]:
        print(poketmon[i][1])
    else:
        pass
