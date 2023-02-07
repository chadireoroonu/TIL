a, b = list(map(int, input().split()))
min = int(input())

if (b + min) >= 60:
    a += (b + min) // 60
    b = (b + min) % 60
    if a >= 24:
        a -= 24
else:
    b += min
    if a >= 24:
        a -= 24

print(f'{a} {b}')