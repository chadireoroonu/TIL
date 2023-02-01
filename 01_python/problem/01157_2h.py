print("$ of tesst cases: ", end="")
a = int(input())

b = []
for i in range(a):
    temp = list(map(int, input().split(' ')))
    temp.sort()
    b.append(temp)

print(b)

print("answer: ")
for i in range(a):
    print(b[i])