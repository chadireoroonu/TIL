import sys
sys.stdin = open('input.txt')

t = int(input())
# for i in range(t):
k, n = list(map(int, input().split()))

path = []
for i in range(k):
    a = list(map(int, input().split()))
    path.append(a)

for i in range(len(path)):
    path_sum = 0
    for j in range(len(path[i])):
        path_sum += path[i][j]

    print(path_sum)