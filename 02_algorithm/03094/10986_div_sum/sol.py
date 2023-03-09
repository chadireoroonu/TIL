import sys
sys.stdin = open('input.txt')

n, m = list(map(int, sys.stdin.readline().split()))
number = list(map(int, sys.stdin.readline().split()))

num = [0] * (n+1)
for q in range(n):
    num[q+1] = number[q] + num[q]

count = 0
for i in range(n):
    for j in range(n, i, -1):
        if i == 0:
            if num[j] != 0 and num[j] % m == 0:
                count += 1
        else:
            if (num[j] - num[j-i]) % m == 0:
                count += 1

print(count)