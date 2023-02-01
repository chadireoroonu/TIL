# 1번 문제
number = int(input())

for i in range(1, number+1):
    print(i)

# 2번 문제
number = int(input())

for i in range(1, number+1):
    print(i, end=' ')

# 3번 문제
number = int(input())
for i in range(number, -1, -1):
    print(i)

# 4번 문제
number = int(input())
for i in range(number, -1, -1):
    print(i, end= ' ')

# 5번 문제
number = int(input())
result = 0
for i in range(1, number+1):
    result += i
print(result)

# 6번 문제
number = int(input())
for i in range(1, number+1):
    print(' '*(number-i)+('*'*i))

# 7번 문제
numbers = [
    85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
    51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
    52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24,
]

num = []
for i in range(len(numbers)):
    min = 100
    for i in range(len(numbers)):
        if numbers[i] < min:
            min = numbers[i]
    num.append(min)
    numbers.remove(min)

print(num[len(num)//2])