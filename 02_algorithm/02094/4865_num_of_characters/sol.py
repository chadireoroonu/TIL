import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    s1 = input()                  # 단어들을 입력 받음
    s2 = input()
    maxi = 0                      # 가장 많은 숫자는 0으로 설정한 뒤 시작
    for i in range(len(s1)):      # s1 단어의 길이 동안 반복하며
        temp = 0                  # 숫자를 세기 위한 임시 변수 0으로 설정
        for j in range(len(s2)):  # s2의 범위 동안 순회하며
            if s1[i] == s2[j]:    # s1의 i번째 글자와 s2의 j번째 글자가 같다면
                temp += 1         # temp +1
        if temp > maxi:           # temp와 maxi를 비교하여 temp가 크다면
            maxi = temp           # maxi 값 재할당

    print(f'#{tc} {maxi}')        # 최종 maxi 출력