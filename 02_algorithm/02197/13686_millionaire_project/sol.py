import sys
sys.stdin = open('input.txt')

# 시간초과 오답
# 테스트 케이스 10개 중 6개 정답
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    # 기준일을 기준으로 훗날에만 되팔 수 있기 때문에
    # 인덱스 정보를 함께 저장할 수 있는 enumerate함수를 사용
    sale = list(enumerate(map(int, input().split())))
    # 총 최대 이익을 담을 money 변수를 선언
    money = 0
    # sale 안을 이중으로 순회하며
    # 구매 날짜별 최대 이익을 더해줄 sub 변수 선언 후
    # j의 인덱스가 i의 인덱스 보다 크다 -> j가 더 미래인 경우면
    # j 판매가와 i 구매가의 차이가 가장 큰 날을 찾아 sub 할당
    for i in sale:
        sub = 0
        for j in sale:
            if i[0] < j[0]:
                if j[1] - i[1] > sub:
                    sub = j[1] - i[1]
        # 순회가 끝나면 money 변수에 일별 최대 이익을 합산
        money += sub

    print(f'#{tc} {money}')
