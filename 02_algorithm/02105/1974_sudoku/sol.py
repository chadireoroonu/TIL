import sys
sys.stdin = open('input.txt')

def result(arr):
    for i in range(9):                     # 가로 칸 검사
        sdoku = []
        for j in range(9):
            if arr[i][j] not in sdoku:
                sdoku.append(arr[i][j])
            else:
                return print(f'#{tc} 0')   # 겹치는 요소를 추가해야 한다면, 0 리턴

    for i in range(9):                     # 세로 칸 검사
        sdoku = []
        for j in range(9):
            if arr[j][i] not in sdoku:
                sdoku.append(arr[j][i])
            else:
                return print(f'#{tc} 0')   # 겹치는 요소를 추가해야 한다면, 0 리턴

    new_arr = []
    for i in range(9):
        temp = ''
        for j in range(9):
            temp += str(arr[i][j])
            if len(temp) == 3:
                new_arr.append(temp)
                temp = ''

    sum_arr = []
    temp_1 = ''
    temp_2 = ''
    temp_3 = ''
    for i in range(27):
        if i % 3 == 0:
            temp_1 += new_arr[i]
            if len(temp_1) == 9:
                sum_arr.append(temp_1)
                temp_1 = ''
        elif i % 3 == 1:
            temp_2 += new_arr[i]
            if len(temp_2) == 9:
                sum_arr.append(temp_2)
                temp_2 = ''
        else:
            temp_3 += new_arr[i]
            if len(temp_3) == 9:
                sum_arr.append(temp_3)
                temp_3 = ''
    temp = []
    for i in range(9):
        if j in range(9):
            if sum_arr[i][j] not in temp:
                temp.append(sum_arr)
            else:
                return print(f'#{tc} 0')

    return print(f'#{tc} 1')

t = int(input())
for tc in range(1, t+1):
    arr = [list(map(int, input().split())) for q in range(9)]

    print(result(arr))