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

    new_arr = []                           # 작은 3*3 칸을 검사하기 위한 작업 시작
    for i in range(9):
        temp = ''
        for j in range(9):
            temp += str(arr[i][j])         # 빈 문자열을 만들어 가로 세칸의 숫자를 문자로 병합
            if len(temp) == 3:
                new_arr.append(temp)       # 병합한 문자열의 길이가 3이면 new_arr 리스트에 추가
                temp = ''                  # 리스트에 추가한 뒤에는 temp 초기화

    sum_arr = []                           # 한 번 더 병합 작업을 진행하기 위한 빈 리스트 생성
    temp_1 = ''                            # 가로 0~2, 3~5, 6~8칸을 분리해 병합하기 위하여
    temp_2 = ''                            # 빈 문자열을 세 개 생성하여 구분
    temp_3 = ''
    for i in range(27):                    # 범위는 전 리스트 동안 반복하며
        if i % 3 == 0:                     # 각 인덱스를 3으로 나누어 temp 1~3에 추가
            temp_1 += new_arr[i]           # 만약 temp의 길이가 9가 된다면,
            if len(temp_1) == 9:           # sum_arr에 병합 문자열을 추가하고 temp 초기화
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

    for i in range(9):                     # sum_arr에 나누어 담긴 3*3 요소들을 검사
        temp = []
        for j in range(9):
            if sum_arr[i][j] not in temp:
                temp.append(sum_arr[i][j])
            else:
                return print(f'#{tc} 0')

    return print(f'#{tc} 1')               # 만약 이제까지 0을 반환한 적이 없다면, 1 반환

t = int(input())
for tc in range(1, t+1):
    arr = [list(map(int, input().split())) for q in range(9)]

    result(arr)
