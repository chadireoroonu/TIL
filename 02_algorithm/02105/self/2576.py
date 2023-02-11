mini = 100
num = 0
for i in range(7):
    n = int(input())
    if n % 2:
        num += n
        if n < mini:
            mini = n
if num > 0:
    print(num)
    print(mini)
else:
    print(-1)