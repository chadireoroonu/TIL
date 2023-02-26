import sys
sys.stdin = open('input.txt')

# 암호 코드를 저장할 함수 생성
# 만약 arr[i]가 1을 포함하면
# arr[i]를 7자리씩 끊어서 코드인 부분 저장
def sol(arr, n, m):
    global code
    for i in range(n):
        if '1' in arr[i]:
            for j in range(m // 7 + 1):
                word = arr[i][j * 7:(j + 1) * 7]
                print(word)
                if '1' in word:
                    code.append(word)
            return

T = int(input())
for tc in range(1, T+1):
    n, m  = list(map(int, input().split()))
    # arr 줄 단위로 묶어서 저장
    arr = [''.join(list(map(str, input()))) for _ in range(n)]
    # 코드들을 담을 빈 리스트 생성 후 함수 실행
    code = []
    print(f'code {code}')
    sol(arr, n, m)

    # code 속 요소들을 숫자로 변환
    num = []
    for i in code:
        if i == '0001101':
            num.append(0)
        elif i == '0011001':
            num.append(1)
        elif i == '0010011':
            num.append(2)
        elif i == '0111101':
            num.append(3)
        elif i == '0100011':
            num.append(4)
        elif i == '0110001':
            num.append(5)
        elif i == '0101111':
            num.append(6)
        elif i == '0111011':
            num.append(7)
        elif i == '0110111':
            num.append(8)
        elif i == '0001011':
            num.append(9)

    print(num)
    # 인덱스는 0부터 시작하므로 문제와 홀,짝 반대
    # 인덱스 짝수 번째 숫자들의 합 * 3 + 인덱스 홀수 번째 숫자들의 합 % 10
    # 나머지가 있다면 올바른 암호코드 아님 0 출력
    # 나머지가 없다면 숫자들의 합 출력
    temp = 0
    result = 0
    for i in range(len(num)):
        if i % 2:
            result += num[i]
        else:
            temp += num[i]

    if (temp * 3 + result) % 10:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {sum(num)}')


