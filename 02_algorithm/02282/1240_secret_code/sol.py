import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = list(map(int, input().split()))
    arr = [''.join(list(map(str, input()))) for _ in range(n)]

    # 문제에서 주어진 코드를 키로 사용하기 위한 딕셔너리 생성
    code = {
        '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
        '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9
    }

    # 배열을 순회하며, 만약 i 행에 '1'이 포함되어 있다면
    # i 행을 뒤에서부터 순회하며 '1'을 만났을 때 문자열 56자리를 슬라이싱
    # 매 행은 같은 코드이므로 한줄 수행후 중단
    temp = ''
    for i in range(n):
        if '1' in arr[i]:
            for j in range(m-1, -1, -1):
                if arr[i][j] == '1':
                    temp = arr[i][j-55:j+1]
                    break

    # 슬라이싱한 문자열을 7자리씩 분할하여 저장
    num = []
    for i in range(8):
        num. append(code[temp[i*7:i*7+7]])

    # 조건에 맞게 숫자 합산
    result = 0
    for i in range(8):
        if i % 2:
            result += num[i]
        else:
            result += 3 * num[i]

    # 올바른 암호인지 판별하여 출력
    if result % 10:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {sum(num)}')