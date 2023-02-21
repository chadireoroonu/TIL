import sys
sys.stdin = open('input.txt')

# 거듭제곱 계산을 위한 함수를 생성
# m 횟수 동안 n * solve(n, m-1)으로
# 재귀 함수를 호출하여 거듭제곱 계산
def solve(n, m):
    if m == 1:
        return n
    else:
        return n * solve(n, m-1)

for q in range(10):
    tc = int(input())
    n, m = list(map(int, input().split()))

    print(f'#{tc} {solve(n, m)}')