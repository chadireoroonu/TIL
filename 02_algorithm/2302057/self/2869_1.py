a, b, v = list(map(int, input().split()))

day = 0
height = 0
while True:
    if height < v:
        day += 1
        height = (a - b) * day + a
    else:
        day += 1
        break

print(day)