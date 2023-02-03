a = int(input())
b = input()

num = []
for i in range(1, len(b)+1):
    c = a * int(b[-i])
    num.append(c)

temp = []
for i in range(len(num)):
    temp.append(num[i] * 10 ** i)

result = 0
for i in temp:
    result += i

for i in num:
    print(i)
print(result)