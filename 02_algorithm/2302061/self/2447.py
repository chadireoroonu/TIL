n = int(input())

num = 1
while True:
    if n == 3:
        break
    else:
        num += 1
        n = n / 3

for i in range(num):
    print('*' * 3)

