import sys
sys.stdin = open('input.txt')

# '+' 모양 퇴치 파리 수 함수
def plus(arr, n, m):
    global maxi
    # 네 방향을 적절히 설정
    # 임시합을 구할 temp 변수 선언
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    temp = 0

    # 배열의 모든 칸에 대하여 네 방향으로
    # 주어진 m 칸 이동하며 파리 수 합산
    for i in range(n):
        for j in range(n):
            temp += arr[i][j]
            for k in range(4):
                for l in range(1, m):
                    ni = i + di[k]*l
                    nj = j + dj[k]*l
                    # 배열의 범위 벗어나면 무시
                    if 0 <= ni < n and 0 <= nj < n:
                        temp += arr[ni][nj]
            # 임시합이 최대보다 크다면 최대 갱신
            if temp > maxi:
                maxi = temp
            # 다시 임시변수 초기화
            temp = 0
    return

# '*' 모양 퇴치 파리 수 함수
def x(arr, n, m):
    global maxi
    # 네 방향을 적절히 설정
    # 임시합을 구할 temp 변수 선언
    di = [-1, -1, 1, 1]
    dj = [-1, 1, -1, 1]
    temp = 0

    # 배열의 모든 칸에 대하여 네 방향으로
    # 주어진 m 칸 이동하며 파리 수 합산
    for i in range(n):
        for j in range(n):
            temp += arr[i][j]
            for k in range(4):
                for l in range(1, m):
                    ni = i + di[k]*l
                    nj = j + dj[k]*l
                    # 배열의 범위 벗어나면 무시
                    if 0 <= ni < n and 0 <= nj < n:
                        temp += arr[ni][nj]
            # 임시합이 최대보다 크다면 최대 갱신
            if temp > maxi:
                maxi = temp
            # 다시 임시변수 초기화
            temp = 0
    return

T = int(input())
for tc in range(1, T+1):
    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 최댓값 0으로 초기 설정
    # 두 함수 호출 후 최댓값 출력
    maxi = 0
    plus(arr, n, m)
    x(arr, n, m)

    print(f'#{tc} {maxi}')
