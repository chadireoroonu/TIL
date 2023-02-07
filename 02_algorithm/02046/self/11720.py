n = int(input())
num = int(input())
numbers = []

for i in range(n):
    numbers.append(num % 10)
    num = num // 10

sum_num = 0
for i in numbers:
    sum_num += i

print(sum_num)