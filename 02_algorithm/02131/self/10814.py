import sys
sys.stdin = open('input.txt')

n = int(input())
people = [list(map(str, input().split())) for q in range(n)]

for i in range(len(people)):
    for j in range(len(people)-1):
        if people[j][0] > people[j + 1][0]:
            people[j], people[j + 1] = people[j + 1], people[j]

for i in range(len(people)):
    print(f'{people[i][0]} {people[i][1]}')