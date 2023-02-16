import sys
sys.stdin = open('input.txt')

def win(students, n):
    if len(students) == 1:
        return print(f'#{tc} {students[0][0] + 1}')
    else:
        if len(students) % 2:
            students.append((len(students), 5))
        delete = []
        for i in range(n):
            if students[i * 2][1] == 1:            # 가위
                if students[i * 2 + 1][1] == 1:    # 가위
                    delete.append(students[i * 2 + 1])
                elif students[i * 2 + 1][1] == 2:  # 바위
                    delete.append(students[i * 2])
                elif students[i * 2 + 1][1] == 3:
                    delete.append(students[i * 2 + 1])
                else:
                    delete.append(students[i * 2 + 1])
            elif students[i * 2][1] == 2:          # 바위
                if students[i * 2 + 1][1] == 1:    # 가위
                    delete.append(students[i * 2 + 1])
                elif students[i * 2 + 1][1] == 2:  # 바위
                    delete.append(students[i * 2 + 1])
                elif students[i * 2 + 1][1] == 3:
                    delete.append(students[i * 2])
                else:
                    delete.append(students[i * 2 + 1])
            else:                                  # 보
                if students[i * 2 + 1][1] == 1:    # 가위
                    delete.append(students[i * 2])
                elif students[i * 2 + 1][1] == 2:  # 바위
                    delete.append(students[i * 2 + 1])
                elif students[i * 2 + 1][1] == 3:
                    delete.append(students[i * 2 + 1])
                else:
                    delete.append(students[i * 2 + 1])
        for i in delete:
            students.remove(i)
        n = len(students)
        if n % 2:
            n = n // 2 + 1
        else:
            n = n // 2
        return win(students, n)

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    if n % 2:
        n = n // 2 + 1
    else:
        n = n // 2
    students = list(enumerate(map(int, input().split())))

    win(students, n)