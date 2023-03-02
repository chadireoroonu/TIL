import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    n, g = list(map(int, input().split()))
    # 인덱스 정보를 저정하기 위한 작업
    document = list(enumerate(map(int, input().split())))

    count = 1   # 출력 횟수 변수
    while document:
        maxi = 0    # 문서 중 중요도 1위 파악
        for i in range(len(document)):
            if document[i][1] >= maxi:
                maxi = document[i][1]

        # 만약 첫 요소 중요도가 가장 높다면 출력
        # 첫 요소 == g => 카운트 출력, 종료
        if document[0][1] == maxi:
            if document[0][0] == g:
                print(count)
                break
            # 첫 요소 != g => 첫 요소 출력, count + 1
            document.pop(0)
            count += 1
        else:   # 첫 요소 != max => 맨 앞 문서 맨 뒤로 이동
            temp = document.pop(0)
            document.append(temp)
