import sys
sys.stdin = open('input.txt')

# 시간초과 오답

# 세제곱근을 구할 함수 생성
# n 이하 숫자 중 세제곱하여 n이 되는 숫자 반환
# 없다면 -1을 반환
def sol(n):
    for i in range(n):
        if i ** 3 == n:
            return i
    return -1

T = int(input())
for tc in range(1, T+1):
    n = int(input())

    print(f'#{tc} {sol(n)}')