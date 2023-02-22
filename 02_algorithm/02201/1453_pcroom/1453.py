import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
people = list(map(int, sys.stdin.readline().split()))
count = 0
com = [0] * 101
for i in people:
    if com[i] == 0:
        com[i] = 1
    else:
        count += 1

print(count)