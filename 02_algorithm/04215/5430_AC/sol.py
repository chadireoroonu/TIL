# D 앞뒤 R 등장 횟수 조사 -> 짝수 삭제, 홀수면 한 개 남기기 -> deque 사용 X
# 뒤집힌 상태인지 확인하는 flag 사용 -> F, B에 삭제 개수 저장
# 최종 배열에서 뒤집기, 앞 뒤 숫자 삭제 개수 파악 후 처리
# try except 사용, 에러 발생 시 error 출력
# n의 인덱스로 잘라내기

# 1차 시도 틀렸습니다 -> 한 자리 숫자만 가능

import sys
sys.stdin = open('input.txt')


T = int(sys.stdin.readline().strip())
for tc in range(1, T+1):
    p = list(map(str, sys.stdin.readline().strip()))
    # deque 안에 요소가 없으면 추가,
    # 요소 있으면, 현재 R, 마지막 요소 R일때 pop
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

    # print(F, B)
    # print(flag)
    n = int(sys.stdin.readline().strip())
    dump = sys.stdin.readline().strip()
    result = ''
    for i in range(2*F+1, 2*n+1-2*B-1):
        result += dump[i]
    result += ''

    if len(result) > 2:
        if flag:
            print(f'[{result}]')
        else:
            print(f'[{result[::-1]}]')

    else:
        print('error')