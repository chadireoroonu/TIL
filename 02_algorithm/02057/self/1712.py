a, b, c = list(map(int, input().split()))

x = 0
while True:
    if x <= a // (c - b):
        x += 1
    else:
        break

if x == 0:
    print(-1)
else:
    print(x)