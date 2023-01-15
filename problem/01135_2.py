
n = str(int(input()))

if len(n) == 1:
    list = (int(n[0]))
elif len(n) == 2:
    list = (int(n[0]), int(n[1]))
elif len(n) == 3:
    list = (int(n[0]), int(n[1]), int(n[2]))
else:
    list = (int(n[0]), int(n[1]), int(n[2]), int(n[3]))

a = sum(list)

print(a)