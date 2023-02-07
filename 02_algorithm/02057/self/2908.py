a, b = list(map(str, input().split()))

a1 = ''
for i in range(1, 4):
    a1 += str(a[-i])

b1 = ''
for i in range(1, 4):
    b1 += str(b[-i])

if int(a1) > int(b1):
    print(a1)
elif int(a1) < int(b1):
    print(b1)