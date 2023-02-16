import sys
sys.stdin = open('input.txt')

a, b = list(map(int, input().split()))

num = []
times = []
for i in range(1, a+1):
    if a % i == 0:
        times.append(i)
for i in range(1, b+1):
    if b % i == 0:
        if i in times:
            num.append(i)
            times.remove(i)
        else:
            times.append(i)

print(num)
print(times)
print(max(num))