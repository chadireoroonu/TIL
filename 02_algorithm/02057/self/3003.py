che = [1, 1, 2, 2, 2, 8]
old = list(map(int, input().split()))
result = []

for i in range(len(che)):
    temp = che[i] - old[i]
    result.append(temp)

for i in result:
    print(i, end= ' ')