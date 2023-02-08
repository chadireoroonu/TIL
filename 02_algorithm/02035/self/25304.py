total = int(input())
present = int(input())

sum_each = 0
for i in range(present):
    a, b = list(map(int, input().split()))
    sum_each += a * b

if total == sum_each:
    print('Yes')
else:
    print('No')