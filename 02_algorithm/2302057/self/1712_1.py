a, b, c = list(map(int, input().split()))

sel = a / (c - b)

if sel - a // (c - b):
    sel = a // (c - b) + 1
else:
    sel = int(a / (c - b))

if sel < 1:
    print(-1)
else:
    print(sel+1)