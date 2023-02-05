a, b, v = list(map(int, input().split()))

day = 0
height = 0
while True:
    if v > height:
        height += a
        if v > height:
            height -= b
            day += 1
        else:
            day += 1
            print(day)
            break