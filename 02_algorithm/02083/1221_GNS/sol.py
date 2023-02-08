import sys
sys.stdin = open('input.txt')

# 숫자 체계가 우리와 다른 어느 행성이 있다.
# 아래는 이 행성에서 사용하는 0 ~ 9의 값을 순서대로 나타낸 것이다.
# "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
# 0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아
# 작은 수부터 차례로 정렬하여 출력하는 프로그램을 작성하라.

# 예를 들어 입력 문자열이 "TWO NIN TWO TWO FIV FOR" 일 경우
# 정렬한 문자열은 "TWO TWO TWO FOR FIV NIN" 이 된다.

# 주어진 테스트 케이스 동안 반복을 진행한다.
# 테스트 케이스 아랫 줄에 공백을 사이에 두고 주어지는
# 테스트 케이스 번호와 총 숫자의 개수를 tc, n으로 입력 받고,
# num이라는 리스트로 크기를 비교할 어느 행성 숫자들을 받아준다.
# 우리가 아는 숫자로 각각의 대입 값을 밸류로 설정한 딕셔너리를 생성한다.
t = int(input())
for q in range(t):
    tc, n = list(map(str, input().split()))
    n = int(n)
    numbers = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
    num = list(map(str, input().split()))

    # 선택 정렬을 해줄 함수를 생성한다.
    # n 범위 안에서 num의 i번째 요소의 numbers 딕셔너리 키 값과
    # num의 i+1부터 n번째 요소의 numbers 딕셔너리 키 값을 비교해
    # 오름차순으로 num 리스트를 재정렬 하고 반환한다.
    def select(num, n):
        for i in range(n-1):
            minidx = i
            for j in range(i+1, n):
                if numbers[num[minidx]] > numbers[num[j]]:
                    minidx = j
            num[i], num[minidx] = num[minidx], num[i]

        return num

    # 문제에서 주어진 조건에 맞도록 tc를 출력하고
    # 함수를 통해 정렬한 리스트의 요소들을 공백을 간격으로 출력한다.
    # 한 테스트 케이스가 끝나면 줄을 바꾸어주기 위해 print()를 삽입한다.
    print(tc)
    for k in select(num, n):
        print(k, end=' ')
    print()

