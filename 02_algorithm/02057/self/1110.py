n = int(input())

goal = n
num = []
a = n // 10 
b = n % 10
c = a + b
n = b * 10 + c % 10
num.append(n)

counting = 1
while True:
    if n != goal:
        a = n // 10 
        b = n % 10
        c = a + b
        n = b * 10 + c % 10
        num.append(n)
        counting += 1
    else:
        break

print(len(num))