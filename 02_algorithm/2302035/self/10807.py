n = int(input())
numbers = list(map(int, input().split()))
num = int(input())

counting = 0
for i in numbers:
    if i == num:
        counting += 1

print(counting)