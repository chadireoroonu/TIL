import sys
sys.stdin = open('input.txt')

# 테스트 케이스가 총 여섯개이므로 여섯번 반복한다.
for tc in range(1, 7):
    n = int(input())
    # 만약 n이 양수라면,
    # 각 자릿수의 숫자들을 담아줄 빈 리스트를 생성하고
    # n이 0이 될때까지 nu에 n을 10으로 나눈 나머지를 넣어준다.
    # 각 자릿수를 유지하기 위해 insert 메서드로 0번째에 넣어준다.
    if n > 0:
        num = []
        while n > 0:
            num.insert(0, n % 10)
            n = n // 10

        # 넣어준 요소들을 아스키 코드로 변환하여 출력한다.
        print(f'#{tc}', end=' ')
        for i in num:
            i = print(chr(i+48), end='')
        print()

        # 만약, n이 음수라면,
        # 우선 양수화하여 양수와 같은 작업을 진행한다.
    else:
        n = -n
        num = []
        while n > 0:
            num.insert(0, n % 10)
            n = n // 10

        # 프린트 단계에서 테스트 케이스를 출력 한 뒤,
        # -를 붙여 아스키 코드로 변환한 숫자들을 출력한다.
        print(f'#{tc}', end=' ')
        print('-', end='')
        for i in num:
            i = print(chr(i + 48), end='')
        print()