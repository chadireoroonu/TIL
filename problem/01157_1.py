a = list(input().split()for _ in range(2))

n = a[0]
a.remove(a[0])

b = a.sort()

print(b[n//2])