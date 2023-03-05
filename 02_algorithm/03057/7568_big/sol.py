import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline().strip())
people = []
for _ in range(n):
    people.append(list(map(int, sys.stdin.readline().split())))

big = [0] * n
for i in range(n):
    temp = 0
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            temp += 1
    big[i] = temp+1

print(*big)