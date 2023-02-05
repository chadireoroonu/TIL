a, b, v = list(map(int, input().split()))

day = (v - a) / (a - b)

if day - (v - a) // (a - b):
    day = (v - a) // (a - b) + 1
else:
    day = (v - a) / (a - b)

print(int(day)+1)