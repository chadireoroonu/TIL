import sys
sys.stdin = open('input.txt')

# 오목 여부를 검사할 함수 생성
def omok(arr, n):
    # 가로 방향 오목 검사
    temp = ''
    for i in range(n):
        for j in range(n-4):
            for k in range(5):
                temp += arr[i][j+k]
                if 'ooooo' in temp:
                    return 'YES'
    # 세로 방향 오목 검사
    for j in range(n):
        temp = ''
        for i in range(n-4):
            for k in range(5):
                temp += arr[i+k][j]
                if 'ooooo' in temp:
                    return 'YES'
    # 음의 기울기 대각선 방향 오목 검사
    for i in range(n):
        for j in range(n):
            temp = ''
            for k in range(5):
                if 0 <= i+k < n and 0 <= j+k < n:
                    temp += arr[i+k][j+k]
            if 'ooooo' in temp:
                return 'YES'
    # 양의 기울기 대각선 방향 오목 검사
    for i in range(n):
        for j in range(n):
            temp = ''
            for k in range(5):
                if 0 <= i+k < n and 0 <= j-k < n:
                    temp += arr[i+k][j-k]
            if 'ooooo' in temp:
                return 'YES'
    # 최종적으로 오목이 안된다면 NO 반환
    return 'NO'

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(str, input())) for _ in range(n)]

    print(f'#{tc} {omok(arr, n)}')