import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    students = list(enumerate(map(int, input().split()), start= 1))
    # students = list(enumerate(students))
    print(students)
    winner = []
    result = []
    for i in range(n//2):
        # if students[i * 2 + 1]:
        if students[i * 2][1] == 1:
            if students[i * 2 + 1][1] == 1:
                students.remove(students[i * 2 + 1])
            elif students[i * 2 + 1][1] == 2:
                students.remove(students[i * 2])
            else:
                students.remove(students[i * 2 + 1])
        elif students[i * 2][1] == 2:
            if students[i * 2 + 1][1] == 1:
                students.remove(students[i * 2])
            elif students[i * 2 + 1][1] == 2:
                students.remove(students[i * 2 + 1])
            else:
                students.remove(students[i * 2])
        else:
            if students[i * 2 + 1][1] == 1:
                students.remove(students[i * 2])
            elif students[i * 2 + 1] == 2:
                students.remove(students[i * 2 + 1])
            else:
                students.remove(students[i * 2 + 1])
    print(students)