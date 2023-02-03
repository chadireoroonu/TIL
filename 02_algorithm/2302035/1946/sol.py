import sys
sys.stdin = open('input.txt')

# 원본 문서는 너비가 10인 여러 줄의 문자열로 이루어져 있다.
# 문자열은 마지막 줄을 제외하고 빈 공간 없이 알파벳으로 채워져 있고 마지막 줄은 왼쪽부터 채워져 있다.
# 이 문서를 압축한 문서는 알파벳과 그 알파벳의 연속된 개수로 이루어진 쌍들이 나열되어 있다. (예 : A 5    AAAAA)
# 압축된 문서를 입력 받아 원본 문서를 만드는 프로그램을 작성하시오.

# 1. 압축된 문서의 알파벳과 숫자 쌍의 개수 N은1이상 10이하의 정수이다. (1 ≤ N ≤ 10)
# 2. 주어지는 알파벳 Ci는 A~Z의 대문자이다. (i는 줄의 번호로 1~N까지의 수)
# 3. 알파벳의 연속된 개수로 주어지는 수 Ki는 1이상 20이하의 정수이다. (1 ≤ Ki ≤ 20, i는 줄의 번호로 1~N까지의 수)
# 4. 원본 문서의 너비는 10으로 고정이다.

T = int(input())
# 주어진 테스트 케이스 동안 반복문을 통한 과정을 진행한다.
# 첫 줄에 주어진 케이스의 입력 줄 수를 받고,
# 모든 문자들을 더해줄 빈 문자열을 생성한다.
for tc in range(1, T+1):
    n = int(input())
    string = ''

    # 주어진 한 케이스 내의 입력 줄 수 동안
    # 문자 ci와 ci의 반복 횟수 ki를 인식하고,
    # ci에 숫자로 변환한 ki를 곱해 문자열에 추가하여
    # 전체 문서의 내용을 한 줄로 구한다.
    for i in range(n):
        ci, ki = input().split()
        string += ci * int(ki)

    # 문제에서 요구하는 대로 테스트 케이스를 먼저 출력한 후,
    # 한 줄로 구한 문자열을 10글자씩 꺼낼 수 있도록
    # 프린트 범위를 설정하여 출력한다.
    print(f'#{tc}')
    for i in range(0, len(string), 10):
        print(string[i : i + 10])