# D 앞뒤 R 등장 횟수 조사 -> 짝수 삭제, 홀수면 한 개 남기기 -> deque 사용 X
# 뒤집힌 상태인지 확인하는 flag 사용 -> F, B에 삭제 개수 저장
# 최종 배열에서 뒤집기, 앞 뒤 숫자 삭제 개수 파악 후 처리
# try except 사용, 에러 발생 시 error 출력
# n의 인덱스로 잘라내기

# 1차 시도 틀렸습니다 -> 한 자리 숫자만 가능
# 2차 시도 16% 틀렸습니다 -> 빈 리스트면 [] 출력, 띄어쓰기 없이 출력 추가 필요

import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline().strip())
for tc in range(1, T+1):
    p = list(map(str, sys.stdin.readline().strip()))
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
    if n-B-F >= 0:
        for i in range(F, n-B):
            result.append(int(dump[i]))
        if result:
            if flag:
                print(result)
            else:
                print(result[::-1])
    else:
        print('error')