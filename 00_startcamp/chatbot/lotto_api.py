# 파이썬으로 웹 요청 보낼 수 있는 라이브러리 불러오기

# 동행복권 로또 당첨 번호 api 사용하기
# (회차 직접 입력)
# 입력받은 회차에 해당하는 당첨번호 확인하기 -> 6개 (보너스 번호 제외)

# (선택사항) - 보너스 번호 확인하기

# import requests

# numbers = input('회차를 입력하세요 : ')

# r = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={numbers}').json()
# # print(r['drwNo'],'회차의 당첨번호는',
# #    r['drwtNo1'], r['drwtNo2'], r['drwtNo3'], r['drwtNo4'],
# #    r['drwtNo5'], r['drwtNo6'],'이며, 보너스 번호는', r['bnusNo'],'입니다.')

# a = 1
# while a < 7:
#     print(r[f'drwtNo{a}'])
#     a += 1

# 4. 이걸 1000번 반복한다.
    # 1. 로또 번호 6개를 추첨 받는다.
    # 2. 내가 추첨 받은 6개의 번호가 1049회차 당첨 번호와 일치 하는지 확인한다.
        # 2-1. 확인하는 방법은 내 번호 6개를 순회하면서
            # 1049회 당첨번호 목록에 해당 숫자가 있는지
            # 있다면 적중 횟수 +1
    # 그래서 적중 횟수가 6개면 1등
    # 5개면 3등
    # 4개면 4등
    # 3개면 2등
    # 2개 이하면 꽝을 출력한다.



import random
import requests

num = list(range(1, 46))

# a = 1
# while a < 7:
#     d = (r[f'drwtNo{a}'])
#     a += 1

n = 0
while n >= 1000:
    r = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1049').json()
    d = [r['drwtNo1'], r['drwtNo2'], r['drwtNo3'], r['drwtNo4'],r['drwtNo5'], r['drwtNo6']]
    c = (random.sample(num, 6))
    count = 0
    for i in d:
        if i in c:
            print(True)
            count += 1

    if count == 6:
        print('1등')
    elif count == 5:
        print('3등')
    elif count == 4:
        print('4등')
    elif count == 3:
        print('5등')
    else:
        print('꽝')

    n =+ 1