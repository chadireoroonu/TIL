n, x = list(map(int, input().split()))
num = list(map(int, input().split()))

small = []
for i in num:
    if i < x:
        small.append(i)

for i in small:
    print(i, end= ' ')