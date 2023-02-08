import sys
sys.stdin = open('input.txt')

m = int(input())
n = int(input())

num = []
for i in range(m, n+1):
    if i != 1:
        couting = 0
        for j in range(1, i):
            if i % j == 0:
                couting += 1
        if couting < 2:
            num.append(i)

sum_num = 0
for i in num:
    sum_num += i

print(sum_num)
print(num[0])