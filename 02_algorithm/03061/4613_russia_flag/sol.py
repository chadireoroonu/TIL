import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = list(map(int, input().split()))
    flag = [input() for _ in range(n)]

    mini = n*m    # 모든 칸으로 최솟값을 설정해두고 시작
    for a in range(n-2):    # 하얀색이 될 수 있는 범위 : 1~n-2줄까지
        for b in range(a, n-1):    # 파란색이 될 수 있는 범위 : 흰색 다음 줄 ~ n-1줄
            paint = 0    # 색칠해야하는 칸

            for i in range(a+1):    # 하얀색
                for j in range(m):
                    if flag[i][j] != 'W':
                        paint += 1

            for i in range(a+1, b+1):    # 파란색
                for j in range(m):
                    if flag[i][j] != 'B':
                        paint += 1

            for i in range(b+1, n):    # 빨간색
                for j in range(m):
                    if flag[i][j] != 'R':
                        paint += 1

            if paint < mini:    # 색칠한 칸 수 최소값과 비교
                mini = paint

    print(f'#{tc} {mini}')