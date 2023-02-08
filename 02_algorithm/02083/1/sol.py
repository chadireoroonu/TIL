import sys
sys.stdin = open('input.txt')

# 주어진 테스트 케이스 동안 반복한다.
# 주어지는 단어를 word로 받아서
# rev라는 빈 문자열을 생성하고
# i의 범위를 1부터 문자열의 길이+1로 설정하여
# 빈 문자열 rev에 word의 맨 뒤 요소부터 맨 앞요소까지
# 차례대로 붙인 후 출력해준다.
t = int(input())
for tc in range(1, t+1):
    word = input()
    rev = ''
    for i in range(1, len(word)+1):
        rev += word[-i]

    print(f'#{tc} {rev}')