n = int(input())
num = list(map(int, input().split()))

total = 0
for i in num:
    if i != 1:
        counting = 0
        for j in range(1, i):
            if i % j == 0:
                counting += 1
        if counting < 2:
            total += 1

print(total)