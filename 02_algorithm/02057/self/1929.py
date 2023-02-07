m, n = list(map(int, input().split()))

num = []
for i in range(m, n+1):
    counting = 0
    for j in range(1, i):
        if i % j == 0:
            counting += 1
    if counting < 2:
        num.append(i)

for i in num:
    print(i)