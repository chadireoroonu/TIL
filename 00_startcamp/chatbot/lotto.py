import random

# 1 ~ 45 숫자를 담은 List 생성
# range(n, m) = n부터 m-1까지의 숫자를 생성
numbers = list(range(1, 46))

for i in range(5):
    print(random.sample(numbers, 6))

# n = 0
#while n < 6:
#    print(random.choice(numbers))
#    n += 1