students = []
for i in range(1, 31):
    students.append(i)

for i in range(28):
    num = int(input())
    if num in students:
        students.remove(num)

for i in students:
    print(i)