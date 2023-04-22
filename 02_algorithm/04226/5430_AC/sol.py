# 뒤집힌 상태인지 확인하는 flag 사용
# R 참고하여 D 등장 시 F, B에 삭제 개수 저장
# 최종 배열에서 뒤집기, 앞 뒤 숫자 삭제 개수 파악 후 출력할 요소 임시 추가
# 띄어쓰기 없는 출력을 위해 문자열로 출력

# 1차 시도 틀렸습니다 -> 한 자리 숫자만 가능
# 2차 시도 16% 틀렸습니다. -> 빈 리스트면 [] 출력, 띄어쓰기 없이 출력

import sys
sys.stdin = open('input.txt')


T = int(sys.stdin.readline().strip())
for tc in range(1, T+1):
    p = list(map(str, sys.stdin.readline().strip()))
    # 현재 요소가 D 라면 flag 따라 F, B 추가
    # flag 1이면 정방향 0이면 역방향
    flag = 1
    F = 0
    B = 0
    for i in range(len(p)):
        if p[i] == 'D':
            if flag:
                F += 1
            else:
                B += 1
        else:
            if flag:
                flag = 0
            else:
                flag = 1

    n = int(sys.stdin.readline().strip())
    temp = sys.stdin.readline().strip()
    dump = temp[1:-1]
    dump = dump.split(',')
    result = []
    if n-B-F >= 0:    # 출력할 수 있는 경우
        for i in range(F, n-B):
            result.append(int(dump[i]))
        if not flag:    # flag 없다면 역방향
            result = result[::-1]
        sol = '['
        for j in range(len(result)):
            if j != len(result)-1:
                sol += str(result[j]) + ','
            else:
                sol += str(result[j])
        sol += ']'
        print(sol)
    else:
        print('error')